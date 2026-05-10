from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "Supplementary Material.md"
APPENDIX_DIR = ROOT / "outputs" / "appendix"
HEAD_METHOD = APPENDIX_DIR / "head_method.md"
FIGURE = APPENDIX_DIR / "figure.md"
TABLE_TEMP = APPENDIX_DIR / "table_temp.md"
FINAL = APPENDIX_DIR / "Supplementary Material.md"

METHODS_HEADING = "## Materials and Methods"
TABLES_HEADING = "## eTables"
REFERENCES_HEADING = "## References"
FIGURES_HEADING = "## eFigures"

SECTION_HEADING_RE = re.compile(r"(?m)^## ")
TABLE_BLOCK_RE = re.compile(
    r"(?ms)^(?:<!-- BEGIN (?:E?TABLE S?\d+) -->\n)?\*\*(?:eTable \d+|Table S\d+)\..*?"
    r"(?:\n<!-- END (?:E?TABLE S?\d+) -->)?"
    r"(?=\n\n(?:<!-- BEGIN (?:E?TABLE S?\d+) -->\n)?\*\*(?:eTable \d+|Table S\d+)\.|\Z)"
)
APPENDIX_LINK_RE = re.compile(r"(?<=\]\()outputs/appendix/")
ROOT_LINK_RE = re.compile(r"(?<=\]\()(?!(?:[a-z][a-z0-9+.-]*:|/|#|outputs/appendix/))([^)]+)")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def join_sections(*parts: str) -> str:
    return "\n\n".join(part.strip() for part in parts if part and part.strip())


def normalize_jama_labels(text: str) -> str:
    text = text.replace("## Supplementary figures", FIGURES_HEADING)
    text = text.replace("## Supplementary tables", TABLES_HEADING)
    text = re.sub(r"\bExtended Data Figure (\d+)\b", r"eFigure \1", text)
    text = re.sub(r"\bFig\. S(\d+)\b", r"eFigure \1", text)
    text = re.sub(r"\bFigure S(\d+)\b", r"eFigure \1", text)
    text = re.sub(r"\bTable S(\d+)\b", r"eTable \1", text)
    return text


def extract_section(text: str, heading: str) -> str:
    start = text.index(heading)
    next_heading = SECTION_HEADING_RE.search(text, start + len(heading))
    end = next_heading.start() if next_heading else len(text)
    return text[start:end].rstrip()


def extract_intro(text: str) -> str:
    return text[: text.index(METHODS_HEADING)].rstrip()


def reorder_contents_block(intro: str) -> str:
    marker = "## Contents"
    if marker not in intro:
        return intro.rstrip()

    prefix, contents_tail = intro.split(marker, 1)
    lines = [line.strip() for line in contents_tail.splitlines() if line.strip()]
    if not lines:
        return intro.rstrip()

    method_line = next((line for line in lines if line.startswith("Materials and Methods")), "")
    reference_line = next((line for line in lines if line.startswith("References.")), "")
    figure_lines = [line for line in lines if line.startswith("Fig. ")]
    table_lines = [line for line in lines if line.startswith("Table ")]
    ordered = [line for line in (method_line, reference_line, *figure_lines, *table_lines) if line]
    if not ordered:
        return intro.rstrip()

    rebuilt = "\n\n".join(ordered)
    return f"{prefix.rstrip()}\n\n{marker}\n\n{rebuilt}"


def rewrite_appendix_links(text: str) -> str:
    return APPENDIX_LINK_RE.sub("", text)


def restore_root_links(text: str) -> str:
    return ROOT_LINK_RE.sub(r"outputs/appendix/\1", text)


def normalize_table_section(section: str) -> str:
    section = section.strip()
    if not section:
        return section
    if not section.startswith(TABLES_HEADING):
        return section

    body = section[len(TABLES_HEADING) :].strip()
    blocks = [block.strip() for block in TABLE_BLOCK_RE.findall(body)]
    if not blocks:
        return section

    return f"{TABLES_HEADING}\n\n" + "\n\n".join(blocks)


def build_fragments(source_text: str) -> tuple[str, str, str]:
    intro = reorder_contents_block(extract_intro(source_text))
    methods = extract_section(source_text, METHODS_HEADING)
    references = extract_section(source_text, REFERENCES_HEADING)
    figures = rewrite_appendix_links(extract_section(source_text, FIGURES_HEADING))
    tables = normalize_table_section(extract_section(source_text, TABLES_HEADING))
    head_method = join_sections(intro, methods, references)
    return head_method, figures, tables


def ensure_fragments(source_text: str) -> None:
    head_method, figure, table_temp = build_fragments(source_text)
    write_text(HEAD_METHOD, head_method)
    write_text(FIGURE, figure)
    write_text(TABLE_TEMP, table_temp)


def merge_fragments() -> str:
    head_method = read_text(HEAD_METHOD).strip()
    figure = read_text(FIGURE).strip()
    table_temp = read_text(TABLE_TEMP).strip()
    merged = join_sections(head_method, figure, table_temp)
    return rewrite_appendix_links(merged) + "\n"


def main() -> None:
    if not SOURCE.exists():
        if not FINAL.exists():
            raise FileNotFoundError(f"Missing source document: {SOURCE}")
        write_text(SOURCE, restore_root_links(normalize_jama_labels(read_text(FINAL))))

    source_text = normalize_jama_labels(read_text(SOURCE))
    ensure_fragments(source_text)

    merged = merge_fragments()
    merged = normalize_jama_labels(merged)
    write_text(FINAL, merged)
    write_text(SOURCE, restore_root_links(merged))


if __name__ == "__main__":
    main()
