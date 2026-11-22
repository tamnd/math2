---
tag: 9DWJ0QE48F
kind: example
name: Quadratic polynomials and triples of numbers are isomorphic
msc: ["15A04"]
topics: [9080WQTZ3M]
audience: ug1
instance_of: [0B8T10CE7N]
uses: [0XSJ25Z9M4, 0JGZCDT5DN, 0RJF668P1T]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_map
    locator: Isomorphism
  - book: isbn:9780134860244
    locator: Section 2.4
---

## Example

A quadratic polynomial is fixed by its three coefficients, so computing with quadratics is the same as computing with triples.
Let $F$ be a field and let $P_2$ be the [[space of polynomials of degree at most 2|0JGZCDT5DN]] over $F$.
Let $T \colon P_2 \to F^3$ be $T(a + bx + cx^2) = (a, b, c)$, the list of coefficients.

1. The map is [[linear|0RJF668P1T]]: the coefficients of $p + q$ are the sums of the coefficients of $p$ and $q$, and the coefficients of $kp$ are $k$ times those of $p$.
2. It is injective: $T(p) = (0, 0, 0)$ means $a = b = c = 0$, so $p = 0$ and the kernel is $\{0\}$.
3. It is surjective: each $(a, b, c) \in F^3$ is $T(a + bx + cx^2)$.
4. So $T$ is a [[linear isomorphism|0XSJ25Z9M4]], and $P_2 \cong F^3$, with inverse $(a, b, c) \mapsto a + bx + cx^2$.

Check with numbers: $(1 + 2x) + (3 - x + x^2) = 4 + x + x^2$, and $(1, 2, 0) + (3, -1, 1) = (4, 1, 1)$.

## Remarks

The map $T$ is the coordinate map for the basis $1, x, x^2$, and another basis gives a different isomorphism $P_2 \to F^3$.
For the basis $1, \; 1 + x, \; (1 + x)^2$, the polynomial $x = -1 + (1 + x)$ has coordinates $(-1, 1, 0)$, not $(0, 1, 0)$.
So the isomorphism depends on the basis.

Through $T$, the derivative on $P_2$ becomes a $3 \times 3$ matrix acting on $F^3$.
It sends $(a, b, c)$ to $(b, 2c, 0)$, the coefficients of $b + 2cx$.

## Explanations

### L1 human

A quadratic polynomial is fixed by its three coefficients.
Adding polynomials adds the coefficients, and scaling a polynomial scales them.
So computing with quadratic polynomials is the same as computing with triples of numbers.

### L2 human

This isomorphism lets matrix methods work on polynomials.
To test whether $1 + x$, $x + x^2$ and $1 + x^2$ are independent over $\R$, test the triples $(1, 1, 0)$, $(0, 1, 1)$ and $(1, 0, 1)$ instead.
The matrix with these rows has determinant $1 \cdot (1 - 0) - 1 \cdot (0 - 1) + 0 = 2 \ne 0$, so the polynomials are independent over $\R$.
Over a field with $1 + 1 = 0$ the determinant is $0$, and indeed the three polynomials add up to $2 + 2x + 2x^2 = 0$ there.
Watch out: the triples come from a chosen basis, and a different basis gives different triples.
