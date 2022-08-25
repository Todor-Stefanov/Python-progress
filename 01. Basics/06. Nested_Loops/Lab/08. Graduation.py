students_name = input()
counter = 0
sum_grades = 0
negative_counter = 0
average_grade = 0
while counter != 12:
    grade = float(input())
    if grade < 4:
        counter += 0
        negative_counter += 1
        if negative_counter > 1:
            counter += 1
            print(f"{students_name} has been excluded at {counter} grade")
            break
    elif grade >= 4:
        counter += 1
        sum_grades += grade
        average_grade = sum_grades / counter

if negative_counter < 2:
    print(f"{students_name} graduated. Average grade: {average_grade:.2f}")
