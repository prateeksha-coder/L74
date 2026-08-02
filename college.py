import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("college.db")
cursor = conn.cursor()

# ==========================
# Create Tables
# ==========================
cursor.executescript("""
DROP TABLE IF EXISTS Department;
DROP TABLE IF EXISTS Faculty;
DROP TABLE IF EXISTS Student;""")

cursor.execute("""
CREATE TABLE Department (
    DeptID INTEGER PRIMARY KEY,
    DeptName TEXT,
    Building TEXT
)
""")

cursor.execute("""
CREATE TABLE Faculty (
    FacultyID INTEGER PRIMARY KEY,
    FacultyName TEXT,
    Subject TEXT,
    Salary INTEGER,
    DeptID INTEGER
    
)
""")

cursor.execute("""
CREATE TABLE Student (
    StudentID INTEGER PRIMARY KEY,
    StudentName TEXT,
    Age INTEGER,
    City TEXT,
    Marks INTEGER,
    DeptID INTEGER)

""")

# ==========================
# Insert Values
# ==========================
cursor.executescript("""
INSERT INTO Department VALUES
    (101, "Computer Science", "Block A"),
    (102, "Electronics", "Block B"),
    (103, "Mechanical", "Block C");

INSERT INTO faculty VALUES
    (1, "Anita Sharma", "Python", 70000, 101),
    (2, "Rahul Verma", "Java", 65000, 101),
    (3, "Priya Singh", "Digital Electronics", 68000, 102),
    (4, "Vikram Patel", "Thermodynamics", 72000, 103),
    (5, "Neha Gupta", "DBMS", 75000, 101);


INSERT INTO Student VALUES
    (201, "Aarav", 20, "Delhi", 88, 101),
    (202, "Diya", 19, "Mumbai", 91, 102),
    (203, "Kabir", 21, "Delhi", 75, 101),
    (204, "Meera", 20, "Pune", 95, 103),
    (205, "Rohan", 22, "Chennai", 68, 102),
    (206, "Ananya", 20, "Delhi", 84, 101),
    (207, "Ishaan", 19, "Mumbai", 79, 103);
    """)



conn.commit()

# ==========================
# SELECT *
# ==========================

print("\nAll Students")
for row in cursor.execute("SELECT * FROM Student"):
    print(row)

# ==========================
# WHERE
# ==========================

print("\nStudents with Marks > 80")
for row in cursor.execute("SELECT * FROM Student WHERE Marks > 80"):
    print(row)

# ==========================
# LIKE
# ==========================

print("\nStudent names starting with A")
for row in cursor.execute("SELECT * FROM Student WHERE StudentName LIKE 'A%'"):
    print(row)

# ==========================
# MIN
# ==========================

print("\nMinimum Marks")
for row in cursor.execute("SELECT MIN(Marks) FROM Student"):
    print(row)

# ==========================
# MAX
# ==========================

print("\nMaximum Marks")
for row in cursor.execute("SELECT MAX(Marks) FROM Student"):
    print(row)

# ==========================
# BETWEEN
# ==========================

print("\nStudents with Marks Between 80 and 90")
for row in cursor.execute(
    "SELECT * FROM Student WHERE Marks BETWEEN 80 AND 90"
):
    print(row)

# ==========================
# ORDER BY
# ==========================

print("\nStudents Sorted by Marks")
for row in cursor.execute(
    "SELECT * FROM Student ORDER BY Marks DESC"
):
    print(row)

# ==========================
# COUNT
# ==========================

print("\nTotal Students")
for row in cursor.execute(
    "SELECT COUNT(*) FROM Student"
):
    print(row)

# ==========================
# AVG
# ==========================

print("\nAverage Marks")
for row in cursor.execute(
    "SELECT AVG(Marks) FROM Student"
):
    print(row)

# ==========================
# SUM
# ==========================

print("\nTotal Faculty Salary")
for row in cursor.execute(
    "SELECT SUM(Salary) FROM Faculty"
):
    print(row)

# ==========================
# INNER JOIN
# ==========================

print("\nStudents with Department")
for row in cursor.execute("""
SELECT Student.StudentName,
       Department.DeptName
FROM Student
INNER JOIN Department
ON Student.DeptID = Department.DeptID
"""):
    print(row)

print("\nFaculty with Department")
for row in cursor.execute("""
SELECT Faculty.FacultyName,
       Faculty.Subject,
       Department.DeptName
FROM Faculty
INNER JOIN Department
ON Faculty.DeptID = Department.DeptID
"""):
    print(row)

conn.close()