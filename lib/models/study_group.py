# study_group.py
import sqlite3

class StudyGroup:
    def __init__(self):
        self.connection = sqlite3.connect("study_group.db")
        self.cursor = self.connection.cursor()
        self.subjects = []

    def create(self, name):
        query = "INSERT INTO study_groups (Name) VALUES (?)"
        self.cursor.execute(query, (name,))
        self.connection.commit()
        return self.cursor.lastrowid

    def read_id(self, id):
        query = "SELECT * FROM study_groups WHERE id =?"
        self.cursor.execute(query, (id,))
        study_group_data = self.cursor.fetchone()

        if study_group_data:
            study_group_id = study_group_data[0]
            query = "SELECT * FROM subjects WHERE study_group_id =?"
            self.cursor.execute(query, (study_group_id,))
            self.subjects = self.cursor.fetchall()

        return study_group_data
    
    def read_by_name(self, name):
        query = "SELECT * FROM study_groups WHERE name =?"
        self.cursor.execute(query, (name,))
        study_group_data = self.cursor.fetchone()
        return study_group_data

    def list_all_groups(self):
        query = """
            SELECT study_groups.id, study_groups.Name, subjects.id, subjects.Name
            FROM study_groups
            LEFT JOIN subjects ON study_groups.id = subjects.study_group_id
        """
        self.cursor.execute(query)
        result_set = self.cursor.fetchall()

        groups = []
        current_group = None

        for row in result_set:
            study_group_id, study_group_name, subject_id, subject_name = row

            if current_group is None or current_group['id'] != study_group_id:
                if current_group:
                    groups.append(current_group)
                current_group = {"id": study_group_id, "name": study_group_name, "subjects": []}

            if subject_id:
                current_group['subjects'].append({"id": subject_id, "name": subject_name})

        if current_group:
            groups.append(current_group)

        return groups


    def update(self, study_group_id, name):
        query = "UPDATE study_groups SET Name =? WHERE id =?"
        self.cursor.execute(query, (name, study_group_id))
        self.connection.commit()

    def delete_group(self, group_id):
        query = "DELETE FROM study_groups WHERE id =?"
        self.cursor.execute(query, (group_id,))
        self.connection.commit()

    
    def close(self):
        self.connection.close()