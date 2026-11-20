---
tag: NZ8PF59MTJ
kind: example
name: Row space of a matrix with a non-reduced echelon form
msc: ["15A03"]
topics: [S6559D61BP]
audience: ug1
instance_of: [069MCGX635]
illustrates: [1JGMW9DM4Z]
uses: [0EP73HK4C4, 0F27PBRWD7]
sources:
  - url: https://en.wikipedia.org/wiki/Row_and_column_spaces
    locator: Row space
---

## Example

Let $A = \begin{pmatrix} 0 & 2 & 4 \\ 1 & 1 & 1 \\ 1 & 3 & 5 \end{pmatrix}$ over $\R$.

1. Exchange rows 1 and 2. The rows become $(1, 1, 1)$, $(0, 2, 4)$, $(1, 3, 5)$.
2. Subtract row 1 from row 3. Row 3 becomes $(0, 2, 4)$.
3. Subtract row 2 from row 3. Row 3 becomes $(0, 0, 0)$. The result
$$U = \begin{pmatrix} 1 & 1 & 1 \\ 0 & 2 & 4 \\ 0 & 0 & 0 \end{pmatrix}$$
is in [[row echelon form|0F27PBRWD7]], not reduced, with pivots $1$ and $2$ in columns 1 and 2.
4. So $(1, 1, 1)$ and $(0, 2, 4)$ form a basis of the [[row space|0EP73HK4C4]] of $A$, and $\dim \operatorname{Row}(A) = 2$.
5. Check: row 3 of $A$ is $(1, 3, 5) = (1, 1, 1) + (0, 2, 4)$, and row 1 of $A$ is $(0, 2, 4)$ itself.
6. A normal vector: $n = (1, -2, 1)$ satisfies $(1, 1, 1) \cdot n = 1 - 2 + 1 = 0$ and $(0, 2, 4) \cdot n = -4 + 4 = 0$. So $\operatorname{Row}(A)$ is the plane $x - 2y + z = 0$ in $\R^3$.
7. Check $An = (0 - 4 + 4,\ 1 - 2 + 1,\ 1 - 6 + 5) = (0, 0, 0)$. So $n$ spans the null space of $A$, which is orthogonal to the row space.

## Remarks

- The basis need not come from the reduced form: any echelon form works.
- The row exchange in step 1 is allowed. It does not change the span of the rows.

## Explanations

### L1 human

Row operations do not change which vectors are combinations of the rows.
After two subtractions a zero row appears, so the three rows span only a plane.

### L2 human

The two nonzero rows of the echelon form are a basis, because of the staircase of pivots.
Over $\R$ the null space is the orthogonal complement of the row space, so one normal vector describes the whole plane.
