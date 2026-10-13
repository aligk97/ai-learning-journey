# Day 33 - Weight, Bias & Activation Functions

## Goal

Understand how a neuron's weights, bias, and activation function affect its output, and choose an appropriate output activation for different machine-learning problems.

## Topics Covered

- Weighted sum: `z = w1*x1 + w2*x2 + ... + b`
- Weight vs. bias
- Why neural networks need nonlinear activation functions
- Step, Sigmoid, ReLU, and Tanh
- Linear and Softmax outputs
- Activation choices for regression and classification
- Why derivatives matter for gradient-based training

## Key Concepts

### Weights and Bias

- **Weight (w):** Multiplies an input and controls its contribution to the weighted sum.
- **Bias (b):** Adds an offset and shifts the neuron's response.
- **Activation (f):** Transforms `z` into the neuron's output.

```python
X = np.array([2.0, 3.0])
weights = np.array([0.5, 0.8])
bias = -1.0
z = np.dot(X, weights) + bias  # 2.4
```

### Why Nonlinearity Matters

Composing only linear (or affine) layers, without nonlinear activations between them, is equivalent to a single affine transformation. Nonlinear activations allow multi-layer networks to represent more complex relationships.

### Activation Functions

| Function | Output range | Typical use |
| --- | --- | --- |
| Step | 0 or 1 | Classical perceptron |
| Sigmoid | Between 0 and 1 | Binary-classification output |
| ReLU | 0 and above | Hidden layers |
| Tanh | Between -1 and 1 | Some hidden layers / architectures |
| Linear (Identity) | Any real number | Regression output |
| Softmax | Probabilities summing to 1 | Single-label multiclass-classification output |

- `step(z) = 1 if z >= 0 else 0`
- `sigmoid(z) = 1 / (1 + exp(-z))`
- `relu(z) = max(0, z)`
- `tanh(z) = tanh(z)`
- `linear(z) = z`

Examples for `z = [-2, 0, 2]`:

| z | Sigmoid | ReLU | Tanh |
| ---: | ---: | ---: | ---: |
| -2 | 0.119 | 0 | -0.964 |
| 0 | 0.500 | 0 | 0 |
| 2 | 0.881 | 2 | 0.964 |

## How to Choose an Output Activation

- **Car price prediction (regression):** Linear output, since price is not limited to the range 0–1.
- **Pass/fail prediction (binary classification):** Sigmoid output, commonly interpreted as a positive-class probability when the model is appropriately trained.
- **One class among several (multiclass classification):** Softmax output.
- **Hidden layers:** ReLU is a commonly used starting point, though different architectures use other activations.

## Derivatives - A First Intuition

A derivative describes how an output changes when an input is changed by a very small amount.

- Positive derivative: increasing the input locally increases the function.
- Negative derivative: increasing the input locally decreases the function.
- Zero derivative: the function is locally flat (this alone does not guarantee a minimum).

The step function's derivative is **0 wherever `z != 0`**, and is **undefined at `z = 0`**. It therefore does not provide useful derivatives for ordinary backpropagation.

A *classical perceptron* can still learn with its own mistake-driven update rule; that training rule does not differentiate the step function.

Sigmoid is smooth and differentiable, although its gradient can become very small when the input is far from zero. ReLU has a useful positive-side gradient and a zero negative-side gradient; at zero it is not differentiable, but implementations use a practical convention.

### Supplementary Gradient Descent Example

For a simple model `prediction = w * x` with `x = 2`, `y = 10`, and squared-error loss:

```text
L(w) = (10 - 2w)^2
     = 100 - 40w + 4w^2

dL/dw = -40 + 8w
At w = 1: dL/dw = -32
```

The derivative `-32` says that at `w = 1`, a tiny increase in `w` decreases loss at an approximate rate of 32 units of loss per 1 unit of weight.

For example, increasing `w` by `0.01` predicts an approximate loss change of `-32 * 0.01 = -0.32`.

With learning rate `0.1`, one Gradient Descent step gives:

```text
w_new = w_old - learning_rate * derivative
      = 1 - 0.1 * (-32)
      = 4.2
```

This is an **introductory reinforcement example** from our Day 33 discussion, not a replacement for the planned Day 35 lesson about training neural networks.

## Practice / Final Check

The `main.py` example:

1. Compares Step, Sigmoid, ReLU, and Tanh on the same values.
2. Calculates a neuron's weighted sum with `np.dot()`.
3. Shows that different activation functions produce different outputs from the same `z`.
4. Changes the bias to see how it shifts the result.

A useful check: explain why car-price regression does not normally use Sigmoid as its output activation, and why the classical perceptron learning rule can work even though the step function's derivative is zero almost everywhere.

## Run

From the repository root:

```bash
uv run python days/day-33-activation-functions/main.py
```

## Day-End Summary

- Weights and bias determine the weighted sum.
- Activation functions control how that sum is transformed.
- Nonlinearity is crucial for the expressive power of deep networks.
- Hidden-layer and output-layer activations serve different purposes.
- Derivatives tell gradient-based optimizers how to adjust parameters.

## Learning Tracks

- **Day 31:** Independent ML final project (still in progress, parallel track).
- **Day 33:** Completed.
- **Next planned lesson:** Day 34 - Hidden Layers & Forward Propagation (not started).

## References

- [PyTorch: Non-linear Activations](https://docs.pytorch.org/docs/stable/nn.html#non-linear-activations-weighted-sum-nonlinearity)
- [Scikit-learn: MLPClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html)
