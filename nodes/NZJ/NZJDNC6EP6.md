---
tag: NZJDNC6EP6
kind: definition
name: Matrix congruence
msc: ["15A63", "15A21"]
topics: [DYAK7YMK7B]
audience: ug1
defines: WJWNYSQKK8
uses: [0CP7YY6NAG, 0TWTS88TWN, 0W809K6AW0, 0QA8CHH8MG]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_congruence
---

## Definition

Two square matrices are congruent when one turns into the other by multiplying with an invertible matrix on the right and its transpose on the left.

Let $F$ be a [[field|04C5ZBG1WT]] and let $n \ge 1$.
Let $A$ and $A'$ be $n \times n$ [[square matrices|0CP7YY6NAG]] over $F$.
Then $A$ and $A'$ are *congruent* if there is an [[invertible|0EB9N0S33C]] $n \times n$ matrix $P$ over $F$ with
$$A' = P^{\mathsf{T}} A P.$$
Here $P^{\mathsf{T}}$ is the [[transpose|09DXWYRD43]] of $P$.

## Notation

Some books write $A \cong A'$ for congruent matrices, and others use no symbol.
Over $\mathbb{C}$, the relation $A' = P^* A P$ with the [[conjugate transpose|0DXKE10PHF]] is a different relation, called $*$-congruence.

## Remarks

The definition has two conditions, and each one has a reason.
The same matrix $P$ appears on both sides, once transposed, because a bilinear form has two slots and a change of basis acts on both of them.
The matrix $P$ must be invertible, so that the relation can be undone and the new matrix describes the form in a genuine basis.
With those two conditions, congruence is an [[equivalence relation|D3E2Y85S6H]], and it keeps the rank and the symmetry of a matrix.

For example, over $\mathbb{R}$ let $A = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ and $P = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$, with $\det P = -2 \neq 0$.
Then
$$P^{\mathsf{T}} A P = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} 2 & 0 \\ 0 & -2 \end{pmatrix},$$
so these two matrices are congruent.

A case that fails is $I_2$ and $-I_2$ over $\mathbb{R}$.
For every invertible $P$ and every $x \neq 0$, $x^{\mathsf{T}} P^{\mathsf{T}} I_2 P x = \lVert Px \rVert^2 > 0$, while $x^{\mathsf{T}} (-I_2) x < 0$, so no $P$ works.
If we drop the condition that $P$ is invertible, the failure is of another kind: $P = 0$ would make every matrix "congruent" to the zero matrix.

If $A$ is the matrix of a [[bilinear form|0SQZMXB6GP]] in one basis and $P$ is the [[change of basis matrix|0MKRHZB3WS]] to a second basis, then $P^{\mathsf{T}} A P$ is the matrix of the same form in the second basis, by the [[change of basis rule|0SPYAGE7T0]].
The concept page [[matrix congruence|WJWNYSQKK8]] develops the idea with more examples.

## Explanations

### L1 human

Two square tables of numbers are congruent when they describe the same form in two coordinate systems.
The new table is the old one with the change of coordinates applied on both sides.
For example, the identity table and the table with $4$ and $9$ on its diagonal are congruent, by the stretch $\operatorname{diag}(2, 3)$.

### L2 human

To show that two matrices are congruent, find an invertible $P$ and compute $P^{\mathsf{T}} A P$.
For $A = I_2$ and $P = \operatorname{diag}(2, 3)$ we get
$$P^{\mathsf{T}} I_2 P = \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix} \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix} = \begin{pmatrix} 4 & 0 \\ 0 & 9 \end{pmatrix}.$$
To show that two matrices are not congruent, find an invariant that differs, such as the rank, or the sign of the determinant over $\mathbb{R}$.
Watch out: $P^{\mathsf{T}} A P$ and $P^{-1} A P$ are different matrices unless $P^{\mathsf{T}} = P^{-1}$.
For $P = \operatorname{diag}(2, 3)$ and $A = I_2$, similarity gives $I_2$ again, while congruence gives $\operatorname{diag}(4, 9)$.
