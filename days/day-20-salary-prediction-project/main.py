import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler


employees = pd.DataFrame({
    "city": [
        "Istanbul", "Ankara", "Izmir", "Istanbul", "Ankara",
        "Izmir", "Istanbul", "Ankara", "Izmir", "Istanbul",
        "Ankara", "Izmir", "Istanbul", "Ankara", "Izmir",
        "Istanbul", "Ankara", "Izmir", "Istanbul", "Ankara",
    ],
    "department": [
        "Software", "Data", "Design", "Software", "Data",
        "Software", "Design", "Data", "Software", "Design",
        "Software", "Data", "Design", "Software", "Data",
        "Software", "Design", "Data", "Software", "Data",
    ],
    "experience": [
        1, 2, 2, 3, 4,
        4, 5, 6, 7, 7,
        8, 9, 9, 10, 11,
        12, 13, 13, 14, 15,
    ],
    "projects": [
        1, 2, 3, 2, 4,
        3, 4, 5, 6, 5,
        7, 7, 6, 8, 8,
        9, 9, 10, 11, 12,
    ],
    "weekly_hours": [
        35, 40, 38, 42, 45,
        40, 37, 46, 44, 39,
        48, 45, 41, 50, 47,
        52, 43, 49, 54, 51,
    ],
    "salary": [
        32000, 36000, 35000, 41000, 45000,
        47000, 46000, 52000, 57000, 55000,
        63000, 67000, 65000, 72000, 76000,
        81000, 83000, 88000, 94000, 99000,
    ],
})


encoder = OneHotEncoder(sparse_output=False, handle_unknown="ignore")
scaler = StandardScaler()

X = employees[["city", "department", "experience", "projects", "weekly_hours"]]
y = employees["salary"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)

# start - stringler sayisal verilere cevrildi.
train_encoded = encoder.fit_transform(X_train[["city", "department"]])
test_encoded = encoder.transform(X_test[["city", "department"]])

train_encoded_df = pd.DataFrame(
    train_encoded,
    columns=encoder.get_feature_names_out(),
    index=X_train.index,
)
test_encoded_df = pd.DataFrame(
    test_encoded,
    columns=encoder.get_feature_names_out(),
    index=X_test.index,
)
# end - stringler sayisal verilere cevrildi.


# start - scaling training data
X_train_only_numeric = X_train[["experience", "projects", "weekly_hours"]]
X_train_only_numeric_scaled = scaler.fit_transform(X_train_only_numeric)

X_train_only_numeric_scaled_df = pd.DataFrame(
    X_train_only_numeric_scaled,
    columns=X_train_only_numeric.columns,
    index=X_train.index,
)

X_test_only_numeric = X_test[["experience", "projects", "weekly_hours"]]
X_test_only_numeric_scaled = scaler.transform(X_test_only_numeric)

X_test_only_numeric_scaled_df = pd.DataFrame(
    X_test_only_numeric_scaled,
    columns=X_test_only_numeric.columns,
    index=X_test.index,
)
# end - scaling training data


X_train_ready = pd.concat(
    [X_train_only_numeric_scaled_df, train_encoded_df],
    axis=1,
)
X_test_ready = pd.concat(
    [X_test_only_numeric_scaled_df, test_encoded_df],
    axis=1,
)


model = LinearRegression()
model.fit(X_train_ready, y_train)

predictions = model.predict(X_test_ready)

results_df = pd.DataFrame({
    "prediction": predictions,
    "real": y_test,
})

print(results_df)


# start - grafik uzerinde gosterimi
plt.title("Gercek Maas vs Tahmin Edilen")
plt.ylabel("Maas")
plt.xlabel("Kisi")
plt.scatter(X_test.index, y_test, label="Gercek maas")
plt.scatter(X_test.index, predictions, label="Tahmin")
plt.legend()
plt.show()
# end - grafik uzerinde gosterimi


r2 = r2_score(y_test, predictions)
mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
rmse = mse ** 0.5

print("r2 score:", r2)
print("mae:", mae)
print("mse:", mse)
print("rmse:", rmse)

# Olceklendirme sayisal feature'lari benzer olceklere getirmek icin yapilir.
# StandardScaler, train verisinden ogrendigi ortalama ve standart sapmayi kullanir.
# Kategoriler dogrudan matematiksel olarak hesaplanamaz. Bu yuzden encoding ile
# sayisal sutunlara cevrilmeleri gerekir.
# R2 degeri modelin hedef degiskeni ne kadar iyi acikladigini gosterir.
# Bu projede R2 cok yuksek cikti, yani test setinde model iyi tahmin yapti.
# MAE tahminlerle gercek degerler arasindaki ortalama mutlak hatayi gosterir.
# RMSE'de hatalarin karesi alinir, karelerin ortalamasi hesaplanir ve son olarak
# karekok alinir. Buyuk hatalar karesi alindigi icin daha fazla cezalandirilir.
# Veri sayisinin az olmasi sonucu yaniltabilir. Degerlerin bu kadar iyi cikmasi
# tesaduf bile olabilir. Daha fazla veri olsaydi sonuc daha guvenilir olurdu.
