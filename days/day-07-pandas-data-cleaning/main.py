import pandas as pd


# Mini task 1 - Missing values
students = pd.DataFrame({
    "name": ["Ali", "Ayşe", "Mehmet", "Zeynep", "Can", "Ece"],
    "age": [23, 21, None, 24, 20, None],
    "score": [85, 92, 58, None, 64, 88],
    "city": ["Istanbul", "Ankara", "Izmir", "Istanbul", None, "Ankara"]
})

print(students.isnull())
print(students.isnull().sum())
print(students[students["age"].isnull()])
print(students[students["score"].notnull()])
print(students.loc[students["city"].isnull(), ["name", "city"]])


# Mini task 2 - dropna and fillna
students = pd.DataFrame({
    "name": ["Ali", "Ayşe", "Mehmet", "Zeynep", "Can", "Ece"],
    "age": [23, 21, None, 24, 20, None],
    "score": [85, 92, 58, None, 64, 88],
    "city": ["Istanbul", "Ankara", "Izmir", "Istanbul", None, "Ankara"]
})

clean_students = students.dropna(subset=["score"])
students["age"] = students["age"].fillna(students["age"].mean())
students["city"] = students["city"].fillna("Unknown")

print(students)
print(clean_students)


# Mini task 3 - Duplicates
students = pd.DataFrame({
    "name": ["Ali", "Ayşe", "Mehmet", "Ali", "Can", "Ayşe"],
    "age": [23, 21, 19, 23, 20, 21],
    "score": [85, 92, 58, 85, 64, 92],
    "city": ["Istanbul", "Ankara", "Izmir", "Istanbul", "Bursa", "Ankara"]
})

print(students.duplicated())
print(students[students.duplicated()])

clean_students = students.drop_duplicates()
print(clean_students)

print(students.duplicated(subset=["name"]))
print(students[students.duplicated(subset=["name"])])


# Mini task 4 - Sorting
students = pd.DataFrame({
    "name": ["Ali", "Ayşe", "Mehmet", "Zeynep", "Can", "Ece"],
    "age": [23, 21, 19, 24, 20, 22],
    "score": [85, 92, 58, 76, 64, 88],
    "city": ["Istanbul", "Ankara", "Izmir", "Istanbul", "Bursa", "Ankara"]
})

print(students.sort_values("score", ascending=True))
print(students.sort_values("score", ascending=False))
print(students.sort_values("age"))
print(students.sort_values(by=["city", "score"], ascending=[True, False]))


# Mini task 5 - GroupBy
students = pd.DataFrame({
    "name": ["Ali", "Ayşe", "Mehmet", "Zeynep", "Can", "Ece", "Mert", "Elif"],
    "age": [23, 21, 19, 24, 20, 22, 25, 21],
    "score": [85, 92, 58, 76, 64, 88, 90, 80],
    "city": [
        "Istanbul", "Ankara", "Izmir", "Istanbul",
        "Bursa", "Ankara", "Istanbul", "Izmir"
    ]
})

print(students.groupby("city")["score"].mean())
print(students.groupby("city")["score"].max())
print(students.groupby("city")["name"].count())
print(students.groupby("city")["score"].agg(["mean", "min", "max"]))


# Day 07 - Final task
students = pd.DataFrame({
    "name": ["Ali", "Ayşe", "Mehmet", "Zeynep", "Can", "Ece", "Ali", "Mert"],
    "age": [23, 21, None, 24, 20, 22, 23, None],
    "score": [85, 92, 58, None, 64, 88, 85, 90],
    "city": ["Istanbul", "Ankara", "Izmir", "Istanbul", None, "Ankara", "Istanbul", "Istanbul"]
})

print(students.isnull().sum())

students["age"] = students["age"].fillna(students["age"].mean())
students["city"] = students["city"].fillna("Unknown")

clean_students = students.dropna(subset=["score"])
clean_students = clean_students.drop_duplicates()
clean_students = clean_students.sort_values("score", ascending=False)

print(clean_students)
print(clean_students.groupby("city")["score"].mean())
print(clean_students.groupby("city")["score"].agg(["mean", "min", "max"]))
