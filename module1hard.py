students = {'Johnni', 'Bilbo', 'Steve', 'Kendrik', 'Aaron'}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
average = sum(grades[0]) / len(grades), sum(grades[1]) / len(grades), sum(grades[2]) / len(grades), sum(
    grades[3]) / len(grades), sum(grades[4]) / len(grades)
journal = zip(sorted(students), average)
print(dict(journal))
