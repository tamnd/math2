---
tag: ~e1faae02
kind: statement
role: theorem
name: Test for exactness
msc: [34A05]
uses: [~c1c26a80]
sources:
  - url: https://en.wikipedia.org/wiki/Exact_differential_equation
    locator: Identifying first-order exact differential equations
---

## Statement

Let $R = (\alpha, \beta) \times (\gamma, \delta)$ be an open rectangle in $\mathbb{R}^2$.
Let $M, N : R \to \mathbb{R}$ be continuous functions such that the partial derivatives $\partial M / \partial y$ and $\partial N / \partial x$ exist and are continuous on $R$.
Then the equation $M\, dx + N\, dy = 0$ is [[exact|~c1c26a80]] on $R$ if and only if
$$\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x} \quad \text{on } R.$$

## Remarks

The condition is necessary on each open set: if $\psi_x = M$ and $\psi_y = N$, the mixed partial derivatives of $\psi$ are equal, so $M_y = N_x$.
For the converse, fix $(x_0, y_0) \in R$ and set $\psi(x, y) = \int_{x_0}^{x} M(s, y_0)\, ds + \int_{y_0}^{y} N(x, t)\, dt$.
The converse holds on each simply connected open set. It can fail on other sets: $(-y\, dx + x\, dy)/(x^2 + y^2) = 0$ satisfies the condition on $\mathbb{R}^2 \setminus \{0\}$, but it is not exact there.

## Explanations

### L1 human

If $\psi$ exists, then $M$ and $N$ are its two partial derivatives.
Their cross derivatives must agree, because the order of differentiation does not matter for nice functions.
On a rectangle, this easy test is also enough.
