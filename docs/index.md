# Data Analytics Fundamentals

This site provides documentation for this project.
Use the navigation to explore module-specific materials.

## How-To Guide

Many instructions are common to all projects.
See [⭐ **Workflow: Apply Example**](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/)
to get this project running on your machine.

## Project Materials

- [project-instructions](./project-instructions.md)
- [your-files](./your-files.md)
- [module](./module/index.md)
- [glossary](./glossary.md)
- [api](./api.md)
---
## Custom Project

### Dataset

This project uses a small, project-owned configuration file as its dataset, rather than an external CSV or API. The dataset lives at:

`data/problem_set_config_ahmad_mohmand.json`

It is a JSON file that holds the parameters the worksheet generator needs to do its job:

- **title** — the worksheet series title (e.g. "Math Practice Worksheets")
- **author** — the author name to print on each worksheet header (Ahmad Saleem Mohmand)
- **subjects** — a list of subjects to generate one worksheet for each (algebra, geometry, statistics)
- **problems_per_worksheet** — how many problems each worksheet should contain (5)
- **difficulty** — a small dictionary holding the random-number ranges used to build problems (coefficients 1–12, constants 1–20)

This structure mirrors the way a real teacher might want to control a tool: change the config to change what gets generated, without touching any Python code.

### Phase 4 Modifications

In Phase 4, I copied the instructor example file `src/datafun/app_case.py` to my own file `src/datafun/app_ahmad_mohmand.py`, updated the header to reflect my own authorship (author, date, filename, run command), and made one focused technical modification to the list-loop function:

- Renamed the global constant `PET_LIST` to `SUBJECT_LIST`
- Renamed the loop variable `pet_name` to `subject_name`
- Changed the list values from `["dog", "cat", "fish"]` to `["algebra", "geometry", "statistics"]`

The modification is a category-A "change an input/setting" change. When I ran the modified file, the for-loop function created `case_algebra.txt`, `case_geometry.txt`, and `case_statistics.txt` in `data/processed/` instead of the original pet files. The list comprehension function automatically picked up the same change and produced `case_favorite_algebra.txt`, `case_favorite_geometry.txt`, and `case_favorite_statistics.txt`. The program completed with "Executed successfully!" and no errors.

The key insight from Phase 4 was that a single named constant defined once at the top of a file can be referenced by every function below it — so a small change in one place propagates through the entire program. This is the value of using a named constant rather than hard-coding values, and it sets up the Phase 5 design where all settings live in an external JSON config.

### Phase 5 Custom Project

In Phase 5, I applied the techniques from the example to a genuinely new problem drawn from my own teaching practice as a high school math teacher: generating **randomized math practice worksheets** for three subjects (algebra, geometry, statistics).

**File:** `src/datafun/problem_set_generator_ahmad_mohmand.py`
**Config:** `data/problem_set_config_ahmad_mohmand.json`
**Run command:** `uv run python -m datafun.problem_set_generator_ahmad_mohmand`

**Skills applied from the example.** The custom project reuses every repetition pattern demonstrated in the example: a for loop over a list (iterating over the subjects from the config), a list comprehension (building the list of random values for the statistics problem), a while loop with a counter (numbering the problems on each worksheet), and writing text files (saving one worksheet per subject to `data/processed/`). It uses the same professional conventions modeled by the example — logging, pathlib, type hints, Final constants, main function, and a conditional execution guard.

**New skills introduced.** Beyond the example, the project introduces the `json` module (reading project settings from an external configuration file rather than hard-coding them), the `random` module (so every run produces a different worksheet), the `datetime` module (stamping each worksheet with the generation date), and a dispatch dictionary (mapping each subject name to its problem-generator function, keeping the main loop short and extensible).

**How it works.** The script follows four clear stages:

1. `read_config()` opens the JSON file at `data/problem_set_config_ahmad_mohmand.json` and returns a dictionary holding the title, author, list of subjects, problems-per-worksheet count, and difficulty range.
2. A `for` loop iterates over the list of subjects from the config.
3. `build_worksheet()` uses a `while` loop with a counter to generate N numbered problems, calling the appropriate problem-generator function for the subject (looked up in the `PROBLEM_GENERATORS` dispatch dictionary).
4. Each worksheet is written to its own file in `data/processed/`, named `worksheet_<subject>_ahmad_mohmand.txt`.

**Example output.** A generated algebra worksheet looks like:

```text
Math Practice Worksheets - Algebra
Author: Ahmad Saleem Mohmand
Generated: 2026-05-28

Instructions: Show your work for each of the 5 problems below.

Problem 1: Solve for x:  7x + 4 = 60
Problem 2: Solve for x:  3x + 11 = 41
Problem 3: Solve for x:  5x + 2 = 32
Problem 4: Solve for x:  9x + 6 = 78
Problem 5: Solve for x:  4x + 13 = 49
```

Algebra problems are constructed so the answer is always a positive integer (the script computes `c = a * x + b` after picking random `a`, `x`, `b`), making the worksheet usable in a real classroom. Each run produces a different set of problems.

**Files produced.** Each run regenerates three worksheets in `data/processed/`: `worksheet_algebra_ahmad_mohmand.txt`, `worksheet_geometry_ahmad_mohmand.txt`, and `worksheet_statistics_ahmad_mohmand.txt`.

**Why this project.** As a high school math teacher, I want practice tools that adapt to whatever subject and difficulty I happen to be teaching. This generator is a small but functional step in that direction — and it demonstrates that the automation patterns taught in this course generalize directly to real teaching work.
