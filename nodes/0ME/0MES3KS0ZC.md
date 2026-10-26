---
tag: 0MES3KS0ZC
kind: statement
role: theorem
name: Division algorithm for polynomials
aliases: [euclidean-division-of-polynomials]
msc: [13F20]
uses: [0Q9EZS90GY, 0DPF6WRZW6, 0BDX4MBKT4]
sources:
  - url: https://en.wikipedia.org/wiki/Polynomial_long_division
    locator: Euclidean division
---

## Statement

Let $R$ be a [[commutative ring|0GYGHKX834]], let $f \in R[x]$ and let $g \in R[x]$ be a [[monic polynomial|0BDX4MBKT4]].
Then there are unique polynomials $q, r \in R[x]$ such that $f = q g + r$ and $\deg r < \deg g$.

## Remarks

The polynomials $q$ and $r$ are the quotient and the remainder. Long division of polynomials computes them.
Over a [[field|0QA8CHH8MG]] $K$, every nonzero $g$ is a unit times a monic polynomial. So the statement holds for every nonzero $g \in K[x]$.
For example, $x^3 + 1 = (x^2 - x + 1)(x + 1) + 0$ and $x^2 + 1 = (x - 1)(x + 1) + 2$.
The statement fails for a divisor that is not monic: in $\mathbb{Z}[x]$, no $q$ and $r$ with $\deg r < 1$ give $x = q \cdot 2x + r$.

## Explanations

### L1 human

This is the polynomial version of division with remainder for integers.
You can divide by a monic polynomial and get a remainder of smaller degree.
The degree plays the role that the size of a number plays for integers.
