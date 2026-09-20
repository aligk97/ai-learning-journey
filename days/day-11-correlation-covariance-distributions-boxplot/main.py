import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Mini task 1 - Correlation
students = pd.DataFrame({
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "score": [48, 55, 61, 68, 75, 82, 88, 95],
    "sleep_hours": [8, 7, 8, 6, 7, 6, 5, 5]
})

print("Mini task 1 - Correlation")
print(students["study_hours"].corr(students["score"]))
print(students["sleep_hours"].corr(students["score"]))
print(students.corr(numeric_only=True))


# Mini task 2 - Covariance
print("\nMini task 2 - Covariance")
print(students["study_hours"].cov(students["score"]))
print(students["sleep_hours"].cov(students["score"]))
print(students.cov(numeric_only=True))


# Mini task 3 - Distribution / histogram
scores = [
    45, 50, 52, 55, 58,
    60, 62, 65, 67, 68,
    70, 71, 72, 73, 75,
    78, 80, 82, 85, 88,
    90, 92, 95
]

plt.figure()
plt.hist(scores, bins=5)
plt.title("Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.show()


# Mini task 4 - Mean, median and skewness
skewed_scores = pd.Series([
    50, 52, 53, 54, 55,
    56, 57, 58, 60, 95
])

mean_score = skewed_scores.mean()
median_score = skewed_scores.median()
skewness_score = skewed_scores.skew()

print("\nMini task 4 - Mean, median and skewness")
print(mean_score)
print(median_score)
print(skewness_score)

plt.figure()
plt.hist(skewed_scores, bins=5)
plt.title("Skewed Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.show()

print("right skewed")


# Mini task 5 - Boxplot and outlier
boxplot_scores = np.array([
    52, 58, 61, 65, 68,
    70, 72, 75, 78, 82,
    85, 88, 92, 150
])

plt.figure()
plt.boxplot(boxplot_scores)
plt.title("Score Boxplot")
plt.show()

print("\nMini task 5 - Boxplot and outlier")
print("150 potential outlier")


# Day 11 - Final check
students = pd.DataFrame({
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "sleep_hours": [8, 8, 7, 7, 7, 6, 6, 6, 5, 5],
    "score": [45, 52, 58, 63, 68, 74, 79, 84, 90, 150]
})

print("\nDay 11 - Final check")
print(students.corr(numeric_only=True))
print(students["study_hours"].corr(students["score"]))

print(students["score"].mean())
print(students["score"].median())
print(students["score"].skew())

q1 = np.percentile(students["score"], 25)
q3 = np.percentile(students["score"], 75)
iqr = q3 - q1
upper_bound = q3 + 1.5 * iqr

print(q1)
print(q3)
print(iqr)
print(upper_bound)

plt.figure()
plt.hist(students["score"], bins=5)
plt.title("Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.show()

plt.figure()
plt.boxplot(students["score"])
plt.title("Score Boxplot")
plt.show()

plt.figure()
plt.plot(students["study_hours"], students["score"], marker="o")
plt.title("Study Hours vs Score")
plt.xlabel("Study Hours")
plt.ylabel("Score")
plt.show()

plt.figure()
plt.scatter(students["study_hours"], students["score"])
plt.title("Study Hours vs Score")
plt.xlabel("Study Hours")
plt.ylabel("Score")
plt.show()

print("study_hours ile score arasinda guclu pozitif iliski var.")
print("Score dagilimi belirgin sekilde right-skewed.")
print("150 potential outlier.")
