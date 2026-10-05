# Day 28 - Pipeline + GridSearchCV

## Goal

Build a cleaner machine learning workflow and search for better hyperparameters with Cross Validation.

## Topics Covered

- `Pipeline`
- Combining preprocessing and a model
- `GridSearchCV`
- Parameter grids
- `best_params_`
- `best_score_`
- `best_estimator_`
- `refit=True`
- GridSearchCV vs RandomizedSearchCV

## Key Concepts

A Pipeline keeps preprocessing and the model together in one workflow.

This is especially useful when scaling is required because the scaler is fitted only on the training portion inside each Cross Validation fold, helping prevent data leakage.

`GridSearchCV` tries every hyperparameter combination in `param_grid` and evaluates each combination with Cross Validation.

`best_params_` shows the best parameter combination found.

`best_score_` shows the mean Cross Validation score of that combination.

`best_estimator_` contains the fitted Pipeline using the best parameters.

With `refit=True`, GridSearchCV fits the best configuration again on the full dataset after the search finishes. This means `grid_search.predict()` can be used directly afterward.

GridSearchCV does not magically know every possible model or parameter. It searches only the values we provide.

RandomizedSearchCV is an alternative that samples a limited number of parameter combinations instead of trying every combination.

## Final Check

`main.py` creates a Pipeline with `StandardScaler` and `KNeighborsClassifier`, searches multiple KNN settings, and prints the best parameters, best Cross Validation score, and best estimator.

It then uses the refitted best Pipeline to predict a new customer.

## Run

From the repository root:

```bash
uv run python days/day-28-pipeline-gridsearch/main.py
```

## Reference

[Scikit-learn: GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html)
