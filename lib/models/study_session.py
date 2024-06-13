import sqlite3

class Schedule:
    def __init__(self):
        self.connection = sqlite3.connect("study_group.db")
        self.cursor = self.connection.cursor()

    def create(self, date, time, study_group_id):
        query = "INSERT INTO study_sessions (date, time, study_group_id) VALUES (?,?,?)"
        self.cursor.execute(query, (date, time, study_group_id))
        self.connection.commit()

    def show_by_id(self, id):
        query = "SELECT * FROM study_sessions WHERE id =?"
        self.cursor.execute(query, (id,))
        schedule_data = self.cursor.fetchall()
    
        if schedule_data:
            for row in schedule_data:
                print(f"ID: {row[0]}, Date: {row[1]}, Time: {row[2]}, Study Group ID: {row[3]}")
        else:
            print(f"No study sessions found for the date: {id}")

    def update_schedule(self, session_id, date, time, study_group_id):
        query = "UPDATE study_sessions SET date =?, time =?, study_group_id =? WHERE id =?"
        self.cursor.execute(query, (date, time, study_group_id, session_id))
        self.connection.commit()

    def delete_study_session(self, session_id):
        query = "DELETE FROM study_sessions WHERE id =?"
        self.cursor.execute(query, (session_id,))
        self.connection.commit()

    def close(self):
        self.connection.close()