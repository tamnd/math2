---
tag: KN2QZ0SMWA
kind: definition
name: Geometric programming
msc: [90C30, 90C25]
defines: DVZGC9Q4Z9
uses: [1W1BXJN9ER, 0J0FCWV32D]
sources:
  - url: https://en.wikipedia.org/wiki/Geometric_programming
---

## Definition

Let $\R^n_{>0}$ be the set of vectors $x \in \R^n$ with all $x_i > 0$.
A *monomial* is a function $m \colon \R^n_{>0} \to \R$ of the form $m(x) = c \, x_1^{a_1} \cdots x_n^{a_n}$ with $c > 0$ and $a_1, \dots, a_n \in \R$.
A *posynomial* is a finite sum of monomials.
A *geometric program* is a problem of the form: minimise $f_0(x)$ over $x \in \R^n_{>0}$ subject to
$$f_i(x) \le 1 \quad (i = 1, \dots, m) \quad \text{and} \quad g_j(x) = 1 \quad (j = 1, \dots, p),$$
where $f_0, \dots, f_m$ are posynomials and $g_1, \dots, g_p$ are monomials.

## Remarks

Put $x_i = e^{y_i}$ with the [[exponential function|0J0FCWV32D]] and take logarithms of the objective and of each constraint.
A monomial becomes $\ln c + a^T y$, an affine function, and a posynomial becomes $\ln \sum_k e^{a_k^T y + b_k}$, a convex function.
So a geometric program is equivalent to a [[convex optimization|1W1BXJN9ER]] problem in $y$.

Example: minimise $x^{-1} y^{-1}$ subject to $x + y \le 1$ is a geometric program: the objective is a monomial with $c = 1$, $a = (-1, -1)$, and $x + y$ is a posynomial.
Its optimum is $4$, at $x = y = 1/2$.

Non-example: minimise $x - y$ subject to $x, y > 0$ and $x y \le 1$ is not a geometric program, because $x - y$ has a negative coefficient and so is not a posynomial.
