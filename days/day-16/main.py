# minitask 1 - Polynomial Regression

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures

students = pd.DataFrame({
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "score": [40, 43, 47, 52, 60, 70, 81, 89, 95, 98]
})

# 1. Feature olarak study_hours sütununu X'e ata.
# X DataFrame olarak kalmalı.

X = students[["study_hours"]]

# 2. Target olarak score sütununu y'ye ata.

y = students["score"]
# 3. study_hours ve score arasında scatter plot çiz.

plt.scatter(X,y)
plt.xlabel("Study Hours")
plt.ylabel("Score")
plt.title("Study Hours vs Score")

# xlabel = "Study Hours"
# ylabel = "Score"
# title = "Study Hours vs Score"

# 4. Grafiği göster.

plt.show()


# minitask 2

# 1. PolynomialFeatures oluştur.
# degree=2 kullan.
# include_bias=False kullan.

poly = PolynomialFeatures(degree=2, include_bias=False)

# 2. X verisini fit_transform ile dönüştür.
# Sonucu X_poly değişkenine ata.

X_poly = poly.fit_transform(X)

# 3. Normal X'i print et.

print(X)

# 4. X_poly'yi print et.

print(X_poly)

# 5. X.shape ve X_poly.shape değerlerini ayrı ayrı print et.

print(X.shape)
print(X_poly.shape)


# minitask 3

from sklearn.linear_model import LinearRegression

# 1. LinearRegression modeli oluştur.
# regression_model değişkenine ata.

regression_model = LinearRegression()

# 2. Modeli X_poly ve y kullanarak eğit.

regression_model.fit(X_poly, y)

# 3. X_poly üzerinden tahmin yap.
# predictions değişkenine ata.

predictions = regression_model.predict(X_poly)

# 4. Modelin intercept_ değerini print et.
print(regression_model.intercept_)

# 5. Modelin coef_ değerlerini print et.
print(regression_model.coef_)

# 6. predictions değerlerini print et.

print(predictions)

plt.scatter(X, y)
plt.plot(X, predictions)
plt.show()