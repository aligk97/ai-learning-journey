import numpy as np

# scores = np.array([
#     [70, 80, 90],
#     [60, 75, 85],
#     [50, 65, 70],
#     [90, 95, 100],
#     [40, 55, 60]
# ])

# #task1

# second_exams = scores[:,1]
# print(second_exams)

# #task2
# first_3_students_2_and_3_exams = scores[-3:, [0,2]]
# print(first_3_students_2_and_3_exams)

# #task3
# numbers = np.array([1, 2, 3, 4, 5, 6])
# print(numbers.reshape(2,3))

# #task4
# scores_small = np.array([
#     [70, 80],
#     [90, 100],
#     [60, 75]
# ])

# flat_scores = scores_small.flatten()
# print(flat_scores)

# #task5
# print(scores_small.T)


# #task6

# data = np.array([
#     [10, 20, 30, 40],
#     [50, 60, 70, 80],
#     [90, 100, 110, 120]
# ])

# selected_data = data[-2:, [1,2]]
# print(selected_data)


# #task7

# data = np.array([
#     [10, 20, 30, 40],
#     [50, 60, 70, 80],
#     [90, 100, 110, 120]
# ])

# flattened_data = data.flatten()
# print(flattened_data)
# reshaped_data = flattened_data.reshape(2,6)
# print(reshaped_data)

# #task8
# data = np.array([
#     [10, 20, 30, 40],
#     [50, 60, 70, 80],
#     [90, 100, 110, 120]
# ])

# final_data = data.T.flatten()
# print(final_data)


#task9 - final

# 1. İlk 4 öğrencinin sadece 2. ve 4. sınav notlarını seç.
#    Değişken adı:
#    selected_scores

# 2. selected_scores array'ini transpose et.
#    Değişken adı:
#    transposed_scores

# 3. transposed_scores'u tek boyutlu hale getir.
#    Değişken adı:
#    flat_scores

# 4. flat_scores'u 4 satır, 2 sütun olacak şekilde reshape et.
#    Değişken adı:
#    reshaped_scores

# 5. scores array'inin son 3 öğrencisini seç ve
#    3 satır × 4 sütun olan bu kısmı 2 satır × 6 sütuna çevir.
#    Değişken adı:
#    last_students_reshaped

scores = np.array([
    [70, 80, 90, 85],
    [60, 75, 85, 70],
    [50, 65, 70, 60],
    [90, 95, 100, 98],
    [40, 55, 60, 50],
    [75, 85, 80, 90]
])

selected_scores = scores[:4,[1,3]]
print(selected_scores)

transposed_scores = selected_scores.T
print(transposed_scores)

flattened_scores = transposed_scores.flatten()
print(flattened_scores)

reshaped_scores = flattened_scores.reshape(4,2)
print(reshaped_scores)

last_students_reshaped = scores[-3:,:].reshape(2,6)
print(last_students_reshaped)