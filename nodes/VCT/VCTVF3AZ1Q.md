---
tag: VCTVF3AZ1Q
kind: proof
name: Proof that adding a multiple of one row to another preserves the determinant
msc: [15A15]
proves: 01ZTQBK64Q
uses: [0PPG793642, 0K4VQB7HWR]
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Basic rules
---

## Proof

1. Let $a_k$ be row $k$ of $A$. Then row $i$ of $B$ is $a_i + c a_j$, and the other rows of $B$ are those of $A$.
2. Let $A'$ be the matrix obtained from $A$ by replacing row $i$ with $a_j$.
3. The matrices $A$, $A'$ and $B$ agree outside row $i$. Their rows $i$ are $a_i$, $a_j$ and $1 \cdot a_i + c \cdot a_j$.
4. By [[multilinearity in the rows|0PPG793642]] with $s = 1$ and $t = c$, we get $\det B = \det A + c \det A'$.
5. Rows $i$ and $j$ of $A'$ are both $a_j$, and $i \ne j$. So $\det A' = 0$, by the rule for [[two equal rows|0K4VQB7HWR]].
6. By steps 4 and 5, $\det B = \det A$.

## Idea

Split the new row into its old part and the added part. The added part gives a matrix with a repeated row, and that determinant is zero.
