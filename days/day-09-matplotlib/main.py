# # # minitask 1

# # import matplotlib.pyplot as plt

# # months = [1, 2, 3, 4, 5, 6]
# # sales = [120, 150, 135, 180, 210, 250]

# # # 1. months değerlerini X ekseni,
# # # sales değerlerini Y ekseni yaparak
# # # bir çizgi grafiği oluştur.

# # plt.plot(months,sales)



# # # 2. Grafiğin başlığı:
# # # Monthly Sales

# # plt.title('Monthly Sales')

# # # 3. X ekseninin adı:
# # # Month

# # plt.xlabel('Month')

# # # 4. Y ekseninin adı:
# # # Sales

# # plt.ylabel('Sales')

# # # 5. Grafiği ekranda göster.

# # plt.show()




# # # minitask 2

# # import matplotlib.pyplot as plt

# # study_hours = [1, 2, 2.5, 3, 4, 5, 6, 7]
# # scores = [45, 50, 58, 61, 68, 75, 86, 92]

# # # 1. study_hours X ekseni,
# # # scores Y ekseni olacak şekilde
# # # scatter plot oluştur.

# # plt.scatter(study_hours, scores)

# # # 2. Başlık:
# # # Study Hours vs Exam Score

# # plt.title('Study Hours vs Exam Score')

# # # 3. X ekseni:
# # # Study Hours

# # plt.xlabel('Study Hours')


# # # 4. Y ekseni:
# # # Exam Score

# # plt.ylabel('Exam Score')


# # # 5. Grafiği göster.

# # plt.show()


# # # minitask 3

# # import matplotlib.pyplot as plt

# # ages = [18, 19, 20, 20, 21, 21, 21, 22, 22, 23,
# #         23, 24, 25, 27, 30, 31, 35, 40]

# # # ages verisinin histogramını oluştur.

# # # Veriyi 6 aralığa böl.
# # # Başlık: Age Distribution
# # # X ekseni: Age
# # # Y ekseni: Frequency

# # plt.hist(ages, bins=6)
# # plt.title("Age Distribution")
# # plt.xlabel('Age')
# # plt.ylabel('Frequency')

# # plt.show()




# import matplotlib.pyplot as plt

# days = [1, 2, 3, 4, 5]

# student_a = [60, 65, 72, 80, 88]
# student_b = [55, 68, 70, 78, 92]

# plt.figure(figsize=(8, 5))

# plt.plot(days, student_a, label="Student A")
# plt.plot(days, student_b, label="Student B")

# plt.title("Student Progress")
# plt.xlabel("Day")
# plt.ylabel("Score")

# plt.legend()
# plt.grid()

# plt.show()



# # minitask 4

# import matplotlib.pyplot as plt

# months = [1, 2, 3, 4, 5, 6]

# product_a = [100, 120, 140, 135, 160, 190]
# product_b = [80, 110, 125, 150, 170, 180]

# # 1. Grafik boyutunu 9x5 yap.

# plt.figure(figsize=(9,5))

# # 2. product_a ve product_b satışlarını
# # aynı grafik üzerinde çiz.

# plt.plot(months,product_a, label="Product A")
# plt.plot(months,product_b, label="Product B")

# # 3. Çizgilerin label değerleri:
# # Product A
# # Product B

# # 4. Başlık:
# # Product Sales Comparison

# plt.title("Product Sales Comparison")

# # 5. X ekseni:
# # Month

# plt.xlabel('Month')

# # 6. Y ekseni:
# # Sales

# plt.ylabel('Sales')

# # 7. Legend ekle.

# plt.legend()


# # 8. Grid ekle.

# plt.grid()
# # 9. Grafiği göster.

# plt.show()




# # minitask 5

# import matplotlib.pyplot as plt

# months = [1, 2, 3, 4, 5, 6]
# revenue = [100, 130, 125, 160, 190, 220]
# expenses = [80, 90, 100, 110, 125, 140]

# # 1. Yan yana 2 grafik oluştur.
# # Grafik boyutu 10x4 olsun.

# fig, axes = plt.subplots(1,2, figsize=(10,4))

# # 2. Sol grafikte months - revenue çiz.
# # Başlığı: Revenue

# axes[0].plot(months,revenue)
# axes[0].set_title("Revenue")


# # 3. Sağ grafikte months - expenses çiz.
# # Başlığı: Expenses

# axes[1].plot(months, expenses)
# axes[1].set_title("Expenses")

# # 4. Grafikleri göster.

# plt.show()




# minitask 6 - Day 09 Final Check

import pandas as pd
import matplotlib.pyplot as plt

students = pd.DataFrame({
    "name": ["Ali", "Ayşe", "Mehmet", "Zeynep", "Can", "Ece", "Mert", "Elif"],
    "study_hours": [2, 5, 3, 7, 1, 6, 4, 8],
    "score": [55, 82, 65, 94, 48, 88, 75, 97],
    "age": [23, 21, 22, 24, 20, 22, 23, 21]
})

# 1. 1 satır ve 2 sütundan oluşan subplot oluştur.
# figsize=(12, 5)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 2. Sol grafikte:
# study_hours ile score arasında scatter plot oluştur.

axes[0].scatter(students["study_hours"], students["score"])

# Başlık:
# Study Hours vs Score
axes[0].set_title("Study Hours vs Score")
# X:
# Study Hours
axes[0].set_xlabel("Study Hours")
# Y:
# Score

axes[0].set_ylabel("Score")
# 3. Sağ grafikte:
# score sütununun histogramını oluştur.
# bins=5
axes[1].hist(students["score"], bins=5)
# Başlık:
# Score Distribution
axes[1].set_title("Score Distribution")
# X:
# Score
axes[1].set_xlabel("Score")
# Y:
# Frequency
axes[1].set_ylabel("Frequency")

# 4. Her iki grafiğe de grid ekle.

axes[0].grid()
axes[1].grid()
# 5. tight_layout kullan.
plt.tight_layout()
# 6. Grafikleri göster.
plt.show()
