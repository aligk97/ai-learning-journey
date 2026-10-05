import pandas as pd

from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier


customers = pd.DataFrame({
    "age": [18, 20, 21, 23, 25, 27, 29, 31, 33, 35,
            38, 40, 42, 45, 48, 50, 52, 55, 58, 60],
    "income": [18000, 20000, 22000, 24000, 27000,
               30000, 32000, 35000, 38000, 40000,
               43000, 45000, 48000, 52000, 55000,
               58000, 62000, 65000, 70000, 75000],
    "purchased": [0, 0, 0, 0, 0,
                  0, 1, 0, 1, 0,
                  1, 0, 1, 1, 1,
                  1, 1, 1, 1, 1]
})

X = customers[["age", "income"]]
y = customers["purchased"]

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("knn", KNeighborsClassifier())
])

param_grid = {
    "knn__n_neighbors": [3, 5, 7],
    "knn__weights": ["uniform", "distance"]
}

grid_search = GridSearchCV(
    estimator=pipeline,
    param_grid=param_grid,
    cv=5,
    scoring="accuracy",
    refit=True
)

grid_search.fit(X, y)

print("Best parameters:", grid_search.best_params_)
print("Best CV score:", grid_search.best_score_)
print("Best estimator:", grid_search.best_estimator_)

new_customer = pd.DataFrame({
    "age": [34],
    "income": [42000]
})

prediction = grid_search.predict(new_customer)
print("New customer prediction:", prediction[0])
