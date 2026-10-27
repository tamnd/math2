---
tag: 0QRBVFJ50X
kind: definition
name: Orthogonal matrix
msc: [15B10]
defines: 0W02QESPJQ
uses: [0W809K6AW0, 06DW9BAWB1]
sources:
  - url: https://en.wikipedia.org/wiki/Orthogonal_matrix
    locator: lead section
inventory: [8KHAEVF7HH]
---

## Definition

Let $n \ge 1$ and let $Q$ be a real $n \times n$ matrix.
The matrix $Q$ is *orthogonal* when
$$Q^T Q = I_n,$$
where $Q^T$ is the [[transpose|09DXWYRD43]] and $I_n$ is the [[identity matrix|06DW9BAWB1]].

## Remarks

Equivalently, $Q$ is invertible with $Q^{-1} = Q^T$, and then also $Q Q^T = I_n$.
Equivalently, the columns of $Q$ form an orthonormal basis of $\R^n$; the same holds for the rows.
The map $x \mapsto Qx$ keeps the dot product, so it is a linear isometry of $\R^n$.
The determinant of an orthogonal matrix is $1$ or $-1$.

## Explanations

### L1 human

Orthogonal matrices describe the rigid motions of space that fix the origin: rotations and reflections.
They keep all lengths and angles.
To invert an orthogonal matrix, we only need to transpose it.
