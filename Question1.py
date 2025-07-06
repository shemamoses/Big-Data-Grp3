def student_management_system():
    students = []

    while True:
        print("\n--- Enter Student Information ---")
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        
        num_courses = int(input("Enter number of courses (2 or 3): "))
        grades = []

        for i in range(num_courses):
            grade = float(input(f"Enter grade for course {i+1}: "))
            grades.append(grade)

        average = sum(grades) / len(grades)

        student = {
            "name": name,
            "age": age,
            "grades": grades,
            "average": average
        }

        students.append(student)

        cont = input("Do you want to add another student? (yes/no): ").lower()
        if cont != "yes":
            break

    print("\n--- Student Information Summary ---")
    for s in students:
        print(f"\nName: {s['name']}")
        print(f"Age: {s['age']}")
        print(f"Grades: {s['grades']}")
        print(f"Average Grade: {s['average']:.2f}")

# Call the function
student_management_system()