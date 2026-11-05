import pandas as pd
import matplotlib.pyplot as plt
import os

# Step 1: Load student analysis data
data = pd.read_csv("final_student_report.csv")

# Step 2: Create a folder to store charts
os.makedirs("charts", exist_ok=True)

# Step 3: Select subject columns
subjects = ["math", "science", "english", "computer"]

# Step 4: Calculate subject-wise average
subject_average = data[subjects].mean()

# CHART 1: Subject-wise average marks
plt.figure(figsize=(8, 5))

plt.bar(subject_average.index, subject_average.values)

plt.title("Subject-wise Average Marks")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")

plt.ylim(0, 100)
plt.tight_layout()

plt.savefig("charts/subject_average.png")
plt.show()
plt.close()


# CHART 2: Student-wise average marks
plt.figure(figsize=(10, 5))

plt.bar(data["name"], data["average_marks"])

plt.title("Student-wise Average Marks")
plt.xlabel("Students")
plt.ylabel("Average Marks")

plt.xticks(rotation=45)
plt.ylim(0, 100)
plt.tight_layout()

plt.savefig("charts/student_average.png")
plt.show()
plt.close()


# CHART 3: Grade distribution
grade_counts = data["grade"].value_counts().sort_index()

plt.figure(figsize=(7, 7))

plt.pie(
    grade_counts.values,
    labels=grade_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Student Grade Distribution")

plt.savefig("charts/grade_distribution.png")
plt.show()
plt.close()


# CHART 4: Attendance analysis
plt.figure(figsize=(10, 5))

plt.bar(data["name"], data["attendance"])

plt.title("Student Attendance Analysis")
plt.xlabel("Students")
plt.ylabel("Attendance Percentage")

plt.xticks(rotation=45)
plt.ylim(0, 100)
plt.tight_layout()

plt.savefig("charts/attendance.png")
plt.show()
plt.close()


print("\nALL FOUR CHARTS CREATED SUCCESSFULLY!")
