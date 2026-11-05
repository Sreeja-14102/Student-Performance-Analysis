import pandas as pd

# Step 1: Load the analysis dataset
data = pd.read_csv("student_analysis.csv")

# Step 2: Calculate total marks
subjects = ["math", "science", "english", "computer"]

data["total_marks"] = data[subjects].sum(axis=1)

# Step 3: Calculate average marks
data["average_marks"] = data[subjects].mean(axis=1)

# Step 4: Assign grades
def calculate_grade(average):

    if average >= 90:
        return "A"

    elif average >= 80:
        return "B"

    elif average >= 70:
        return "C"

    elif average >= 60:
        return "D"

    else:
        return "F"


data["grade"] = data["average_marks"].apply(calculate_grade)

# Step 5: Assign student rankings
data["rank"] = data["average_marks"].rank(
    ascending=False,
    method="dense"
).astype(int)

# Step 6: Classify student performance
def performance_category(average):

    if average >= 90:
        return "Excellent"

    elif average >= 80:
        return "Very Good"

    elif average >= 70:
        return "Good"

    elif average >= 60:
        return "Average"

    else:
        return "Needs Improvement"


data["performance"] = data["average_marks"].apply(
    performance_category
)

# Step 7: Sort students by rank
data = data.sort_values(by="rank")

# Step 8: Display student report
print("\nSTUDENT PERFORMANCE REPORT")

print(
    data[[
        "student_id",
        "name",
        "total_marks",
        "average_marks",
        "grade",
        "rank",
        "performance"
    ]].to_string(index=False)
)

# Step 9: Save final report
data.to_csv("final_student_report.csv", index=False)

print("\nFinal student report saved successfully!")