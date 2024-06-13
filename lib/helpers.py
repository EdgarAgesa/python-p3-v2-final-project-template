# lib/helpers.py

from models.study_group import StudyGroup
from models.subject import Subject
from models.study_session import Schedule

def exit_program():
    print("Goodbye!")
    exit()

def create_study_group():
    name = input("Enter the name of the study group: ")
    study_group = StudyGroup()
    study_group.create(name)
    print(f"Study group {name} created!")


def read_study_group():
    name = input("Enter the name of the study group: ")
    study_group = StudyGroup()
    result = study_group.read(name)
    if result:
        study_group_id = result[0]
        print(f"Study group found: ID - {study_group_id}, Name - {result[1]}")
        print("Subjects in the study group:")
        for subject in study_group.subjects:
            print(f"ID - {subject[0]}, Name - {subject[1]}")
        else:
            print("Subjects not in the study group")
    else:
        print("Study group not found.")
def list_groups():
    study_group = StudyGroup()
    groups = study_group.list_all_groups()

    if groups:
        print("Study groups:")
        for group in groups:
            group_id = group["id"]
            group_name = group["name"]
            subjects = group["subjects"]

            print(f"ID: {group_id}, Name: {group_name}")
            print("Subjects:")
            for subject in subjects:
                subject_id = subject["id"]
                subject_name = subject["name"]
                print(f"ID: {subject_id}, Name: {subject_name}")
            print()
            
    else:
        print("No study groups found.")

def update_study_group():
    study_group_id = int(input("Enter the study_group_ID of the study group to update: "))
    new_name = input("Enter the new name for the study group: ")
    study_group = StudyGroup()
    study_group.update(study_group_id, new_name)
    study_group.close()
    print(f"Study group with ID {study_group_id} updated to {new_name}.")

def delete_study_group():
    study_group_id = int(input("Enter the study_group_ID of the study group to delete: "))
    study_group = StudyGroup()
    result = study_group.read_by_id(study_group_id)

    if result:
        study_group.delete_group(study_group_id)
        study_group.close()
        print(f"Study group with ID {study_group_id} deleted.")
    else:
        print(f"Study group with ID {study_group_id} does not exist.")

def add_subject():
    name = input("Enter the name of the subject: ")
    study_group_id = int(input("Enter the study_group_ID: "))
    subject = Subject()
    subject.create_subject(name, study_group_id)
    subject.close()
    print(f"Subject {name} created to study_group {study_group_id}!")

def add_subject_to_study_group():
    study_group_name = input("Enter the name of the study group: ")
    subject_id = input("Enter the ID of the subject: ")

    subject = Subject()
    study_group = StudyGroup().read(study_group_name)
    if study_group:
        subject_result = Subject().read_by_id(subject_id)
        if subject_result:
            subject_name = subject_result[1]
            subject.assign_to_study_group(subject_id, study_group[0])
            print(f"Subject '{subject_name}' (ID: {subject_id}) added to study group '{study_group_name}'.")
        else:
            print(f"Subject with ID '{subject_id}' not found.")
    else:
        print("Study group not found.")


def subject_exists():
    id = input("Enter subject id: ")
    subject = Subject()
    result = subject.read_by_id(id)
    subject.close()

    if result:
        subject_id, subject_name = result
        print(f"Subject {subject_id} Name: {subject_name} exists in database")
    else:
        print(f"Subject {id} does not exist.")

def update_subject_name():
    subject_id = int(input("Enter the subject_ID of the subject to update: "))
    new_name = input("Enter the new name for the subject: ")

    subject = Subject()
    result = subject.read_by_id(subject_id)

    if result:
        subject.update_subject_name(subject_id, new_name)
        subject.close()
        print(f"Subject with ID {subject_id} updated to '{new_name}'.")
    else:
        print(f"Subject with ID {subject_id} does not exist.")

def delete_subject_from_study_group():
    subject_id = int(input("Enter the subject_ID of the subject to delete: "))
    subject = Subject()
    result = subject.read_by_id(subject_id)

    if result:
        subject.delete_subject(subject_id)
        subject.close()
        print(f"Subject with ID {subject_id} deleted.")
    else:
        print(f"Subject with ID {subject_id} does not exist.")

def create_schedule():
    date = input("Enter the date: ")
    time = input("Enter the time: ")
    study_group_id = int(input("Enter the study_group_ID: "))

    schedule = Schedule()
    schedule.create(date, time, study_group_id)
    schedule.close()
    print(f"Study session created on {date} at {time} for study group {study_group_id}.")

def display_sessions_by_id():
    id = int(input("Enter the id to display study sessions: "))

    schedule = Schedule()
    result = schedule.show_by_id(id)
    schedule.close()

    if result:
        print(f"Study sessions for ID {id}:")
        for row in result:
            print(f"ID: {row[0]}, Date: {row[1]}, Time: {row[2]}, Study Group ID: {row[3]}")
    
def update_study_session():
    session_id = int(input("Enter the ID of the study session to change: "))
    date = input("Enter the new date: ")
    time = input("Enter the new time: ")
    study_group_id = int(input("Enter the new study group ID: "))

    schedule = Schedule()
    result = schedule.show_by_id(session_id)

    if result:
        schedule.update_schedule(session_id, date, time, study_group_id)
        schedule.close()
        print(f"Study session with ID {session_id} updated to {date} on {time} for group {study_group_id} successfully.")
    else:
        print(f"No study session found for ID {session_id}.")

def delete_study_session():
    session_id = int(input("Enter the ID of the study session to delete: "))

    schedule = Schedule()
    result = schedule.show_by_id(session_id)

    if result:
        schedule.delete_study_session(session_id)
        schedule.close()
        print(f"Study session with ID {session_id} deleted successfully.")
    else:
        print(f"No study session found for ID {session_id}.")