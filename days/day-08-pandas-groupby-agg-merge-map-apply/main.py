# # minitask 1

# import pandas as pd

# sales = pd.DataFrame({
#     "city": ["Istanbul", "Ankara", "Istanbul", "Izmir", "Ankara", "Istanbul"],
#     "product": ["Laptop", "Phone", "Phone", "Laptop", "Laptop", "Laptop"],
#     "price": [40000, 25000, 30000, 35000, 38000, 42000],
#     "quantity": [2, 3, 1, 2, 1, 3]
# })

# # 1. city'ye göre grupla.
# # Her şehir için price sütununun:
# # - ortalamasını
# # - minimumunu
# # - maksimumunu
# # tek bir agg() kullanarak hesapla.

# results = sales.groupby('city')["price"].agg(['mean','min','max'])
# print(results)

# # 2. city'ye göre grupla.
# # price için mean ve max,
# # quantity için sum ve mean hesapla.

# results = sales.groupby('city').agg({
#     "price": ['mean','max'],
#     "quantity": ["sum", 'max']
# })

# print(results)



# # minitask 2

# import pandas as pd

# sales = pd.DataFrame({
#     "city": ["Istanbul", "Ankara", "Istanbul", "Izmir", "Ankara", "Istanbul"],
#     "product": ["Laptop", "Phone", "Phone", "Laptop", "Laptop", "Laptop"],
#     "price": [40000, 25000, 30000, 35000, 38000, 42000],
#     "quantity": [2, 3, 1, 2, 1, 3]
# })

# # city'ye göre grupla ve named aggregation kullanarak
# # aşağıdaki sütunları oluştur:

# print(sales.groupby('city').agg(
#     average_price = ("price",'mean'),
#     lowest_price = ("price",'min'),
#     total_quantity = ("quantity",'sum'),
#     average_quantity = ("quantity",'mean'),
# ))

# # average_price -> price ortalaması
# # lowest_price -> price minimumu
# # total_quantity -> quantity toplamı
# # average_quantity -> quantity ortalaması



# # minitask 3

# import pandas as pd

# students = pd.DataFrame({
#     "student_id": [1, 2, 3, 4],
#     "name": ["Ali", "Ayşe", "Mehmet", "Zeynep"],
#     "city": ["Istanbul", "Ankara", "Izmir", "Istanbul"]
# })

# scores = pd.DataFrame({
#     "student_id": [1, 2, 3, 4],
#     "score": [85, 92, 67, 78]
# })

# # 1. students ve scores DataFrame'lerini
# # student_id üzerinden birleştir.

# result = pd.merge(students,scores,on="student_id")

# # 2. Birleştirilmiş DataFrame'i ekrana yazdır.

# print(result)



# # minitask 4

# import pandas as pd

# students = pd.DataFrame({
#     "student_id": [1, 2, 3, 4],
#     "name": ["Ali", "Ayşe", "Mehmet", "Zeynep"]
# })

# scores = pd.DataFrame({
#     "student_id": [2, 3, 4, 5],
#     "score": [92, 67, 78, 88]
# })

# # 1. inner merge yap ve yazdır.
# print(pd.merge(students,scores,on="student_id",how="inner"))

# # 2. left merge yap ve yazdır.
# print(pd.merge(students,scores,on="student_id",how="left"))


# # 3. outer merge yap ve yazdır.
# print(pd.merge(students,scores,on="student_id",how="outer"))



# # minitask 5

# import pandas as pd

# students = pd.DataFrame({
#     "name": ["Ali", "Ayşe", "Mehmet", "Zeynep", "Can"],
#     "grade": ["A", "B", "C", "A", "B"]
# })

# grade_points = {
#     "A": 4,
#     "B": 3,
#     "C": 2
# }

# # 1. grade sütunundaki değerleri grade_points kullanarak dönüştür.
# students['points'] = students['grade'].map(grade_points)
# # 2. Sonucu yeni bir "point" sütununa kaydet.

# # 3. DataFrame'i yazdır.

# print(students)


# # minitask 6

# import pandas as pd

# students = pd.DataFrame({
#     "name": ["Ali", "Ayşe", "Mehmet", "Zeynep", "Can"],
#     "score": [85, 92, 58, 76, 64]
# })

# # 1. classify_score isminde bir fonksiyon oluştur.
# # score >= 80 ise "High"
# # score >= 60 ise "Medium"
# # diğer durumlarda "Low" döndürsün.

# def classify_score(score):
#     if score >= 80:
#         return "High"
#     elif score >= 60:
#         return "Medium"
#     return "Low"

# students["level"] = students["score"].map(classify_score)

# # 2. score sütununa map() ile bu fonksiyonu uygula.
# # Sonucu "level" isimli yeni sütuna kaydet.


# # 3. DataFrame'i yazdır.

# print(students)



# import pandas as pd

# employees = pd.DataFrame({
#     "name": ["Ali", "Ayşe", "Mehmet", "Zeynep"],
#     "salary": [45000, 60000, 38000, 70000],
#     "experience": [3, 6, 2, 8]
# })

# # 1. employee_level(row) isminde bir fonksiyon oluştur.
# #
# # salary >= 60000 ve experience >= 5 ise:
# # "Senior"
# #
# # experience >= 3 ise:
# # "Mid"
# #
# # diğer durumlarda:
# # "Junior"


# def employee_level(row):
#     if row["salary"] >= 60000 and row['experience'] >= 5:
#         return "Senior"
#     if row['experience'] >= 3:
#         return "Mid"
#     return "Junior"


        


# # 2. apply() ve axis=1 kullanarak fonksiyonu
# # DataFrame'in her satırına uygula.
# #
# # Sonucu "level" isimli yeni sütuna kaydet.

# employees["level"] = employees.apply(employee_level, axis=1)

# # 3. DataFrame'i yazdır.


# print(employees)




# minitask 8 - Day 08 Final Check

import pandas as pd

employees = pd.DataFrame({
    "employee_id": [1, 2, 3, 4, 5],
    "name": ["Ali", "Ayşe", "Mehmet", "Zeynep", "Can"],
    "department_id": [10, 20, 10, 30, 20],
    "salary": [45000, 65000, 52000, 70000, 48000],
    "experience": [3, 6, 4, 8, 2]
})

departments = pd.DataFrame({
    "department_id": [10, 20, 30],
    "department": ["Software", "Sales", "Finance"]
})

# 1. employees ve departments DataFrame'lerini
# department_id üzerinden birleştir.

merged_df = pd.merge(employees,departments, on="department_id", how="inner")

# 2. Oluşan DataFrame'i department sütununa göre grupla.
# Named aggregation kullanarak:
#
# average_salary -> salary ortalaması
# highest_salary -> salary maksimumu
# employee_count -> employee_id sayısı
#
# sütunlarını oluştur.

department_summary = merged_df.groupby('department').agg(
    average_salary = ('salary', 'mean'),
    highest_salary = ('salary', 'max'),
    employee_count = ('employee_id', "count")
)

# 3. Aşağıdaki dictionary'yi kullanarak department sütununu map() ile
# department_code isimli yeni bir sütuna dönüştür.

department_codes = {
    "Software": "SW",
    "Sales": "SL",
    "Finance": "FN"
}
merged_df["department_code"] = merged_df["department"].map(department_codes)


# 4. employee_level(row) fonksiyonunu oluştur.
#
# salary >= 60000 ve experience >= 5 -> "Senior"
# experience >= 3 -> "Mid"
# diğerleri -> "Junior"
#
# apply(axis=1) kullanarak sonucu level sütununa kaydet.


def employee_level(row):
    if row["salary"] >= 60000 and row["experience"] >= 5:
        return "Senior"
    if row['experience'] >= 3:
        return "Mid"
    return "Junior"

merged_df["level"] = merged_df.apply(employee_level, axis=1)

# 5. Son çalışan DataFrame'ini yazdır.

print(merged_df)

# 6. Department bazlı aggregation sonucunu yazdır.

print(department_summary)
