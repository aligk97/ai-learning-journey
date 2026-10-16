# Day 36 — Backpropagation with NumPy

## Goal

Understand how a neural network calculates gradients through multiple layers using the chain rule, including ReLU derivatives and batch processing.

## Network Architecture

**2 input features → 2 hidden neurons (ReLU) → 1 linear output (regression)**

We train on two examples:

```python
X = np.array([[ 1.0, 2.0],
              [-1.0, 2.0]])
y = np.array([[5.0],
              [4.0]])
```

Initial parameters:

```python
W1 = np.array([[1.0, 0.0],
               [0.0, 1.0]])
b1 = np.zeros((1, 2))
W2 = np.array([[1.0],
               [1.0]])
b2 = np.zeros((1, 1))
```

## Forward Propagation

```python
Z1 = X @ W1 + b1
A1 = np.maximum(0, Z1)
y_pred = A1 @ W2 + b2
loss = np.mean((y_pred - y) ** 2)
```

Results:

```text
Z1 = [[ 1, 2],
      [-1, 2]]

A1 = [[1, 2],
      [0, 2]]

y_pred = [[3],
          [2]]

MSE = 4.0
```

## Backpropagation: Chain Rule

Backpropagation calculates derivatives; **Gradient Descent updates parameters**.

For mean squared error, with two samples and one output per sample:

```python
dY = 2 * (y_pred - y) / y.size
```

### Output Layer

```python
dW2 = A1.T @ dY
db2 = np.sum(dY, axis=0, keepdims=True)
```

```text
dY  = [[-2], [-2]]
dW2 = [[-2], [-8]]
db2 = [[-4]]
```

### Hidden Layer

```python
dA1 = dY @ W2.T
dZ1 = dA1 * (Z1 > 0)  # ReLU derivative
dW1 = X.T @ dZ1
db1 = np.sum(dZ1, axis=0, keepdims=True)
```

```text
dA1 = [[-2, -2],
       [-2, -2]]

dZ1 = [[-2, -2],
       [ 0, -2]]

dW1 = [[-2,  0],
       [-4, -8]]

db1 = [[-2, -4]]
```

The transpose (`.T`) ensures matrices align. The gradient shapes match the corresponding parameter shapes.

## ReLU Derivative and Gradient Blocking

For `z > 0`, the ReLU derivative is 1; for `z < 0`, it is 0. We conventionally use 0 at `z = 0`.

In our second training example, hidden neuron 1 receives `z = -1`. Its activation and derivative become zero, so **that particular example** contributes no gradient to the incoming weights and bias of that neuron. Other examples can still update those parameters.

If a ReLU neuron remains inactive for every training example, it may stop learning (the **dying ReLU** problem).

## Batch Gradients

All training samples share the same weight matrices.

- `dY` includes the mean-loss scaling by the number of output elements (`y.size`).
- Matrix multiplications accumulate gradient contributions from the whole batch.
- Bias gradients use `np.sum(..., axis=0, keepdims=True)` to combine samples.
- Update weights only **after computing every gradient** with the old parameters.

## Gradient Descent and Results

```python
W1 -= learning_rate * dW1
b1 -= learning_rate * db1
W2 -= learning_rate * dW2
b2 -= learning_rate * db2
```

With `learning_rate = 0.01` and one batch update:

| Metric | Before | After |
|---|---:|---:|
| First prediction (target 5) | 3.0000 | 3.5584 |
| Second prediction (target 4) | 2.0000 | 2.4160 |
| Mean squared error | 4.0000 | 2.29363328 |

These values are verified with assertions in `main.py`.

## Shapes

| Variable | Shape |
|---|---|
| `X` | `(2, 2)` |
| `W1`, `dW1` | `(2, 2)` |
| `b1`, `db1` | `(1, 2)` |
| `Z1`, `A1`, `dZ1` | `(2, 2)` |
| `W2`, `dW2` | `(2, 1)` |
| `b2`, `db2` | `(1, 1)` |
| `y`, `y_pred`, `dY` | `(2, 1)` |

## Review Questions

1. Why does a negative ReLU input cause zero gradient for that example?
2. Why does `dW1 = X.T @ dZ1` produce a `(2, 2)` matrix?
3. Why are the bias gradients summed over `axis=0`?
4. Why must all gradients be computed before updating the weights?

## Run

From the repository root:

```bash
python days/day-36-backpropagation/main.py
```

The script uses NumPy, prints every main intermediate value, and asserts the expected gradients and improved loss.

## Day-End Summary

**Forward → Loss → Backward (chain rule + activation derivatives) → Update → Repeat.**

- Backpropagation makes it possible to learn the weights and biases of **every layer**.
- ReLU can block gradient flow for inactive hidden units.
- Batch training combines gradients from multiple examples efficiently.
- Day 37 moves to **PyTorch tensors and basics**, where autograd can calculate gradients automatically.

**Day 31 (independent ML final project) remains in progress in parallel.**
