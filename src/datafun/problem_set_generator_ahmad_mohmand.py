"""src/datafun/problem_set_generator_ahmad_mohmand.py - Custom project: random math problem-set generator.

Author: Ahmad Saleem Mohmand
Date: 2026-05

Phase 5 custom project for datafun-02-automation.

This script reads a JSON configuration file listing math subjects (algebra,
geometry, statistics) and a difficulty range, then generates one practice
worksheet per subject with N randomized problems. Each worksheet is written
as a text file to data/processed/.

Skills applied from the example project:
  - imports, logging, pathlib for cross-platform paths
  - type hints, global constants with Final
  - reading external configuration (JSON)
  - for loop over a list (subjects)
  - list comprehension (building problem strings)
  - while loop with a counter (problem numbering)
  - writing text files
  - main function with conditional execution guard

New skill introduced beyond the example:
  - random number generation with the `random` module
  - reading JSON with the `json` module

Terminal command to run this file from the root project folder:

    uv run python -m datafun.problem_set_generator_ahmad_mohmand
"""

# === DECLARE IMPORTS (BRING IN FREE CODE) ===

from datetime import datetime
import json
import logging
from pathlib import Path
import random
from typing import Final

from datafun_toolkit.logger import get_logger, log_header

# === CONFIGURE LOGGER ONCE PER MODULE ===

LOG: logging.Logger = get_logger("P05", level="INFO")

# === DECLARE GLOBAL CONSTANTS ===

ROOT_DIR: Final[Path] = Path.cwd()
DATA_DIR: Final[Path] = ROOT_DIR / "data"
PROCESSED_DIR: Final[Path] = DATA_DIR / "processed"
CONFIG_FILE: Final[Path] = DATA_DIR / "problem_set_config_ahmad_mohmand.json"
# === DECLARE A HELPER FUNCTION TO READ CONFIG ===


def read_config(*, path: Path) -> dict:
    """Read a JSON configuration file and return its contents as a dictionary.

    Arguments:
        path: Full path to the JSON file to read.

    Returns:
        A dictionary holding the configuration values.
    """
    LOG.info(f"Reading config from: {path.name}")
    with path.open(encoding="utf-8") as f:
        config: dict = json.load(f)
    LOG.info(f"Config loaded with {len(config['subjects'])} subjects")
    return config


# === DECLARE A HELPER FUNCTION TO WRITE A FILE ===


def write_text_file(*, path: Path, content: str) -> None:
    """Write content to a text file, creating parent directories as needed.

    Arguments:
        path: Full path to the file to create or overwrite.
        content: Text content to write.

    Returns:
        None
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    LOG.info(f"Wrote file: {path.name}")


# === DECLARE PROBLEM-GENERATING FUNCTIONS (ONE PER SUBJECT) ===


def make_algebra_problem(*, difficulty: dict) -> str:
    """Generate one random algebra problem of the form 'ax + b = c'.

    Arguments:
        difficulty: A dict with coefficient and constant ranges.

    Returns:
        A string describing the problem.
    """
    a: int = random.randint(
        difficulty["coefficient_min"], difficulty["coefficient_max"]
    )
    x: int = random.randint(difficulty["constant_min"], difficulty["constant_max"])
    b: int = random.randint(difficulty["constant_min"], difficulty["constant_max"])
    c: int = a * x + b
    return f"Solve for x:  {a}x + {b} = {c}"


def make_geometry_problem(*, difficulty: dict) -> str:
    """Generate one random geometry problem (rectangle area).

    Arguments:
        difficulty: A dict with coefficient and constant ranges.

    Returns:
        A string describing the problem.
    """
    length: int = random.randint(difficulty["constant_min"], difficulty["constant_max"])
    width: int = random.randint(difficulty["constant_min"], difficulty["constant_max"])
    return f"Find the area of a rectangle with length {length} and width {width}."


def make_statistics_problem(*, difficulty: dict) -> str:
    """Generate one random statistics problem (mean of a small list).

    Arguments:
        difficulty: A dict with coefficient and constant ranges.

    Returns:
        A string describing the problem.
    """
    values: list[int] = [
        random.randint(difficulty["constant_min"], difficulty["constant_max"])
        for _ in range(5)
    ]
    return f"Find the mean of:  {values}"


# === DISPATCH TABLE: MAP A SUBJECT NAME TO ITS GENERATOR FUNCTION ===

PROBLEM_GENERATORS: Final[dict] = {
    "algebra": make_algebra_problem,
    "geometry": make_geometry_problem,
    "statistics": make_statistics_problem,
}
# === DECLARE THE WORKSHEET-BUILDING FUNCTION ===


def build_worksheet(
    *, subject: str, num_problems: int, difficulty: dict, title: str, author: str
) -> str:
    """Build a single worksheet's text content as one string.

    Arguments:
        subject: Subject name (e.g. 'algebra').
        num_problems: How many problems to include.
        difficulty: Difficulty configuration dictionary.
        title: Worksheet series title (e.g. 'Math Practice Worksheets').
        author: Author name to print in the header.

    Returns:
        The full worksheet content as a single string ready to write to a file.
    """
    LOG.info("========================")
    LOG.info(f"Building worksheet for subject: {subject}")
    LOG.info("========================")

    # Look up which generator function to use for this subject
    generator = PROBLEM_GENERATORS[subject]

    # Build the header lines for the worksheet
    today: str = datetime.now().strftime("%Y-%m-%d")
    header_lines: list[str] = [
        f"{title} - {subject.title()}",
        f"Author: {author}",
        f"Generated: {today}",
        "",
        f"Instructions: Show your work for each of the {num_problems} problems below.",
        "",
    ]

    # Build the numbered problem lines using a while loop with a counter
    problem_lines: list[str] = []
    i: int = 1
    while i <= num_problems:
        problem_text: str = generator(difficulty=difficulty)
        problem_lines.append(f"Problem {i}: {problem_text}")
        i += 1  # WHY: increment to avoid an infinite loop

    # Combine the header and the problems into one big string
    all_lines: list[str] = header_lines + problem_lines
    return "\n".join(all_lines) + "\n"


# === DEFINE THE MAIN FUNCTION ===


def main() -> None:
    """Entry point: read config, generate one worksheet per subject, write each to file.

    Arguments: None
    Returns: None
    """
    log_header(LOG, "P05")

    LOG.info("========================")
    LOG.info("START main()")
    LOG.info("========================")

    # Step 1: read the config
    config: dict = read_config(path=CONFIG_FILE)
    title: str = config["title"]
    author: str = config["author"]
    subjects: list[str] = config["subjects"]
    num_problems: int = config["problems_per_worksheet"]
    difficulty: dict = config["difficulty"]

    # Step 2: for each subject in the list, build and write a worksheet
    for subject in subjects:
        content: str = build_worksheet(
            subject=subject,
            num_problems=num_problems,
            difficulty=difficulty,
            title=title,
            author=author,
        )
        filename: str = f"worksheet_{subject}_ahmad_mohmand.txt"
        path: Path = PROCESSED_DIR / filename
        write_text_file(path=path, content=content)

    LOG.info("========================")
    LOG.info(f"Generated {len(subjects)} worksheets successfully!")
    LOG.info("========================")


# === CONDITIONAL EXECUTION GUARD ===

# WHY: Only call main() when running this file directly as a script.
# This is standard Python boilerplate.

if __name__ == "__main__":
    main()
