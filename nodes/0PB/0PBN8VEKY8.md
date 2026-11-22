---
tag: 0PBN8VEKY8
kind: concept
name: Annihilating polynomial
aliases: [annihilating-polynomials, annihilator-of-an-endomorphism]
msc: ["15A18"]
topics: [6R1D6QPY3S]
audience: ug2
uses: [0E3MV6E6MG]
sources:
  - url: https://en.wikipedia.org/wiki/Minimal_polynomial_(linear_algebra)
    locator: Formal definition
  - book: isbn:9780135367971
---

## Summary

An annihilating polynomial of a linear map is a polynomial equation that the map satisfies, such as $T^2 = T$ or $T^3 = 0$.
Such an equation limits what the map can do, and in particular it limits its eigenvalues to the roots of the polynomial.
Let $T$ be an endomorphism of a vector space $V$ over a field $F$.
A polynomial $p \in F[x]$ *annihilates* $T$ when
$$p(T) = 0,$$
where $p(T)$ is the [[value of p at T|0E3MV6E6MG]], and the zero on the right is the zero map of $V$.
The annihilating polynomials of $T$ form an ideal $I_T$ of $F[x]$, and the [[formal definition|052M4SX57M]] states the definition for maps and for matrices.
When $V$ is finite-dimensional, $I_T$ is not zero, and its monic generator is the [[minimal polynomial|03NDVCSHSB]].

## Motivation

A single polynomial relation can tell you a lot about a map.
If a matrix satisfies $A^2 = A$, then each eigenvalue $\lambda$ satisfies $\lambda^2 = \lambda$, so it is $0$ or $1$, and you know this before you compute any eigenvector.
The same relation lets you reduce every power: $A^3 = A \cdot A^2 = A^2 = A$, and so on.

Relations of this kind appear all over linear algebra.
A projection satisfies $P^2 = P$, a reflection satisfies $R^2 = I$, and a nilpotent map satisfies $N^k = 0$ for some $k$.
The [[Cayley-Hamilton theorem|0F765KFC2J]] says that every square matrix satisfies its own characteristic polynomial, so every matrix has a relation of degree $n$.
Later, the shortest relation, the minimal polynomial, decides whether a map can be diagonalized.

## Notation

The ideal of annihilating polynomials is written $I_T$, $\operatorname{Ann}(T)$ or $\ker(\operatorname{ev}_T)$, where $\operatorname{ev}_T \colon F[x] \to \operatorname{End}_F(V)$ sends $p$ to $p(T)$.
In a polynomial such as $x^2 - x - 2$, the constant term turns into a multiple of the identity, so $p(T) = T^2 - T - 2I$.
Some books write the constant as $2$ and mean $2I$; read it that way.

## Remarks

### A first check by hand

Take $A = \begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix}$ and $p(x) = x^2 - 5x + 6$.
First compute the square:
$$A^2 = \begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix} \begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix} = \begin{pmatrix} 4 & 5 \\ 0 & 9 \end{pmatrix}.$$
Then put everything together entry by entry:
$$A^2 - 5A + 6I = \begin{pmatrix} 4 - 10 + 6 & 5 - 5 \\ 0 & 9 - 15 + 6 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}.$$
So $p$ annihilates $A$.
Since $p(x) = (x - 2)(x - 3)$, the eigenvalues of $A$ can only be $2$ or $3$, and indeed they are the diagonal entries $2$ and $3$ of the triangular matrix $A$.

### Relations that come from geometry

The [[projection of the plane|F5TTF31NR5]] $P = \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}$ satisfies $P^2 = P$, because projecting twice is the same as projecting once.
So $x^2 - x$ annihilates $P$, and so does every multiple of it, such as $x^3 - x = (x + 1)(x^2 - x)$.

The reflection $R = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ swaps the two coordinates, so doing it twice gives back every vector.
This means $R^2 = I$, and $x^2 - 1$ annihilates $R$.

The shift $N$ with $N e_1 = 0$, $N e_2 = e_1$ and $N e_3 = e_2$ moves each basis vector one step down the chain.
After three steps every vector is $0$, so $x^3$ annihilates $N$, as the [[example of a diagonal and a nilpotent matrix|APPAHXTJ6C]] works out.

### The rules you can use

The set $I_T$ is closed under addition, and under multiplication by every polynomial, because evaluation at $T$ respects sums and products.
So $I_T$ is an ideal, by the theorem that [[the ideal of annihilating polynomials is nonzero and principal|AH34SFJ8SF]].
The same theorem shows that $I_T \ne 0$ when $\dim V = n$ is finite: the $n^2 + 1$ maps $I, T, \dots, T^{n^2}$ lie in a space of dimension $n^2$, so they are linearly dependent.

Every annihilating polynomial vanishes at every eigenvalue.
If $T v = \lambda v$ with $v \ne 0$, then $T^k v = \lambda^k v$ for each $k$, so
$$0 = p(T) v = p(\lambda) v,$$
and $p(\lambda) = 0$ because $v \ne 0$.
Similar matrices have the same annihilating polynomials, because $p(S A S^{-1}) = S\, p(A)\, S^{-1}$.

### What it is not

A polynomial that kills one vector need not kill the map.
For the [[shear|HTAWRAC3QE]] $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$, the matrix $A - I$ sends $e_1$ to $0$ but sends $e_2$ to $e_1$.
So $x - 1$ is not an annihilating polynomial of $A$, as the [[non-example on one vector|BF2G985KRZ]] shows, although $(x - 1)^2$ is.

In infinite dimension there may be no annihilating polynomial except $0$.
The [[derivative on smooth functions|1SKH5XJ5RB]] has every real number $\lambda$ as an eigenvalue, with the eigenvector $e^{\lambda x}$.
A nonzero $p$ with $p(D) = 0$ would vanish at every real number, and a nonzero polynomial has only finitely many roots.

### Watch out

An annihilating polynomial can have roots that are not eigenvalues.
The matrix $A$ of the first check is also annihilated by $(x - 2)(x - 3)(x - 7)$, since it is a multiple of $(x - 2)(x - 3)$, but $7$ is not an eigenvalue of $A$.
So the roots of an annihilating polynomial give a list of candidates, and you still have to test each one.
Only for the minimal polynomial are the roots exactly the eigenvalues.

### History

Hoffman and Kunze build their account of the minimal polynomial on the ideal of annihilating polynomials, and many later books follow this order.

### Try it

First, show that $x^2 + 1$ annihilates $J = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$.
The square is $J^2 = \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix} = -I$, so $J^2 + I = 0$.

Second, a matrix satisfies $A^2 = 2A$; which eigenvalues are possible?
The polynomial $x^2 - 2x = x(x - 2)$ annihilates $A$, so every eigenvalue is $0$ or $2$.

Third, does $x - 2$ annihilate $\operatorname{diag}(2, 3)$?
No, because $\operatorname{diag}(2, 3) - 2I = \operatorname{diag}(0, 1) \ne 0$.

## Explanations

### L1 human

Think of a machine that moves vectors, and suppose that running it twice gives the same result as running it once.
Then the machine satisfies the equation "twice equals once", which we write $T^2 = T$, or $T^2 - T = 0$.
The polynomial $x^2 - x$ is called an annihilating polynomial, because putting the machine into it gives zero.
A stretch factor $\lambda$ of the machine must satisfy the same equation, $\lambda^2 = \lambda$.
So the only possible stretch factors are $0$ and $1$.

### L2 human

Here is a typical use: find the eigenvalues of $A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$ from a relation.
Compute the square:
$$A^2 = \begin{pmatrix} 1 + 4 & 2 + 8 \\ 2 + 8 & 4 + 16 \end{pmatrix} = \begin{pmatrix} 5 & 10 \\ 10 & 20 \end{pmatrix} = 5A.$$
So $x^2 - 5x = x(x - 5)$ annihilates $A$, and every eigenvalue is $0$ or $5$.
Both occur, because $A (2, -1)^{\mathsf{T}} = (0, 0)^{\mathsf{T}}$ and $A (1, 2)^{\mathsf{T}} = (5, 10)^{\mathsf{T}} = 5 (1, 2)^{\mathsf{T}}$.
Check: the trace is $5 = 0 + 5$ and the determinant is $4 - 4 = 0 = 0 \cdot 5$.
The relation $A^2 = 5A$ came from noticing that $A$ has rank $1$, and it gave the eigenvalues with no determinant at all.

### L3 human

The ideal $I_T$ is the kernel of the evaluation homomorphism $F[x] \to \operatorname{End}_F(V)$, and its image is the commutative algebra $F[T]$, so $F[T] \cong F[x]/I_T$.
In the language of modules, $V$ is a module over $F[x]$ with $x$ acting as $T$, and $I_T$ is the annihilator of this module.
For an element $a$ of any finite-dimensional algebra over $F$, the same kernel is nonzero, and in a finite field extension this is the reason that every element is [[algebraic|0VX9EP2GS8]].
The sub-area on [[canonical forms under similarity|GEBYZKYV3D]] uses $I_T$ and the module structure to classify maps up to similarity.
