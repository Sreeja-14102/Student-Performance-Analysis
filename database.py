import pandas as pd
import sqlite3

# Step 1: Load the final student report
data = pd.read_csv("final_student_report.csv")

# Step 2: Connect to SQLite database
connection = sqlite3.connect("student_database.db")

# Step 3: Create a table and insert student data
data.to_sql(
    "student_performance",
    connection,
    if_exists="replace",
    index=False
)

print("Student data inserted into database successfully!")

# Step 4: Retrieve all student records using SQL
query = "SELECT * FROM student_performance"

result = pd.read_sql_query(query, connection)

# Step 5: Display database records
print("\nSTUDENT DATABASE RECORDS")
print(result.to_string(index=False))

# Step 6: Count total students
count_query = "SELECT COUNT(*) FROM student_performance"

count = pd.read_sql_query(count_query, connection)

print("\nTOTAL STUDENTS:", count.iloc[0, 0])

# Step 7: Close database connection
connection.close()

print("\nDatabase connection closed!")
