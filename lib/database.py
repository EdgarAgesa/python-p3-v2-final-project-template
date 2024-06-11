import sqlite3

# Connect to the database
conn = sqlite3.connect('study_group.db')
cursor = conn.cursor()

# Create the study_groups table
cursor.execute('''
    CREATE TABLE study_groups (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
''')

# Create the subjects table
cursor.execute('''
    CREATE TABLE subjects (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        study_group_id INTEGER NOT NULL,
        FOREIGN KEY (study_group_id) REFERENCES study_groups (id)
    )
''')

# Create the study_sessions table
cursor.execute('''
    CREATE TABLE study_sessions (
        id INTEGER PRIMARY KEY,
        date TEXT NOT NULL,
        time TEXT NOT NULL,
        study_group_id INTEGER NOT NULL,
        FOREIGN KEY (study_group_id) REFERENCES study_groups (id)
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()