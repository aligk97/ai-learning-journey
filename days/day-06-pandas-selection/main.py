import pandas as pd

students = pd.DataFrame({
    "name": ["Ali", "Ayşe", "Mehmet", "Zeynep", "Can", "Ece"],
    "age": [23, 21, 19, 24, 20, 22],
    "score": [85, 92, 58, 76, 64, 88],
    "city": ["Istanbul", "Ankara", "Izmir", "Istanbul", "Bursa", "Ankara"]
})

print(students[["name", "score"]])
print(students.iloc[:3, [0, 1, 2]])
print(students.loc[2:4, ["name", "city"]])
print(students[students["score"] >= 70])
print(students[(students["city"] == "Istanbul") & (students["score"] > 70)])
print(students[(students["city"] == "Ankara") | (students["score"] > 90)])
print(students.loc[students["score"] > 70, ["name", "score"]])
