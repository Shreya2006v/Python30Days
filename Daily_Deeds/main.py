from student import Student
import json

# Load existing data
def load_students(filename):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            return [Student(s["name"], s["grades"]) for s in data]
    except FileNotFoundError:
        return []

# Save student data
def save_students(students, filename):
    with open(filename, "w") as f:
        json.dump([s.to_dict() for s in students], f, indent=2)

def display_students(students):
    for s in students:
        print(f"{s.name} - Grades: {s.grades}, Avg: {s.average():.2f}")

def main():
    filename = "data.json"
    students = load_students(filename)

    while True:
        print("\n1. Add Student\n2. View Students\n3. Save and Exit")
        choice = input("Choose: ")

        if choice == "1":
            name = input("Name: ")
            grades = list(map(int, input("Enter grades (comma-separated): ").split(",")))
            students.append(Student(name, grades))
        elif choice == "2":
            display_students(students)
        elif choice == "3":
            save_students(students, filename)
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
