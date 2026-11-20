---
tag: 0X0HQYSZ0K
kind: concept
name: Determinant of a linear map
msc: [15A04, 15A15]
topics: [DTBK11SR77]
audience: ug2
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Determinant of an endomorphism
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: History
---

## Summary

The determinant of an endomorphism $T$ of a finite-dimensional vector space $V$ is the [[determinant|00KDZRW4C0]] of the matrix of $T$ in a basis of $V$.
The same basis is used for the domain and the codomain, and the [[definition|03F5KP94K0]] gives the details.
The value does not depend on the basis, so it is a property of $T$ itself; see the [[invariance statement|0KMN32XGPF]].
It tells whether $T$ is invertible, and it is multiplicative under composition.
Without a basis, $T$ acts on the top exterior power $\Lambda^n V$, which is a line, as multiplication by $\det T$.

## Motivation

Many linear maps come without a preferred basis, for example maps on spaces of polynomials or of matrices.
We want a number that measures the map and not the choice of coordinates.
A change of basis replaces the matrix of $T$ by a [[similar|0E89HQATM8]] matrix, and similar matrices have the same determinant.
So the determinant of any matrix of $T$ gives such a number.

## Notation

- $\det T$ or $\det(T)$ is the determinant of $T \colon V \to V$.
- $[T]_B$ is the [[matrix of $T$|0YQSGNYE3K]] in the basis $B$, used for both the domain and the codomain.
- $n = \dim V$, and $\Lambda^n V$ is the $n$-th exterior power of $V$.

## Remarks

### Examples

- $\det \operatorname{id}_V = 1$, and $\det(c \operatorname{id}_V) = c^n$ for a scalar $c$.
- The map $p(x) \mapsto p(2x)$ on polynomials of degree at most $2$ has determinant $8$: [[example|~1e526ee8]].
- The transpose map on $2 \times 2$ matrices has determinant $-1$: [[example|~f6e84b87]].
- The rotation of $\mathbb{R}^2$ by an angle $\theta$ has determinant $\cos^2 \theta + \sin^2 \theta = 1$.

### Non-examples

- A linear map $\mathbb{R}^2 \to \mathbb{R}^3$ has no determinant, because its matrices are not square: [[non-example|~884a037c]].
- For a map $V \to W$ between two different spaces of equal dimension, the determinant of its matrix depends on the two bases.
- The identity map of an infinite-dimensional space has no determinant in this sense, because it has no finite matrix.

### Basic properties

- $\det(S \circ T) = \det S \cdot \det T$ for endomorphisms $S$ and $T$ of $V$.
- $T$ is invertible if and only if $\det T \ne 0$, and then $\det(T^{-1}) = (\det T)^{-1}$.
- $\det T$ is the [[product of the eigenvalues|0C2F40MEBC]] of $T$ in an algebraic closure of $F$, counted with algebraic multiplicity.
- $\det T = (-1)^n \chi_T(0)$, where $\chi_T(x) = \det(x \operatorname{id}_V - T)$ is the [[characteristic polynomial|0J5EMJRRFM]].
- For a basis $v_1, \dots, v_n$, $T v_1 \wedge \dots \wedge T v_n = \det T \cdot v_1 \wedge \dots \wedge v_n$ in $\Lambda^n V$.
- The dual map $T^*$ has $\det T^* = \det T$, because its matrix in the dual basis is the [[transpose|0W809K6AW0]] of $[T]_B$.

### History

Determinants were used long before matrices.
A determinant was first a property of a system of linear equations.

### Common errors

- Using one basis for the domain and another for the codomain; the determinant of that matrix depends on the two bases.
- Expecting $\det(S + T) = \det S + \det T$; the determinant is not additive.
- Expecting $\det(cT) = c \det T$; the correct rule is $\det(cT) = c^n \det T$.

## Explanations

### L1 human

A linear map from a space to itself has a determinant.
To compute it, choose a basis, write the matrix of the map, and take the determinant of the matrix.
Every basis gives the same number, so the number belongs to the map.
The map is invertible exactly when this number is not zero.

### L2 human

Let $T$ act on polynomials of degree at most $1$ by $T(p) = p + p'$.

1. In the basis $1, x$: $T(1) = 1$ and $T(x) = 1 + x$, so $[T] = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ and $\det T = 1$.
2. In the basis $x, 1$: $T(x) = x + 1$ and $T(1) = 1$, so $[T] = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$, again with determinant $1$.
3. So $T$ is invertible, although its formula does not show an inverse at once.

The typical use is to test whether a map on a space of functions or matrices is invertible, with one matrix computation.
A trap: the matrix must use the same basis on both sides.
For the identity of $\mathbb{R}^2$ with basis $e_1, e_2$ in the domain and $2 e_1, e_2$ in the codomain, the matrix is $\operatorname{diag}(1/2, 1)$, with determinant $1/2$ and not $1$.

### L3 human

The space $\Lambda^n V$ has dimension $1$, so the induced map $\Lambda^n T$ is multiplication by a scalar, and this scalar is $\det T$.
This definition needs no basis, and it makes $\det(S \circ T) = \det S \cdot \det T$ a consequence of functoriality.
The same construction works for a free module of finite rank over a commutative ring.
Mathlib's `LinearMap.det` is defined for every module over a commutative ring, and it takes the value $1$ when the module has no finite basis.
