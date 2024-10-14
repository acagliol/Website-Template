import sqlite3

# Connect to the database
conn = sqlite3.connect('teachers.db')
cursor = conn.cursor()

# Add the new last_name column
cursor.execute('ALTER TABLE teachers ADD COLUMN last_name TEXT')

# Get the total number of rows in the database
cursor.execute('SELECT COUNT(*) FROM teachers')
total_rows = cursor.fetchone()[0]

# Process each row in the database
for row_number in range(total_rows):
    cursor.execute('SELECT id, first_name FROM teachers WHERE rowid = ?', (row_number + 1,))
    row = cursor.fetchone()
    id, full_name = row
    names = full_name.split(' ', 1)  # Split at the first space
    first_name, last_name = names if len(names) == 2 else (names[0], '')
    cursor.execute('UPDATE teachers SET first_name = ?, last_name = ? WHERE id = ?', (first_name, last_name, id))

# Save (commit) the changes
conn.commit()

# Close the connection
conn.close()

print("Database updated successfully!")
