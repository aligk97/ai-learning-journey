# Day 26 - Random Forest

## Goal

Understand ensemble learning and train a Random Forest classifier.

## Topics Covered

- Random Forest and ensemble learning
- Bootstrap sampling and random feature subsets
- `RandomForestClassifier`
- `n_estimators` and `random_state`
- `fit()`, `predict()`, and accuracy
- `feature_importances_`
- Decision Tree vs Random Forest

## Key Concepts

Random Forest combines many Decision Trees. Each tree uses a bootstrap sample, and each split considers a random subset of features.

`n_estimators=100` creates 100 trees. `random_state=42` makes the random choices reproducible.

Voting is a useful intuition. In scikit-learn, classification averages the trees' class probabilities and chooses the class with the highest average.

Scaling is generally unnecessary for tree-based models.

`feature_importances_` measures relative importance through impurity reduction. It does not establish causation. Correlated features can share importance.

| Decision Tree | Random Forest |
|---|---|
| One tree | Many trees |
| Easier to interpret | Harder to interpret |
| Usually faster | More computation |
| Can overfit | Often reduces variance; can still overfit |

## Final Check

`random_forest.py` predicts `purchased` from `age`, `income`, and `experience`, using 20 synthetic customers, a 20% test split, and 100 trees.

It prints accuracy, feature importances, actual labels, and predictions.

Four test samples are only a learning example, not reliable performance evidence.

## Run

From the repository root:

```bash
uv run python days/day-26-random-forest/random_forest.py
```

## Reference

[Scikit-learn: RandomForestClassifier](https://scikit-learn.org/1.8/modules/generated/sklearn.ensemble.RandomForestClassifier.html)
