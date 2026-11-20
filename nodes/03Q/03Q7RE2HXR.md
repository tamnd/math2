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

Let $K$ be a [[commutative ring|0310REJJY8]] and let $A$ be an $n \times n$ matrix over $K$, with [[determinant|0C3CFHDN6R]] $\det A \in K$.

1. $A$ is [[invertible|0TWTS88TWN]] over $K$ if and only if $\det A$ is a [[unit|019NFGFPR5]] of $K$. Then $A^{-1} = (\det A)^{-1} \operatorname{adj} A$, with the [[adjugate|0GMPYM0NSR]] $\operatorname{adj} A$.
2. For a ring homomorphism $\varphi \colon K \to L$ to a commutative ring $L$, let $\varphi(A)$ be the matrix $(\varphi(a_{ij}))$. Then $\det \varphi(A) = \varphi(\det A)$.
3. An integer matrix has an inverse with integer entries if and only if its determinant is $1$ or $-1$.

## Remarks

### Why each hypothesis is needed

$K$ must be commutative.
Over a non-commutative ring the Leibniz sum is not multiplicative, and it can vanish for an invertible matrix.
In part 1, "nonzero" is not enough: over $\mathbb{Z}/6\mathbb{Z}$ the matrix $\operatorname{diag}(2, 1)$ has $\det = 2 \neq 0$, but $2$ is not a unit, and the matrix has no inverse.

### Consequences

- Over a field, the units are the nonzero elements, and part 1 gives the [[invertibility criterion|FBSAPTP1PR]].
- Over $\mathbb{Z}/m\mathbb{Z}$, a matrix is invertible if and only if $\gcd(\det A, m) = 1$.
- Over the polynomial ring $F[x]$, a matrix is invertible if and only if its determinant is a nonzero constant.
- Part 2 is the basis of the generic matrix method: identities proved over $\mathbb{Z}[x_{ij}]$ hold over every commutative ring.

### Converse

Part 1 is an equivalence.
For a non-square matrix there is no determinant, and a non-square matrix over a nonzero commutative ring has no two-sided inverse.

### Generalizations

For a linear endomorphism $f$ of a finitely generated free module, $f$ is bijective if and only if $\det f$ is a unit.
For a finitely generated module $M$, every surjective endomorphism is bijective; the proof uses the Cayley-Hamilton theorem over $K$.

## Explanations

### L1 human

Over the rational or real numbers, a square matrix can be inverted when its determinant is not $0$.
Over the integers we can only divide by $1$ and $-1$.
So an integer matrix has an integer inverse exactly when its determinant is $1$ or $-1$.

### L2 human

Over $\mathbb{Z}/6\mathbb{Z}$, let $A = \begin{pmatrix} 1 & 2 \\ 3 & 1 \end{pmatrix}$.

1. $\det A = 1 - 6 = -5 \equiv 1 \pmod 6$, which is a unit.
2. $\operatorname{adj} A = \begin{pmatrix} 1 & -2 \\ -3 & 1 \end{pmatrix} \equiv \begin{pmatrix} 1 & 4 \\ 3 & 1 \end{pmatrix}$, and $(\det A)^{-1} = 1$.
3. So $A^{-1} = \begin{pmatrix} 1 & 4 \\ 3 & 1 \end{pmatrix}$.
4. Check: $A A^{-1} = \begin{pmatrix} 7 & 6 \\ 6 & 13 \end{pmatrix} \equiv I_2 \pmod 6$.

Over $\mathbb{Z}$, $\begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$ has $\det = 1$ and the integer inverse $\begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix}$.
A trap: $\begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix}$ has $\det = 2 \neq 0$, but its inverse $\operatorname{diag}(1/2, 1)$ is not an integer matrix.

### L3 human

$\det$ is a natural transformation from the functor $\mathrm{GL}_n$ to the functor $\mathbb{G}_m$ on commutative rings, and part 2 is this naturality.
The group $\mathrm{GL}_n(\mathbb{Z})$ of integer matrices with $\det = \pm 1$ is the automorphism group of the lattice $\mathbb{Z}^n$.
