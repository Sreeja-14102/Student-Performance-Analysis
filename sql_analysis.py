import sqlite3

# Step 1: Connect to database
connection = sqlite3.connect("student_database.db")

# Step 2: Create cursor
cursor = connection.cursor()

# Step 3: Create a function to execute SQL queries
def run_query(title, query):

    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)

    cursor.execute(query)

    # Get column names
    columns = [item[0] for item in cursor.description]

    print(columns)

    # Display query results
    for row in cursor.fetchall():
        print(row)


# Query 1: Select all student records
run_query(
    "QUERY 1: SELECT",
    "SELECT * FROM student_performance"
)

# Query 2: WHERE
run_query(
    "QUERY 2: WHERE",
    """
    SELECT name, average_marks
    FROM student_performance
    WHERE average_marks > 80
    """
)

# Query 3: AND and OR
run_query(
    "QUERY 3: AND AND OR",
    """
    SELECT name, grade, attendance
    FROM student_performance
    WHERE (grade = 'A' OR grade = 'B')
    AND attendance >= 80
    """
)

# Query 4: ORDER BY
run_query(
    "QUERY 4: ORDER BY",
    """
    SELECT name, average_marks
    FROM student_performance
    ORDER BY average_marks DESC
    """
)

# Query 5: LIMIT
run_query(
    "QUERY 5: LIMIT",
    """
    SELECT name, average_marks
    FROM student_performance
    ORDER BY average_marks DESC
    LIMIT 5
    """
)

# Query 6: COUNT
run_query(
    "QUERY 6: COUNT",
    """
    SELECT COUNT(*)
    FROM student_performance
    """
)

# Query 7: AVG
run_query(
    "QUERY 7: AVG",
    """
    SELECT AVG(math)
    FROM student_performance
    """
)

# Query 8: MAX
run_query(
    "QUERY 8: MAX",
    """
    SELECT MAX(math)
    FROM student_performance
    """
)

# Query 9: MIN
run_query(
    "QUERY 9: MIN",
    """
    SELECT MIN(math)
    FROM student_performance
    """
)

# Query 10: SUM
run_query(
    "QUERY 10: SUM",
    """
    SELECT SUM(total_marks)
    FROM student_performance
    """
)

# Query 11: GROUP BY
run_query(
    "QUERY 11: GROUP BY",
    """
    SELECT grade, COUNT(*) AS student_count
    FROM student_performance
    GROUP BY grade
    """
)

# Query 12: HAVING
run_query(
    "QUERY 12: HAVING",
    """
    SELECT grade, COUNT(*) AS student_count
    FROM student_performance
    GROUP BY grade
    HAVING COUNT(*) >= 2
    """
)

# Query 13: DISTINCT
run_query(
    "QUERY 13: DISTINCT",
    """
    SELECT DISTINCT gender
    FROM student_performance
    """
)

# Query 14: BETWEEN
run_query(
    "QUERY 14: BETWEEN",
    """
    SELECT name, average_marks
    FROM student_performance
    WHERE average_marks BETWEEN 80 AND 90
    """
)

# Query 15: SUBQUERY
run_query(
    "QUERY 15: SUBQUERY",
    """
    SELECT name, average_marks
    FROM student_performance
    WHERE average_marks > (
        SELECT AVG(average_marks)
        FROM student_performance
    )
    """
)

# Step 4: Close database connection
connection.close()

print("\nALL 15 SQL QUERIES EXECUTED SUCCESSFULLY!")
