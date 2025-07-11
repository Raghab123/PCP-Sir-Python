"""MINI PROJECT: Student Report Card Management System
Problem Statement:
Design and implement a Student Report Card Management System using Python that allows a teacher to:
● Add new student records (name, roll number, subject-wise marks).
● View the report of all students.
● Display the topper(s) of the class based on average marks.
● Search for a student by roll number.
● Display all students who have failed in one or more subjects.
● Optionally update marks of any student."""



students = []

while True:
    print("\n--- Student Report Card Menu ---")
    print("1) Add Student")
    print("2) View All Students")
    print("3) Show Topper(s)")
    print("4) Search by Roll Number")
    print("5) Show Students Who Failed")
    print("6) Update Marks")
    print("7) Exit")

    choice = input("Enter your choice: ")

    # 1. Add Student
    if choice == "1":
        name = input("Enter name: ")
        roll = input("Enter roll number: ")
        m1 = int(input("Marks in Subject 1: "))
        m2 = int(input("Marks in Subject 2: "))
        m3 = int(input("Marks in Subject 3: "))
        student = {"name": name, "roll": roll, "marks": [m1, m2, m3]}
        students.append(student)
        print("Student added.")

    # 2. View All
    elif choice == "2":
        if len(students) == 0:
            print("No student records found.")
        else:
            for s in students:
                print("Name:", s["name"])
                print("Roll No:", s["roll"])
                print("Marks:", s["marks"])
                print("Average:", sum(s["marks"]) / 3)
                print("-" * 20)

    # 3. Show Topper(s)
    elif choice == "3":
        if len(students) == 0:
            print("No student data.")
        else:
            max_avg = 0
            for s in students:
                avg = sum(s["marks"]) / 3
                if avg > max_avg:
                    max_avg = avg
            print("Topper(s):")
            for s in students:
                if sum(s["marks"]) / 3 == max_avg:
                    print(s["name"], "- Roll:", s["roll"], "- Avg:", max_avg)

    # 4. Search by Roll Number
    elif choice == "4":
        r = input("Enter roll number to search: ")
        found = False
        for s in students:
            if s["roll"] == r:
                print("Name:", s["name"])
                print("Roll No:", s["roll"])
                print("Marks:", s["marks"])
                print("Average:", sum(s["marks"]) / 3)
                found = True
        if not found:
            print("Student not found.")

    # 5. Show Students Who Failed
    elif choice == "5":
        for s in students:
            failed = False
            for mark in s["marks"]:
                if mark < 35:
                    failed = True
            if failed:
                print(s["name"], "- Roll:", s["roll"], "- Marks:", s["marks"])

    # 6. Update Marks
    elif choice == "6":
        r = input("Enter roll number to update: ")
        found = False
        for s in students:
            if s["roll"] == r:
                print("Current Marks:", s["marks"])
                m1 = int(input("New marks for Subject 1: "))
                m2 = int(input("New marks for Subject 2: "))
                m3 = int(input("New marks for Subject 3: "))
                s["marks"] = [m1, m2, m3]
                print("Marks updated.")
                found = True
        if not found:
            print("Student not found.")

    # 7. Exit
    elif choice == "7":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Try again.")
