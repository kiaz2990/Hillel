#task 1
#part 1
with open('students.txt', 'r') as students:
    for student in students:
        student_info = student.split()
        scores_map = map(int, student_info[2:])
        scores_list = list(scores_map)
        avg_score = round((sum(scores_list) / len(scores_list)), 2)
        result_1 = f"{student_info[0]} {student_info[1]} {avg_score}"
        if float(avg_score) < float(5):
            print(result_1)

# part 2
with open('students.txt', 'r') as students:
    summary_score = 0
    scores_number = 0
    for student in students:
        student_info = student.split()
        scores_map = map(int, student_info[2:])
        scores_list = list(scores_map)
        summary_score = summary_score + sum(scores_list)
        scores_number = scores_number + len(scores_list)
    avg_summary_score = round(summary_score / scores_number, 2)
    print("Average score per class: {}".format(avg_summary_score))

# part 3
with open('students.txt', 'r') as students, open('result.txt', 'w') as result:
    for student in students:
        student_info = student.split()
        student_name = f"{student_info[1]} {student_info[0][0]}."
        scores_map = map(int, student_info[2:])
        scores_list = list(scores_map)
        avg_score = round((sum(scores_list) / len(scores_list)), 2)
        result.write("{:15}{}\n".format(student_name, avg_score))
#############################################################################
# task 2
with open('test.txt', 'a') as file:
    while True:
        s = input()
        if s == '':
            break
        file.write(s + '\n')
