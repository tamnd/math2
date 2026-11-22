---
tag: 4HC79H7TJR
kind: example
name: Expansion with unsigned minors gives a wrong determinant
msc: ["15A15"]
topics: [DTBK11SR77]
audience: ug1
instance_of: [0BT9BYWVRY]
not_instance_of:
  - target: 0XPKR18APA
    note: the first minor M12 = -2 of A is not the cofactor C12 = 2, since the sign (-1)^(1+2) is -1
uses: [0W2QAVJQ1W, 0SD528P0EK, 0C08BQ3M05]
sources:
  - url: https://en.wikipedia.org/wiki/Minor_(linear_algebra)
    locator: First minors
---

## Example

Let
$$A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 10 \end{pmatrix}.$$
We expand $\det A$ along the first row twice, once with the [[minors|0SD528P0EK]] alone and once with the [[cofactors|0W2QAVJQ1W]], and see that only the second is right.
The minor $M_{12}$ is a minor of $A$ but not a cofactor of $A$.

1. The first minors of row $1$ are
$$M_{11} = 50 - 48 = 2, \qquad M_{12} = 40 - 42 = -2, \qquad M_{13} = 32 - 35 = -3.$$
2. The cofactor in position $(1, 2)$ carries the sign $(-1)^{1+2} = -1$, so $C_{12} = -M_{12} = 2$.
   Hence $M_{12} \neq C_{12}$.
   The other two positions have even $i + j$, so $C_{11} = M_{11} = 2$ and $C_{13} = M_{13} = -3$.
3. The expansion with minors and no signs gives
$$1 \cdot 2 + 2 \cdot (-2) + 3 \cdot (-3) = 2 - 4 - 9 = -11.$$
4. The [[Laplace expansion|0C08BQ3M05]] with cofactors gives
$$1 \cdot 2 + 2 \cdot 2 + 3 \cdot (-3) = 2 + 4 - 9 = -3.$$
5. Check by the [[rule of Sarrus|7H2P40X0MV]]: the three products down to the right and the three products up to the right give
$$(50 + 84 + 96) - (105 + 48 + 80) = 230 - 233 = -3.$$
   So $\det A = -3$, and the unsigned expansion is wrong.

## Remarks

A minor and a cofactor agree when $i + j$ is even, and they differ by a sign when $i + j$ is odd.
So the mistake never shows on the diagonal, and it shows exactly at the positions of the minus signs in the checkerboard
$$\begin{pmatrix} + & - & + \\ - & + & - \\ + & - & + \end{pmatrix}.$$
If the entry $a_{12} = 2$ is replaced by $0$, the wrong expansion and the right one give the same value $2 - 9 = -7$, so a single example can hide the error.
That matrix has rows $(1, 0, 3)$, $(4, 5, 6)$ and $(7, 8, 10)$, and Sarrus gives $(50 + 0 + 96) - (105 + 48 + 0) = -7$.

## Explanations

### L1 human

The signs plus, minus, plus are part of the rule for expanding a $3 \times 3$ determinant.
Each entry of the first row is multiplied by the $2 \times 2$ determinant that is left when its row and column are covered.
Without the minus sign in the middle, this determinant comes out as $-11$ instead of $-3$.

### L2 human

The lesson is to write the checkerboard of signs before every expansion.
Watch out most when you expand along a row or column with a single nonzero entry in a position with odd $i + j$.
Then the expansion has one term, and a missing sign turns the true answer into its negative, which no size check will catch.
For the matrix with rows $(0, 2, 0)$, $(1, 0, 0)$ and $(0, 0, 1)$, expanding along row $1$ gives $2 \cdot C_{12} = 2 \cdot (-1) = -2$, while the unsigned version gives $+2$.
