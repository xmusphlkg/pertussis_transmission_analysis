from __future__ import annotations

from pathlib import Path
from zipfile import ZipFile
import xml.etree.ElementTree as ET

import pandas as pd


SPREADSHEET_NS = {"a": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
REL_NS = {"rel": "http://schemas.openxmlformats.org/package/2006/relationships"}
OFFICE_REL = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"


def read_xlsx(path: str | Path, *, sheet_name: str | None = None) -> pd.DataFrame:
    """Read a simple .xlsx worksheet without requiring openpyxl."""
    path = Path(path)
    with ZipFile(path) as archive:
        shared_strings = _read_shared_strings(archive)
        target = _worksheet_target(archive, sheet_name=sheet_name)
        root = ET.fromstring(archive.read(target))
        rows = [_read_row(row, shared_strings) for row in root.findall("a:sheetData/a:row", SPREADSHEET_NS)]
    rows = [row for row in rows if any(str(value).strip() for value in row)]
    if not rows:
        return pd.DataFrame()
    header = [str(value).strip() or f"column_{idx + 1}" for idx, value in enumerate(rows[0])]
    width = len(header)
    normalized = [(row + [""] * width)[:width] for row in rows[1:]]
    return pd.DataFrame(normalized, columns=header)


def _read_shared_strings(archive: ZipFile) -> list[str]:
    try:
        root = ET.fromstring(archive.read("xl/sharedStrings.xml"))
    except KeyError:
        return []
    values = []
    for item in root.findall("a:si", SPREADSHEET_NS):
        values.append("".join(text.text or "" for text in item.findall(".//a:t", SPREADSHEET_NS)))
    return values


def _worksheet_target(archive: ZipFile, *, sheet_name: str | None) -> str:
    workbook = ET.fromstring(archive.read("xl/workbook.xml"))
    relationships = ET.fromstring(archive.read("xl/_rels/workbook.xml.rels"))
    relationship_targets = {
        relationship.attrib["Id"]: relationship.attrib["Target"]
        for relationship in relationships.findall("rel:Relationship", REL_NS)
    }
    sheets = workbook.findall("a:sheets/a:sheet", SPREADSHEET_NS)
    if not sheets:
        raise ValueError("Workbook does not contain worksheets.")
    chosen = sheets[0]
    if sheet_name is not None:
        matching = [sheet for sheet in sheets if sheet.attrib.get("name") == sheet_name]
        if not matching:
            raise ValueError(f"Worksheet not found: {sheet_name}")
        chosen = matching[0]
    relationship_id = chosen.attrib[OFFICE_REL]
    target = relationship_targets[relationship_id]
    return target if target.startswith("xl/") else f"xl/{target}"


def _read_row(row: ET.Element, shared_strings: list[str]) -> list[str]:
    cells = []
    max_index = -1
    for cell in row.findall("a:c", SPREADSHEET_NS):
        index = _column_index(cell.attrib.get("r", "A1"))
        max_index = max(max_index, index)
        cells.append((index, _cell_text(cell, shared_strings)))
    values = [""] * (max_index + 1)
    for index, value in cells:
        values[index] = value
    return values


def _column_index(cell_reference: str) -> int:
    letters = "".join(char for char in cell_reference if char.isalpha())
    index = 0
    for letter in letters:
        index = index * 26 + ord(letter.upper()) - 64
    return index - 1


def _cell_text(cell: ET.Element, shared_strings: list[str]) -> str:
    cell_type = cell.attrib.get("t")
    if cell_type == "inlineStr":
        return "".join(text.text or "" for text in cell.findall(".//a:t", SPREADSHEET_NS))
    value = cell.find("a:v", SPREADSHEET_NS)
    if value is None or value.text is None:
        return ""
    if cell_type == "s":
        idx = int(value.text)
        return shared_strings[idx] if idx < len(shared_strings) else value.text
    return value.text
