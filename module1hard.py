students = {'Johnni', 'Bilbo', 'Steve', 'Kendrik', 'Aaron'}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
average_grades = {student: sum(grade) / len(grade) for student, grade in zip(sorted(students), grades)}
print(average_grades)
