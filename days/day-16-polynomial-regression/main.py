# # minitask 1 - Polynomial Regression

# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.preprocessing import PolynomialFeatures

# students = pd.DataFrame({
#     "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#     "score": [40, 43, 47, 52, 60, 70, 81, 89, 95, 98]
# })

# # 1. Feature olarak study_hours sütununu X'e ata.
# # X DataFrame olarak kalmalı.

# X = students[["study_hours"]]

# # 2. Target olarak score sütununu y'ye ata.

# y = students["score"]
# # 3. study_hours ve score arasında scatter plot çiz.

# plt.scatter(X,y)
# plt.xlabel("Study Hours")
# plt.ylabel("Score")
# plt.title("Study Hours vs Score")

# # xlabel = "Study Hours"
# # ylabel = "Score"
# # title = "Study Hours vs Score"

# # 4. Grafiği göster.

# plt.show()


# # minitask 2

# # 1. PolynomialFeatures oluştur.
# # degree=2 kullan.
# # include_bias=False kullan.

# poly = PolynomialFeatures(degree=3, include_bias=False)

# # 2. X verisini fit_transform ile dönüştür.
# # Sonucu X_poly değişkenine ata.

# X_poly = poly.fit_transform(X)

# # 3. Normal X'i print et.

# print(X)

# # 4. X_poly'yi print et.

# print(X_poly)

# # 5. X.shape ve X_poly.shape değerlerini ayrı ayrı print et.

# print(X.shape)
# print(X_poly.shape)


# # minitask 3

# from sklearn.linear_model import LinearRegression

# # 1. LinearRegression modeli oluştur.
# # regression_model değişkenine ata.

# regression_model = LinearRegression()

# # 2. Modeli X_poly ve y kullanarak eğit.

# regression_model.fit(X_poly, y)

# # 3. X_poly üzerinden tahmin yap.
# # predictions değişkenine ata.

# predictions = regression_model.predict(X_poly)

# # 4. Modelin intercept_ değerini print et.
# print(regression_model.intercept_)

# # 5. Modelin coef_ değerlerini print et.
# print(regression_model.coef_)

# # 6. predictions değerlerini print et.

# print(predictions)




# # minitask 4

# # 1. Gerçek verileri scatter plot ile çiz.
# # X ekseni: study_hours
# # y ekseni: score

# plt.scatter(X, y, label="Actual")

# # 2. Polynomial Regression tahminlerini çizgi olarak çiz.
# # x ekseni: X
# # y ekseni: predictions

# plt.plot(X, predictions, label="Polynomial Prediction")


# # 3. xlabel = "Study Hours"

# plt.xlabel("Study Hours")

# # 4. ylabel = "Score"

# plt.ylabel("Score")

# # 5. title = "Polynomial Regression"

# plt.title("Polynomial Regression")

# # 6. legend ekle.

# plt.legend()
# # Gerçek veriler için label="Actual"
# # Tahmin çizgisi için label="Polynomial Prediction"

# # 7. Grafiği göster.

# plt.show()


# # minitask 5

# from sklearn.linear_model import LinearRegression

# # 1. Normal X ve y ile LinearRegression modeli oluştur.
# # linear_model değişkenine ata.

# linear_model = LinearRegression()

# # 2. linear_model'i X ve y ile eğit.

# linear_model.fit(X, y)

# # 3. X üzerinden tahmin yap.
# # linear_predictions değişkenine ata.

# linear_predictions = linear_model.predict(X)

# # 4. Gerçek verileri scatter plot ile çiz.
# # label="Actual"

# plt.scatter(X, y, label="Actual")

# # 5. Linear Regression tahminlerini çiz.
# # label="Linear Regression"

# plt.plot(X, linear_predictions, label="Linear Regression")


# # 6. Polynomial Regression tahminlerini çiz.
# # label="Polynomial Regression"

# plt.plot(X, predictions, label="Polynomial")


# # 7. xlabel = "Study Hours"
# # ylabel = "Score"
# # title = "Linear vs Polynomial Regression"

# plt.xlabel("Study Hours")
# plt.ylabel("Score")
# plt.title('Linear vs Polynomial Regression')

# # 8. legend ekle.

# plt.legend()

# # 9. Grafiği göster.

# plt.show()



# # minitask 6

# import pandas as pd

# from sklearn.linear_model import LinearRegression
# from sklearn.preprocessing import PolynomialFeatures
# from sklearn.metrics import r2_score

# students = pd.DataFrame({
#     "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#     "score": [40, 43, 47, 52, 60, 70, 81, 89, 95, 98]
# })

# # 1. study_hours sütununu X'e ata.
# # X DataFrame olarak kalmalı.

# X = students[["study_hours"]]

# # 2. score sütununu y'ye ata.

# y = students["score"]

# # 3. LinearRegression modeli oluştur ve X, y ile eğit.

# linear_regression = LinearRegression()

# linear_regression.fit(X,y)

# # 4. X üzerinden linear tahminleri oluştur.
# # linear_predictions değişkenine ata.

# linear_predictions = linear_regression.predict(X)

# # 5. degree=2 ve include_bias=False olacak şekilde
# # PolynomialFeatures oluştur.

# poly = PolynomialFeatures(degree=2, include_bias=False)

# # 6. X'i polynomial feature'lara dönüştür.
# # X_poly değişkenine ata.

# x_poly = poly.fit_transform(X)

# # 7. İkinci bir LinearRegression modeli oluştur.
# # polynomial_model değişkenine ata.

# polynomial_model = LinearRegression()

# # 8. polynomial_model'i X_poly ve y ile eğit.

# polynomial_model.fit(x_poly, y)

# # 9. X_poly üzerinden polynomial tahminleri oluştur.
# # polynomial_predictions değişkenine ata.

# polynomial_predictions = polynomial_model.predict(x_poly)

# # 10. Linear Regression için R² hesapla.
# # linear_r2 değişkenine ata.

# linear_r2 = r2_score(y, linear_predictions)

# # 11. Polynomial Regression için R² hesapla.
# # polynomial_r2 değişkenine ata.

# polynomial_r2 = r2_score(y, polynomial_predictions)

# # 12. İki R² değerini ayrı ayrı print et.

# print(linear_r2)
# print(polynomial_r2)


# # minitask 7

# import pandas as pd
# import matplotlib.pyplot as plt

# from sklearn.linear_model import LinearRegression
# from sklearn.preprocessing import PolynomialFeatures
# from sklearn.metrics import r2_score


# students = pd.DataFrame({
#     "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#     "score": [40, 43, 47, 52, 60, 70, 81, 89, 95, 98]
# })

# X = students[["study_hours"]]
# y = students["score"]

# results = []

# plt.scatter(X, y, label="Actual")

# for degree in range(1, 6):

#     poly = PolynomialFeatures(
#         degree=degree,
#         include_bias=False
#     )

#     X_poly = poly.fit_transform(X)

#     model = LinearRegression()
#     model.fit(X_poly, y)

#     predictions = model.predict(X_poly)

#     score = r2_score(y, predictions)

#     results.append({
#         "degree": degree,
#         "predictions": predictions,
#         "r2_score": score
#     })

#     plt.plot(
#         X,
#         predictions,
#         label=f"Degree {degree}"
#     )

# plt.xlabel("Study Hours")
# plt.ylabel("Score")
# plt.title("Polynomial Regression Degrees")
# plt.legend()

# plt.show()

# for result in results:
#     print(
#         f"Degree {result['degree']}: "
#         f"R² = {result['r2_score']:.5f}"
#     )


# minitask 8 - Overfitting fikri

# import pandas as pd
# from sklearn.preprocessing import PolynomialFeatures
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import r2_score

# students = pd.DataFrame({
#     "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#     "score": [40, 43, 47, 52, 60, 70, 81, 89, 95, 98]
# })

# X = students[["study_hours"]]
# y = students["score"]

# # 1. degree=2 için PolynomialFeatures oluştur.
# poly = PolynomialFeatures(degree=2, include_bias=False)
# # 2. X'i dönüştür.
# X_poly = poly.fit_transform(X)
# # 3. LinearRegression modeli oluştur ve eğit.
# model = LinearRegression()
# model.fit(X_poly, y)
# # 4. Tahmin yap.
# predictions_2 = model.predict(X_poly)
# # 5. R² değerini hesapla ve print et.

# r2_2 = r2_score(y, predictions_2)

# # 6. Aynı işlemleri degree=9 için de yap.


# poly = PolynomialFeatures(degree=9, include_bias=False)
# X_poly_9 = poly.fit_transform(X)
# model = LinearRegression()
# model.fit(X_poly_9, y)
# predictions_9 = model.predict(X_poly_9)

# r2_9 = r2_score(y, predictions_9)

# # 7. Degree 2 ve degree 9 R² değerlerini karşılaştır.

# print("r2_2:", r2_2)
# print("r2_9:", r2_9)


# Day 16 - Final Check

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


students = pd.DataFrame({
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "score": [40, 43, 47, 52, 60, 70, 81, 89, 95, 98]
})

# 1. study_hours sütununu X'e ata.
# X DataFrame olarak kalmalı.

X = students[["study_hours"]]

# 2. score sütununu y'ye ata.

y = students["score"]


# 3. degree=2 ve include_bias=False olacak şekilde
# PolynomialFeatures oluştur.

poly = PolynomialFeatures(degree=2, include_bias=False)


# 4. X'i polynomial feature'lara dönüştür.
# X_poly değişkenine ata.

X_poly = poly.fit_transform(X)


# 5. LinearRegression modeli oluştur.

model = LinearRegression()

# 6. Modeli X_poly ve y ile eğit.

model.fit(X_poly, y)

# 7. X_poly üzerinden tahmin yap.
# predictions değişkenine ata.

predictions = model.predict(X_poly)
# 8. R² değerini hesapla.
# r2 değişkenine ata.

r2 = r2_score(y, predictions)
# 9. R² değerini print et.

print("r2 score is: ", r2)
# 10. Gerçek verileri scatter plot olarak çiz.
# label="Actual"

plt.scatter(X,y, label="Actual")


# 11. Polynomial Regression tahminlerini çiz.
# label="Polynomial Regression"

plt.plot(X, predictions, label="Polynomial Regression")

# 12.
# xlabel = "Study Hours"
# ylabel = "Score"
# title = "Polynomial Regression - Day 16 Final Check"

plt.xlabel("Study Hours")
plt.ylabel('Score')
plt.title("Polynomial Regression - Day 16 Final Check")

# 13. legend ekle ve grafiği göster.

plt.legend()

plt.show()