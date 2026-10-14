# Day 34 - Hidden Layers & Forward Propagation

## Goal

Understand how inputs move through connected neurons in a multilayer neural network, and implement the full forward pass with NumPy for one example and a batch.

## Topics Covered

- Input layer, hidden layer, and output layer
- Connections, weights, bias, and activation
- Forward propagation: \`Z = X @ W + b\`
- ReLU in a hidden layer vs. linear output for regression
- Weight-matrix dimensions and why each neuron needs its own weights
- NumPy matrix multiplication with \`@\`
- Batch processing and bias broadcasting

## Network Architecture

**2 input features → 2 hidden neurons (ReLU) → 1 output neuron (linear)**

A neuron computes a weighted sum and applies an activation function. The next layer uses the previous layer's activations as its inputs.

For this example:

\`\`\`python
W1 = np.array([[0.5, -1.0],
               [1.0,  0.5]])
b1 = np.array([-1.0, 1.0])

W2 = np.array([[0.4],
               [0.6]])
b2 = np.array([0.2])
\`\`\`

### Why is W1 a 2×2 matrix?

The input contains **2 features**, but the hidden layer contains **2 neurons**. Each hidden neuron needs a weight for each input feature:

- First column of \`W1\` = weights of hidden neuron 1: \`[0.5, 1.0]\`.
- Second column of \`W1\` = weights of hidden neuron 2: \`[-1.0, 0.5]\`.
- Rows correspond to **input features**; columns correspond to **hidden neurons**.

Thus, \`W1.shape == (2, 2)\` (4 weights in total). There are also 2 separate hidden-layer bias values in \`b1\`. With 2 features and only **1 hidden neuron**, the weight matrix would have shape \`(2, 1)\`.

## Forward Propagation

\`\`\`python
Z1 = X @ W1 + b1
A1 = np.maximum(0, Z1)  # ReLU
Z2 = A1 @ W2 + b2
output = Z2             # Linear regression output
\`\`\`

- \`Z1\`: hidden layer values **before** activation.
- \`A1\`: hidden layer values **after** ReLU.
- \`Z2\`: output layer's weighted sum.
- \`output = Z2\`: linear activation leaves the output unchanged, which is a common choice for regression.

The ReLU rule is \`ReLU(z) = max(0, z)\`. For example, \`-3\` becomes \`0\`, while \`0.5\` stays \`0.5\`.

If the output must allow negative predictions (e.g., temperature), ReLU would be an unsuitable output activation. The activation used at the output depends on the task.

## Single-Example Result

For input \`X = [[2, 3]]\`:

\`\`\`text
Z1     = [[3.0, 0.5]]
A1     = [[3.0, 0.5]]
output = [[1.7]]
\`\`\`

## Batch Processing: 3 Examples at Once

\`\`\`python
X = np.array([
    [2, 3],
    [1, 4],
    [4, 0],
])
\`\`\`

Each row is one example, and each column is an input feature. The **same weights** are applied to every row, and NumPy broadcasts the bias values.

\`\`\`text
Z1 = [[3.0,  0.5],
      [3.5,  2.0],
      [1.0, -3.0]]

A1 = [[3.0, 0.5],
      [3.5, 2.0],
      [1.0, 0.0]]

Output = [[1.7],
          [2.8],
          [0.6]]
\`\`\`

Notice how ReLU replaces the final \`-3.0\` with \`0.0\`.

### Matrix Shapes

| Tensor | Shape | Meaning |
| --- | --- | --- |
| \`X\` | \`(3, 2)\` | 3 examples, 2 input features |
| \`W1\` | \`(2, 2)\` | 2 features → 2 hidden neurons |
| \`b1\` | \`(2,)\` | One bias per hidden neuron |
| \`A1\` | \`(3, 2)\` | 2 activations for each example |
| \`W2\` | \`(2, 1)\` | 2 hidden neurons → 1 output |
| \`b2\` | \`(1,)\` | One output bias |
| \`Output\` | \`(3, 1)\` | One prediction for each example |

The essential matrix-multiplication rule is that the left operand's number of columns must match the right operand's number of rows.

## Final Check

1. Explain why two features and two hidden neurons require **four weights**, not two.
2. Explain the difference between \`Z1\` and \`A1\`.
3. Explain why \`np.maximum(0, Z1)\` is used in the hidden layer but not the linear output layer.
4. Explain how a single \`X @ W1\` computes results for all three examples at once.

## Run

From the repository root:

\`\`\`bash
uv run python days/day-34-hidden-layers-forward-propagation/main.py
\`\`\`

## Day-End Summary

- Forward propagation **calculates predictions using existing weights and biases**.
- ReLU provides a nonlinear hidden-layer transformation.
- Each layer has its own weight matrix; matrix dimensions reflect connections between layers.
- A batch passes multiple input rows through the same network efficiently.
- **No learning happens in this lesson**: weights are fixed and no loss or gradient is calculated.

## Learning Tracks

- **Day 31:** Independent ML final project (in progress in parallel).
- **Day 34:** Completed.
- **Next lesson:** Day 35 - Loss Function & Gradient Descent.

## References

- [NumPy: matmul](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html)
- [NumPy: broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html)
- [PyTorch: ReLU](https://docs.pytorch.org/docs/stable/generated/torch.nn.ReLU.html)
