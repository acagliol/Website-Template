import sqlite3

# Replace these with your desired values
database_path = "scheduling/counselor/templates/counselorfile/students.db"
html_path = "scheduling/counselor/templates/counselorfile/accounts.html"
table_element_id = "student-table"


def read_student_data(database_path):
    """
    Reads student data from a SQLite database.

    Args:
        database_path: Path to the SQLite database file.

    Returns:
        A list of dictionaries containing student information.
    """
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students")
    students = []
    for row in cursor.fetchall():
        student = {
            "Last Name": row[0],
            "First Name": row[1],
            "ID": row[2],
            "Grade": row[3],
        }
        students.append(student)
    connection.close()
    return students


def insert_data_into_html(students, html_path, table_element_id):
    """
    Inserts student data into an existing HTML table element.

    Args:
        students: A list of dictionaries containing student information.
        html_path: Path to the HTML file.
        table_element_id: ID of the table element where to insert data.
    """
    with open(html_path, "r") as f:
        html_content = f.read()

    # Locate the closing tag of the table element
    table_end_index = html_content.find("<!-- go here -->")

    # Generate the HTML string with student data
    student_data_html = ""
    for student in students:
        student_data_html += "<tr>"
        student_data_html += "<td>{}</td>".format(student["Last Name"])
        student_data_html += "<td>{}</td>".format(student["First Name"])
        student_data_html += "<td>{}</td>".format(student["ID"])
        student_data_html += "<td>{}</td>".format(student["Grade"])
        student_data_html += "</tr>"

    # Insert the student data HTML string before the closing tag
    updated_html_content = html_content[:table_end_index] + student_data_html + html_content[table_end_index:]

    # Save the updated HTML content
    with open(html_path, "w") as f:
        f.write(updated_html_content)



# Read student data from the database
students = read_student_data(database_path)

# Insert student data into the HTML file
insert_data_into_html(students, html_path, table_element_id)

print("Student data inserted into HTML successfully!")
