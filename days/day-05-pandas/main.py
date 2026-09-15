import pandas as pd
import pathlib

current_folder = pathlib.Path(__file__).resolve().parent


#minitask 1

# prices = pd.Series([35000,1200,2500,10000], index=['Laptop','Mouse','Keyboard','Monitor'])
# print(prices)
# print(prices["Keyboard"])

#minitask 2

# products = pd.DataFrame({
#     "Product": ["Laptop","Mouse", "Keyboard", "Monitor"],
#     "Price": [35000,1200,2500,10000],
#     "Stock": [5,20,10,7]
# })

# print(products)
# print(products["Price"])


#minitask 3

# products = pd.DataFrame({
#     "Product": ["Laptop","Mouse", "Keyboard", "Monitor"],
#     "Price": [35000,1200,2500,10000],
#     "Stock": [5,20,10,7]
# })

# print(products.shape)
# print(products.columns)
# print(products.dtypes)
# print(products["Stock"])
# print(products["Product"])


#minitask 4

# products = pd.DataFrame({
#     "Product": ["Laptop","Mouse", "Keyboard", "Monitor"],
#     "Price": [35000,1200,2500,10000],
#     "Stock": [5,20,10,7]
# })

# print(products.head(2))
# print('---------')
# print(products.tail(2))
# print('---------')
# products.info()
# print('---------')
# print(products.describe())

# students = pd.read_csv(current_folder / 'students.csv')
# print(students.head(3))
# print('------------------')
# print(students.shape)
# print('------------------')
# print(students.columns)
# print('------------------')
# students.info()
# print('------------------')
# print(students.describe())



#minitask 6

# students = pd.read_csv(current_folder / 'students.csv')

# print(students.loc[2])
# print("---------------------")
# print(students.loc[1,"Score"])
# print("---------------------")
# print(students.iloc[0])
# print("---------------------")
# print(students.iloc[4,1])


# minitask 7

# students = pd.read_csv(current_folder / 'students.csv')
# # 1. loc kullanarak Ali, Mehmet ve Ayse'nin satırlarını birlikte getir

# print (students.loc[range(0,3)])

# # 2. loc kullanarak sadece Name ve Score sütunlarını getir

# print(students.loc[range(0,students.shape[0]),['Name',"Score"]])

# # 3. iloc kullanarak ilk 3 öğrencinin tüm sütunlarını getir

# print(students.iloc[range(0,3)])

# # 4. iloc kullanarak ilk 3 öğrencinin sadece Name ve Score sütunlarını getir

# print(students.iloc[range(0,3), [0,2]])



# # minitask 8

# students = pd.read_csv(current_folder / 'students.csv')


# # 1. Score değeri 80 veya üzeri olan öğrencileri getir

# print(students[students["Score"] >= 80])

# # 2. Age değeri 22'den büyük olan öğrencileri getir

# print(students[students["Age"] > 22])

# # 3. Score değeri 80 veya üzeri olan öğrencilerden sadece Name ve Score sütunlarını getir

# print(students[students["Score"] >= 80].loc[:,["Name","Score"]])
# #ilk once loc kullanmak daha iyi.
# #students.loc[students["Score"] >= 80, ["Name", "Score"]]

# # 4. Age değeri 22 veya üzeri VE Score değeri 80 veya üzeri olan öğrencileri getir

# print(students[(students["Age"] >= 22) & (students["Score"] >= 80)])


# # minitask 9
# students = pd.read_csv(current_folder / 'students.csv')

# # 1. Score değeri 85'ten büyük olan öğrencileri getir

# print(students[students["Score"] > 85])

# # 2. Age değeri 21 ile 24 arasında olan öğrencileri getir

# print(students[(students["Age"] > 21) & (students["Age"] < 24) ])


# # 3. Score değeri 80'in altında VEYA Age değeri 21'in altında olan öğrencileri getir

# print(students[(students["Score"] < 80) | (students["Age"] < 21) ])


# # 4. Score değeri 80 veya üzeri olan öğrencilerden sadece Name sütununu getir

# print(students.loc[(students["Score"] >= 80), "Name"])


# # 5. Name değeri "Ali" olmayan öğrencileri getir

# print(students[~(students["Name"] == "Ali")])



# # minitask 10

# students = pd.read_csv(current_folder / 'students.csv')

# # 1. Öğrencileri önce Age sütununa göre küçükten büyüğe,
# # Age eşitse Score sütununa göre büyükten küçüğe sırala

# print(students.sort_values(["Age","Score"], ascending=[True,False]))


# # minitask 11

# students = pd.read_csv(current_folder / 'students.csv')


# # 1. Score değeri 80 veya üzeriyse True, değilse False olacak şekilde
# # "Passed" isminde yeni bir sütun oluştur

# students["Passed"] = students["Score"] >= 80



# # 2. Age sütununun 2 katını içeren "Double_Age" isminde yeni bir sütun oluştur

# students["Double_Age"] = students["Age"] * 2


# minitask 12

# students = pd.read_csv(current_folder / "students.csv")

# # 1. "Age" sütununu sil

# students = students.drop(columns=["Age"])

# # 2. "Score" sütununun adını "Exam_Score" olarak değiştir

# students = students.rename(columns={"Score": "Exam_Score"})



# # minitask 13

# students_missing = pd.DataFrame({
#     "Name": ["Ali", "Mehmet", "Ayse", "Can", "Zeynep"],
#     "Age": [23, None, 25, 22, None],
#     "Score": [85, 70, None, 78, 88]
# })

# # 1. Her sütunda kaç tane eksik değer olduğunu göster

# print(students_missing.isna().sum())

# # 2. Age sütunundaki eksik değerleri Age ortalamasıyla doldur

# students_missing["Age"] = students_missing["Age"].fillna(students_missing["Age"].mean())

# # 3. Score sütununda eksik değer bulunan satırları sil

# students_missing = students_missing.dropna(subset=["Score"])





# minitask 14

# students_categories = pd.DataFrame({
#     "Name": ["Ali", "Mehmet", "Ayse", "Can", "Zeynep", "Ece"],
#     "Department": ["Software", "Software", "AI", "Software", "AI", "Data"],
#     "Passed": [True, False, True, False, True, True]
# })

# # 1. Department sütunundaki farklı bölümleri göster

# print(students_categories["Department"].unique())

# # 2. Her bölümde kaç öğrenci olduğunu göster

# print(students_categories["Department"].value_counts())

# # 3. Passed sütununda kaç True ve kaç False olduğunu göster

# print(students_categories["Passed"].value_counts())


# Day 05 - Final Task

students = pd.DataFrame({
    "Name": ["Ali", "Mehmet", "Ayse", "Can", "Zeynep", "Ece"],
    "Age": [23, 21, 25, 22, None, 24],
    "Department": ["Software", "Software", "AI", "Software", "AI", "Data"],
    "Score": [85, 70, 95, None, 88, 76]
})

# 1. Veri setinin genel yapısını incele:
# shape, info() ve describe() çıktılarını göster

print(students.shape)
students.info()
print(students.describe())


# 2. Age sütunundaki eksik değerleri Age ortalamasıyla doldur

students["Age"] = students["Age"].fillna(students["Age"].mean())

# 3. Score sütununda eksik değer bulunan satırları sil

students["Score"] = students["Score"].dropna()

# 4. Score >= 80 ise True olacak şekilde "Passed" sütunu oluştur

students["Passed"] = students["Score"] >= 80

# 5. Sadece Passed == True olan öğrencilerden
# Name, Department ve Score sütunlarını getir

passed_students = students.loc[students["Passed"] == True,["Name", "Department", 'Score']]
print(passed_students)

# 6. Sonucu Score değerine göre büyükten küçüğe sırala

print(passed_students["Score"].sort_values(ascending=True))

# 7. Her Department'ta kaç öğrenci kaldığını göster

print(passed_students["Department"].value_counts())