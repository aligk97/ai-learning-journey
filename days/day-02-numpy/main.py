import numpy as np

# scores = [45,72,88,91,63]

# np_scores = np.array(scores)

# print(np_scores * 2)


# print(np_scores.shape)
# print(np_scores.ndim)
# print(np_scores.size)
# print(np_scores.dtype)

#task1

# default_scores = [45, 72, 88, 91, 63, 55, 100, 38]
# scores = np.array(default_scores)

# passed_scores = scores[scores >=60]

# print(passed_scores.mean())
# print(passed_scores.max())
# print(passed_scores.min())
# print(len(passed_scores))



#task 2

# default_scores = [45, 72, 88, 91, 63, 55, 100, 38]
# scores = np.array(default_scores)

# selected_scores = scores[(scores >=50) & (scores <=90)]
# print(selected_scores.mean())

# updated_scores = selected_scores + 5

# print(updated_scores)

# extreme_notes = scores[(scores < 60) | (scores > 90)]
# print(extreme_notes)


# scores = np.array([
#     [70, 80, 90],
#     [60, 75, 85],
#     [50, 65, 70],
#     [90, 95, 100]
# ])

# student_averages = scores.mean(axis=1)
# print(student_averages)
# successful_students = student_averages[student_averages >= 75]
# print(successful_students)

# successful_students_exams = scores[scores.mean(axis=1) >= 75]
# print(successful_students_exams)

# max_exam_each_students = scores.max(axis=1)
# print(max_exam_each_students)


# #final task

scores = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [50, 65, 70],
    [90, 95, 100],
    [40, 55, 60]
])

student_averages = scores.mean(axis=1)
print('average', student_averages)

passed_students = scores[student_averages >= 70]
print('all exams of passed students')
print(passed_students)

passed_averages = passed_students.mean(axis=1)
print('passed averages')
print(passed_averages)
 
print("max score of class", scores.max())

print('average of class', scores.mean(axis=0))

print("max score of each student", scores.max(axis=1))

extreme_students = scores[(student_averages < 60) | (student_averages > 90)].mean(axis=1)

print("extreme_students", extreme_students)



