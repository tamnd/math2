---
tag: PPTD47MP45
kind: statement
role: theorem
name: Quadratic transformations of hypergeometric functions
msc: ["33C05"]
uses: [463X5V31D9]
about: [463X5V31D9]
sources:
  - url: https://en.wikipedia.org/wiki/Hypergeometric_function
---

## Statement

Let ${}_2F_1$ be the [[hypergeometric function|463X5V31D9]], with principal powers, and let $a, b \in \C$.

1. If $a + b + \frac12 \notin \set{0, -1, -2, \ldots}$, then for all $z \in \C$ with $\operatorname{Re} z < \frac12$,
$${}_2F_1\left(2a, 2b; a + b + \tfrac12; z\right) = {}_2F_1\left(a, b; a + b + \tfrac12; 4z(1 - z)\right).$$
2. If $2b \notin \set{0, -1, -2, \ldots}$, then for all $z \in \C$ with $\abs{z} < 1$,
$${}_2F_1(a, b; 2b; z) = (1 - z)^{-a/2} \, {}_2F_1\left(\tfrac{a}{2}, b - \tfrac{a}{2}; b + \tfrac12; \frac{z^2}{4z - 4}\right).$$
3. If $1 + a - b \notin \set{0, -1, -2, \ldots}$, then for all $z \in \C$ with $\abs{z} < 1$,
$${}_2F_1(a, b; 1 + a - b; z) = (1 - z)^{-a} \, {}_2F_1\left(\tfrac{a}{2}, \tfrac{1 + a}{2} - b; 1 + a - b; \frac{-4z}{(1 - z)^2}\right).$$

## Remarks

In each formula both sides solve the same second-order hypergeometric equation in $z$.
Indeed, the substitution of a quadratic rational function of $z$ into a hypergeometric equation with special parameters gives back a hypergeometric equation.
Both sides are holomorphic near $z = 0$ with value $1$ there and the exponent $0$ there, which singles out one solution; analytic continuation then extends the identity to the stated domains.
For instance in part 1, $4z(1 - z) = 1 - (1 - 2z)^2$ maps the half-plane $\operatorname{Re} z < \frac12$ into $\C \setminus [1, \infty)$.

Such transformations exist only for special parameters.
Consider the exponent differences $1 - c$, $c - a - b$ and $a - b$ of the equation.
A quadratic transformation exists if two of them are equal up to sign or one of them is $\pm\frac12$.
All three parts fit this pattern: in part 1, the right side has $c - a - b = \frac12$; in part 2, $c = 2b$ gives $c - a - b = -(a - b)$; in part 3, $c = 1 + a - b$ gives $1 - c = -(a - b)$.

Example: with $a = b = \frac12$ in part 3, $1 + a - b = 1$ and the formula expresses ${}_2F_1(\frac12, \frac12; 1; z)$, which is $\frac{2}{\pi}$ times the complete elliptic integral of the first kind with parameter $z$, through $(1 - z)^{-1/2} \, {}_2F_1(\frac14, \frac14; 1; \frac{-4z}{(1-z)^2})$.

## Explanations

### L1 human

Some hypergeometric functions can be rewritten in terms of another hypergeometric function of a squared or quadratic expression in $z$, such as $4z(1 - z)$.
This only works when the three parameters satisfy a special relation.
These formulas connect hypergeometric functions with elliptic integrals and the arithmetic–geometric mean.

### L2 human

Linear transformations such as Pfaff and Euler exist for all parameters and come from the Möbius symmetries of $\set{0, 1, \infty}$.
Quadratic transformations come instead from rational maps of degree $2$ of the sphere that send singular points to singular points, which is possible only for special exponents.
Kummer and Goursat studied them systematically; for more special parameters there are also transformations of higher degree.
