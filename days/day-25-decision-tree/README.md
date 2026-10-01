# Day 25 - Decision Tree

## Topics Covered

- Decision Tree classification
- How a tree splits data into decision nodes
- `DecisionTreeClassifier`
- `max_depth`
- `min_samples_split`
- `min_samples_leaf`
- `accuracy_score`
- `get_depth()`
- `get_n_leaves()`
- `feature_importances_`

## Key Ideas

A decision tree makes predictions by asking a sequence of questions about feature values.

Each split divides the current group of samples into smaller groups. The model keeps choosing splits that make the target groups cleaner.

Important control parameters:

- `max_depth` limits how deep the tree can grow.
- `min_samples_split` controls whether a node has enough samples to be split.
- `min_samples_leaf` controls the minimum number of samples that must remain in each child/leaf after a split.

## Final Check

Built a Decision Tree classification model using:

- Age
- Income
- Purchase status

The data was split into training and testing sets, then classified using `DecisionTreeClassifier` with:

- `max_depth=3`
- `min_samples_split=4`
- `min_samples_leaf=2`
- `random_state=42`

Model performance was evaluated using accuracy.

The trained tree was also inspected with:

- `get_depth()`
- `get_n_leaves()`
- `feature_importances_`

## Day-End Summary

Day 25 focused on understanding how a decision tree grows and how its growth can be controlled.

The core idea:

```text
max_depth limits how far the tree can grow.
min_samples_split checks whether the current node can split.
min_samples_leaf checks whether the children after a split are large enough.
```

## Next

Day 26 - Random Forest
