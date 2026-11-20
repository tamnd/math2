---
tag: B2YDT3YNCW
kind: example
name: The first minors and leading principal minors of a 3 × 3 matrix
msc: ["15A15"]
topics: [DTBK11SR77]
audience: ug1
instance_of: [0BT9BYWVRY]
uses: [0SD528P0EK, 0ZN2J42SK7, 0C08BQ3M05]
sources:
  - url: https://en.wikipedia.org/wiki/Minor_(linear_algebra)
    locator: First minors
---

## Example

Let $A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 10 \end{pmatrix}$ over $\mathbb{Q}$.
We compute some [[minors|0SD528P0EK]] by the [[2 × 2 formula|0ZN2J42SK7]].

1. $M_{11}$ deletes row $1$ and column $1$: $\det \begin{pmatrix} 5 & 6 \\ 8 & 10 \end{pmatrix} = 50 - 48 = 2$.
2. $M_{12}$ deletes row $1$ and column $2$: $\det \begin{pmatrix} 4 & 6 \\ 7 & 10 \end{pmatrix} = 40 - 42 = -2$.
3. $M_{13}$ deletes row $1$ and column $3$: $\det \begin{pmatrix} 4 & 5 \\ 7 & 8 \end{pmatrix} = 32 - 35 = -3$.
4. The leading principal minors are $\det(1) = 1$, $\det \begin{pmatrix} 1 & 2 \\ 4 & 5 \end{pmatrix} = 5 - 8 = -3$, and $\det A$.
5. Expansion along row $1$ by the [[Laplace expansion|0C08BQ3M05]] gives $\det A = 1 \cdot M_{11} - 2 \cdot M_{12} + 3 \cdot M_{13} = 2 + 4 - 9 = -3$.
6. Check by row reduction: $R_2 - 4R_1$ and $R_3 - 7R_1$ give rows $(0, -3, -6)$ and $(0, -6, -11)$. Then $\det A = 1 \cdot ((-3)(-11) - (-6)(-6)) = 33 - 36 = -3$.

## Remarks

The matrix has $9$ first minors and $\binom{3}{2}^2 = 9$ minors of order $2$; for a $3 \times 3$ matrix these are the same.
The second leading principal minor is $-3 < 0$, so $A$ is not positive definite; for a symmetric matrix this is the test of [[Sylvester's criterion|0WKEF78PMV]], although $A$ here is not symmetric.

## Explanations

### L1 human

Each entry of a $3 \times 3$ table has a minor: cover its row and its column, and take the $2 \times 2$ determinant of the four numbers left.
Here the three minors of the first row are $2$, $-2$ and $-3$.

### L2 human

The minors of row $1$, with the signs $+, -, +$, give the determinant $-3$.
A second method, row reduction, gives the same value, which checks the minors.
A trap: in step 5 the middle sign is minus; without it one gets $2 - 4 - 9 = -11$, which is wrong.
