"""
Ahmad Mohmand
Analysis Extension Module
This module provides statistical analysis functions for educational data.
"""

import statistics


def analyze_grades(grades: list[float]) -> dict:
    """
    Analyze a list of student grades and return statistics.

    Args:
        grades: List of numerical grades

    Returns:
        Dictionary containing mean, median, and grade distribution
    """
    if not grades:
        return {"error": "No grades provided"}

    result = {
        "mean": round(statistics.mean(grades), 2),
        "median": round(statistics.median(grades), 2),
        "std_dev": round(statistics.stdev(grades), 2) if len(grades) > 1 else 0,
        "min": min(grades),
        "max": max(grades),
        "count": len(grades),
    }

    return result


def main():
    """Demonstrate the grade analysis function."""
    # Sample student grades
    sample_grades = [88, 92, 76, 95, 84, 89, 91, 78, 85, 93]

    print("=" * 50)
    print("Grade Analysis Tool - Ahmad Mohmand")
    print("=" * 50)
    print(f"\nAnalyzing {len(sample_grades)} student grades...")
    print(f"Grades: {sample_grades}\n")

    stats = analyze_grades(sample_grades)

    print("Statistical Results:")
    print(f"  Mean (Average): {stats['mean']}")
    print(f"  Median: {stats['median']}")
    print(f"  Standard Deviation: {stats['std_dev']}")
    print(f"  Range: {stats['min']} - {stats['max']}")
    print(f"  Total Students: {stats['count']}")
    print("=" * 50)


if __name__ == "__main__":
    main()
