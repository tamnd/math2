---
tag: XNG0N654EM
kind: example
name: Three polynomials that form a basis over Q but not over F2
msc: [15A15, 15A75]
topics: [DTBK11SR77]
audience: ug2
instance_of: [05CJSSXPR3]
uses: [0V94H674MB, 5D1CHPV9Z3]
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Determinant of n vectors
---

## Example

Let $V$ be the space of polynomials of degree at most $2$ over a field $F$, with basis $B = (1, x, x^2)$.
Let $v_1 = 1 + x$, $v_2 = x + x^2$ and $v_3 = 1 + x^2$.

1. The coordinate matrix is $M = \begin{pmatrix} 1 & 0 & 1 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix}$.
2. Expansion along row 1 gives $\det M = 1 \cdot (1 - 0) - 0 + 1 \cdot (1 - 0) = 2$.
3. So the [[definition|0V94H674MB]] gives $\det_B(v_1, v_2, v_3) = 2$.
4. Over $F = \mathbb{Q}$, $2 \ne 0$, so by the [[basis criterion|5D1CHPV9Z3]] the three polynomials form a basis.
5. Check over $\mathbb{Q}$ by solving: $a v_1 + b v_2 + c v_3 = 0$ gives $a + c = 0$, $a + b = 0$ and $b + c = 0$.
6. These equations give $a = -c$, $b = c$ and $2c = 0$, so $a = b = c = 0$, and the family is independent.
7. Over $F = \mathbb{F}_2$, $2 = 0$, so the criterion says that the family is not a basis.
8. Check over $\mathbb{F}_2$: $v_1 + v_2 = 1 + 2x + x^2 = 1 + x^2 = v_3$, a linear dependence.

## Remarks

The same integer matrix has determinant $2$ in every field, but $2$ is $0$ exactly in characteristic $2$.
So the family is a basis over every field of characteristic other than $2$.
Over the ring $\mathbb{Z}$, the family is not a basis of the polynomials with integer coefficients, since $2$ is not a unit; for example, $1$ is not an integer combination.

## Explanations

### L1 human

Three polynomials of degree at most $2$ form a basis when their coordinate matrix has a nonzero determinant.
Here the determinant is $2$.
This is nonzero over the rationals, but it is zero when we compute modulo $2$.

### L2 human

The determinant answers the basis question in one computation, for every field at once.
A trap: a determinant that is "nonzero as an integer" can vanish in the field you work in.
