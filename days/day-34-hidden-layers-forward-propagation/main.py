import numpy as np

# Day 34 - Hidden Layers & Forward Propagation
# Architecture: 2 inputs -> 2 hidden neurons (ReLU) -> 1 output (linear).
# All weights/biases are manually chosen. No training occurs today.


def relu(values):
    """ReLU: keep positive values, replace negative values with zero."""
    return np.maximum(0, values)


# First layer: rows = input features, columns = hidden neurons.
# Two input features and two hidden neurons => W1 has shape (2, 2).
W1 = np.array([
    [0.5, -1.0],
    [1.0,  0.5],
])
b1 = np.array([-1.0, 1.0])

# Second layer: two hidden neuron outputs -> one prediction.
W2 = np.array([
    [0.4],
    [0.6],
])
b2 = np.array([0.2])


def forward(X):
    """Forward propagation for one or more input rows."""
    Z1 = X @ W1 + b1       # NumPy broadcasts b1 across rows.
    A1 = relu(Z1)         # Hidden-layer activation.
    Z2 = A1 @ W2 + b2    # Linear output for a regression example.
    return Z1, A1, Z2


# Part 1: Forward pass for one sample.
single_X = np.array([[2.0, 3.0]])
single_Z1, single_A1, single_output = forward(single_X)

print("=== Single example ===")
print("Input:", single_X)
print("Before ReLU:", single_Z1)
print("After ReLU:", single_A1)
print("Prediction:", single_output)  # [[1.7]]


# Part 2: Batch processing for three samples.
X = np.array([
    [2.0, 3.0],
    [1.0, 4.0],
    [4.0, 0.0],
])
Z1, A1, output = forward(X)

print("\n=== Batch of three examples ===")
print("Input X:\n", X)
print("Z1 (before ReLU):\n", Z1)
print("A1 (after ReLU):\n", A1)
print("Output:\n", output)

# One matrix multiplication processes all three examples.
print("\n=== Matrix shapes ===")
for name, array in [
    ("X", X),
    ("W1", W1),
    ("b1", b1),
    ("Z1", Z1),
    ("A1", A1),
    ("W2", W2),
    ("b2", b2),
    ("Output", output),
]:
    print(f"{name:>6}: {array.shape}")

# Verify the results derived during the lesson.
assert np.allclose(Z1, [[3.0, 0.5], [3.5, 2.0], [1.0, -3.0]])
assert np.allclose(A1, [[3.0, 0.5], [3.5, 2.0], [1.0, 0.0]])
assert np.allclose(output, [[1.7], [2.8], [0.6]])
print("\nAll forward-propagation checks passed.")

# Key ideas:
# 1) Each hidden neuron has one weight per input feature.
# 2) ReLU changes negative hidden pre-activations to zero.
# 3) A regression output can use linear activation (output = Z2).
# 4) With batch inputs, each row gets its own prediction.
# 5) Forward propagation computes predictions; it does not learn weights.
