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

Let $T \colon V \to V$ be an [[endomorphism|0J7H0YBFDJ]] of a vector space $V$ of dimension $n \ge 1$ over a field $F$.
The characteristic polynomial $p_T$ of $T$ is the [[characteristic polynomial|0VSSPAFM2C]] of the [[matrix of $T$|0YQSGNYE3K]] in a basis of $V$.
It does not depend on the basis, because the matrices of $T$ in two bases are [[similar|0E89HQATM8]].
It is monic of degree $n$, its roots in $F$ are the eigenvalues of $T$, and it is multiplicative on invariant direct sums.

## Motivation

The eigenvalues of $T$ do not depend on a basis, so a polynomial that finds them should not depend on one either.
The theorem on the [[characteristic polynomial of an endomorphism|C98TZ6ZAXC]] shows that each basis gives the same polynomial.
This makes the trace, the determinant and the algebraic multiplicities invariants of the map $T$ itself.

## Notation

The formal definition is the [[definition of the characteristic polynomial of a linear map|0BZ81AJNWF]].
Common symbols are $p_T$, $\chi_T$ and $c_T$.
Mathlib writes `LinearMap.charpoly T`, for an endomorphism of a finite free module over a commutative ring.

## Remarks

### Examples

- [[A rotation of the plane|5AE98D7959]] by the angle $\theta$ has $p_T(t) = t^2 - 2 \cos\theta \, t + 1$, in the standard basis and in each other basis.
- [[A projection of the plane|F5TTF31NR5]] onto a line along another line has $p_T(t) = t(t - 1)$.
- [[The derivative on polynomials of degree at most 2|1SKH5XJ5RB]] has $p_D(t) = t^3$, because its matrix in the basis $1, x, x^2$ is strictly upper triangular.
- The identity of $V$ has $p(t) = (t - 1)^n$, and the zero map has $p(t) = t^n$.

### Non-examples

- [[The left shift on all sequences|HBVWZ0FXWC]] has no characteristic polynomial: every scalar is an eigenvalue, and a nonzero polynomial has finitely many roots.
- A linear map $V \to W$ with $V \ne W$ has a matrix that need not be square, and it has no characteristic polynomial.

### Basic properties

- $p_T$ does not depend on the basis, is monic of degree $n$, and is multiplicative on invariant direct sums, by the theorem on the [[characteristic polynomial of an endomorphism|C98TZ6ZAXC]].
- If $U$ is a $T$-invariant subspace, then $p_{T|_U}$ divides $p_T$, by the same theorem.
- The roots of $p_T$ in $F$ are the eigenvalues of $T$, by the theorem that [[eigenvalues are the roots of the characteristic polynomial|053QVHF6N7]].
- The coefficient of $t^{n-1}$ is $-\operatorname{tr} T$, the [[trace of the linear map|0KZDNGA561]], and the constant term is $(-1)^n \det T$.
- $p_T(T) = 0$, by the [[Cayley-Hamilton theorem for linear maps|0QEM68Y0DE]].

### History

Cayley stated in 1858 that a matrix satisfies its own characteristic equation.
The characteristic polynomial of a linear map is well defined because similar matrices have the same characteristic polynomial.

### Common errors

- Using the matrices of $T$ in two different bases for the source and the target. The characteristic polynomial needs the same basis on both sides.
- Applying the definition in infinite dimension, where there is no determinant of $tI - T$.

## Explanations

### L1 human

A linear map has many matrices, one for each choice of basis.
These matrices look different, but they all have the same characteristic polynomial.
So the polynomial belongs to the map, not to one matrix.
Its roots are the stretch factors of the map.

### L2 human

We compute $p_T$ for the map $T(x, y) = (y, x)$ on $\R^2$ in two bases.

1. In the standard basis, $[T] = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, so $p_T(t) = t^2 - 1$.
2. In the basis $b_1 = (1, 1)$, $b_2 = (1, -1)$: $T(b_1) = b_1$ and $T(b_2) = (-1, 1) = -b_2$.
3. So $[T]_B = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$, and $p(t) = (t - 1)(t + 1) = t^2 - 1$.
4. The two bases give the same polynomial.

The typical use is to choose a basis in which the matrix is triangular or block triangular, and to read $p_T$ from it.
A trap: the matrices in the two bases are different, so only invariants such as $p_T$ can be compared.

### L3 human

For an endomorphism $T$ of a finite free module $V$ over a commutative ring $K$, $p_T$ is the determinant of $t - T$ acting on $K[t] \otimes_K V$.
For a field $K$, it is the product of the invariant factors of $V$ as a $K[t]$-module, while the [[minimal polynomial|03NDVCSHSB]] is the largest invariant factor.
