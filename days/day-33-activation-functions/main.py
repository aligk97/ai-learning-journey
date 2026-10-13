import numpy as np


# Day 33 - Weight, Bias & Activation Functions
# A neuron first computes z = X @ weights + bias.
# An activation function transforms this value into an output.


def step(z):
    return np.where(np.asarray(z) >= 0, 1, 0)


def sigmoid(z):
    return 1 / (1 + np.exp(-np.asarray(z)))


def relu(z):
    return np.maximum(0, z)


def tanh(z):
    return np.tanh(z)


# Part 1: Compare functions on the same inputs.
values = np.array([-2.0, 0.0, 2.0])

print("=== Activation function comparison ===")
print("Inputs: ", values)
print("Step:   ", step(values))
print("Sigmoid:", np.round(sigmoid(values), 3))
print("ReLU:   ", relu(values))
print("Tanh:   ", np.round(tanh(values), 3))


# Part 2: One neuron, different activation functions.
# The input features and parameter values are chosen for illustration.
X = np.array([2.0, 3.0])
weights = np.array([0.5, 0.8])
bias = -1.0

z = np.dot(X, weights) + bias  # 2 * 0.5 + 3 * 0.8 - 1 = 2.4

print("\n=== Single neuron ===")
print("Weighted sum (z):", round(float(z), 3))
print("Linear output:   ", round(float(z), 3))  # Regression-style output
print("Sigmoid output:  ", round(float(sigmoid(z)), 3))
print("ReLU output:     ", round(float(relu(z)), 3))
print("Tanh output:     ", round(float(tanh(z)), 3))


# Part 3: See how changing the bias shifts the weighted sum.
print("\n=== Bias comparison ===")
for new_bias in [-3.0, -1.0, 0.0]:
    weighted_sum = np.dot(X, weights) + new_bias
    print(
        f"bias={new_bias:4.1f} | z={weighted_sum:4.1f} "
        f"| sigmoid={sigmoid(weighted_sum):.3f}"
    )


# Main lesson:
# - Weight controls how much each feature contributes.
# - Bias shifts the weighted sum.
# - Activation functions transform the result.
# - ReLU is a common hidden-layer choice.
# - Linear outputs suit regression; sigmoid is common for binary classification.
# - Multi-class single-label classification commonly uses softmax at the output.
# No training takes place in this lesson: weights and bias stay fixed.
