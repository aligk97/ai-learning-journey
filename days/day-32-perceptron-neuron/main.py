import numpy as np


# Part 1: A single artificial neuron (manual weights and bias)
student_features = np.array([3, 1])  # Study hours, completed homework
weights = np.array([0.5, 0.4])
bias = -0.2

z = np.dot(student_features, weights) + bias


def step_function(value):
    """Return 1 when the weighted sum is >= 0, otherwise 0."""
    return 1 if value >= 0 else 0


print("=== Single neuron ===")
print("Weighted sum:", z)
print("Prediction:", step_function(z))


# Part 2: Train a perceptron to learn the OR logic gate
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1],
])
y = np.array([0, 1, 1, 1])

weights = np.zeros(X.shape[1], dtype=float)
bias = 0.0
learning_rate = 0.1
epochs = 20

print("\n=== Perceptron training ===")
for epoch in range(epochs):
    mistakes = 0

    for x, target in zip(X, y):
        # Forward calculation: weighted sum, then activation
        z = np.dot(x, weights) + bias
        prediction = step_function(z)

        # Perceptron learning rule
        error = target - prediction
        weights += learning_rate * error * x
        bias += learning_rate * error

        if error != 0:
            mistakes += 1

    print(f"Epoch {epoch + 1}: {mistakes} mistake(s)")

    if mistakes == 0:
        break  # Every training example was classified correctly


# Evaluate the trained perceptron on all four OR inputs
print("\n=== Final predictions ===")
print("Weights:", weights)
print("Bias:", round(bias, 2))

predictions = []
for x, target in zip(X, y):
    prediction = step_function(np.dot(x, weights) + bias)
    predictions.append(prediction)
    print(f"{x} -> predicted: {prediction}, expected: {target}")

assert np.array_equal(predictions, y), "The perceptron did not learn OR."
