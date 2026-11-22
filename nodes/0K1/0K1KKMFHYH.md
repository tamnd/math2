---
tag: 0K1KKMFHYH
kind: statement
role: proposition
name: Determinant of a triangular matrix
msc: ["15A15"]
topics: [DTBK11SR77]
audience: ug1
about: [00KDZRW4C0]
uses: [0C3CFHDN6R, 0MKABWDRNC, 0EZSD6T9E0]
formal:
  - system: lean4
    library: mathlib
    decl: Matrix.det_of_upperTriangular
    match: weaker
sources:
  - url: https://en.wikipedia.org/wiki/Triangular_matrix
    locator: Properties
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Gaussian elimination
---

## Statement

For a triangular matrix the determinant is just the product of the diagonal entries, and this is what makes determinants cheap to compute.
Let $K$ be a commutative ring, let $n \ge 1$, and let $A = (a_{ij})$ be an $n \times n$ matrix over $K$ that is [[upper triangular|0MKABWDRNC]] or [[lower triangular|0EZSD6T9E0]].
Then
$$\det A = a_{11} a_{22} \cdots a_{nn},$$
where $\det$ is the [[determinant|0C3CFHDN6R]].

## Remarks

### A first computation

Take the upper triangular matrix
$$A = \begin{pmatrix} 2 & 1 & 5 & 3 \\ 0 & 3 & 1 & 4 \\ 0 & 0 & -1 & 2 \\ 0 & 0 & 0 & 4 \end{pmatrix}.$$
The statement gives $\det A = 2 \cdot 3 \cdot (-1) \cdot 4 = -24$, and the entries above the diagonal play no role.
Check by expansion along the first column, where only the entry $2$ is nonzero:
$$\det A = 2 \det \begin{pmatrix} 3 & 1 & 4 \\ 0 & -1 & 2 \\ 0 & 0 & 4 \end{pmatrix} = 2 \cdot 3 \det \begin{pmatrix} -1 & 2 \\ 0 & 4 \end{pmatrix} = 6 \cdot (-4) = -24.$$

### Why the zeros must be on one side

The rule needs all zeros below the diagonal, or all zeros above it.
The matrix $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ has the diagonal product $0$, but its determinant is $0 - 1 = -1$.
Its zeros are on the diagonal, not on one side of it, so the rule does not apply.

### Computing by row reduction

The main use is the last step of [[Gaussian elimination|0JVJ2WCXZH]].
Bring $A$ to an echelon form $U$ by $s$ row exchanges and by additions of multiples of rows.
Since an echelon form of a square matrix is upper triangular, the [[effect of row operations|09YB3WQG38]] gives
$$\det A = (-1)^s\, u_{11} u_{22} \cdots u_{nn}.$$
Over a field this takes about $\tfrac{2}{3} n^3$ arithmetic operations.
The [[Leibniz formula|016PE4VZ8Q]] has $n!$ terms, which is already $3\,628\,800$ terms for $n = 10$.

### Other consequences

A [[diagonal matrix|044JNC7ZAA]] is triangular, so its determinant is the product of its diagonal, and in particular $\det I_n = 1$.
Over a field, a triangular matrix is invertible exactly when no diagonal entry is $0$, by the [[invertibility criterion|FBSAPTP1PR]].
A block triangular matrix has determinant equal to the product of the determinants of its diagonal blocks, by the [[block triangular rule|0J9TVTNB4K]].
Over an algebraically closed field every matrix is similar to a triangular one, and this gives $\det A$ as the [[product of the eigenvalues|0C2F40MEBC]].

### The converse

For $2 \times 2$ matrices over a field the converse holds: $ad - bc = ad$ forces $bc = 0$, so $b = 0$ or $c = 0$, and the matrix is triangular.
For $3 \times 3$ matrices it fails.
The matrix $\begin{pmatrix} 1 & 0 & 1 \\ 1 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$ is not triangular.
Expansion along row $3$ gives $\det = 1 \cdot (1 \cdot 1 - 0 \cdot 1) = 1$, which is the product of the diagonal entries.

### Try it

Compute $\det \begin{pmatrix} 3 & 0 & 0 \\ 7 & -2 & 0 \\ 1 & 5 & 4 \end{pmatrix}$.
The matrix is lower triangular, so the determinant is $3 \cdot (-2) \cdot 4 = -24$.

## Explanations

### L1 human

A triangular table has only zeros below the diagonal, or only zeros above it.
Its determinant is the product of the numbers on the diagonal.
For example, $\det \begin{pmatrix} 2 & 7 \\ 0 & 3 \end{pmatrix} = 2 \cdot 3 - 7 \cdot 0 = 6$, and the $7$ does not matter.
To find any determinant, you can first make the table triangular by row moves and then use this rule.

### L2 human

Here is a typical use: compute
$$\det \begin{pmatrix} 2 & 4 & 2 \\ 1 & 5 & 3 \\ 3 & 8 & 9 \end{pmatrix}$$
by reduction to triangular form.
Subtract $\tfrac{1}{2}$ times row $1$ from row $2$ and $\tfrac{3}{2}$ times row $1$ from row $3$, which gives the rows $(0, 3, 2)$ and $(0, 2, 6)$.
Subtract $\tfrac{2}{3}$ times the new row $2$ from row $3$, which gives $(0, 0, \tfrac{14}{3})$.
No exchanges were made, so
$$\det = 2 \cdot 3 \cdot \tfrac{14}{3} = 28.$$
Check by the rule of Sarrus: $90 + 36 + 16 - 30 - 48 - 36 = 28$.
The problem shows the typical use: elimination does the hard part, and the triangular rule reads off the answer.
Watch out: zeros scattered off the diagonal do not help; only a full triangle of zeros does.

### L3 human

The invertible upper triangular matrices form a subgroup $B$ of $\mathrm{GL}_n(K)$, the standard Borel subgroup.
On $B$ the determinant is the product of the $n$ homomorphisms $A \mapsto a_{ii}$ to the group of units.
In a basis adapted to a full flag of invariant subspaces, the matrix of an endomorphism is triangular, so the rule reads the determinant from the action on the successive quotients of the flag.
The same idea, applied to blocks, gives the [[block triangular rule|0J9TVTNB4K]].
