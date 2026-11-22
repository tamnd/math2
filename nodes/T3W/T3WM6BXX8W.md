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

We give one diagonal form on $\mathbb{R}^2$ of each [[type|01RBSSGMY5]], together with the values that prove its type.

1. $Q_1 = x^2 + y^2$ is [[positive definite|0RP20HFYM3]].
   It is a sum of two squares, so it is at least $0$, and it is $0$ only at $(0, 0)$.
2. $Q_2 = x^2$ is positive semidefinite.
   It is at least $0$ everywhere, but $Q_2(0, 1) = 0$ at a nonzero vector, so it is not definite.
3. $Q_3 = -x^2 - y^2$ is negative definite, since $Q_3 = -Q_1$.
4. $Q_4 = -y^2$ is negative semidefinite.
   It is at most $0$ everywhere, and $Q_4(1, 0) = 0$.
5. $Q_5 = x^2 - y^2$ is indefinite, since $Q_5(1, 0) = 1 > 0$ and $Q_5(0, 1) = -1 < 0$.
6. The zero form $Q_6 = 0$ is both positive semidefinite and negative semidefinite, and it is not definite.

The matrices are $\operatorname{diag}(1, 1)$, $\operatorname{diag}(1, 0)$, $\operatorname{diag}(-1, -1)$, $\operatorname{diag}(0, -1)$, $\operatorname{diag}(1, -1)$ and the zero matrix.
Their eigenvalues are their diagonal entries, and the signs match [[the table of types|01RBSSGMY5]].

## Remarks

The graphs are a bowl, a trough along the $y$-axis, an upside-down bowl, an upside-down trough along the $x$-axis, a saddle, and a flat plane.
The level set $Q = 1$ shows the same differences.
It is a circle for $Q_1$, the two lines $x = \pm 1$ for $Q_2$, and a hyperbola for $Q_5$, and it is empty for $Q_3$, $Q_4$ and $Q_6$.

These six forms are models for all real binary forms.
Every real quadratic form in two variables can be brought to exactly one of them by an invertible change of variables.
The diagonalization by squares gives at least one, and [[Sylvester's law of inertia|0WFED3K3DQ]] shows that two of the six are never equivalent.
For example, $x^2 + 2xy + y^2 = (x + y)^2$ becomes $Q_2$ with the new variable $x' = x + y$.

## Explanations

### L1 human

These six forms are the patterns that every form in two variables follows.
Each pattern has its own graph: a bowl, a trough, an upside-down bowl or trough, a saddle, or a flat sheet.
To find the type of another form, change variables until it looks like one of these.

### L2 human

The typical use is a list to compare against: complete the squares in a given form, then read off which model it is.
For example, $x^2 - 4xy + 3y^2 = (x - 2y)^2 - y^2$ becomes $Q_5$ with $x' = x - 2y$ and $y' = y$, so it is indefinite.
Watch out: with the inclusive convention, $Q_1$ is also positive semidefinite, so "semidefinite" alone does not say that a form fails to be definite.
