# JAMA Network Open 投稿导向的建模审查报告

日期：2026-05-16

更新：2026-05-19

本审查报告保留为历史审计记录。2026-05-19 的重跑已经解决当时最严重的 Bayesian uncertainty 阻断项：原高维 MCMC 路径已替换为固定弱可辨识 nuisance 参数后的确定性 beta-grid posterior predictive 路径；`outputs/summaries/bayesian_beta_grid_quality.csv` 显示 10/10 国家通过预先定义的网格有效性检查（最小边界下降 20.6、最小有效网格点 10.2、最大单点权重 0.193）。因此，下面关于“当前 MCMC 完全不收敛、不能使用 CrI”的判断只适用于 2026-05-16 的旧输出，不再代表当前 canonical 输出状态。

目标期刊：JAMA Network Open

审查依据：

- WHO 2025 *Guidance for using modelling for immunization decision-making*，重点按“模型问题定义、数据情境化、模型开发与参数估计、模型验证、情景分析、结果解释”六步审查。
- JAMA Network Open Instructions for Authors，稿件类型按 Original Investigation / Decision Analytical Model；需结构化摘要、Key Points、数据共享声明、EQUATOR 报告规范，并在 3000 词正文、最多 5 个主文图表、50-75 篇参考文献范围内组织。

## 总体判断

这个项目的模型框架已经具备投稿基础：8 个年龄组、敏感/耐药双菌株、母体保护和剂次历史、国家接触矩阵、日历时间、报告率、校准、情景模拟、敏感性分析和补充图表都已经搭起来了。对 JAMA Network Open 来说，最合适的包装不是“发现新的生物学规律”，而是“一个面向公共卫生决策的 decision analytical model，说明疫苗传播阻断、耐药和干预组合如何改变婴儿负担与策略优先级”。

但当前版本还不应投稿。核心原因不是模型太弱，而是可追溯性、校准状态、不确定性分析和正文数值一致性没有达到 JAMA 统计审稿和方法审稿的门槛。特别是：输出是旧配置生成的；MCMC 收敛诊断显示完全未通过；主文结果与当前输出文件不一致；多数组合情景输出标记为未校准分析。这些问题会直接削弱可信度。

## 必须先修复的阻断项

1. 全部生产输出必须来自同一冻结配置。

   `python -m src_python.utils.validation` 失败，原因是 `baseline_timeseries` 的元数据哈希为旧值，而当前配置哈希已经变化。这意味着当前摘要、图、主文数字和配置不是同一套产物。JAMA 审稿人通常不会接受“代码可运行但结果不可追溯”的模型论文。

   建议：冻结一次代码和配置后，按顺序重跑数据处理、校准、情景模拟、图表和补充材料。重跑后 `outputs/metadata/*_run_metadata.json` 的 `config_hash` 应一致，`git.dirty` 应只包含允许的生成文件或为空。

2. Bayesian posterior predictive 结果现在不能作为可信 CrI 使用。

   `outputs/summaries/bayesian_convergence_summary.txt` 显示：

   - All parameters converged: False
   - Parameters converged: 0 / 110
   - Worst rank-normalized R-hat: 11.4472
   - Minimum bulk ESS: 4

   因此，主文中所有“Bayesian posterior predictive”“95% CrI”的结果都必须暂时删除、降级为 exploratory，或在修复 MCMC 后重算。JAMA 的统计审稿会优先检查这个。

   建议：如果保留贝叶斯分析，至少做到每个国家关键参数 R-hat < 1.05、bulk ESS > 100，并把 trace/rank plots、posterior predictive checks、参数相关图放入补充材料。若短期无法实现，改用预先定义的 probabilistic sensitivity analysis / Latin hypercube uncertainty interval，不要称为 Bayesian CrI。

3. 主文数值与当前输出不一致。

   `manuscript/draft.md` 报告的疫苗效果、基线负担和干预排序与当前 `outputs/summaries/*.csv` 明显不一致。例如当前输出中若按现有 CSV 汇总，next-generation vaccine 与 combined strategy 接近消除负担，而正文仍写 42.8% 和 53.0% 级别的下降。由于输出本身又是 stale config，正确做法不是直接替换为当前 CSV 数字，而是先重跑全链路，再从最终 summary 输出建立锁定核对表并更新正文。

   建议：从最终 summary 输出建立一份锁定的人工核对表，并据此直接更新主文数字，避免正文与输出版本漂移。

4. “校准国家情景”与输出标记冲突。

   当前 `country_scenarios_summary.csv`、`vaccine_scenarios_summary.csv`、`intervention_scenarios_summary.csv` 等多处 `absolute_fit_status` 为 `uncalibrated_scenario_analysis`，而正文称为 calibrated country profiles。这在 WHO 指南框架下属于验证与解释不一致。

   建议：重跑校准后，确保每个国家的 accepted calibration artifact 被生产情景读取；主文只把通过校准的国家称为 calibrated。若某些国家只用于情景探索，正文需明确区分。

5. 报告率敏感性仍然改变真实传播路径。

   `src_python/model/ode_system.py` 第 96-98 行用 `params.reporting_rate` 缩放治疗率。因此 reporting-rate sensitivity 不只是 observation-model perturbation，它会改变治疗、耐药选择和传播。README 和修订笔记中“报告率敏感性只扰动观测模型”的说法需要修正，或代码要拆分。

   建议：把 `reporting_rate`、`diagnosis_rate`、`treatment_access_rate` 分开。报告率敏感性只改变 observed reported cases；检测/治疗情景另设 detection-guided treatment scenario。

## 模型设计审查

### 优点

- 年龄结构比常见 5 组模型更适合百日咳：0-2 月、3-11 月、儿童、青少年、育龄成人、中老年拆分有明确流行病学意义。
- 显式保留母体保护和剂次来源，使 VE_sus、VE_sym、VE_inf、VE_dur 能作用在感染来源历史上，比简单 vaccinated/unvaccinated 二分更有说服力。
- 双菌株结构让疫苗传播阻断与大环内酯耐药可以在同一框架下比较，这是论文的主要创新点。
- 有日历时间、WPP 人口、Prem/contactdata 接触矩阵、WHO/JRF 免疫资料、报告率敏感性和耐药时间线，数据来源链条比较完整。

### 主要风险

- 模型复杂度远高于可观测数据。国家级报告病例很难同时识别传播率、报告率、VE_sus、VE_inf、感染期、耐药 fitness 和导入率。JAMA 统计审稿会问哪些参数是数据识别出来的，哪些只是文献先验或情景假设。
- 耐药 dynamics 目前容易走向固定。即便 low resistance scenario，end-period resistant fraction 的中位数也接近固定。这可能来自 fitness_R=1、耐药导入和治疗选择共同作用。需要证明这不是模型结构强迫出来的结果。
- maternal immunization intervention 同时改变出生保护、婴儿覆盖、年轻成人覆盖、母体保护时长和母婴接触矩阵，导致该情景不是一个单一、可解释的政策干预。
- next-generation vaccine profile 的 VE_sus=0.80、VE_inf=0.65、VE_dur=0.40 是强假设，当前模拟接近消除疾病。它适合作为“upper-bound product profile”，不应写成近期可实施策略。

### 修改建议

1. 在 Methods 中增加“model purpose and decision context”小节。

   推荐表述：本研究不预测某国实际未来疫情，而是比较在统一机制模型下，疫苗传播阻断和耐药管理如何改变婴儿负担与干预排序。

2. 增加一张主文或补充表：参数可识别性分类。

   分类为：

   - directly observed：人口、年龄结构、报告病例、疫苗覆盖、部分耐药比例。
   - calibrated：beta_S、reporting multiplier、seasonality 等。
   - literature-informed fixed：latent duration、infectious duration、waning、VE profiles。
   - scenario-only：next-generation vaccine profile、fitness advantage、resistance-guided treatment efficacy。

3. 把复杂干预拆解。

   maternal immunization 至少拆成：

   - direct infant antibody protection only
   - adult/maternal boosting only
   - cocooning/contact reduction only
   - combined maternal package

   combined strategy 也应拆分为 next-generation vaccine、resistance-guided treatment、maternal、adolescent booster 的 incremental contribution，避免“组合有效但不知道为什么有效”。

4. 耐药模块需要一个历史验证。

   对 China、Japan、Australia 等有时间线的国家，至少做短期 hindcast：用较早年份耐药比例初始化，检验模型能否在合理 fitness/importation/treatment pressure 下接近后续观察值。若做不到，则不要把 near-fixation 写成预测，只写成 stress-test outcome。

## 校准、验证与不确定性

WHO 指南强调，模型用于情景分析前必须证明能复现历史负担，并说明不确定性代表什么。当前项目已有校准代码和诊断图，但还不够投稿。

### 需要补强的验证

- In-sample fit：每个国家报告病例时间序列，显示观察值 vs 模型均值。
- Out-of-sample validation：保留最近 1-2 年或最近若干报告区间，校准前期、预测后期。
- Epidemic plausibility：峰间隔、季节相位、年龄负担分布、报告率后验/校准值是否合理。
- Resistance plausibility：起始耐药比例、末期耐药比例、时间到固定是否与证据相符。
- Code validation：保留单元测试结果；当前 `pytest` 已通过 48 个测试，但 publication validation 失败，后者必须修复。

### 不确定性分析路线

可选路线 A：保留 Bayesian。

- 先修复 MCMC：去掉固定参数的 ESS/R-hat 诊断；减少不可识别参数；考虑分国家分层或先验更强的 calibration；必要时改用 SMC/ensemble MCMC/tempering。
- 只有在收敛达标后，主文才使用 Bayesian CrI。

可选路线 B：改成 JAMA 更容易接受的 deterministic/probabilistic sensitivity。

- 主文报告点估计和跨国家 IQR。
- 补充报告 LHS/PRCC、one-way tornado、关键假设 stress tests。
- 把 uncertainty interval 明确写成 “scenario uncertainty range” 或 “probabilistic sensitivity interval”，不要称为 credible interval。

## JAMA Network Open 写法建议

当前 `manuscript/draft.md` 已经接近 JAMA 风格，但需要更紧。

### 标题

建议：

**Pertussis Vaccine Transmission Blocking, Macrolide Resistance, and Intervention Prioritization: A Decision Analytical Model**

标题避免过长，也不要暗示实际临床试验证据。

### Article Type

保留：

**Original Investigation; Decision Analytical Model**

并在 Methods 第一段写明：reported following relevant non-cost aspects of CHEERS 2022 and WHO immunization modelling guidance。

### Key Points

JAMA 风格下 Key Points 应极短，且只放最终可追溯数字。建议模板：

**Question:** In age-structured pertussis transmission models, how do vaccine transmission-blocking effects and macrolide resistance alter projected infant burden and intervention rankings?

**Findings:** In this decision analytical model using 10 country profiles, interventions that changed transmission or restored resistant-strain treatment effectiveness produced larger model-projected reductions in infant pertussis burden than marginal increases in childhood coverage alone. Effect sizes varied substantially by reporting, resistance, and vaccine-mechanism assumptions.

**Meaning:** Pertussis policy models should distinguish clinical protection from transmission blocking and should report resistance-aware treatment assumptions, validation, and uncertainty explicitly.

在 MCMC 和输出重跑前，Key Points 里不要写精确百分比。

### 摘要结构

使用 JAMA 结构：

- Importance
- Objective
- Design, Setting, and Data Sources
- Exposures
- Main Outcomes and Measures
- Results
- Conclusions and Relevance

Results 中只放：

- 国家数、时间范围和模型设置。
- 主要比较结果，给出 median/IQR 或 validated uncertainty interval。
- 一句说明校准和不确定性状态。

避免把 “near fixation” 写成确定事实；改成 “under the neutral-fitness, country-timeline scenario”。

### 主文结构

JAMA 3000 词内建议分配：

- Introduction：300-400 词。只讲百日咳复燃、aP 传播阻断不完全、MRBP、决策缺口。
- Methods：850-1000 词。模型结构、数据来源、校准、情景、不确定性、验证。
- Results：900-1100 词。按 4 个主图展开。
- Discussion：700-850 词。主要发现、政策解释、与文献对比、限制。
- Conclusions：2-3 句。

### 主图建议

最多 5 个主文图表。建议保留 4 个主图：

1. Country context and calibration validation
2. Vaccine mechanism scenarios
3. Resistance and vaccine transmission-blocking interaction
4. Intervention prioritization

如果加入主文表，优先放 “policy scenario definitions and implementation assumptions”。其余参数表、国家输入、校准诊断、矩阵重建、全网格热图放 supplement。

## 结果解释建议

1. 不要写“某干预应优先实施”，写“在这些假设下优先级较高”。

2. 区分三类结果：

   - calibrated baseline burden：只限校准通过国家。
   - mechanism comparison：用于机制解释，不作为国家预测。
   - stress tests：耐药固定比例、fitness grid、next-generation vaccine。

3. 对负效果要主动解释。

   当前 higher child coverage 在部分输出中可能增加婴儿负担或减少不明显。需要检查是否来自年龄免疫重分配、routine relaxation、校准状态或数值/情景设计。如果是真实模型结果，Discussion 要解释为“marginal gains in already high-coverage profiles may be small and sensitive to age-specific transmission routes”，不要让它显得像代码错误。

4. 时间窗口必须做敏感性。

   WHO 指南提醒同一情景在不同时间窗下可能改变结论。建议报告 5 年、10 年、26 年三个窗口的 intervention ranking，至少放补充材料。

## 投稿前执行清单

1. 冻结配置与代码。
2. 删除或隔离旧输出，重跑 `src_python.data.build_who_inputs`、`src_python.calibration.run_all`、`src_python.simulation.run_all`。
3. 重跑 R 图表和补充材料。
4. `pytest` 通过；`src_python.utils.validation` 通过。
5. 增加验证：所有主文 scenario summary 不得是 `uncalibrated_scenario_analysis`，除非正文明确标为 exploratory。
6. MCMC 若保留，收敛诊断必须通过；否则移出主文，改为敏感性分析。
7. 从最终 summary 自动生成 Abstract、Key Points 和 Results 数字。
8. 补充材料加入 CHEERS non-cost checklist、WHO modelling checklist、数据来源质量/适用性表、参数可识别性表、校准与验证图。
9. Data Sharing Statement 写明代码、配置、处理后输入、生成输出、运行环境和 DOI/URL。
10. AI disclosure 按 JAMA 要求写清工具、版本、用途，并强调作者核查和负责。

## 当前最优策略

建议短期内不要扩大模型复杂度，而是先把“可追溯、可验证、可解释”补齐。JAMA Network Open 更看重临床/公共卫生意义、透明方法和结果稳健性。本文真正有竞争力的主线是：

> 在统一的年龄结构百日咳决策模型中，把疫苗的临床保护和传播阻断分开，并把大环内酯耐药纳入治疗/PEP假设后，干预排序会明显改变；因此，百日咳政策模型不应只报告儿童覆盖率或报告病例，还应同时报告婴儿负担、总感染、耐药感染和机制性不确定性。

这条主线适合 JAMA Network Open。前提是先修复上面的阻断项。
