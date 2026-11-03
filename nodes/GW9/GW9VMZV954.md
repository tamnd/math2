---
tag: GW9VMZV954
kind: definition
name: Backus–Gilbert method
msc: [86A22, 65R32, 45B05]
defines: M73DV1KFP2
uses: [C54MFNX576, 526TCVMSHP, 0VKKP8X6Q6]
sources:
  - url: https://en.wikipedia.org/wiki/Backus%E2%80%93Gilbert_method
---

## Definition

Let $m \colon [a, b] \to \R$ be an unknown model, and let the data be
$$d_i = \int_a^b G_i(x)\, m(x)\, dx, \qquad i = 1, \dots, N.$$
Here the data kernels $G_i$ are known, square-integrable and linearly independent, as in a [[Fredholm integral equation|526TCVMSHP]] of the first kind.
Fix a point $x_0 \in [a, b]$.
For coefficients $c = (c_1, \dots, c_N)$, the estimate $\hat m(x_0) = \sum_i c_i d_i$ equals $\int_a^b A(x)\, m(x)\, dx$ with averaging kernel $A = \sum_i c_i G_i$.
The *Backus–Gilbert method* chooses $c$ to minimise the spread
$$s(c) = \int_a^b (x - x_0)^2 A(x)^2\, dx$$
subject to the normalisation $\int_a^b A(x)\, dx = 1$.

## Remarks

With $Q_{ij} = \int_a^b (x - x_0)^2 G_i G_j\, dx$ and $u_i = \int_a^b G_i\, dx$, the problem is to minimise $c^T Q c$ subject to $u^T c = 1$, and [[Lagrange multipliers|0VKKP8X6Q6]] give
$$c = \frac{Q^{-1} u}{u^T Q^{-1} u}$$
when $Q$ is invertible.
Example: $N = 1$ and $G_1 = 1$ on $[0, 1]$; then $A = c_1$ and the normalisation forces $c_1 = 1$, so $\hat m(x_0) = d_1$ is the mean of $m$ on $[0, 1]$, the best that one datum can give.
Non-example: a kernel with $\int A = 2$ is excluded, since then the estimate of a constant model $m = 1$ would be $2$.
With data errors of covariance $C$, one minimises $s(c) + \lambda\, c^T C c$ instead, and varying $\lambda > 0$ traces the trade-off curve between resolution and variance.
Backus and Gilbert used the spread with an extra factor $12$, which makes the spread of a box kernel centred at $x_0$ equal to its width.

## Explanations

### L1 human

The data are weighted averages of the unknown.
The method combines them into a new average whose weight is concentrated near the chosen point, as tightly as the data allow.
