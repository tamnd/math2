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

Let $A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 10 \end{pmatrix}$, with $\det A = -3$.

1. The first [[minors|0SD528P0EK]] of row $1$ are $M_{11} = 2$, $M_{12} = -2$, $M_{13} = -3$.
2. The [[cofactor|0W2QAVJQ1W]] $C_{12}$ is $(-1)^{1+2} M_{12} = 2$, so $M_{12} \neq C_{12}$.
3. The expansion with minors and no signs gives $1 \cdot 2 + 2 \cdot (-2) + 3 \cdot (-3) = -11$.
4. The [[Laplace expansion|0C08BQ3M05]] with cofactors gives $1 \cdot 2 + 2 \cdot 2 + 3 \cdot (-3) = -3$.
5. Check by the rule of Sarrus: $50 + 84 + 96 - 105 - 48 - 80 = -3$. So the unsigned version is wrong.

## Remarks

A minor and a cofactor agree when $i + j$ is even, and differ by a sign when $i + j$ is odd.
So the error is invisible on the diagonal and appears only off the diagonal.

## Explanations

### L1 human

The signs plus, minus, plus are part of the rule.
Without them the expansion of this $3 \times 3$ determinant gives $-11$ instead of $-3$.

### L2 human

Always write the checkerboard of signs before an expansion.
A trap: for a row with a single nonzero entry in an odd position, the missing sign changes the answer to its negative.
