---
tag: T3WM6BXX8W
kind: example
name: The five types of quadratic forms in the plane
msc: [15A63]
topics: [6TSCEW8QMK]
audience: ug1
instance_of: [01RBSSGMY5]
uses: [01RBSSGMY5, 0RP20HFYM3]
sources:
  - url: https://en.wikipedia.org/wiki/Definite_quadratic_form
    locator: lead section
---

## Example

We give one form on $\R^2$ of each type, with a vector that shows the type.

1. $Q_1 = x^2 + y^2$ is [[positive definite|0RP20HFYM3]]: it is a sum of squares, and it is $0$ only at $(0, 0)$.
2. $Q_2 = x^2$ is positive semidefinite: $Q_2 \ge 0$ everywhere, but $Q_2(0, 1) = 0$, so it is not positive definite.
3. $Q_3 = -x^2 - y^2$ is negative definite: $Q_3 = -Q_1$.
4. $Q_4 = -y^2$ is negative semidefinite: $Q_4 \le 0$ everywhere, and $Q_4(1, 0) = 0$.
5. $Q_5 = x^2 - y^2$ is indefinite: $Q_5(1, 0) = 1 > 0$ and $Q_5(0, 1) = -1 < 0$.
6. The zero form $Q_6 = 0$ is both positive semidefinite and negative semidefinite, and not definite.

The matrices are $\operatorname{diag}(1, 1)$, $\operatorname{diag}(1, 0)$, $\operatorname{diag}(-1, -1)$, $\operatorname{diag}(0, -1)$, $\operatorname{diag}(1, -1)$ and $0$.
Their eigenvalues are the diagonal entries, and their signs agree with [[the table of types|01RBSSGMY5]].

## Remarks

The graphs are a bowl, a trough along the $y$-axis, an upside-down bowl, an upside-down trough along the $x$-axis, and a saddle.
The level set $Q = 1$ is a circle for $Q_1$, the two lines $x = \pm 1$ for $Q_2$, and a hyperbola for $Q_5$.
It is empty for $Q_3$, $Q_4$ and $Q_6$.
Every real quadratic form in two variables is equivalent to exactly one of these six, by [[Sylvester's law of inertia|0WFED3K3DQ]].

## Explanations

### L1 human

These six forms are the models of all real quadratic forms in two variables.
Each one has a different shape of graph.
To find the type of another form, bring it to one of these by a change of variables.

### L2 human

The typical use is as a list of models: complete squares, then compare with the list.
A trap: "semidefinite" includes "definite" in this page, so $Q_1$ is also positive semidefinite.
