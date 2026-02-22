import csv
from typing import List
from models import Student



def validate_grade(grade_str: str) -> float:

    try:
        grade = float(grade_str)
        if 0 <= grade <= 100:
            return grade
        else:
            raise ValueError("Grade must be between 0 and 100")
    except ValueError:
        raise ValueError("Invalid grade format. Must be a number.")



def validate_student_id(student_id: str) -> bool:

    return bool(student_id and student_id.strip())


def load_students_from_csv(filename: str) -> List[Student]:

    students = []
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                student_id = row['student_id'].strip()
                name = row['name'].strip()
                grades = row['grades'].strip()
                if grades:
                    grades = [float(g.strip()) for g in grades.split(',') if g.strip()]
                else:
                    grades = []
                student = Student(student_id, name, grades)
                students.append(student)
    except FileNotFoundError:
        pass
    except Exception as e:
        raise IOError(f"Error reading CSV file: {e}")
    return students



def save_students_to_csv(filename: str, students: List[Student]):

    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['student_id', 'name', 'grades'])
            for student in students:
                grades_str = ','.join(str(g) for g in student.grade)
                writer.writerow([student.student_id, student.name, grades_str])
    except Exception as e:
        raise IOError(f"Error writing CSV file: {e}")