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

Let $K$ be a commutative ring and let $A = (a_{ij})$ be an $n \times n$ [[upper triangular|0MKABWDRNC]] or [[lower triangular|0EZSD6T9E0]] matrix over $K$.
Then
$$\det A = a_{11} a_{22} \cdots a_{nn},$$
where $\det$ is the [[determinant|0C3CFHDN6R]].

## Remarks

### Why each hypothesis is needed

The zeros must lie on one side of the diagonal.
The matrix $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ has zero diagonal but $\det = -1$, so the product of the diagonal entries is not the determinant in general.

### Consequences

- A [[diagonal matrix|044JNC7ZAA]] has determinant equal to the product of its diagonal entries; in particular $\det I_n = 1$.
- A triangular matrix over a field is invertible if and only if all its diagonal entries are nonzero.
- Computation by row reduction: bring $A$ to an echelon form $U$ by $s$ row swaps and by additions of multiples of rows. By the [[effect of row operations|09YB3WQG38]], $\det A = (-1)^s u_{11} \cdots u_{nn}$.
- Over a field this costs about $\tfrac{2}{3} n^3$ arithmetic operations, against $n! \cdot n$ for the [[Leibniz formula|016PE4VZ8Q]].

### Converse

For $2 \times 2$ matrices the converse holds: $ad - bc = ad$ forces $bc = 0$ over a field, so $b = 0$ or $c = 0$.
For $n = 3$ it fails.
The matrix $\begin{pmatrix} 1 & 0 & 1 \\ 1 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$ is not triangular.
Expansion along row $3$ gives $\det = 1 \cdot (1 \cdot 1 - 0 \cdot 1) = 1$, which is the product of the diagonal entries.

### Generalizations

A block triangular matrix has determinant equal to the product of the determinants of its diagonal blocks; see the [[block triangular rule|0J9TVTNB4K]].
Over an algebraically closed field every matrix is similar to a triangular matrix, which gives $\det A$ as the [[product of the eigenvalues|0C2F40MEBC]].

## Explanations

### L1 human

A triangular table has only zeros below the diagonal, or only zeros above it.
Its determinant is the product of the diagonal entries.
For example, $\det \begin{pmatrix} 2 & 7 \\ 0 & 3 \end{pmatrix} = 2 \cdot 3 = 6$.
To find any determinant, first make the table triangular by row moves, and then use this rule.

### L2 human

Let $A = \begin{pmatrix} 2 & 1 & 5 & 3 \\ 0 & 3 & 1 & 4 \\ 0 & 0 & -1 & 2 \\ 0 & 0 & 0 & 4 \end{pmatrix}$.

1. $A$ is upper triangular, so $\det A = 2 \cdot 3 \cdot (-1) \cdot 4 = -24$.
2. Check by expansion along the first column: $\det A = 2 \det \begin{pmatrix} 3 & 1 & 4 \\ 0 & -1 & 2 \\ 0 & 0 & 4 \end{pmatrix}$.
3. Expanding again along the first column gives $2 \cdot 3 \cdot \det \begin{pmatrix} -1 & 2 \\ 0 & 4 \end{pmatrix} = 6 \cdot (-4) = -24$.

The typical use is the last step of a computation by row reduction.
A trap: the rule needs zeros on one full side of the diagonal; zeros scattered in other places do not help.

### L3 human

The upper triangular invertible matrices form the Borel subgroup $B$ of $\mathrm{GL}_n$, and $\det$ restricted to $B$ is the product of the diagonal characters.
The rule is the reason why $\det$ is computed in $O(n^3)$ operations over a field, and in $O(n^\omega)$ by fast matrix multiplication.
