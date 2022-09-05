student = input()
students_dict = {}
while ":" in student:
    info = student.split(":")
    name, id, course = info[0], info[1], info[2]
    if course not in students_dict:
        students_dict[course] = {}
    students_dict[course][id] = name
    student = input()

course = " ".join(student.split("_"))
for key, value in students_dict.items():
    if key == course:
        for id, name in value.items():
            print(f"{name} - {id}")




