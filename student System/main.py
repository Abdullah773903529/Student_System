# from models import Student, ClassRoom
#
# s1 =Student("Ahmed","s1", [80,95,77,90,50])
# print(s1.calculate_average())
# print(s1.determine_grade_category())
# print(s1)
#
# room = ClassRoom()
#
# # إنشاء طلاب
# s1 = Student("أحمد", "S001", [80, 90, 100])
# s2 = Student("فاطمة", "S002", [70, 75, 80])
# s3 = Student("يوسف", "S003", [95, 85, 90])
#
# # إضافة طلاب
# room.add_student(s1)
# room.add_student(s2)
# room.add_student(s3)
# print(room.search_student("S003"))
# print(room.search_student("S004"))



from models import Classroom, Student
from analytics import top_performer, lowest_performer, rank_students, grade_distribution
from utils import load_students_from_csv, save_students_to_csv, validate_grade, validate_student_id

DATA_FILE = "data.csv"


def display_menu():
    print("\n" + "="*40)
    print(" STUDENT PERFORMANCE ANALYZER")
    print("="*40)
    print("1. Add student")
    print("2. Remove student")
    print("3. Search student")
    print("4. Show classroom average")
    print("5. Show top performer")
    print("6. Show lowest performer")
    print("7. Rank all students")
    print("8. Show grade distribution")
    print("9. Save data to file")
    print("10. Load data from file")
    print("0. Exit")
    print("="*40)


def add_student_flow(classroom: Classroom):

    print("\n--- Add Student ---")
    student_id = input("Enter student ID: ").strip()
    if not validate_student_id(student_id):
        print("Invalid ID. Cannot be empty.")
        return
    name = input("Enter student name: ").strip()
    if not name:
        print("Invalid name. Cannot be empty.")
        return
    # Input grades
    grades = []
    print("Enter grades (one per line, empty line to finish):")
    while True:
        grade_str = input("Grade: ").strip()
        if grade_str == "":
            break
        try:
            grade = validate_grade(grade_str)
            grades.append(grade)
        except ValueError as e:
            print(f"Error: {e}. Please try again.")
            continue
    try:
        student = Student(name, student_id, grades)
        classroom.add_student(student)
        print(f"Student {name} added successfully.")
    except ValueError as e:
        print(f"Error: {e}")


def remove_student_flow(classroom: Classroom):

    print("\n--- Remove Student ---")
    student_id = input("Enter student ID to remove: ").strip()
    if classroom.remove_student(student_id):
        print(f"Student with ID {student_id} removed.")
    else:
        print(f"No student found with ID {student_id}.")


def search_student_flow(classroom: Classroom):

    print("\n--- Search Student ---")
    key = input("Enter student ID or name (partial): ").strip()
    student = classroom.search_student(key)
    if student:
        print("Found:")
        print(student)
    else:
        print("No matching student found.")


def show_classroom_avg(classroom: Classroom):
    """Display classroom average."""
    avg = classroom.calculate_classroom_average()
    print(f"\nClassroom average (average of student averages): {avg:.2f}")


def show_top_performer(classroom: Classroom):
    try:
        top = top_performer(classroom)
        print("\nTop performer:")
        print(top)
    except ValueError as e:
        print(e)


def show_lowest_performer(classroom: Classroom):
    try:
        low = lowest_performer(classroom)
        print("\nLowest performer:")
        print(low)
    except ValueError as e:
        print(e)


def show_ranking(classroom: Classroom):

    ranked = rank_students(classroom)
    if not ranked:
        print("No students to rank.")
        return
    print("\n--- Student Ranking (by average) ---")
    for i, student in enumerate(ranked, 1):
        print(f"{i}. {student}")


def show_distribution(classroom: Classroom):

    dist = grade_distribution(classroom)
    print("\n--- Grade Distribution ---")
    for grade, count in dist.items():
        print(f"{grade}: {count}")


def save_data(classroom: Classroom):

    try:
        students = classroom.get_all_students()
        save_students_to_csv(DATA_FILE, students)
        print(f"Data saved to {DATA_FILE} successfully.")
    except IOError as e:
        print(f"Error saving: {e}")


def load_data(classroom: Classroom):
    try:
        students = load_students_from_csv(DATA_FILE)
        return students
    except Exception as e:
        print(f"Error loading: {e}")
        return None


def main():
    classroom = Classroom()
    try:
        students = load_students_from_csv(DATA_FILE)
        for s in students:
            classroom.add_student(s)
        print(f"Loaded {len(students)} students from {DATA_FILE}.")
    except Exception as e:
        print(f"Note: No data loaded ({e}). Starting fresh.")

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        try:
            if choice == '1':
                add_student_flow(classroom)
            elif choice == '2':
                remove_student_flow(classroom)
            elif choice == '3':
                search_student_flow(classroom)
            elif choice == '4':
                show_classroom_avg(classroom)
            elif choice == '5':
                show_top_performer(classroom)
            elif choice == '6':
                show_lowest_performer(classroom)
            elif choice == '7':
                show_ranking(classroom)
            elif choice == '8':
                show_distribution(classroom)
            elif choice == '9':
                save_data(classroom)
            elif choice == '10':

                students = load_students_from_csv(DATA_FILE)

                classroom = Classroom()
                for s in students:
                    classroom.add_student(s)
                    # print(f"Student : {s.student_id} , Student : {s.name} , Grade: {s.grade}")
                print(f"Loaded {len(students)} students from {DATA_FILE}.")
            elif choice == '0':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 0 and 10.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()