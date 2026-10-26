---
tag: 0KA7A4ENVJ
kind: statement
role: theorem
name: Determinant via the Schur complement
msc: [15A15]
uses: [0C3CFHDN6R, 01AXG9KZQF, 0TWTS88TWN]
sources:
  - url: https://en.wikipedia.org/wiki/Schur_complement
    locator: Properties
---

## Statement

Let $K$ be a commutative ring and let $A$ be an invertible $p \times p$ matrix over $K$.
Let $B$, $C$ and $D$ be matrices over $K$ of sizes $p \times q$, $q \times p$ and $q \times q$.
Then
$$\det \begin{pmatrix} A & B \\ C & D \end{pmatrix} = \det A \cdot \det(D - C A^{-1} B),$$
where $\det$ is the [[determinant|00KDZRW4C0]].
The matrix $D - C A^{-1} B$ is the *Schur complement* of $A$ in the [[block matrix|0ASDFEQS6P]].

## Remarks

The proof factors the block matrix as $\begin{pmatrix} I & 0 \\ C A^{-1} & I \end{pmatrix} \begin{pmatrix} A & B \\ 0 & D - C A^{-1} B \end{pmatrix}$.
Then it uses the rule for [[block triangular matrices|0J9TVTNB4K]].
For $p = q = 1$ and $a \ne 0$, it gives $\det \begin{pmatrix} a & b \\ c & d \end{pmatrix} = a(d - cb/a) = ad - bc$.

## Explanations

### L1 human

Block elimination removes the block $C$, in the same way as Gaussian elimination removes an entry.
What remains in the lower right corner is the Schur complement.
The determinant is then the product of two smaller determinants.
