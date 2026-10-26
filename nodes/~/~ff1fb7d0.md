---
tag: ~ff1fb7d0
kind: definition
name: Higher partial derivatives
msc: [26B05]
defines: ~d9348c6b
uses: [~9beb78a9]
sources:
  - url: https://en.wikipedia.org/wiki/Partial_derivative
    locator: Higher order partial derivatives
---

## Definition

Let $U \subseteq \mathbb{R}^n$ be open, let $f \colon U \to \mathbb{R}$, and let $i, j \in \{1, \dots, n\}$.
Suppose that the [[partial derivative|~9beb78a9]] $\partial f / \partial x_i$ exists at each point of $U$.
The second partial derivative of $f$ with respect to $x_i$ and then $x_j$ at $a \in U$ is
$$\frac{\partial^2 f}{\partial x_j \, \partial x_i}(a) = \frac{\partial}{\partial x_j}\left(\frac{\partial f}{\partial x_i}\right)(a),$$
when this partial derivative exists. It is also written $f_{x_i x_j}(a)$ or $\partial_j \partial_i f(a)$.
For $i = j$, one writes $\partial^2 f / \partial x_i^2$.
By induction, a partial derivative of order $k \ge 2$ is a partial derivative of a partial derivative of order $k - 1$: $\dfrac{\partial^k f}{\partial x_{i_k} \cdots \partial x_{i_1}} = \dfrac{\partial}{\partial x_{i_k}} \left( \dfrac{\partial^{k-1} f}{\partial x_{i_{k-1}} \cdots \partial x_{i_1}} \right)$.

## Remarks

In $\partial^2 f / \partial x_j \, \partial x_i$ the variable nearest to $f$ is differentiated first. In $f_{x_i x_j}$ the variable written first is differentiated first.
For $f(x, y) = x^3 y^2$, one gets $f_{xx} = 6 x y^2$, $f_{xy} = f_{yx} = 6 x^2 y$ and $f_{yy} = 2 x^3$.
If the second partial derivatives are continuous, then the order of differentiation does not matter, by [[Schwarz's theorem|~08d2c32d]]. Without continuity, the mixed partial derivatives [[can differ|~f53918a3]].
The second partial derivatives at a point form the [[Hessian matrix|~4b597766]].

## Explanations

### L1 human

A second partial derivative measures how a slope changes. For example, $f_{xy}$ measures how the slope in the $x$-direction changes as you move in the $y$-direction.
You compute it by differentiating twice, one variable at a time.
