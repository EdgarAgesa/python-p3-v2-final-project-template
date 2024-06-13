# lib/models/subject.py

import sqlite3

class Subject:
    def __init__(self):
        self.connection = sqlite3.connect("study_group.db")
        self.cursor = self.connection.cursor()

    def create_subject(self, name, study_group_id=None):
        query = "INSERT INTO subjects (Name, study_group_id) VALUES (?,?)"
        self.cursor.execute(query, (name, study_group_id))
        self.connection.commit()

    def read_by_id(self, id):
        query = "SELECT * FROM subjects WHERE id =?"
        self.cursor.execute(query, (id,))
        subject_data = self.cursor.fetchone()
        if subject_data:
            return subject_data[0], subject_data[1]
        else:
            return None

    def assign_to_study_group(self, subject_id, study_group_id):
        query = "UPDATE subjects SET study_group_id =? WHERE id =?"
        self.cursor.execute(query, (study_group_id, subject_id))
        self.connection.commit()

    def delete_subject(self, subject_id):
        query = "DELETE FROM subjects WHERE id =?"
        self.cursor.execute(query, (subject_id,))
        self.connection.commit()

    def update_subject_name(self, subject_id, new_name):
        query = "UPDATE subjects SET Name =? WHERE id =?"
        self.cursor.execute(query, (new_name, subject_id))
        self.connection.commit()

    def close(self):
        self.connection.close()