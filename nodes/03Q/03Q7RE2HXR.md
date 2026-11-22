---
tag: 03Q7RE2HXR
kind: statement
role: theorem
name: Determinants over commutative rings
aliases: [a-matrix-is-invertible-iff-its-determinant-is-a-unit]
msc: ["15A15", "13C99"]
topics: [DTBK11SR77]
audience: grad
about: [00KDZRW4C0]
uses: [0C3CFHDN6R, 0TWTS88TWN, 0GMPYM0NSR, 019NFGFPR5, 0310REJJY8]
formal:
  - system: lean4
    library: mathlib
    decl: Matrix.isUnit_iff_isUnit_det
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Invertible_matrix
    locator: Invertible matrix theorem
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Over a commutative ring
---

## Statement

The determinant makes sense over any commutative ring, and there a matrix is invertible exactly when its determinant can be divided by.
Let $K$ be a [[commutative ring|0310REJJY8]], and let $A$ be an $n \times n$ matrix over $K$ with [[determinant|0C3CFHDN6R]] $\det A \in K$, defined by the Leibniz formula.

1. $A$ is [[invertible|0TWTS88TWN]] over $K$ if and only if $\det A$ is a [[unit|019NFGFPR5]] of $K$.
   In that case $A^{-1} = (\det A)^{-1} \operatorname{adj} A$, where $\operatorname{adj} A$ is the [[adjugate|0GMPYM0NSR]].
2. Let $\varphi \colon K \to L$ be a ring homomorphism to a commutative ring $L$, and let $\varphi(A)$ be the matrix with entries $\varphi(a_{ij})$.
   Then $\det \varphi(A) = \varphi(\det A)$.
3. An integer matrix has an inverse with integer entries if and only if its determinant is $1$ or $-1$.

## Remarks

### Units, not nonzero elements

Over a field every nonzero element is a unit, so part 1 is the familiar [[criterion over a field|FBSAPTP1PR]].
Over other rings the two notions split, and the determinant test has to ask for a unit.
In $\mathbb{Z}/6\mathbb{Z}$, the matrix $\operatorname{diag}(2, 1)$ has determinant $2 \neq 0$.
An inverse would force $\det A \cdot \det(A^{-1}) = 1$, so $2$ would have to be a unit, and $2x \equiv 1 \pmod 6$ has no solution.
So this matrix has no inverse over $\mathbb{Z}/6\mathbb{Z}$.

### Why the ring must be commutative

The Leibniz sum can be written down over any ring, but over a noncommutative ring it loses its meaning.
Over the quaternions, take the matrix with rows $(1, i)$ and $(j, k)$.
Its Leibniz sum is
$$1 \cdot k - i \cdot j = k - k = 0.$$
Yet the matrix is invertible.
If $x_1 + i x_2 = 0$ and $j x_1 + k x_2 = 0$, then $x_1 = -i x_2$, and the second equation becomes $(-ji + k) x_2 = 2k x_2 = 0$, so $x_2 = 0$ and $x_1 = 0$.
A map of finite-dimensional spaces over the quaternions with trivial kernel is invertible, so the test of part 1 fails here.

### What it gives you

Over $\mathbb{Z}/m\mathbb{Z}$ the units are the classes prime to $m$, so a matrix is invertible exactly when $\gcd(\det A, m) = 1$.
Over a polynomial ring $F[x]$ with $F$ a field, the units are the nonzero constants, so a polynomial matrix has a polynomial inverse exactly when its determinant is a nonzero constant.
For example, the matrix with rows $(1, x)$ and $(0, 1)$ has determinant $1$ and the inverse with rows $(1, -x)$ and $(0, 1)$.
Part 3 is the case $K = \mathbb{Z}$, whose only units are $1$ and $-1$.

Part 2 says that the determinant commutes with every change of ring.
This is the basis of the method of generic matrices: an identity among determinants proved for the matrix of indeterminates $(x_{ij})$ over $\mathbb{Z}[x_{ij}]$ holds over every commutative ring, by mapping each $x_{ij}$ to an entry.

### The converse and square shape

Part 1 is already an equivalence.
A non-square matrix has no determinant, and over a nonzero commutative ring it also has no two-sided inverse, so the theorem loses nothing by asking for square matrices.

### Generalizations

For an endomorphism $f$ of a finitely generated free module, the determinant of any matrix of $f$ is the same, and $f$ is bijective exactly when this determinant is a unit.
For a finitely generated module $M$ that need not be free, every surjective endomorphism is still bijective; the standard proof uses the determinant trick behind the Cayley-Hamilton theorem.
The proofs are in the [[proof node|91NHW201A1]].

## Explanations

### L1 human

Over the ordinary numbers you can divide by anything except $0$, so a matrix can be undone when its determinant is not $0$.
Over the whole numbers you can only divide by $1$ and $-1$ and stay a whole number.
So a matrix of whole numbers has an inverse made of whole numbers exactly when its determinant is $1$ or $-1$.
For example, the matrix with rows $(2, 1)$ and $(1, 1)$ has determinant $2 - 1 = 1$, and its inverse has rows $(1, -1)$ and $(-1, 2)$.

### L2 human

Work over $\mathbb{Z}/6\mathbb{Z}$ with
$$A = \begin{pmatrix} 1 & 2 \\ 3 & 1 \end{pmatrix}.$$
The determinant is $1 \cdot 1 - 2 \cdot 3 = -5$, and $-5 \equiv 1 \pmod 6$ is a unit, so $A$ is invertible.
The adjugate swaps the diagonal entries and negates the others:
$$\operatorname{adj} A = \begin{pmatrix} 1 & -2 \\ -3 & 1 \end{pmatrix} \equiv \begin{pmatrix} 1 & 4 \\ 3 & 1 \end{pmatrix} \pmod 6.$$
Since $(\det A)^{-1} = 1$, this is already $A^{-1}$.
Check:
$$\begin{pmatrix} 1 & 2 \\ 3 & 1 \end{pmatrix} \begin{pmatrix} 1 & 4 \\ 3 & 1 \end{pmatrix} = \begin{pmatrix} 7 & 6 \\ 6 & 13 \end{pmatrix} \equiv \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} \pmod 6.$$
The typical use is exactly this: decide invertibility by one gcd and write the inverse with the adjugate, with no division by pivots.
Watch out: $\operatorname{diag}(2, 1)$ over $\mathbb{Z}$ has determinant $2 \neq 0$, but its inverse $\operatorname{diag}(1/2, 1)$ is not an integer matrix.

### L3 human

Part 2 says that $\det$ is a natural transformation from the functor $K \mapsto M_n(K)$ to the functor $K \mapsto K$ on commutative rings.
Restricted to units, it is a natural homomorphism from $\mathrm{GL}_n$ to the multiplicative group $\mathbb{G}_m$, and part 1 identifies $\mathrm{GL}_n(K)$ as the matrices that this map sends to units.
The group $\mathrm{GL}_n(\mathbb{Z})$ of integer matrices with determinant $\pm 1$ is the group of automorphisms of the lattice $\mathbb{Z}^n$, and its subgroup $\mathrm{SL}_n(\mathbb{Z})$ of matrices with determinant $1$ is the automorphism group that keeps the orientation.
For noncommutative rings the determinant is replaced by other tools, such as the Dieudonné determinant over division rings.
