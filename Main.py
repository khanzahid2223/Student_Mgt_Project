
class Student:
    def __init__(self, student_id, name, age, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.marks = marks

    def calculate_total(self):
        return sum(self.marks)

    def calculate_average(self):
        return self.calculate_total() / len(self.marks)

    def calculate_grade(self):
        average = self.calculate_average()

        if average >= 90:
            return "A+"
        elif average >= 80:
            return "A"
        elif average >= 70:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 35:
            return "D"
        else:
            return "F"

    def calculate_result(self):
        for mark in self.marks:
            if mark < 35:
                return "FAIL"
        return "PASS"

    def display(self):
        print("\n------ STUDENT DETAILS ------")
        print("Student ID :", self.student_id)
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Marks      :", self.marks)
        print("Total      :", self.calculate_total(), "/ 300")
        print("Average    :", round(self.calculate_average(), 2))
        print("Grade      :", self.calculate_grade())
        print("Result     :", self.calculate_result())


class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self):
        student_id = input("Enter Student ID: ")

        if student_id in self.students:
            print("Student ID already exists!")
            return

        name = input("Enter Student Name: ")

        try:
            age = int(input("Enter Age: "))

            if age <= 0:
                print("Age must be positive.")
                return

            marks = []

            for i in range(3):
                while True:
                    try:
                        mark = float(
                            input(f"Enter marks for Subject {i + 1}: ")
                        )

                        if 0 <= mark <= 100:
                            marks.append(mark)
                            break
                        else:
                            print("Marks must be between 0 and 100.")

                    except ValueError:
                        print("Enter a valid number.")

            student = Student(student_id, name, age, marks)
            self.students[student_id] = student

            print("Student added successfully!")

        except ValueError:
            print("Invalid age. Please enter a number.")

    def display_students(self):
        if not self.students:
            print("No student records found.")
            return

        for student in self.students.values():
            student.display()

    def search_student(self):
        student_id = input("Enter Student ID to search: ")

        student = self.students.get(student_id)

        if student:
            student.display()
        else:
            print("Student not found!")

    def update_student(self):
        student_id = input("Enter Student ID to update: ")

        if student_id not in self.students:
            print("Student not found!")
            return

        student = self.students[student_id]

        new_name = input("Enter new name: ")
        if new_name.strip():
            student.name = new_name

        try:
            new_age = int(input("Enter new age: "))

            if new_age <= 0:
                print("Age must be positive.")
                return

            student.age = new_age

            print("Enter updated marks:")

            new_marks = []

            for i in range(3):
                while True:
                    try:
                        mark = float(
                            input(f"Subject {i + 1} marks: ")
                        )

                        if 0 <= mark <= 100:
                            new_marks.append(mark)
                            break
                        else:
                            print("Marks must be between 0 and 100.")

                    except ValueError:
                        print("Enter a valid number.")

            student.marks = new_marks
            print("Student updated successfully!")

        except ValueError:
            print("Invalid age.")

    def delete_student(self):
        student_id = input("Enter Student ID to delete: ")

        if student_id in self.students:
            del self.students[student_id]
            print("Student deleted successfully!")
        else:
            print("Student not found!")

    def show_topper(self):
        if not self.students:
            print("No student records found.")
            return

        topper = max(
            self.students.values(),
            key=lambda student: student.calculate_average()
        )

        print("\n------ CLASS TOPPER ------")
        topper.display()

    def show_menu(self):
        while True:
            print("\n==============================")
            print("  STUDENT MANAGEMENT SYSTEM")
            print("==============================")
            print("1. Add Student")
            print("2. Display All Students")
            print("3. Search Student")
            print("4. Update Student")
            print("5. Delete Student")
            print("6. Show Class Topper")
            print("7. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_student()

            elif choice == "2":
                self.display_students()

            elif choice == "3":
                self.search_student()

            elif choice == "4":
                self.update_student()

            elif choice == "5":
                self.delete_student()

            elif choice == "6":
                self.show_topper()

            elif choice == "7":
                print("Thank you for using the system!")
                break

            else:
                print("Invalid choice! Select 1 to 7.")


system = StudentManagementSystem()
system.show_menu()
