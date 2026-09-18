# Day 10 - Statistics Basics

## Goal

Understand basic statistics concepts used in data analysis and machine learning.

## Topics Covered

- Mean
- Median
- Variance
- Standard deviation
- Quartiles
- IQR
- Outlier detection
- Removing outliers
- Correlation basics

## Key Concepts

### Mean

Mean is the average value of a dataset.

```python
scores.mean()
```

### Median

Median is the middle value of sorted data.

```python
np.median(scores)
```

### Variance

Variance shows how spread out the values are from the mean.

```python
scores.var()
```

### Standard Deviation

Standard deviation shows the spread of values in the original unit.

```python
scores.std()
```

### Quartiles

Quartiles split the data into four parts.

```python
q1 = np.percentile(scores, 25)
q3 = np.percentile(scores, 75)
```

### IQR

IQR means Interquartile Range.

```python
iqr = q3 - q1
```

### Outlier Detection

Outliers can be detected using lower and upper bounds.

```python
lower_bound = q1 - (1.5 * iqr)
upper_bound = q3 + (1.5 * iqr)
```

A value is an outlier if it is smaller than the lower bound or greater than the upper bound.

```python
outliers = scores[(scores < lower_bound) | (scores > upper_bound)]
```

Normal values should be inside both bounds.

```python
clean_scores = scores[
    (scores >= lower_bound) & (scores <= upper_bound)
]
```

## Final Check Notes

The value `150` is an outlier in the scores dataset.

The original mean is higher because the outlier pulls the average upward.

After removing the outlier, the mean becomes lower and more representative of the normal scores.

## Correlation Note

Correlation shows the direction and strength of the relationship between two variables.

A correlation around `0.87` means there is a strong positive relationship.

However, correlation does not prove causation.

This means we cannot say:

> More study hours definitely cause higher scores.

We can only say:

> Study hours and scores have a strong positive relationship in this dataset.

## Day Summary

In Day 10, I learned how to calculate basic statistics values, detect outliers using the IQR method, remove outliers, compare mean values before and after cleaning, and interpret a basic correlation result.