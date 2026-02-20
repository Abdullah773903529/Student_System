class Student:
    def __init__(self, name: str, student_id :str, grades: list = None):
        self.__name = name
        self.student_id = student_id
        self.__grades = grades if grades is not None else []

    @property
    def grade(self)->list:
        return self.__grades.copy()

    @grade.setter
    def grade(self, grade:list):
        if not all(isinstance(grade, (int , float) )for grade in grade):
            return ValueError('grades must be a list')
        else: self.__grades = list(grade)

    @property
    def name(self)->str:
        return self.__name

    @name.setter
    def name(self, new_name:str):
        if  not isinstance(new_name, str)or not new_name.strip():
            return ValueError('name must be a string')
        else: self.__name = new_name.strip()

    def add_grade(self, grade:list)->None:
        if not isinstance(grade, (int , float)):
            return print('grades must be a list')
        else: self.__grades.append(float(grade))

    def calculate_average(self)->float:
        if not self.__grades:
            return 0
        else:
            return sum(self.__grades)/len(self.__grades)

    def determine_grade_category(self)->str:
        avg = self.calculate_average()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 50:
            return 'D'
        else:
            return 'F'

    def __str__(self):
        return f'Student ID: {self.student_id},Student Name:{self.__name}, Grades: {self.grade}'

class Classroom:
    def __init__(self):
        self.__students = []

    def add_student(self, student: Student)->None:
        if not isinstance(student, Student):
            return print('students must be a list')
        if any(s.student_id == student.student_id for s in self.__students):
            return print(f"Student with ID {student.student_id} already exists.")
        self.__students.append(student)

    def remove_student(self, student_id)->None:
        for i,s in enumerate(self.__students):
            if s.student_id == student_id:
                del self.__students[i]
                return True
            return False

    def search_student(self, student_id: str):
        for s in self.__students:
            if s.student_id == student_id:
                return s
        else: print(f'Student with ID {student_id} does not exist.')



    def calculate_classroom_average(self) -> float:
        if not self.__students:
            return 0.0
        total = sum(s.calculate_average() for s in self.__students)
        return total / len(self.__students)

    def get_all_students(self)->list:
        return self.__students.copy()