---
tag: 0Q9EZS90GY
kind: definition
name: Polynomial ring
msc: [13F20]
defines: 0SDC934R52
uses: [0894J980RK]
sources:
  - url: https://en.wikipedia.org/wiki/Polynomial_ring
    locator: Definition (univariate case)
---

## Definition

Let $R$ be a [[ring|0894J980RK]].
A polynomial over $R$ is a sequence $(a_0, a_1, a_2, \dots)$ of elements of $R$ such that $a_n = 0$ for all but finitely many $n$.
The element $a_n$ is the coefficient of degree $n$.
The polynomial ring $R[x]$ is the set of these polynomials, with these operations:
$$(a_n)_n + (b_n)_n = (a_n + b_n)_n, \qquad (a_n)_n \cdot (b_n)_n = (c_n)_n, \quad c_n = \sum_{i + j = n} a_i b_j.$$
With these operations, $R[x]$ is a ring.

## Remarks

Let $x$ be the polynomial $(0, 1, 0, 0, \dots)$, and identify $r \in R$ with $(r, 0, 0, \dots)$.
Then each polynomial with $a_n = 0$ for $n > d$ is $a_0 + a_1 x + \dots + a_d x^d$, in exactly one way.
If $R$ is a [[commutative ring|0GYGHKX834]], then $R[x]$ is commutative.
A polynomial is a formal expression and not a function: over $\mathbb{F}_2$, $x^2 + x$ is a nonzero polynomial, but it is zero at both elements of $\mathbb{F}_2$.

## Explanations

### L1 human

A polynomial is a finite list of coefficients.
You add polynomials coefficient by coefficient.
You multiply them with the rule $x^i \cdot x^j = x^{i + j}$ and the distributive law.
