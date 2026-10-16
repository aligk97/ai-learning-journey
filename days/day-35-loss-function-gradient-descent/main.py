"""Day 35 — Loss Functions & Gradient Descent.

A small NumPy demo of MSE, Binary Cross-Entropy, and learning rate.
Day 36 covers full multi-layer backpropagation.
"""

import numpy as np


def mse(y_true, y_pred):
    """Mean squared error for regression."""
    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float)
    return np.mean((y_true - y_pred) ** 2)


def binary_cross_entropy(y_true, probabilities):
    """Mean binary cross-entropy; clip to avoid log(0)."""
    y_true = np.asarray(y_true, dtype=float)
    p = np.asarray(probabilities, dtype=float)
    p = np.clip(p, 1e-12, 1 - 1e-12)
    return np.mean(-(y_true * np.log(p) + (1 - y_true) * np.log(1 - p)))


# 1. Two kinds of loss
print("MSE example:", mse([10, 20, 30], [8, 15, 32]))
print("BCE, correct confident prediction:", binary_cross_entropy([1], [0.9]))
print("BCE, incorrect confident prediction:", binary_cross_entropy([1], [0.1]))
print()

# 2. Simple regression model: y_pred = w * x + b
x = 2.0
y_true = 10.0
w = 3.0
b = 1.0                 # Fixed during this example
learning_rate = 0.1

for epoch in range(1, 6):
    # Forward pass: make a prediction
    y_pred = w * x + b

    # Compute loss with the CURRENT weight
    loss = (y_true - y_pred) ** 2

    # dL/dw by the chain rule
    dL_dw = 2 * (y_pred - y_true) * x

    # Gradient Descent updates the weight
    w -= learning_rate * dL_dw

    # Show the loss before the update and the new weight
    print(f"Epoch {epoch}: loss_before_update={loss:.6f}, weight_after_update={w:.6f}")

# 3. Final prediction after training
final_pred = w * x + b
final_loss = (y_true - final_pred) ** 2
print(f"\nFinal prediction: {final_pred:.6f}; final loss: {final_loss:.6f}")

# Experiment: change learning_rate to 0.01, 0.3, or 0.5 and compare.
