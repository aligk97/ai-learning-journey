# Day 25 - Final Check

import pandas as pd

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


customers = pd.DataFrame({
    "age": [
        18, 20, 21, 23, 25,
        27, 29, 31, 33, 35,
        38, 40, 42, 45, 48,
        50, 52, 55, 58, 60,
    ],
    "income": [
        18000, 20000, 22000, 24000, 27000,
        30000, 32000, 35000, 38000, 40000,
        43000, 45000, 48000, 52000, 55000,
        58000, 62000, 65000, 70000, 75000,
    ],
    "purchased": [
        0, 0, 0, 0, 0,
        0, 1, 0, 1, 1,
        0, 1, 1, 1, 1,
        1, 0, 1, 1, 1,
    ],
})


# 1. age ve income sütunlarını X değişkenine ata.

X = customers[["age", "income"]]


# 2. purchased sütununu y değişkenine ata.

y = customers["purchased"]


# 3. Veriyi train ve test olarak ayır.
# test_size=0.25
# random_state=42

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
)


# 4. DecisionTreeClassifier oluştur.
# max_depth=3
# min_samples_split=4
# min_samples_leaf=2
# random_state=42

model = DecisionTreeClassifier(
    max_depth=3,
    min_samples_split=4,
    min_samples_leaf=2,
    random_state=42,
)


# 5. Modeli train verisiyle eğit.

model.fit(X_train, y_train)


# 6. X_test üzerinde tahmin yap.

predictions = model.predict(X_test)


# 7. Accuracy hesapla ve print et.

accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)


# 8. Ağacın gerçek derinliğini yazdır.

print("Tree Depth:", model.get_depth())


# 9. Ağacın kaç tane leaf oluşturduğunu yazdır.

print("Leaf Count:", model.get_n_leaves())


# 10. Feature importance değerlerini yazdır.
# age ve income için ayrı ayrı göster.

print("Feature Importances:")
for feature_name, importance in zip(X.columns, model.feature_importances_):
    print(f"{feature_name}: {importance:.3f}")


# 11. Kendi yorumun:
#
# a) min_samples_split=4 neyi kontrol ediyor?
#
# Bir node içerisinde en az 4 sample varsa,
# o node bölünmeye aday olabilir.
#
# b) min_samples_leaf=2 neyi kontrol ediyor?
#
# Bir split yapıldıktan sonra oluşan her child/leaf tarafında
# en az 2 sample kalması gerekir.
#
# c) max_depth=3 neyi kontrol ediyor?
#
# Ağacın en fazla depth 3'e kadar büyümesini kontrol eder.
#
# d) Bir node içerisinde 3 sample varsa,
#    min_samples_split=4 olduğunda tekrar bölünebilir mi?
#
# Hayır.
# Çünkü node içerisinde 3 sample var.
# 3 >= 4 olmadığı için bölünemez.
#
# e) Bir node içerisinde 10 sample varsa ama yapılacak split
#    9 sample / 1 sample oluşturuyorsa,
#    min_samples_leaf=2 olduğunda bu split yapılabilir mi?
#
# Hayır.
# Çünkü bir tarafta sadece 1 sample kalıyor.
# min_samples_leaf=2 şartını sağlamıyor.
