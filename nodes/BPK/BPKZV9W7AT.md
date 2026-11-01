---
tag: BPKZV9W7AT
kind: definition
name: Matrix pencil
msc: [15A22]
defines: KQ7V0J5CGG
uses: [0VD9ZSWWJG, 04C5ZBG1WT, 00KDZRW4C0, 0BQAA2BK3Q]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_pencil
---

## Definition

Let $\mathbb{K}$ be a [[field|04C5ZBG1WT]], let $m, n \ge 1$, and let $A$ and $B$ be $m \times n$ [[matrices|0VD9ZSWWJG]] over $\mathbb{K}$.
The *matrix pencil* of $A$ and $B$ is the matrix $A - \lambda B$ with entries in the polynomial ring $\mathbb{K}[\lambda]$.
When $m = n$, the pencil is *regular* if the polynomial $\det(A - \lambda B)$ is not the zero polynomial, and *singular* otherwise.
For a regular pencil, an *eigenvalue* is a root $\lambda_0$ of $\det(A - \lambda B)$, and an *eigenvector* for $\lambda_0$ is a vector $v \ne 0$ with $Av = \lambda_0 Bv$.

## Remarks

Some authors write $\lambda B - A$ or $A + \lambda B$; this changes only signs.
When $B$ is singular, a regular pencil is often said to have an eigenvalue $\infty$, since $\mu A - B$ is singular at $\mu = 0$.
Example: $A = \begin{pmatrix} 2 & 0 \\ 0 & 6 \end{pmatrix}$ and $B = \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix}$ give $\det(A - \lambda B) = (2 - \lambda)(6 - 2\lambda)$, so the pencil is regular with eigenvalues $2$ and $3$.
Non-example: $A = B = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ give $\det(A - \lambda B) = (1 - \lambda) \cdot 0 = 0$, so the pencil is singular.
If $B$ is invertible, the eigenvalues of the pencil are the ordinary [[eigenvalues|0BQAA2BK3Q]] of $B^{-1}A$.
