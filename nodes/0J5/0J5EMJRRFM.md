---
tag: 0J5EMJRRFM
kind: concept
name: Characteristic polynomial of a linear map
msc: ["15A04", "15A18"]
topics: [6R1D6QPY3S]
audience: ug2
uses: [0VSSPAFM2C, 0J7H0YBFDJ, 0YQSGNYE3K, 0E89HQATM8]
sources:
  - url: https://en.wikipedia.org/wiki/Characteristic_polynomial
    locator: Formal definition
  - url: https://en.wikipedia.org/wiki/Cayley%E2%80%93Hamilton_theorem
    locator: lead section
  - book: isbn:9780134860244
  - book: isbn:9780135367971
---

## Summary

A linear map from a space to itself has many matrices, one for each basis, but all of them have the same characteristic polynomial.
So the polynomial belongs to the map, and its roots are the eigenvalues of the map.
Let $F$ be a field, let $V$ be a vector space over $F$ of dimension $n \ge 1$, and let $T \colon V \to V$ be an [[endomorphism|0J7H0YBFDJ]].
The *characteristic polynomial* of $T$ is
$$p_T(t) = \det\big(t I_n - [T]_B\big),$$
the [[characteristic polynomial|0VSSPAFM2C]] of the [[matrix of T|0YQSGNYE3K]] in a basis $B$ of $V$, with the same basis on both sides.
It does not depend on $B$, because two such matrices are [[similar|0E89HQATM8]].
The [[formal definition|0BZ81AJNWF]] states it.

## Motivation

An eigenvalue of $T$ is defined without any basis: $\lambda$ is an eigenvalue when $T(v) = \lambda v$ for some $v \ne 0$.
A polynomial that finds the eigenvalues should therefore not depend on a basis either.
The theorem on the [[characteristic polynomial of an endomorphism|C98TZ6ZAXC]] shows that every basis gives the same polynomial, so $p_T$ is a property of $T$ alone.

This has a practical side.
You may compute $p_T$ in whichever basis makes the matrix simplest, for example a basis in which the matrix is triangular.
It also makes the trace, the determinant and the algebraic multiplicities into invariants of the map, and the [[Cayley-Hamilton theorem for linear maps|0QEM68Y0DE]] says that $p_T(T) = 0$.

## Notation

Books write $p_T$, $\chi_T$ or $c_T$, the same symbols as for matrices.
Mathlib writes `LinearMap.charpoly T`, for an endomorphism of a finite free module over a commutative ring.
The notation hides the basis on purpose, since the result does not depend on it.

## Remarks

### One map in two bases

Let $T(x, y) = (y, x)$ on $\mathbb{R}^2$, the reflection in the line $y = x$.
In the standard basis, $T(1, 0) = (0, 1)$ and $T(0, 1) = (1, 0)$, so
$$[T] = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad p(t) = t^2 - 1.$$
Now take the basis $b_1 = (1, 1)$, $b_2 = (1, -1)$.
Then $T(b_1) = (1, 1) = b_1$ and $T(b_2) = (-1, 1) = -b_2$, so
$$[T]_B = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}, \qquad p(t) = (t - 1)(t + 1) = t^2 - 1.$$
The matrices differ, and the polynomial is the same, as the theorem promises.
The second basis is better, because there the eigenvalues $1$ and $-1$ can be read off the diagonal.

### More examples

[[The rotation of the plane by the angle theta|5AE98D7959]] has $p_T(t) = t^2 - 2 \cos\theta \, t + 1$ in every basis.
A [[projection of the plane|F5TTF31NR5]] onto one line along another line has $p_T(t) = t(t - 1)$, since in a basis made of one vector from each line its matrix is $\operatorname{diag}(1, 0)$.

[[The derivative on polynomials of degree at most 2|1SKH5XJ5RB]] has $D(1) = 0$, $D(x) = 1$ and $D(x^2) = 2x$.
Its matrix in the basis $1, x, x^2$ is strictly upper triangular, so $p_D(t) = t^3$.
The identity of $V$ has $p(t) = (t - 1)^n$, and the zero map has $p(t) = t^n$.

### What it is not

The [[left shift on all sequences|HBVWZ0FXWC]] has no characteristic polynomial, because the space of sequences has infinite dimension and there is no determinant.
Nothing could replace it either: over $\mathbb{R}$ every real number is an eigenvalue of the left shift, and a nonzero polynomial has only finitely many roots.

A linear map $V \to W$ between two different spaces has no characteristic polynomial.
Its matrix need not be square, and even when $\dim V = \dim W$ there is no natural way to compare a vector with its image.

### The rules you can use

The polynomial $p_T$ is monic of degree $n = \dim V$.
Its roots in $F$ are the eigenvalues of $T$, by the theorem that [[eigenvalues are the roots of the characteristic polynomial|053QVHF6N7]].
The coefficient of $t^{n-1}$ is $-\operatorname{tr} T$, with the [[trace of the linear map|0KZDNGA561]], and the constant term is $(-1)^n \det T$.
If $U$ is a $T$-invariant subspace, then $p_{T|_U}$ divides $p_T$, and if $V = U \oplus W$ with both parts invariant, then $p_T = p_{T|_U} \, p_{T|_W}$, by the theorem on the [[characteristic polynomial of an endomorphism|C98TZ6ZAXC]].

### Watch out

The definition uses the same basis $B$ for the input and the output of $T$.
If you use one basis for the input and another for the output, you get a matrix $[T]_{C \leftarrow B}$ whose characteristic polynomial can change.
For example, the identity of $\mathbb{R}^2$ with the input basis $((2, 0), (0, 1))$ and the standard output basis has the matrix $\operatorname{diag}(2, 1)$.
Its polynomial $(t - 2)(t - 1)$ is not the polynomial $(t - 1)^2$ of the identity.

### Try it

First, find $p_T$ for $T(x, y) = (x + y, y)$ on $\mathbb{R}^2$.
The matrix in the standard basis has rows $(1, 1)$ and $(0, 1)$, which is triangular, so $p_T(t) = (t - 1)^2$.

Second, let $T$ be the reflection of $\mathbb{R}^3$ in a plane through $0$; find $p_T$ without coordinates.
Take two vectors in the plane and one normal vector as a basis; then $[T] = \operatorname{diag}(1, 1, -1)$, so $p_T(t) = (t - 1)^2 (t + 1)$.

## Explanations

### L1 human

A linear map can be written down as a matrix once you choose axes.
Different axes give different tables of numbers for the same map.
The characteristic polynomial is a summary that comes out the same for every choice.
For the mirror that swaps $x$ and $y$ it is always $t^2 - 1$, whose roots $1$ and $-1$ say that some arrows stay and some arrows flip.

### L2 human

Here is a typical use: find $p_T$ for the map $T(p) = p(x + 1)$ on the polynomials of degree at most $2$.
In the basis $1, x, x^2$ we have $T(1) = 1$, $T(x) = x + 1$ and $T(x^2) = x^2 + 2x + 1$.
The coordinate columns give
$$[T] = \begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 2 \\ 0 & 0 & 1 \end{pmatrix},$$
which is upper triangular with $1$ on the diagonal, so $p_T(t) = (t - 1)^3$.
So $1$ is the only eigenvalue, and the constant polynomials are eigenvectors, since shifting $x$ does not change a constant.
The lesson is to pick a basis that makes the matrix triangular, and then read $p_T$ from the diagonal.

### L3 human

For an endomorphism $T$ of a finite free module $V$ over a commutative ring $K$, $p_T$ is the determinant of $t - T$ acting on $K[t] \otimes_K V$, which needs no basis at all.
Over a field, $V$ is a finitely generated torsion module over $F[t]$, with $t$ acting as $T$.
Then $p_T$ is the product of the invariant factors of this module, and the [[minimal polynomial|03NDVCSHSB]] is the largest of them.
The sub-areas on diagonalization and on canonical forms read the structure of $T$ from these factors.
