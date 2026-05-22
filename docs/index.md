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
