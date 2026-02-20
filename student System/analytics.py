def top_performer(classroom):

    students = classroom.get_all_students()
    if not students:
        return None
    return max(students, key=lambda s: s.calculate_average())

def lowest_performer(classroom):

    students = classroom.get_all_students()
    if not students:
        return None
    return min(students, key=lambda s: s.calculate_average())

def rank_students(classroom):

    students = classroom.get_all_students()
    return sorted(students, key=lambda s: s.calculate_average(), reverse=True)

def grade_distribution(classroom):

    distribution = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    for student in classroom.get_all_students():
        category = student.determine_grade_category()# it will return the student's estimate lik A, B, C, D or F to variable category
        distribution[category] += 1 # we will search in the dictionary key about category result and add +1 to this result value
    return distribution