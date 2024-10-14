import sqlite3

# Replace these with your desired values
database_path = "scheduling/counselor/templates/counselorfile/teacher1.db"  # Updated database name
html_path = "scheduling/counselor/templates/counselorfile/accounts.html"
table_element_id = "teachertable"

def read_teacher_data(database_path):
    """
    Reads teacher data from a SQLite database.

    Args:
        database_path: Path to the SQLite database file.

    Returns:
        A list of dictionaries containing teacher information.
    """
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()
    cursor.execute("SELECT teacher_First, teacher_Last, depts FROM TEACHERS_teachers")  # Adjusted query
    teachers = []
    for row in cursor.fetchall():
        teacher = {
            "Last Name": row[0],
            "First Name": row[1],
            "Department": row[2],  # Updated column name
        }
        teachers.append(teacher)
    connection.close()
    return teachers


# ... (the rest of the code remains the same)

def insert_data_into_html(teachers, html_path, table_element_id):
    """
    Inserts teacher data into an existing HTML table element.

    Args:
        teachers: A list of dictionaries containing teacher information.
        html_path: Path to the HTML file.
        table_element_id: ID of the table element where to insert data.
    """
    with open(html_path, "r") as f:
        html_content = f.read()

    # Locate the closing tag of the table element
    table_end_index = html_content.find("<!-- go here -->")

    # Generate the HTML string with teacher data
    teacher_data_html = ""
    for teacher in teachers:
        teacher_data_html += "<tr>"
        teacher_data_html += "<td>{}</td>".format(teacher["Last Name"])
        teacher_data_html += "<td>{}</td>".format(teacher["First Name"])
        teacher_data_html += "<td>{}</td>".format(teacher["Department"])
        teacher_data_html += "</tr>"

    # Insert the teacher data HTML string before the closing tag
    updated_html_content = html_content[:table_end_index] + teacher_data_html + html_content[table_end_index:]

    # Save the updated HTML content
    with open(html_path, "w") as f:
        f.write(updated_html_content)

# Read teacher data from the database
teachers = read_teacher_data(database_path)

# Insert teacher data into the HTML file
insert_data_into_html(teachers, html_path, table_element_id)

print("teacher data inserted into HTML successfully!")
