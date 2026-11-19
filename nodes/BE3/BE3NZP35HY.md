---
tag: BE3NZP35HY
kind: statement
role: proposition
name: Augmentation principle for reduced row echelon form
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: ug1
uses: [0WF5AQYTW6, 0T6MWGZSXA, BF9SMZMJZE, K41GT10YM6]
about: [0WF5AQYTW6]
proofs: [CQ1CPPK3JH]
sources:
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section1-3.xml#L683
    locator: src/section1-3.xml:683
  - url: https://understandinglinearalgebra.org/
    locator: Chapter 1
---

## Statement

Let $F$ be a [[field|04C5ZBG1WT]], let $A$ be an $m \times n$ matrix over $F$, and let $C$ be an $m \times k$ matrix over $F$.
Call $B = [A \mid C]$ an augmentation of $A$: its first $n$ columns are the columns of $A$.
Then the [[reduced row echelon form|0WF5AQYTW6]] of $B$ is an augmentation of the reduced row echelon form of $A$:
$$\operatorname{rref}[A \mid C] = [\operatorname{rref}(A) \mid D] \quad \text{for some } m \times k \text{ matrix } D.$$
In other words, the first $n$ columns of the reduced row echelon form of $B$ make up the reduced row echelon form of $A$.

## Remarks

### Why each hypothesis is needed

1. The added columns must be on the right. For $A = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$ and the added column $\begin{bmatrix} 1 \\ 2 \end{bmatrix}$ on the left, the RREF of $\begin{bmatrix} 1 & 1 \\ 2 & 1 \end{bmatrix}$ is $I_2$, whose last column $e_2$ is not $\operatorname{rref}(A) = e_1$.
2. The statement is about the reduced form; for echelon forms that are not reduced, the left block is an echelon form of $A$, but there is no unique one to compare with.

### Consequences

1. To solve $Ax = b$, one may reduce $[A \mid b]$ and read $\operatorname{rref}(A)$ from the left block.
2. $\operatorname{rank} [A \mid b]$ is $\operatorname{rank} A$ or $\operatorname{rank} A + 1$, since the left block has $\operatorname{rank} A$ pivots and at most one more pivot can appear in the last column.
3. Reducing $[A \mid I]$ gives $[\operatorname{rref}(A) \mid P]$ with $PA = \operatorname{rref}(A)$, which is the method for inverses.

### Converse

The converse "if the left block of $\operatorname{rref}(B)$ is $\operatorname{rref}(A)$, then $B$ is an augmentation of $A$" is false: $B = [2A \mid C]$ has the same left block.

## History

The name "augmentation principle" is used by Austin in *Understanding Linear Algebra*, Chapter 1.

## Explanations

### L1 human

When you add extra columns on the right of a table and reduce it, the left part reduces exactly as it would alone.
This is because the row moves are chosen by looking at the left columns first.
So the extra columns ride along without changing the left part.

### L2 human

Let $A = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}$ and $C = \begin{bmatrix} 3 \\ 7 \end{bmatrix}$.

1. $\operatorname{rref}(A) = \begin{bmatrix} 1 & 2 \\ 0 & 0 \end{bmatrix}$, by $R_2 \leftarrow R_2 - 2R_1$.
2. For $[A \mid C]$, the same step gives $\left[\begin{array}{cc|c} 1 & 2 & 3 \\ 0 & 0 & 1 \end{array}\right]$, and $R_1 \leftarrow R_1 - 3R_2$ gives $\left[\begin{array}{cc|c} 1 & 2 & 0 \\ 0 & 0 & 1 \end{array}\right]$.
3. The left block is $\operatorname{rref}(A)$, as the principle says.

The typical use is to justify reading the coefficient part of a reduced augmented matrix.
A trap: the right block $D$ is not $\operatorname{rref}(C)$ in general; in step 2 it is $e_2$, while $\operatorname{rref}(C) = e_1$.
