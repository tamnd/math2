---
tag: NZJDNC6EP6
kind: definition
name: Matrix congruence
msc: [15A63, 15A21]
defines: WJWNYSQKK8
uses: [0CP7YY6NAG, 0TWTS88TWN, 0W809K6AW0, 0QA8CHH8MG]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_congruence
---

## Definition

Let $F$ be a [[field|04C5ZBG1WT]] and let $n \ge 1$.
Let $A$ and $B$ be $n \times n$ matrices over $F$.
Then $A$ and $B$ are *congruent* if there is an [[invertible|0EB9N0S33C]] $n \times n$ matrix $P$ over $F$ with
$$B = P^{T} A P.$$
Here $P^{T}$ is the [[transpose|09DXWYRD43]] of $P$.

## Remarks

Example: over $\R$, let $A = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ and $P = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$.
Then $P$ is invertible, since $\det P = -2$, and $P^{T} A P = \begin{pmatrix} 2 & 0 \\ 0 & -2 \end{pmatrix}$, so these two matrices are congruent.
Non-example: over $\R$, the identity $I_2$ and $-I_2$ are not congruent, because $x^{T} P^{T} I_2 P x = \norm{Px}^2 \ge 0$ for all $x \in \R^2$, while $x^{T} (-I_2) x < 0$ for $x \ne 0$.
Congruence is an equivalence relation on $n \times n$ matrices.
Let $A$ be the matrix of a [[bilinear form|0SQZMXB6GP]] in one basis, and let $P$ be the [[change of basis matrix|0MKRHZB3WS]] to a second basis.
Then $P^{T} A P$ is the matrix of the same form in the second basis; see [[change of basis for a bilinear form|0SPYAGE7T0]].
Congruence keeps symmetry and the rank, and it multiplies the determinant by the nonzero square $(\det P)^2$.
Over $\C$, the complex analogue often uses the [[conjugate transpose|0DXKE10PHF]] $P^{*}$ in place of $P^{T}$; this is called $*$-congruence.
