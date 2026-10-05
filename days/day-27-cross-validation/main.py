import pandas as pd

from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


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

cv = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

models = {
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )
}

for name, model in models.items():
    scores = cross_val_score(
        model,
        X,
        y,
        cv=cv,
        scoring="accuracy"
    )

    print(f"\n{name}")
    print("Fold scores:", scores)
    print("Mean accuracy:", scores.mean())
    print("Score std:", scores.std())
