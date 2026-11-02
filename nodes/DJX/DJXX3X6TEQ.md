---
tag: DJXX3X6TEQ
kind: definition
name: Affine arithmetic
msc: [65G30, 65G40]
defines: YPE8E9CVXP
uses: [QPKKTE1ZY0, 0Q1D85B8G6]
sources:
  - url: https://en.wikipedia.org/wiki/Affine_arithmetic
---

## Definition

An *affine form* is an expression
$$\hat x = x_0 + \sum_{i=1}^{k} x_i \varepsilon_i,$$
with real coefficients $x_0, \ldots, x_k$ and *noise symbols* $\varepsilon_1, \ldots, \varepsilon_k$.
The noise symbols stand for unknown reals in $[-1, 1]$, shared by all affine forms of a computation.
Its *range* is the [[interval|0Q1D85B8G6]] $[x_0 - r, x_0 + r]$ with radius $r = \sum_{i=1}^{k} \abs{x_i}$.
*Affine arithmetic* computes with affine forms by the following rules.

1. Affine operations are exact: $\hat x \pm \hat y = (x_0 \pm y_0) + \sum (x_i \pm y_i) \varepsilon_i$ and $c \hat x + d = (c x_0 + d) + \sum c x_i \varepsilon_i$ for reals $c, d$.
2. A nonlinear operation $g$ is replaced by an affine form $\hat z = z_0 + \sum z_i \varepsilon_i + z_{k+1} \varepsilon_{k+1}$ with a new noise symbol $\varepsilon_{k+1}$. It is chosen so that $g(x, y, \ldots) \in \hat z$ for all values of $\varepsilon_1, \ldots, \varepsilon_k$ in $[-1, 1]$.
3. For multiplication one may take $\hat x \hat y = x_0 y_0 + \sum_{i=1}^{k} (x_0 y_i + y_0 x_i) \varepsilon_i + r_x r_y \, \varepsilon_{k+1}$, where $r_x, r_y$ are the radii of $\hat x, \hat y$.

## Remarks

Example: $\hat x = 2 + \varepsilon_1$ represents $x \in [1, 3]$, and $\hat x - \hat x = 0$ by rule 1, while [[interval arithmetic|QPKKTE1ZY0]] gives $[1, 3] - [1, 3] = [-2, 2]$.
Example: $\hat x \cdot \hat x = 4 + 4\varepsilon_1 + \varepsilon_2$ by rule 3, with range $[-1, 9]$, which contains the true range $[1, 9]$ of $x^2$.
Non-example: replacing $x^2$ by its tangent $4 + 4\varepsilon_1$ alone, without a new noise term, violates rule 2: at $\varepsilon_1 = 1$ it gives $8$, but $x^2 = 9$.
In a computer the coefficients are rounded outward, and the rounding errors are also absorbed into a new noise term.
