
students_count = int(input("How many student names you want to add? "))

with open("students.txt", "a+") as file:

    file.seek(0)

    print("\nExisting student names:")
    for x in file:
        print(x.strip())

    for i in range(students_count):
        student_name = input("Enter student name: ")
        file.write(student_name + "\n")

    file.seek(0)

    print("\nUpdated student list:")
    for x in file:
        print(x.strip())
