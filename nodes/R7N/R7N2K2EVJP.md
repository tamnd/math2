---
tag: R7N2K2EVJP
kind: example
name: Counting columns does not give the rank and the nullity
msc: ["15A03"]
topics: [9080WQTZ3M]
audience: ug1
not_instance_of:
  - target: 0ZZXSBTR4J
    note: the matrix with rows (1, 2) and (2, 4) has two nonzero columns but rank 1
  - target: 0APCFW7639
    note: the same matrix has no zero column but nullity 1
uses: [0JGB7A6GTS, 00K4FK4NBH]
sources:
  - url: https://en.wikipedia.org/wiki/Rank_(linear_algebra)
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Kernel_(linear_algebra)
    locator: Properties
---

## Example

Let $A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$, and let $T(x) = Ax$ on $\R^2$.
A naive count gives "rank $2$" for the two nonzero columns and "nullity $0$" for the absence of zero columns.
Both counts are wrong.

1. The second column $(2, 4)$ is $2$ times the first column $(1, 2)$.
2. So the image is the line spanned by $(1, 2)$, and the [[rank|0JGB7A6GTS]] is $1$, not $2$.
3. Row reduction gives $\begin{pmatrix} 1 & 2 \\ 0 & 0 \end{pmatrix}$. So $Ax = 0$ means $x_1 + 2x_2 = 0$, with one free variable $x_2$.
4. The kernel is spanned by $(-2, 1)$. Check: $A(-2, 1) = (-2 + 2,\ -4 + 4) = (0, 0)$.
5. So the [[nullity|00K4FK4NBH]] is $1$, not $0$.

The correct values satisfy $1 + 1 = 2$, as the rank-nullity theorem requires; the naive values $2 + 0$ happen to have the same sum, which hides the error.

## Remarks

- The rank is the number of independent columns, not the number of nonzero columns.
- The nullity is the number of free variables after row reduction, not the number of zero columns.
- Before row reduction, only zero columns are visible; dependent columns need a computation.

## Explanations

### L1 human

The two columns of this matrix point in the same direction.
So the map squeezes the plane onto a line, and its rank is $1$.
One direction, the direction of $(-2, 1)$, is sent to zero, so the nullity is $1$.

### L2 human

The example shows why rank and nullity need row reduction or an independence check.
Counting nonzero columns gives only an upper bound for the rank.
The trap is that the wrong values $2$ and $0$ still add up to $2$, so the rank-nullity theorem alone does not catch the error.
