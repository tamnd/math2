---
tag: ~c1eee70a
kind: definition
name: Hessian matrix
msc: [26B05]
defines: ~4b597766
uses: [~ff1fb7d0]
sources:
  - url: https://en.wikipedia.org/wiki/Hessian_matrix
    locator: Definitions and properties
---

## Definition

Let $U \subseteq \mathbb{R}^n$ be open, let $f \colon U \to \mathbb{R}$, and let $a \in U$ be a point at which all second [[partial derivatives|~ff1fb7d0]] of $f$ exist.
The Hessian matrix of $f$ at $a$ is the $n \times n$ matrix
$$H_f(a) = \left( \frac{\partial^2 f}{\partial x_i \, \partial x_j}(a) \right)_{1 \le i, j \le n},$$
whose entry in row $i$ and column $j$ is $\partial^2 f / \partial x_i \, \partial x_j$ at $a$.
It is also written $\nabla^2 f(a)$ or $D^2 f(a)$.

## Remarks

If the second partial derivatives of $f$ are continuous near $a$, then $H_f(a)$ is a symmetric matrix, by [[Schwarz's theorem|~08d2c32d]].
For $f(x, y) = x^2 + 3 x y - y^2$, the Hessian matrix at each point is $\begin{pmatrix} 2 & 3 \\ 3 & -2 \end{pmatrix}$.
The Hessian matrix is the Jacobian matrix of the gradient map $x \mapsto \nabla f(x)$, when this map is differentiable.
At a critical point, the signs of the eigenvalues of $H_f(a)$ decide the [[second derivative test|~75be542b]].

## Explanations

### L1 human

The gradient tells how a function tilts; the Hessian tells how it bends.
For a bowl like $x^2 + y^2$ the Hessian is $2 I$, and both directions bend upward. For a saddle like $x^2 - y^2$ one direction bends up and the other bends down.
