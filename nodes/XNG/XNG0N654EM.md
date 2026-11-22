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

Let $V$ be the space of polynomials of degree at most $2$ over a field $F$, with the basis $B = (1, x, x^2)$.
Let $v_1 = 1 + x$, $v_2 = x + x^2$ and $v_3 = 1 + x^2$.
We compute $\det_B(v_1, v_2, v_3)$ and read off when the three polynomials form a basis.

1. The coordinates in $B$ list the coefficients of $1$, $x$ and $x^2$, so the columns are $(1, 1, 0)$, $(0, 1, 1)$ and $(1, 0, 1)$:
$$M = \begin{pmatrix} 1 & 0 & 1 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix}.$$
2. Expand along the first row:
$$\det M = 1 \cdot (1 \cdot 1 - 0 \cdot 1) - 0 \cdot (1 \cdot 1 - 0 \cdot 0) + 1 \cdot (1 \cdot 1 - 1 \cdot 0) = 1 + 1 = 2.$$
3. So the [[definition|0V94H674MB]] gives $\det_B(v_1, v_2, v_3) = 2$.
4. Over $F = \mathbb{Q}$ we have $2 \ne 0$, so by the [[basis criterion|5D1CHPV9Z3]] the three polynomials form a basis.
5. Check over $\mathbb{Q}$ by solving $a v_1 + b v_2 + c v_3 = 0$.
   The coefficients of $1$, $x$ and $x^2$ give $a + c = 0$, $a + b = 0$ and $b + c = 0$.
6. The first two equations give $a = -c$ and $b = c$, and then the third gives $2c = 0$.
   So $a = b = c = 0$, and the family is independent, as the determinant said.
7. Over $F = \mathbb{F}_2$ we have $2 = 0$, so the criterion says that the family is not a basis.
8. Check over $\mathbb{F}_2$: $v_1 + v_2 = 1 + 2x + x^2 = 1 + x^2 = v_3$, a linear dependence.

## Remarks

The matrix $M$ has integer entries, and its determinant is the integer $2$ read in each field.
That number is $0$ exactly in fields of characteristic $2$, so the family is a basis over every field whose characteristic is not $2$.

Over the ring $\mathbb{Z}$ the answer changes again.
The criterion for free modules needs the determinant to be a unit, and $2$ is not a unit of $\mathbb{Z}$.
Indeed, writing $1 = a v_1 + b v_2 + c v_3$ gives $a + c = 1$, $a + b = 0$ and $b + c = 0$, hence $2a = 1$, which has no integer solution.

## Explanations

### L1 human

Three polynomials of degree at most $2$ form a basis when their coordinate matrix has a nonzero determinant.
Here the determinant is $2$.
That is nonzero over the rational numbers, but it is zero when we compute modulo $2$, and there the three polynomials are dependent.

### L2 human

The determinant answers the basis question in one computation, and for every field at once.
The solving in steps 5 and 6 needed the division by $2$ hidden in $2c = 0$, and that is the same $2$ as the determinant.
Watch out: a determinant that is a nonzero integer can still be zero in the field you work in.
