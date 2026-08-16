students = []

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Student
    if choice == "1":
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")
        course = input("Enter course: ")

        student = {
            "name": name,
            "roll": roll,
            "course": course
        }

        students.append(student)
        print("Student added successfully!")

    # View Students
    elif choice == "2":
        if len(students) == 0:
            print("No students found!")
        else:
            print("\n--- Student List ---")
            for student in students:
                print("Name:", student["name"])
                print("Roll No:", student["roll"])
                print("Course:", student["course"])
                print("-------------------")

    # Search Student
    elif choice == "3":
        roll = input("Enter roll number to search: ")
        found = False

        for student in students:
            if student["roll"] == roll:
                print("\nStudent Found!")
                print("Name:", student["name"])
                print("Roll No:", student["roll"])
                print("Course:", student["course"])
                found = True

        if found == False:
            print("Student not found!")

    # Update Student
    elif choice == "4":
        roll = input("Enter roll number to update: ")

        for student in students:
            if student["roll"] == roll:
                student["name"] = input("Enter new name: ")
                student["course"] = input("Enter new course: ")
                print("Student updated successfully!")
                break
        else:
            print("Student not found!")

    # Delete Student
    elif choice == "5":
        roll = input("Enter roll number to delete: ")

        for student in students:
            if student["roll"] == roll:
                students.remove(student)
                print("Student deleted successfully!")
                break
        else:
            print("Student not found!")

    # Exit
    elif choice == "6":
        print("Thank You! Program Closed.")
        break

    else:
        print("Invalid choice! Please try again.")