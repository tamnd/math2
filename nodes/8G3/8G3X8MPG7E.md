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

Two matrices commute when the order in which we multiply them does not matter.
Exactly, [[square matrices|0JXZKX526R]] $A$ and $B$ of the same size commute when
$$AB = BA,$$
and the [[formal definition|MX26N71ZD3]] states this over any commutative ring.
[[Matrix multiplication|032Q9FB8MT]] is [[not commutative|0P506SPZP2]] in general, so commuting pairs are special, and for them the algebra of numbers works again: the [[binomial theorem|DS9TS6AFMW]] holds, and $e^{A + B} = e^{A} e^{B}$ by [[the exponential rule for commuting matrices|04BD23PSK5]].
Over $\mathbb{C}$, commuting matrices also share an eigenvector.

## Motivation

Many rules of school algebra use $ab = ba$ without saying so, such as $(a + b)^2 = a^2 + 2ab + b^2$, $(ab)^n = a^n b^n$ and $a^2 - b^2 = (a - b)(a + b)$.
For matrices, each of these rules can fail, and it holds when the two matrices commute.
So commuting is the condition to check before we use such a rule.

As maps, $AB = BA$ says that applying $B$ and then $A$ has the same effect as applying $A$ and then $B$.
Scaling the plane by the same factor in every direction and then rotating it gives the same result as rotating and then scaling, but a shear and a rotation in general give different results in the two orders.
In quantum mechanics, two observables can be measured together exactly when their matrices commute.

## Notation

The condition $AB = BA$ is often written $[A, B] = 0$, where $[A, B] = AB - BA$ is the [[commutator|0PXW0BN7DW]].
In Mathlib, `Commute A B` means `A * B = B * A`, for elements of any semigroup.

## Remarks

### First examples

Every matrix commutes with itself, with its powers, with $I$ and with every [[scalar matrix|067NKSBEWT]] $cI$.
Two [[diagonal matrices|0Q9PGXD9E4]] of the same size commute, because their products are computed entry by entry on the diagonal.
More generally, [[a polynomial in A commutes with A|BSTF110SFK]], since $A \cdot A^j = A^{j + 1} = A^j \cdot A$ for each $j$.

A less obvious pair is worked out in [[two upper triangular 2 × 2 matrices that commute|EVM25ZY7BV]]:
$$\begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 3 & 5 \\ 0 & 3 \end{pmatrix} = \begin{pmatrix} 3 & 11 \\ 0 & 3 \end{pmatrix} = \begin{pmatrix} 3 & 5 \\ 0 & 3 \end{pmatrix} \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}.$$

### What it is not

The [[matrix units|A4HTT7JFD1]] $E_{12}$ and $E_{21}$ do not commute, since $E_{12} E_{21} = E_{11}$ but $E_{21} E_{12} = E_{22}$.
The shears $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ and $\begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$ do not commute either, and for them [[the square formula fails|60W7PZXBVB]].
Commuting is not transitive: $I$ commutes with every matrix, but not every two matrices commute.

### The rules you can use

Let $A$ be an $n \times n$ matrix over a field $F$.
The matrices that commute with $A$ form a subspace that is closed under products, the [[centralizer|02YYV36BFM]] of $A$, and it contains every polynomial in $A$.
The matrices that commute with every $n \times n$ matrix are exactly [[the scalar matrices|TX4J5JR205]].
If $AB = BA$ and both are [[nilpotent|07BSPZPSMF]], then $A + B$ is nilpotent, by the binomial theorem.
If $A$ is invertible, it commutes with $A^{-1}$, since $A A^{-1} = I = A^{-1} A$.

### Common eigenvectors

Suppose $AB = BA$ and $Av = \lambda v$.
Then
$$A(Bv) = B(Av) = \lambda (Bv),$$
so $B$ maps the $\lambda$ [[eigenspace|0N6960W0BV]] of $A$ into itself; it is an [[invariant subspace|0ACX5QT8TE]] of $B$.
Over $\mathbb{C}$, $B$ has an eigenvector inside it, and that vector is an eigenvector of both matrices.
For diagonalizable matrices, commuting is equivalent to [[simultaneous diagonalization|0FK17N4DKA]].

For example, $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ and $S = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ commute, since $A = 2I + S$.
They share the eigenvectors $(1, 1)$, with $A$ giving $3$ and $S$ giving $1$, and $(1, -1)$, with $A$ giving $1$ and $S$ giving $-1$.

### Watch out

Do not expand $(A + B)^2$ as $A^2 + 2AB + B^2$ before checking that $AB = BA$; in general it is $A^2 + AB + BA + B^2$.
The inverse of a product is $(AB)^{-1} = B^{-1} A^{-1}$, and this equals $A^{-1} B^{-1}$ only when $A$ and $B$ commute.
Similarly, $e^{A + B} = e^A e^B$ can fail for matrices that do not commute.

### History

In 1884 Sylvester studied the matrix equation $px = xq$; the case $p = q$ asks for the matrices that commute with a given one.

### Try it

First, which $2 \times 2$ matrices commute with $D = \operatorname{diag}(1, 2)$?
For $X = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ we get $DX = \begin{pmatrix} a & b \\ 2c & 2d \end{pmatrix}$ and $XD = \begin{pmatrix} a & 2b \\ c & 2d \end{pmatrix}$.
So $b = 2b$ and $2c = c$, which force $b = c = 0$: exactly the diagonal matrices.

Second, does every matrix commute with its transpose?
No: $E_{21} = E_{12}^{\mathsf{T}}$, and $E_{12} E_{21} = E_{11}$ differs from $E_{21} E_{12} = E_{22}$.

## Explanations

### L1 human

For numbers, the order of a product never matters: $3 \cdot 5 = 5 \cdot 3$.
For matrices it usually does, and matrices that commute are the pairs for which it does not.
Think of putting on socks and shoes: the order matters, so those two actions do not commute.
Putting on a hat and putting on gloves can be done in either order, so those two do.

### L2 human

The matrix $AB - BA$ measures how far $A$ and $B$ are from commuting.
For $E_{12}$ and $E_{21}$ it is
$$E_{12} E_{21} - E_{21} E_{12} = E_{11} - E_{22} = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}.$$
Its [[trace|07PTPSZPME]] is $0$, and this is always so, by the [[cyclic property|0Y4NF1DRKD]] $\operatorname{tr}(AB) = \operatorname{tr}(BA)$.
Since $\operatorname{tr} I_n = n \ne 0$ over $\mathbb{R}$, no two real matrices satisfy $AB - BA = I$, as [[this theorem|E2P5TNE0G9]] shows.

### L3 human

The centralizer of $A$ in $M_n(F)$ is a subalgebra of dimension at least $n$.
It equals the algebra $F[A]$ of polynomials in $A$ exactly when the minimal polynomial of $A$ equals its characteristic polynomial, and then $A$ is called nonderogatory.
For example, $\operatorname{diag}(1, 2)$ is nonderogatory, and its centralizer is the $2$-dimensional algebra of diagonal matrices, while the centralizer of $I$ is all of $M_n(F)$.
