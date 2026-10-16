"""Day 36 — Backpropagation from scratch with NumPy.

Network: 2 inputs -> 2 ReLU hidden neurons -> 1 linear output.
Demonstrates a ReLU gradient mask and batch mean gradients.
"""

import numpy as np

# Two training examples, each with two input features.
X = np.array([[1.0, 2.0],
              [-1.0, 2.0]])
y = np.array([[5.0],
              [4.0]])

# Weights: rows = inputs from previous layer; columns = neurons.
W1 = np.array([[1.0, 0.0],
               [0.0, 1.0]])
b1 = np.zeros((1, 2))
W2 = np.array([[1.0],
               [1.0]])
b2 = np.zeros((1, 1))
learning_rate = 0.01


def forward(inputs):
    """Forward pass with the CURRENT weight/bias values."""
    z1 = inputs @ W1 + b1
    a1 = np.maximum(0, z1)   # ReLU hidden activation
    predictions = a1 @ W2 + b2  # Linear output (regression)
    return z1, a1, predictions


# 1) Forward propagation for a batch of 2 rows.
Z1, A1, y_pred = forward(X)
loss_before = np.mean((y_pred - y) ** 2)
print("Z1 before ReLU:\n", Z1)
print("A1 after ReLU:\n", A1)
print("ReLU derivative mask:\n", (Z1 > 0).astype(int))
print("Predictions before:", y_pred.ravel())
print("Mean squared error before:", loss_before)

# 2) Backpropagation: use ONE parameter snapshot for all gradients.
# Mean squared error over 2 samples, 1 output per sample.
dY = 2 * (y_pred - y) / y.size  # shape: (2, 1)

# Output layer gradients.
dW2 = A1.T @ dY                 # shape: (2, 1)
db2 = np.sum(dY, axis=0, keepdims=True)  # shape: (1, 1)

# Pass gradient through W2 and ReLU to the hidden layer.
dA1 = dY @ W2.T                 # shape: (2, 2)
dZ1 = dA1 * (Z1 > 0)            # elementwise ReLU derivative

# First layer gradients: sum each sample's contribution.
dW1 = X.T @ dZ1                 # shape: (2, 2)
db1 = np.sum(dZ1, axis=0, keepdims=True)  # shape: (1, 2)

print("\nGradients:")
for name, grad in [("dW2", dW2), ("db2", db2),
                   ("dA1", dA1), ("dZ1", dZ1),
                   ("dW1", dW1), ("db1", db1)]:
    print(f"{name}:\n{grad}")

# Verify the hand-computed batch gradients.
assert np.allclose(dW2, [[-2], [-8]])
assert np.allclose(dW1, [[-2, 0], [-4, -8]])
assert np.allclose(db2, [[-4]])
assert np.allclose(db1, [[-2, -4]])
assert dZ1[1, 0] == 0  # ReLU blocks the second example's first neuron.

# 3) Gradient Descent: update all parameters AFTER computing gradients.
W1 -= learning_rate * dW1
b1 -= learning_rate * db1
W2 -= learning_rate * dW2
b2 -= learning_rate * db2

# 4) Check whether the updated network performs better.
_, _, updated_pred = forward(X)
loss_after = np.mean((updated_pred - y) ** 2)
print("\nPredictions after:", updated_pred.ravel())
print("Mean squared error after:", loss_after)

assert np.allclose(updated_pred.ravel(), [3.5584, 2.4160])
assert np.isclose(loss_after, 2.29363328)
assert loss_after < loss_before
print("\nAll Day 36 checks passed.")
