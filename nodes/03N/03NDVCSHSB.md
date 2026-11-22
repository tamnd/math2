---
tag: 03NDVCSHSB
kind: concept
name: Minimal polynomial
aliases: [minimal-polynomial-of-an-endomorphism, minimal-polynomial-of-a-matrix]
msc: ["15A18"]
topics: [6R1D6QPY3S]
audience: ug2
specializes: [0PBN8VEKY8]
uses: [0PBN8VEKY8, 0E3MV6E6MG]
sources:
  - url: https://en.wikipedia.org/wiki/Minimal_polynomial_(linear_algebra)
    locator: Formal definition
  - book: isbn:9780135367971
  - book: isbn:9783031410253
    locator: Chapter 5
same_as:
  wikidata: Q1163608
  wikipedia: Minimal polynomial (linear algebra)
---

## Summary

The minimal polynomial of a linear map is the shortest polynomial equation that the map satisfies.
It is a compact record of the map: its roots are the eigenvalues, and its factors tell you whether the map can be diagonalized.
Let $T$ be an endomorphism of a finite-dimensional vector space $V$ over a field $F$.
The *minimal polynomial* $m_T \in F[x]$ is the monic polynomial of least degree with
$$m_T(T) = 0.$$
Equivalently, it is the monic generator of the ideal of [[annihilating polynomials|0PBN8VEKY8]] of $T$, so every polynomial that annihilates $T$ is a multiple of $m_T$.
For an $n \times n$ matrix $A$, the minimal polynomial $m_A$ is that of the map $x \mapsto Ax$, and the [[formal definition|0V58FPM3EQ]] states both versions.

## Motivation

The characteristic polynomial lists the eigenvalues with their algebraic multiplicities, but it cannot tell the identity $I_2$ from the shear $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$: both have $(x - 1)^2$.
The minimal polynomial tells them apart.
The identity satisfies $I - I = 0$, so $m = x - 1$, while the shear needs the square, so $m = (x - 1)^2$.
The repeated factor is the trace of the fact that the shear is not diagonalizable.

This is the main use of the idea.
A map is diagonalizable [[exactly when its minimal polynomial splits into distinct linear factors|0MPAJRB23T]], and the sub-area on [[diagonalization|Z6S6PWMJPH]] builds on this.
The minimal polynomial also turns high powers $T^k$ and the inverse $T^{-1}$ into polynomials in $T$ of low degree, and in the sub-area on [[canonical forms|GEBYZKYV3D]] it gives the size of the largest Jordan block of each eigenvalue.

## Notation

Books write $m_T$, $\mu_T$ or $\min_T$, and $m_A$ or $\mu_A$ for a matrix.
Mathlib writes `minpoly F T`.
The theorem that [[the ideal of annihilating polynomials is nonzero and principal|AH34SFJ8SF]] shows that $m_T$ exists and is unique, so the article "the" is justified.
Field theory uses the same name for the [[minimal polynomial of an algebraic element|0H628RSGWX]], and the two ideas agree when $T$ is viewed as an element of the algebra $\operatorname{End}_F(V)$.

## Remarks

### A first computation

Take $A = \begin{pmatrix} 2 & 0 & 0 \\ 0 & 2 & 1 \\ 0 & 0 & 2 \end{pmatrix}$.
It is triangular with diagonal $2, 2, 2$, so its characteristic polynomial is $(x - 2)^3$, and its minimal polynomial is a monic divisor of it with the root $2$.
So $m_A$ is $x - 2$, $(x - 2)^2$ or $(x - 2)^3$.
The first candidate fails, since
$$A - 2I = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix} \ne 0.$$
This matrix sends $e_3$ to $e_2$ and sends $e_1$ and $e_2$ to $0$, so its square sends every basis vector to $0$, and $(A - 2I)^2 = 0$.
So $m_A = (x - 2)^2$, of degree $2$, while the characteristic polynomial has degree $3$.

### More examples

For a diagonal matrix, each distinct diagonal entry gives one factor.
The [[diagonal and nilpotent example|APPAHXTJ6C]] shows that $\operatorname{diag}(1, 1, 2)$ has $m = (x - 1)(x - 2)$, because
$$(D - I)(D - 2I) = \operatorname{diag}(0, 0, 1) \operatorname{diag}(-1, -1, 0) = 0,$$
while neither factor alone kills $D$.
The same page shows that the $3 \times 3$ shift $N$, with $N e_1 = 0$, $N e_2 = e_1$ and $N e_3 = e_2$, has $m = x^3$, since $N^2 \ne 0$ and $N^3 = 0$.

The [[matrix with 4 on the diagonal and 1 elsewhere|7XFGVVTZ2X]] is $A = 3I + J$, where $J$ is the $3 \times 3$ matrix of ones.
Since $J^2 = 3J$, we get
$$(A - 3I)(A - 6I) = J(J - 3I) = J^2 - 3J = 0,$$
so $m_A = (x - 3)(x - 6)$, while $p_A = (x - 3)^2 (x - 6)$.
A [[projection of the plane|F5TTF31NR5]] other than $0$ and $I$ has $m = x^2 - x$, and the [[shear|HTAWRAC3QE]] has $m = (x - 1)^2$.

### The rules you can use

Every annihilating polynomial is a multiple of $m_T$, by the theorem that the [[minimal polynomial divides every annihilating polynomial|0VTAD25A3G]].
So once you know one polynomial $p$ with $p(T) = 0$, you only have to test the monic divisors of $p$.
The [[Cayley-Hamilton theorem|0F765KFC2J]] gives one such $p$, the characteristic polynomial, so $m_T$ [[divides the characteristic polynomial|093X6MN6Y6]] and $\deg m_T \le \dim V$.

The roots of $m_T$ in $F$ are exactly the eigenvalues of $T$, by the theorem that the [[eigenvalues are the roots of the minimal polynomial|0QF4ZEFG52]].
In particular, $T$ is invertible exactly when $m_T(0) \ne 0$.
The degree of $m_T$ is the dimension of the algebra $F[T]$ of polynomials in $T$.
Similar matrices have the same minimal polynomial, because $p(S A S^{-1}) = S\, p(A)\, S^{-1}$ for every polynomial $p$.

### What it is not

The [[identity matrix of size 2|MSQTBBM86Q]] is annihilated by its characteristic polynomial $(x - 1)^2$, but that is not its minimal polynomial, since $x - 1$ already annihilates $I_2$ and has smaller degree.
The polynomial $2x - 2$ also annihilates $I_2$ and has the least degree, but it is not monic, so it is not the minimal polynomial either.
The minimal polynomial is not the product of $x - \lambda$ over the distinct eigenvalues in general: for the shear this product is $x - 1$, and it does not annihilate the shear.

### Watch out

Do not assume that $m_T = p_T$.
They agree for the shear, but they differ for the identity and for $3I + J$ above.
Do not read the exponent of $x - \lambda$ in $m_T$ as the algebraic multiplicity of $\lambda$.
For the matrix of the first computation, the eigenvalue $2$ has algebraic multiplicity $3$, but the exponent in $m_A$ is $2$, which is the size of its largest Jordan block.

### History

Hoffman and Kunze define the minimal polynomial as the monic generator of the ideal of annihilating polynomials.
Axler, in *Linear Algebra Done Right*, introduces it before determinants and uses it in place of the characteristic polynomial to find eigenvalues.

### Try it

First, find the minimal polynomial of $R = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$.
Since $R^2 = I$, it divides $x^2 - 1$, and neither $R - I$ nor $R + I$ is zero, so $m_R = x^2 - 1$.

Second, find the minimal polynomial of $5 I_3$.
It is $x - 5$, because $5I_3 - 5I_3 = 0$ and no constant other than $0$ annihilates a map.

Third, find the minimal polynomial of $B = \begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix}$.
Both $1$ and $2$ are eigenvalues, so both $x - 1$ and $x - 2$ divide $m_B$, and $m_B$ divides the characteristic polynomial $(x - 1)(x - 2)$, so $m_B = (x - 1)(x - 2)$.

## Explanations

### L1 human

A square matrix satisfies many equations, such as $A^2 - 5A + 6I = 0$.
Among all of them, take the shortest one whose leading coefficient is $1$.
That is the minimal polynomial.
Every other equation that the matrix satisfies is a multiple of it, in the same way as every number in the list $6, 12, 18, \dots$ is a multiple of the smallest one.
Its roots are exactly the stretch factors of the matrix, the eigenvalues.

### L2 human

Here is a typical use: is $A = \begin{pmatrix} 3 & 1 \\ -1 & 1 \end{pmatrix}$ diagonalizable?
The characteristic polynomial is
$$\det(xI - A) = (x - 3)(x - 1) + 1 = x^2 - 4x + 4 = (x - 2)^2.$$
So $m_A$ is $x - 2$ or $(x - 2)^2$.
The matrix $A - 2I = \begin{pmatrix} 1 & 1 \\ -1 & -1 \end{pmatrix}$ is not zero, so $m_A = (x - 2)^2$.
Check: $(A - 2I)^2 = \begin{pmatrix} 1 - 1 & 1 - 1 \\ -1 + 1 & -1 + 1 \end{pmatrix} = 0$.
The repeated factor shows that $A$ is not diagonalizable.
Watch out: the shortcut "test only the divisors of $p_A$" rests on the Cayley-Hamilton theorem, so cite it when you use it.

### L3 human

View $V$ as a module over $F[x]$, with $x$ acting as $T$.
Then $m_T$ generates the annihilator of this module, and in the invariant factor decomposition $V \cong \bigoplus_{i=1}^{k} F[x]/(a_i)$ with $a_1 \mid a_2 \mid \dots \mid a_k$, it is the largest factor $a_k$.
The characteristic polynomial is the product $a_1 \cdots a_k$, which gives a second proof that $m_T$ divides $p_T$ and that $p_T$ divides $m_T^k$.
This is the theory of [[modules over a principal ideal domain|WKJXXX0DYG]], and it leads to the rational and Jordan canonical forms.
