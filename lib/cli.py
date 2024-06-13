# lib/cli.py

from helpers import (
    exit_program,
    create_study_group,
    read_study_group,
    list_groups,
    update_study_group,
    delete_study_group,
    add_subject,
    add_subject_to_study_group,
    subject_exists,
    update_subject_name,
    delete_subject_from_study_group,
    create_schedule,
    display_sessions_by_id,
    update_study_session,
    delete_study_session  
)


def main():
    while True:
        menu()
        choice = input(">>> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            create_study_group()
        elif choice == "2":
            read_study_group()
        elif choice == "3":
            list_groups()
        elif choice == "4":
            update_study_group()
        elif choice == "5":
            delete_study_group()
        elif choice == "6":
            add_subject()
        elif choice == "7":
            add_subject_to_study_group()
        elif choice == "8":
            subject_exists()
        elif choice == "9":
            update_subject_name()
        elif choice == "10":
            delete_subject_from_study_group()
        elif choice == "11":
            create_schedule()
        elif choice == "12":
            display_sessions_by_id()
        elif choice == "13":
            update_study_session()
        elif choice == "14":
            delete_study_session()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("=======GROUP TABLE========")
    print("1. Create a new group")
    print("2. Search study_group by ID")
    print("3. List groups")
    print("4. Update a study_group")
    print("5. Delete a study group")
    print("=========SUBJECT TABLE===========")
    print("6. Create a subject")
    print("7. Add subjects to the group")
    print("8. Check subject by ID")
    print("9. Change a subject name")
    print("10. Delete a subject ")
    print("===========SCHEDULE TABLE============")
    print("11. Create a schedule")
    print("12. Search sessions by id")
    print("13. Update a study session")
    print("14. Delete a study session")
    print("=======================")


if __name__ == "__main__":
    main()
