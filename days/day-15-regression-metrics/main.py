from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np


# minitask 1 - RMSE

y_test = [50, 60, 70, 80, 90]
predictions = [52, 58, 73, 77, 94]

# 1. MSE'yi hesapla.
mse = mean_squared_error(y_test, predictions)

# 2. MSE'nin karekökünü alarak RMSE'yi hesapla.
rmse = np.sqrt(mse)

# 3. RMSE değerini yazdır.
print(rmse)


# Day 15 - Final Check

y_test = [55, 62, 70, 78, 85, 92]
predictions = [57, 60, 74, 75, 88, 89]

# 1. MAE hesapla.
mae = mean_absolute_error(y_test, predictions)

# 2. MSE hesapla.
mse = mean_squared_error(y_test, predictions)

# 3. RMSE hesapla.
rmse = np.sqrt(mse)

# 4. R² hesapla.
r2 = r2_score(y_test, predictions)

# 5. Tüm sonuçları ayrı ayrı print et.
print(mae)
print(mse)
print(rmse)
print(r2)
