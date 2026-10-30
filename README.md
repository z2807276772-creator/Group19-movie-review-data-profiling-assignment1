# Assignment 1: Data Profiling (EDA) Report (10 marks)

**Course:** Data Engineering  
**Industry Domain:** Entertainment / Streaming Services

| Name | Matric Number |
|---|---|
| ZHANG YUN | A205865 |
| LIU QINGRONG | A206149 |
| ZHOU SHILI | A207335 |
| KOU JINGWEN | A207356 |
| ZHANG NIANTIAN | A214108 |

## Scenario and purpose

A movie streaming platform receives thousands of user comments on its movies. Which movies are viewers most unhappy with, so the platform can improve its recommendations?

This submission focuses on diagnosing and handling data quality, not sentiment modelling, movie rankings, or a recommendation system. It profiles a real public IMDb-derived sample, reports observed issues honestly, and explains why it remains insufficient for a production movie-only dissatisfaction question.

## Start here

Open `Assignment1_Data_Profiling.ipynb`. It includes the three-sentence scenario, source URL/acquisition, initial profiling, missingness decisions, IQR length flags, duplicates/types/formats/validity checks, three labeled diagnostic figures, PII and bias handling, before/after validation, and conclusion. Outputs are saved after actual fresh-kernel execution.

## Run from scratch

Use Python 3.12 and a terminal in this folder:

```text
python -m venv .venv
```

Activate on Windows with `.venv\Scripts\activate`, or on macOS/Linux with `source .venv/bin/activate`, then:

```text
python -m pip install -r requirements.txt
python -m ipykernel install --user --name assignment1 --display-name "Assignment 1"
jupyter notebook Assignment1_Data_Profiling.ipynb
```

Select the Assignment 1 kernel and Restart Kernel / Run All. Run from the project root, preserving `data/source_manifest.json`. First run downloads approximately 1.4 MB; subsequent runs verify the cached data. No credentials are needed. Allow around 1 minute and 1 GB memory. If download fails, check network access to codeload.github.com and retry. If file verification fails, inspect/remove only the local cached `data/raw/recsys.zip` and re-download; never bypass hash checks. A changed source requires deliberate re-profiling.

Headless execution using the active Python environment:

```text
python scripts/verify_notebook.py
```

This starts a fresh kernel, executes every code cell, saves outputs, asserts source dimensions and all quality contracts, and writes `reports/execution_check.json`. It does not depend on an existing interactive session. In Colab, upload/unzip the whole submission project, set the working directory to its root, install requirements and Run All; opening the notebook alone without its manifest is insufficient.

## Data provenance and rights

- Repository: https://github.com/SimpliSolve/RecSysData
- Pinned commit: `64fa993402e02ee77d210ad507ca33452c95f4f8`
- Acquisition: https://codeload.github.com/SimpliSolve/RecSysData/zip/64fa993402e02ee77d210ad507ca33452c95f4f8
- Source documentation: https://github.com/SimpliSolve/RecSysData/blob/64fa993402e02ee77d210ad507ca33452c95f4f8/README.md
- Original content provider and conditions: https://www.imdb.com/conditions
- Accessed: 31 October 2026.

All 39 review CSVs contain 327 comments across 39 screen-title folders. All 20 daily metadata CSVs contain 50 metadata records. Actual review columns include local review sequence, rating, title/body, user handle/profile link, extraction date and spoiler flag. Metadata provides movie title/link. Title matching is conservative; incomplete IDs and movie/TV catalog contamination remain explicit limitations.

The maintainer states educational/research use only and cautions against republication without compliance with IMDb terms. No permissive redistribution license was verified. Raw data and cleaned comments are retained **locally only**, excluded from Git and the submission ZIP. Automatic download is provided; it does not grant additional rights. Only code, file hashes, text-free aggregate outputs and rendered diagnostic charts are intended for upload. Do not add a blanket open-data license to the source reviews.

## Directory

```text
Assignment1_Data_Profiling.ipynb  # main report, code and executed outputs
README.md                       # purpose, running, rights and submission status
requirements.txt                # tested direct dependencies (Notebook UI range)
.gitignore                      # prevents accidental private-data upload
data/source_manifest.json       # pinned selected paths, byte sizes and SHA-256
data/raw/                       # private local source ZIP, ignored
data/processed/                 # private local text tables and audit, ignored
reports/figures/                 # three diagnostic PNGs
reports/*.csv                   # aggregate completeness/coverage/validation tables
reports/quality_summary.json    # computed results and quality contracts
reports/execution_check.json    # actual fresh-kernel execution result
scripts/verify_notebook.py      # repeatable execution/check command
work/                          # local working material, excluded from submission
```

## Key interpretation

Missing ratings are kept as missing rather than imputed opinions. Profile identifiers are removed, selected explicit contact/link patterns are masked, and text normalization preserves case/negation. Valid extreme reviews are flagged and retained; no fabricated duplicates or invalid scores are introduced. A technically rating-ready view is not representative or verified movie-only data. Pattern masking is not full anonymization, and no row-level text is published. See the executed notebook for all measured counts and decisions.

## Course alignment

The original supplied Assignment 1 PDF was inspected. Notebook sections 1–9 cover each required item; Figures 1–3 expose missingness, extreme text lengths, and group imbalance. All team names and matric numbers are reproduced above and in the notebook. The course requires submitting **only the GitHub repository link** containing a notebook runnable from top to bottom. No course deadline, hidden rubric, or submission portal status is inferred.

## GitHub repository and course submission

Repository: https://github.com/z2807276772-creator/movie-review-data-profiling-assignment1

This repository contains the executed notebook, run instructions, pinned source manifest, verification script and text-free diagnostic outputs. Local fresh-kernel execution and an independent run starting without the source archive both passed; see `reports/execution_check.json` and `reports/reproduction_check.json`. Raw and processed review data are local-only and excluded from Git.

The repository is private. The lecturer needs explicit access before they can inspect or grade it; alternatively, the owner can choose public visibility if permitted by course and team preferences. Public visibility exposes the required team names and matric numbers.

The course requires submitting only the repository URL through the normal course submission channel. Uploading files to GitHub is separate from course submission. No course-platform submission has been made.
