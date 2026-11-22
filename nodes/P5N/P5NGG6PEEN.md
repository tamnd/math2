---
tag: P5NGG6PEEN
kind: example
name: Rule of Sarrus checked by row reduction
msc: ["15A15"]
topics: [DTBK11SR77]
audience: school
instance_of: [7H2P40X0MV]
uses: [7H2P40X0MV, 09YB3WQG38, 0K1KKMFHYH]
sources:
  - url: https://en.wikipedia.org/wiki/Rule_of_Sarrus
    locator: lead section
---

## Example

Let $A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 10 \end{pmatrix}$ over $\mathbb{Q}$.
We compute $\det A$ by the [[rule of Sarrus|7H2P40X0MV]], and we check it by row reduction.

1. The three down diagonals give
$$1 \cdot 5 \cdot 10 + 2 \cdot 6 \cdot 7 + 3 \cdot 4 \cdot 8 = 50 + 84 + 96 = 230.$$
2. The three up diagonals give
$$7 \cdot 5 \cdot 3 + 8 \cdot 6 \cdot 1 + 10 \cdot 4 \cdot 2 = 105 + 48 + 80 = 233.$$
3. So the rule gives $\det A = 230 - 233 = -3$.
4. For the check, subtract $4$ times row $1$ from row $2$, and $7$ times row $1$ from row $3$.
   The rows become $(1, 2, 3)$, $(0, -3, -6)$ and $(0, -6, -11)$.
5. Subtract $2$ times the new row $2$ from the new row $3$.
   Row $3$ becomes $(0, -6, -11) - (0, -6, -12) = (0, 0, 1)$.
6. Each step added a multiple of one row to another row, so the determinant did not change, by the [[effect of row operations|09YB3WQG38]].
7. The result is upper triangular, so its determinant is the product of the diagonal entries, by the [[triangular rule|0K1KKMFHYH]]:
$$1 \cdot (-3) \cdot 1 = -3.$$
8. The two methods agree.

## Remarks

The two sums $230$ and $233$ are large and close, and the determinant is their small difference.
This is common, and it means that an error of a few units in one product changes the answer completely.
Row reduction keeps the numbers smaller, and that is one reason it is the better method for larger matrices.

Now change $a_{33} = 10$ to $a_{33} = 9$.
The determinant is linear in $a_{33}$, and the coefficient of $a_{33}$ is the $2 \times 2$ determinant $1 \cdot 5 - 2 \cdot 4 = -3$ of the top left corner.
So the new determinant is
$$-3 + (9 - 10) \cdot (-3) = 0.$$
This fits the rows $(1, 2, 3)$, $(4, 5, 6)$ and $(7, 8, 9)$: the third row is $2 \cdot (4, 5, 6) - (1, 2, 3)$, so the rows are dependent.

## Explanations

### L1 human

The three down products add up to $230$, and the three up products add up to $233$.
The determinant is the difference, $-3$.
Clearing the entries below the diagonal gives the same number in another way: the diagonal ends as $1$, $-3$ and $1$, and their product is $-3$.

### L2 human

Row reduction is a check that uses different arithmetic, so it catches slips in the rule.
Watch out for row swaps during a reduction.
A swap changes the sign of the determinant, so each swap must be counted, while adding a multiple of a row changes nothing.
