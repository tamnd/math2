---
tag: 8G3X8MPG7E
kind: concept
name: Commuting matrices
msc: [15A27]
topics: [Y1ESNQ2V52]
audience: ug1
uses: [0JXZKX526R, 032Q9FB8MT]
sources:
  - url: https://en.wikipedia.org/wiki/Commuting_matrices
  - url: https://en.wikipedia.org/wiki/Commuting_matrices
    locator: Characterizations and properties
same_as:
  wikidata: Q3360633
  wikipedia: Commuting matrices
---

## Summary

Two [[square matrices|0JXZKX526R]] $A$ and $B$ of the same size commute when $AB = BA$; the [[formal definition|MX26N71ZD3]] states it.
[[Matrix multiplication|032Q9FB8MT]] is [[not commutative|0P506SPZP2]] in general, so commuting pairs are special.
For commuting matrices, the algebra of numbers works: the [[binomial theorem|~af4d44e0]] holds, and $e^{A + B} = e^{A} e^{B}$ by [[this theorem|04BD23PSK5]].
Over $\mathbb{C}$, commuting matrices have a common eigenvector.

## Motivation

Many rules of school algebra use $ab = ba$ without saying so.
Examples are $(a + b)^2 = a^2 + 2ab + b^2$, $(ab)^n = a^n b^n$ and $a^2 - b^2 = (a - b)(a + b)$.
For matrices these rules hold exactly for commuting pairs, so commuting is the condition to check before such a rule is used.
In quantum mechanics, two observables can be measured together exactly when their matrices commute.

## Notation

- The condition $AB = BA$ is often written $[A, B] = 0$, where $[A, B] = AB - BA$ is the [[commutator|0PXW0BN7DW]].
- In Mathlib, `Commute A B` means `A * B = B * A`, for elements of any semigroup.

## Remarks

### Examples

- [[A polynomial in A commutes with A|~8d0e01aa]].
- [[Two upper triangular 2 × 2 matrices that commute|~5ce7b775]].
- Every matrix commutes with itself, with its powers, with $I$ and with every [[scalar matrix|067NKSBEWT]] $cI$.
- Two [[diagonal matrices|0Q9PGXD9E4]] of the same size commute, because their products are computed entry by entry on the diagonal.

### Non-examples

- [[The pair used to test the square formula|60W7PZXBVB]]: $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ and $\begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$ do not commute.
- The [[matrix units|~709aa34e]] $E_{12}$ and $E_{21}$ do not commute: $E_{12} E_{21} = E_{11}$ and $E_{21} E_{12} = E_{22}$.

### Basic properties

Let $A$ be an $n \times n$ matrix over a field $F$.

- Each polynomial $p(A) = c_0 I + c_1 A + \dots + c_k A^k$ commutes with $A$. The reason is $A \cdot A^j = A^{j + 1} = A^j \cdot A$ for each $j$.
- The matrices that commute with $A$ form a subspace that is closed under products, the [[centraliser|02YYV36BFM]] of $A$.
- The matrices that commute with every $n \times n$ matrix are the [[scalar matrices|~30ae7883]].
- If $AB = BA$, then the [[binomial theorem|~af4d44e0]] gives $(A + B)^m = \sum_{k = 0}^{m} \binom{m}{k} A^k B^{m - k}$.
- If $AB = BA$ and $A$ and $B$ are [[nilpotent|07BSPZPSMF]], then $A + B$ is nilpotent, by the binomial theorem.
- Commuting is not transitive: $I$ commutes with every matrix, but not every two matrices commute.

### Common eigenvectors

Over $\mathbb{C}$, two commuting matrices $A$ and $B$ have a common [[eigenvector|0N6960W0BV]].
The reason uses only one step of algebra: if $Av = \lambda v$, then $A(Bv) = BAv = \lambda Bv$.
So each eigenspace of $A$ is an [[invariant subspace|0ACX5QT8TE]] of $B$, and $B$ has an eigenvector in it.
For diagonalisable matrices, commuting is equivalent to [[simultaneous diagonalisation|0FK17N4DKA]].
Eigenvectors and diagonalisation are treated in later parts of linear algebra.

### Common errors

- Using $(A + B)^2 = A^2 + 2AB + B^2$ without checking that $AB = BA$.
- Using $(AB)^{-1} = A^{-1} B^{-1}$; the correct rule is $(AB)^{-1} = B^{-1} A^{-1}$, and the two agree only when $A$ and $B$ commute.

## Explanations

### L1 human

For numbers, the order of a product never matters, but for matrices it usually does.
Matrices that commute are the pairs for which the order does not matter.
As maps, applying $A$ then $B$ gives the same result as applying $B$ then $A$.
For example, every matrix commutes with itself, with its powers, and with every [[scalar matrix|067NKSBEWT]] $cI$.
The matrices $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ and $\begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$ do not commute.

### L2 human

The matrix $AB - BA$ measures the failure of $A$ and $B$ to commute.
Its [[trace|07PTPSZPME]] is always $0$, by the [[cyclic property|0Y4NF1DRKD]].
So no two matrices over $\mathbb{R}$ have $AB - BA = I$, by [[this theorem|~94d188c9]].

### L3 human

The matrices that commute with a fixed matrix $A$ over a field form a subalgebra of $M_n(F)$.
This subalgebra equals the set of polynomials in $A$ exactly when the minimal polynomial of $A$ equals its characteristic polynomial.
Then $A$ is called nonderogatory.
