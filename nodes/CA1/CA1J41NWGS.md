---
tag: CA1J41NWGS
kind: definition
name: Schur complement
msc: [15A09, 15A15]
defines: 6HWFBXYPZP
uses: [01AXG9KZQF, 0TWTS88TWN, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Schur_complement
---

## Definition

Let $F$ be a field and let $p, q \ge 1$.
Let $M$ be a $(p + q) \times (p + q)$ [[block matrix|0ASDFEQS6P]] over $F$,
$$M = \begin{pmatrix} A & B \\ C & D \end{pmatrix},$$
where $A$ is $p \times p$, $B$ is $p \times q$, $C$ is $q \times p$ and $D$ is $q \times q$.
If $A$ is [[invertible|0EB9N0S33C]], the *Schur complement of $A$ in $M$* is the $q \times q$ matrix
$$M/A = D - C A^{-1} B.$$
If $D$ is invertible, the *Schur complement of $D$ in $M$* is the $p \times p$ matrix
$$M/D = A - B D^{-1} C.$$

## Remarks

Example: let $M = \begin{pmatrix} 2 & 1 \\ 4 & 5 \end{pmatrix}$ with $p = q = 1$ and $A = (2)$.
Then $M/A = 5 - 4 \cdot \tfrac{1}{2} \cdot 1 = 3$, and indeed $\det M = 10 - 4 = 6 = 2 \cdot 3$.
Non-example: for $M = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ and $A = (0)$, the block $A$ is not invertible, so $M/A$ is not defined, although $M$ itself is invertible.
The definition comes from the factorisation
$$M = \begin{pmatrix} I_p & 0 \\ C A^{-1} & I_q \end{pmatrix} \begin{pmatrix} A & 0 \\ 0 & M/A \end{pmatrix} \begin{pmatrix} I_p & A^{-1} B \\ 0 & I_q \end{pmatrix},$$
which gives $\det M = \det A \cdot \det(M/A)$; see [[determinant via the Schur complement|0KA7A4ENVJ]].
In particular, when $A$ is invertible, $M$ is invertible if and only if $M/A$ is invertible.
The same formulas hold over any commutative ring when $A$ is invertible.
