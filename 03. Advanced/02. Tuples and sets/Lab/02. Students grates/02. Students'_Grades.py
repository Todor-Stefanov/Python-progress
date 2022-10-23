number_of_students = int(input())

record = {}
for i in range(number_of_students):
    student_grade = tuple(input().split(" "))
    student, grade = student_grade
    if student not in record:
        record[student] = []
    grade = float(grade)
    record[student].append(grade)


for key, values in record.items():
    grades_formatted = ' '.join(f"{value:.2f}" for value in values)
    average = sum(values) / len(values)
    print(f"{key} -> {grades_formatted} (avg: {average:.2f})")
