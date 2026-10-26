---
tag: ~ced085ba
kind: statement
role: theorem
name: Determinant via the Schur complement
msc: [15A15]
uses: [~0dd14763, ~fa645e80, ~63729221]
sources:
  - url: https://en.wikipedia.org/wiki/Schur_complement
    locator: Properties
---

## Statement

Let $K$ be a commutative ring and let $A$ be an invertible $p \times p$ matrix over $K$.
Let $B$, $C$ and $D$ be matrices over $K$ of sizes $p \times q$, $q \times p$ and $q \times q$.
Then
$$\det \begin{pmatrix} A & B \\ C & D \end{pmatrix} = \det A \cdot \det(D - C A^{-1} B),$$
where $\det$ is the [[determinant|~362fc72a]].
The matrix $D - C A^{-1} B$ is the *Schur complement* of $A$ in the [[block matrix|~92c2a9c5]].

## Remarks

The proof factors the block matrix as $\begin{pmatrix} I & 0 \\ C A^{-1} & I \end{pmatrix} \begin{pmatrix} A & B \\ 0 & D - C A^{-1} B \end{pmatrix}$.
Then it uses the rule for [[block triangular matrices|~d38416bf]].
For $p = q = 1$ and $a \ne 0$, it gives $\det \begin{pmatrix} a & b \\ c & d \end{pmatrix} = a(d - cb/a) = ad - bc$.

## Explanations

### L1 human

Block elimination removes the block $C$, in the same way as Gaussian elimination removes an entry.
What remains in the lower right corner is the Schur complement.
The determinant is then the product of two smaller determinants.
