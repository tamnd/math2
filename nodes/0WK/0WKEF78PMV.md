---
tag: 0WKEF78PMV
kind: statement
role: theorem
name: "Sylvester's criterion"
msc: [15B57, 15A15]
uses: [0QQCG3JWJ4, 0SD528P0EK]
sources:
  - url: https://en.wikipedia.org/wiki/Sylvester's_criterion
    locator: lead section
same_as:
  wikidata: Q2709660
  wikipedia: "Sylvester's criterion"
---

## Statement

Let $A$ be an $n \times n$ complex Hermitian matrix.
For $1 \le k \le n$, let $\Delta_k$ be the determinant of the upper left $k \times k$ submatrix of $A$.
Then $A$ is [[positive definite|0KX66CZMBB]] if and only if $\Delta_k > 0$ for all $k = 1, \dots, n$.

## Remarks

The numbers $\Delta_k$ are the *leading principal [[minors|0BT9BYWVRY]]* of $A$.
For $\begin{pmatrix} a & b \\ b & c \end{pmatrix}$ real, the test is $a > 0$ and $ac - b^2 > 0$.
For positive semidefinite matrices, the analogous test needs all principal minors, not only the leading ones, to be nonnegative.

## Explanations

### L1 human

Sylvester's criterion tests positive definiteness with $n$ determinants.
We check the top left $1 \times 1$, $2 \times 2$, and so on, up to the full matrix.
All of them must be positive.
