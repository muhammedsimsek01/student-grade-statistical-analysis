import statistics
import matplotlib.pyplot as plt
from collections import Counter


"""
Student Grade Statistical Analysis System
Author: Muhammed Zeyni Simsek

This program:
- Collects grades from 20 students
- Validates user input
- Calculates mean, median, mode, and standard deviation
- Visualizes the grades with a bar chart
- Saves the chart as an image file
"""


def get_grades(student_count=20):
    """
    Collects grades from the user.

    Only values between 0 and 100 are accepted.
    Invalid input is rejected without stopping the program.
    """

    grades = []

    print(f"\nEnter grades for {student_count} students.")
    print("Grades must be between 0 and 100.\n")

    for student_number in range(1, student_count + 1):

        while True:

            try:
                grade = float(
                    input(
                        f"Enter grade for student "
                        f"{student_number}: "
                    )
                )

                if 0 <= grade <= 100:
                    grades.append(grade)
                    break

                print(
                    "Invalid grade. "
                    "Please enter a value between 0 and 100."
                )

            except ValueError:

                print(
                    "Invalid input. "
                    "Please enter a numeric value."
                )

    return grades


def calculate_mode(grades):
    """
    Calculates the mode of the grade list.

    If multiple values have the same highest frequency,
    all of them are returned.

    If every grade appears only once,
    the function returns None.
    """

    frequency_counter = Counter(grades)

    highest_frequency = max(
        frequency_counter.values()
    )

    if highest_frequency == 1:
        return None

    modes = [
        value
        for value, frequency
        in frequency_counter.items()
        if frequency == highest_frequency
    ]

    return sorted(modes)


def calculate_statistics(grades):
    """
    Calculates the main statistical values.

    Returns:
    - Mean
    - Median
    - Mode
    - Sample standard deviation
    """

    mean = statistics.mean(grades)

    median = statistics.median(grades)

    mode = calculate_mode(grades)

    standard_deviation = statistics.stdev(
        grades
    )

    return (
        mean,
        median,
        mode,
        standard_deviation
    )


def print_results(
    grades,
    mean,
    median,
    mode,
    standard_deviation
):
    """
    Displays the statistical results
    in a clear and organized format.
    """

    print("\n" + "=" * 50)

    print(
        "STUDENT GRADE STATISTICAL ANALYSIS"
    )

    print("=" * 50)

    print(
        f"\nEntered Grades:\n{grades}"
    )

    print(
        f"\nMean: {mean:.2f}"
    )

    print(
        f"Median: {median:.2f}"
    )

    if mode is not None:

        mode_text = ", ".join(
            f"{value:.2f}"
            for value in mode
        )

        print(
            f"Mode: {mode_text}"
        )

    else:

        print(
            "Mode: No clear mode "
            "(all grades are unique)"
        )

    print(
        f"Standard Deviation: "
        f"{standard_deviation:.2f}"
    )

    print("\n" + "=" * 50)


def create_chart(
    grades,
    mean,
    median,
    mode,
    standard_deviation
):
    """
    Creates a bar chart showing student grades.

    Horizontal reference lines show:
    - Mean
    - Median
    - Mode
    - Mean + standard deviation
    - Mean - standard deviation
    """

    student_numbers = list(
        range(1, len(grades) + 1)
    )

    plt.figure(
        figsize=(12, 6)
    )

    plt.bar(
        student_numbers,
        grades,
        label="Student Grades"
    )

    # Mean line
    plt.axhline(
        mean,
        linestyle="--",
        linewidth=2,
        label=f"Mean = {mean:.2f}"
    )

    # Median line
    plt.axhline(
        median,
        linestyle="-.",
        linewidth=2,
        label=f"Median = {median:.2f}"
    )

    # Mode line or lines
    if mode is not None:

        for index, value in enumerate(mode):

            label = (
                f"Mode = {value:.2f}"
                if index == 0
                else None
            )

            plt.axhline(
                value,
                linestyle=":",
                linewidth=2,
                label=label
            )

    # Mean + standard deviation
    plt.axhline(
        mean + standard_deviation,
        linestyle=":",
        linewidth=1.5,
        label=(
            "Mean + Standard Deviation = "
            f"{mean + standard_deviation:.2f}"
        )
    )

    # Mean - standard deviation
    plt.axhline(
        mean - standard_deviation,
        linestyle=":",
        linewidth=1.5,
        label=(
            "Mean - Standard Deviation = "
            f"{mean - standard_deviation:.2f}"
        )
    )

    plt.title(
        "Student Grade Statistical Analysis"
    )

    plt.xlabel(
        "Student Number"
    )

    plt.ylabel(
        "Grade"
    )

    plt.xticks(
        student_numbers
    )

    plt.ylim(
        0,
        100
    )

    plt.legend()

    plt.grid(
        axis="y",
        linestyle="--",
        alpha=0.5
    )

    plt.tight_layout()

    plt.savefig(
        "student_grade_analysis.png",
        dpi=150
    )

    print(
        "\nChart saved as "
        "'student_grade_analysis.png'."
    )

    plt.show()


def main():
    """
    Main function that runs the program.
    """

    grades = get_grades(20)

    (
        mean,
        median,
        mode,
        standard_deviation
    ) = calculate_statistics(
        grades
    )

    print_results(
        grades,
        mean,
        median,
        mode,
        standard_deviation
    )

    create_chart(
        grades,
        mean,
        median,
        mode,
        standard_deviation
    )


if __name__ == "__main__":
    main()