---
tag: 0NS2QYVC4Y
kind: definition
name: Gradient
msc: [26B12]
defines: 0ABK9V9Y64
uses: [0135XZZQ8M, 09EGC6F8PT, 0XPR1E85W0]
sources:
  - url: https://en.wikipedia.org/wiki/Gradient
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Gradient
    locator: Cartesian coordinates
---

## Definition

Let $U \subseteq \mathbb{R}^n$ be open, let $f \colon U \to \mathbb{R}$, and let $a \in U$ be a point at which $f$ is [[differentiable|0135XZZQ8M]].
The gradient of $f$ at $a$ is the unique vector $\nabla f(a) \in \mathbb{R}^n$ such that
$$Df(a)(v) = \nabla f(a) \cdot v \quad \text{for each } v \in \mathbb{R}^n,$$
where $\cdot$ is the dot product of [[Euclidean space|0XPR1E85W0]].
In coordinates, it is the vector of [[partial derivatives|09EGC6F8PT]]
$$\nabla f(a) = \left(\frac{\partial f}{\partial x_1}(a), \dots, \frac{\partial f}{\partial x_n}(a)\right).$$
Other notations are $\operatorname{grad} f(a)$ and $\nabla f(a)$, where $\nabla$ is the [[del operator|0H6DP8CHND]].

## Remarks

The vector exists and is unique because each linear map $\mathbb{R}^n \to \mathbb{R}$ is $v \mapsto w \cdot v$ for exactly one $w \in \mathbb{R}^n$.
For $f(x, y) = x^2 + 3 x y$, the gradient is $\nabla f(x, y) = (2x + 3y, \, 3x)$.
A gradient is a column vector, and the derivative $Df(a)$ is the row vector of the same entries. Some books do not make this distinction.
The map $a \mapsto \nabla f(a)$ is a [[vector field|0299VCW1TH]] on $U$, the gradient field of $f$.

## Explanations

### L1 human

The gradient collects all slopes of $f$ along the axes into one arrow.
On a map of a hill, the gradient at a point is an arrow that points straight uphill. The arrow is longer where the hill is steeper.
