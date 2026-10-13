# Day 32 - Perceptron & Artificial Neuron

## Goal

Understand how a single artificial neuron makes a prediction and how a perceptron learns weights and bias from examples.

## Topics Covered

- Artificial neuron: inputs, weights, bias, and output
- Weighted sum and NumPy's `np.dot()`
- Step activation function
- Perceptron learning rule
- Learning rate and epoch
- Training a perceptron on the OR logic gate

## Key Concepts

An artificial neuron combines input features using weights, adds a bias, and applies an activation function:

```text
z = x1*w1 + x2*w2 + ... + b
prediction = step(z)
step(z) = 1 if z >= 0 else 0
```

- **Input (x):** Feature values fed into the neuron.
- **Weight (w):** How strongly each input affects the result.
- **Bias (b):** An offset that shifts the decision boundary.
- **Activation:** Converts the weighted sum into the neuron's output.

Example from the lesson:

```python
X = np.array([3, 1])
weights = np.array([0.5, 0.4])
bias = -0.2
z = np.dot(X, weights) + bias  # 1.7
```

The example predicts class `1` because `z >= 0`. These weights were chosen manually, so this first example does **not** involve learning.

## How a Perceptron Learns

For each training example, a perceptron:

1. Calculates the weighted sum and makes a prediction.
2. Computes `error = target - prediction`.
3. Adjusts its weights and bias:

```text
new_weight = old_weight + learning_rate * error * input
new_bias   = old_bias   + learning_rate * error
```

An **epoch** is one full pass through the training data. When a prediction is correct, the error is zero and the parameters do not change for that example.

## OR Gate Example

| x1 | x2 | Target |
|---:|---:|-------:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

`main.py` starts with zero weights and zero bias, then trains using `learning_rate = 0.1`. It reports mistakes per epoch and checks that the final predictions match the OR table.

## Final Check

- Compute a weighted sum using `np.dot()`.
- Explain the purpose of weights, bias, and a step activation function.
- Understand why `error = target - prediction` changes the parameters.
- Distinguish a manually configured neuron from a trained perceptron.
- Explain why a single perceptron cannot learn a non-linearly separable pattern such as XOR.

## Run

From the repository root:

```bash
uv run python days/day-32-perceptron-neuron/main.py
```

## Takeaway

Learning means updating weights and bias to reduce mistakes. This simple perceptron learning rule introduces the key idea behind neural-network training; modern multi-layer networks typically use differentiable activations, gradient-based optimization, and backpropagation.

## Learning Tracks

**Day 31:** Independent ML final project (ongoing in parallel).

**Next lesson:** Day 33 - Weight, Bias & Activation Functions.

## Reference

[Scikit-learn: Perceptron](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Perceptron.html)
