##📚 Group3 Members

- SHEMA Moses 26590
- GATERA K Jessica 27630
-
-
-
-

# 📚 Group3 Question 1 - Student Management System

## 📌 Description

This project implements a simple **Student Management System** using Python. The program collects data for multiple students including their name, age, number of courses, and corresponding grades. It calculates the average grade for each student and displays a summary of all student data entered.

---

## ✅ Features

- Collects student information: name, age, course grades.
- Allows input for 2 or 3 courses.
- Computes average grade automatically.
- Stores all student data in a list of dictionaries.
- Displays a summary report after data entry is complete.

---

## 🧑‍💻 How to Run the Program

1. Make sure you have **Python 3.x** installed on your system.
2. Copy the code below into a file named `student_management.py`.
3. Open your terminal or command prompt.
4. Navigate to the folder where the file is saved.
5. Run the program with:

```bash
python student_management.py
```

---

## 🧾 Python Code

```python
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
```

---

## 📋 Sample Output

```
--- Enter Student Information ---
Enter student name: Alice
Enter student age: 20
Enter number of courses (2 or 3): 3
Enter grade for course 1: 85
Enter grade for course 2: 90
Enter grade for course 3: 80
Do you want to add another student? (yes/no): no

--- Student Information Summary ---

Name: Alice
Age: 20
Grades: [85.0, 90.0, 80.0]
Average Grade: 85.00
```

---

## 📝 Notes

- Only 2 or 3 courses are supported.
- Grade inputs must be numerical (decimals are allowed).
- The program stops collecting data when the user types **no**.

---

# 🔁 Group3 Question 2 - Palindrome Checker

## 📌 Description
This project implements a simple Palindrome Checker using Python. A palindrome is a word, phrase, or sequence that reads the same backward as forward (e.g., madam, racecar). This program takes a string input from the user and checks if it is a palindrome, ignoring case differences.

## ✅ Features
Accepts any string input from the user.

Reverses the string and compares it with the original.

Ignores case sensitivity for comparison.

Provides a clear message indicating whether the input is a palindrome or not.

## 🧑‍💻 How to Run the Program
1. Make sure you have Python 3.x installed on your system.

2. Copy the code below into a file named palindrome_checker.py.

3. Open your terminal or command prompt.

4. Navigate to the folder where the file is saved.

5. Run the program with:

   ```bash
    python palindrome_checker.py
    ```
    
## 🧾 Python Code

```python
    def check_palindrome():
    text = input("\nEnter a string to check if it's a palindrome: ")
    reversed_text = text[::-1]

    if text.lower() == reversed_text.lower():
        print("Yes, it is a palindrome")
    else:
        print("No, it is not a palindrome")

# Call the function
check_palindrome()

```
## 📋 Sample Output

```
    Enter a string to check if it's a palindrome: RaceCar
    Yes, it is a palindrome

```

```
    Enter a string to check if it's a palindrome: Python
    No, it is not a palindrome

```

## 📝 Notes

* The check is not case-sensitive.

* Spaces, punctuation, and numbers are not removed, so the program works best for single words or clean phrases.

* You can improve it further by ignoring spaces and non-alphanumeric characters.



## 👨‍🎓 Created By Group 3

---
