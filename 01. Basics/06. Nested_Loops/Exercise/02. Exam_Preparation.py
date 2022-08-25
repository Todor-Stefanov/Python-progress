number_of_allowed_bad_grades = int(input())

problem_counter = 0
bad_grade_counter = 0
all_grade_counter = 0
last_problem = ""
problem = input()

while problem != "Enough":
    grade = int(input())
    if grade <= 4:
        bad_grade_counter += 1
        if bad_grade_counter == number_of_allowed_bad_grades:
            print(f"You need a break, {bad_grade_counter} poor grades.")
            break
    all_grade_counter += grade
    problem_counter += 1
    last_problem = problem
    problem = input()
average_score = all_grade_counter / problem_counter

if bad_grade_counter < number_of_allowed_bad_grades:
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {problem_counter}")
    print(f"Last problem: {last_problem}")

