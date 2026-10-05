# Day 27 - Cross Validation

## Goal

Evaluate machine learning models more reliably than with a single train/test split.

## Topics Covered

- Cross Validation
- K-Fold logic
- Stratified K-Fold
- `cross_val_score`
- Mean validation score
- Score variation / standard deviation
- Comparing models with the same folds

## Key Concepts

A single train/test split can give a lucky or unlucky result depending on which samples land in the test set.

Cross Validation repeats the train/validation process across multiple folds so every sample gets a chance to be used for validation.

With 5-fold Cross Validation, the dataset is divided into 5 parts. The model trains 5 times, each time using a different fold for validation.

`cross_val_score()` returns one score for each fold.

The mean score gives a more stable estimate of performance. The standard deviation shows how much the score changes between folds.

For classification, `StratifiedKFold` tries to preserve the class ratio in each fold.

Cross Validation does not automatically choose the best model. We compare models using the same validation strategy and then decide which model is more promising.

## Final Check

`main.py` compares a Decision Tree and Random Forest using 5-fold Stratified Cross Validation.

For each model it prints:

- Fold scores
- Mean accuracy
- Score standard deviation

## Run

From the repository root:

```bash
uv run python days/day-27-cross-validation/main.py
```

## Reference

[Scikit-learn: Cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html)
