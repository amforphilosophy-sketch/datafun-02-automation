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
For this custom project, I created a Math Worksheet Generator designed to help high school math teachers create randomized practice worksheets for students. The "dataset" in this case is dynamically generated mathematics problems rather than a static data file.

### Signals
The worksheet generator creates two types of mathematical signals:
- **Linear Algebra Equations**: Problems in the form ax + b = c that students must solve for x
- **Arithmetic Operations**: Basic calculations involving addition, subtraction, multiplication, and division

### Experiments
I experimented with different problem generation approaches:
- Random coefficient generation within appropriate ranges for high school students
- Ensuring division problems result in whole numbers to avoid frustration
- Creating professional formatting with clear headers, instructions, and answer blanks
- Generating synchronized answer keys alongside student worksheets

### Results
The worksheet generator successfully produces:
- Customizable worksheets with 8 algebra problems and 12 arithmetic problems
- Clean, printable text format with professional headers
- Timestamped filenames for easy organization
- Separate answer key files for teacher convenience
- All output saved to the `artifacts/` directory for easy access

Example output includes problems like:
- `5x - 16 = -5` (Answer: x = 2.2)
- `9x - 4 = -50` (Answer: x = -5.11)
- `6x - 12 = 9` (Answer: x = 3.5)

### Interpretation
This tool provides significant value for math educators by:
- **Saving time**: Generating fresh worksheets in seconds instead of manual creation
- **Preventing cheating**: Each run produces different problems with the same difficulty level
- **Ensuring accuracy**: Automatically calculated answer keys eliminate human error
- **Supporting differentiation**: Easy to modify parameters for different skill levels

The worksheet generator demonstrates practical Python skills including random number generation, file I/O, datetime formatting, and modular function design. Most importantly, it solves a real problem that math teachers face daily: creating varied, quality practice materials efficiently.

---

## Custom Project (Phase 5): Random Math Problem-Set Generator

**Author:** Ahmad Saleem Mohmand
**File:** `src/datafun/problem_set_generator_ahmad_mohmand.py`
**Config:** `data/problem_set_config_ahmad_mohmand.json`
**Run command:** `uv run python -m datafun.problem_set_generator_ahmad_mohmand`

### Project Overview
This custom project applies the automation techniques from the example project (`app_case.py`) to a new problem drawn from my own teaching practice as a high school math teacher. It generates **randomized practice worksheets** for three subjects — algebra, geometry, and statistics — with one worksheet per subject and a configurable number of problems per worksheet.

### Skills Applied From the Example
The custom project reuses every repetition pattern demonstrated in the example:

- **for loop over a list** — iterating over the list of subjects from the config
- **list comprehension** — building the list of random values for the statistics problem
- **while loop with a counter** — numbering the problems on each worksheet (1, 2, 3, …)
- **writing text files** — saving one worksheet per subject to `data/processed/`
- **logging, pathlib, type hints, Final constants, main function, conditional execution guard** — the same professional Python conventions modeled by the example

### New Skills Introduced
Beyond the example, the project introduces:

- **`json` module** — reads project settings from an external configuration file rather than hard-coding them in the script
- **`random` module** — produces a different worksheet every run, which is the point of a practice generator
- **`datetime` module** — stamps each generated worksheet with the date it was created
- **dispatch dictionary** — maps each subject name to its problem-generator function, keeping the main loop short and extensible (adding a new subject only requires adding one entry)

### How It Works
The script follows four clear stages:

1. **Read the config.** `read_config()` opens the JSON file at `data/problem_set_config_ahmad_mohmand.json` and returns a dictionary holding the title, author, list of subjects, problems-per-worksheet count, and a difficulty range.
2. **Loop over the subjects.** A `for` loop iterates over the list of subjects from the config.
3. **Build each worksheet.** `build_worksheet()` uses a `while` loop with a counter to generate N numbered problems, calling the appropriate problem-generator function for the subject (looked up in the `PROBLEM_GENERATORS` dispatch dictionary).
4. **Write each worksheet to its own file** in `data/processed/`, named `worksheet_<subject>_ahmad_mohmand.txt`.

### Example Output
A generated algebra worksheet looks like:

```text
