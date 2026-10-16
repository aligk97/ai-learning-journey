# Day 35 — Loss Functions & Gradient Descent

## Goal
Understand how a neural network measures its prediction error and uses gradients to improve its parameters.

## Topics Covered
- Forward propagation recap: `y_pred = w * x + b`
- Loss functions: Mean Squared Error (MSE) and Binary Cross-Entropy (BCE)
- Gradient Descent and learning rate
- Chain rule and the basic idea of backpropagation
- NumPy implementation of a small training loop

## Key Concepts

### 1. Mean Squared Error (MSE)
MSE is commonly used for regression:

```text
MSE = (1/n) * sum((y_true - y_pred)**2)
```

It squares errors, so larger mistakes contribute more to the loss.

### 2. Binary Cross-Entropy (BCE)
BCE is commonly used for binary classification, where `y` is 0 or 1 and `p` is the predicted probability of class 1:

```text
BCE = -(y * ln(p) + (1 - y) * ln(1 - p))
```

For `y = 1`, a prediction of `p = 0.9` gives a much smaller loss than `p = 0.1`.
In the NumPy example, probabilities are clipped to prevent taking the logarithm of zero.

### 3. Gradient Descent
Gradient Descent updates parameters in the direction that reduces loss locally:

```text
w_new = w_old - learning_rate * dL/dw
```

- A **negative derivative** leads to an increase in the weight.
- A **positive derivative** leads to a decrease in the weight.
- An excessively large learning rate may overshoot the minimum or cause divergence.

### 4. Worked Example
Given:

```text
x = 2, y_true = 10, w = 3, b = 1, learning_rate = 0.1
```

Forward pass:

```text
y_pred = 3 * 2 + 1 = 7
loss = (10 - 7)**2 = 9
```

Gradient with respect to the weight:

```text
dL/dw = 2 * (y_pred - y_true) * x
      = 2 * (7 - 10) * 2
      = -12
```

Update:

```text
w_new = 3 - 0.1 * (-12) = 4.2
y_pred_new = 4.2 * 2 + 1 = 9.4
loss_new = (10 - 9.4)**2 = 0.36
```

The bias is held fixed in this first example so the effect of the weight update is easier to see.

### 5. Backpropagation Preview
Backpropagation uses the **chain rule** to calculate the loss gradient for each parameter, starting at the output and working backward through the layers.

```text
Forward propagation -> Calculate loss -> Backpropagation (gradients)
-> Gradient Descent (parameter updates) -> Repeat
```

Backpropagation **calculates gradients**; Gradient Descent **updates weights and biases**. We will explore full multi-layer backpropagation in **Day 36**, following the original roadmap.

## Important NumPy Operations
- `np.mean(...)`: calculate average error.
- `np.log(...)`: natural logarithm used in BCE.
- `np.clip(...)`: keep probabilities away from exactly 0 and 1.
- `for epoch in range(...)`: repeat a parameter update multiple times.

## Practice / Review
1. Compute MSE for true values `[10, 20, 30]` and predictions `[8, 15, 32]`.
2. Compare BCE for `y = 1` with `p = 0.9` and `p = 0.1`.
3. Change the learning rate in `main.py` and observe whether loss decreases or diverges.
4. Explain why a gradient's sign determines the direction of a weight update.

## Files
- `main.py` — MSE, Binary Cross-Entropy, and a simple Gradient Descent training loop.

## Day-End Summary
- We can quantify prediction error using appropriate loss functions.
- Gradient Descent reduces loss by using derivatives to update parameters.
- Learning rate controls update size.
- Backpropagation makes gradient calculations possible across multiple layers.

**Next: Day 36 — Backpropagation**
