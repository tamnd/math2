---
tag: 05CJSSXPR3
kind: concept
name: Determinant of a family of vectors in a basis
msc: [15A15, 15A75]
topics: [DTBK11SR77]
audience: ug2
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Determinant of n vectors
---

## Summary

The determinant of a family of $n$ vectors in a basis $B$ of an $n$-dimensional space is a scalar, written $\det_B(v_1, \dots, v_n)$.
It is the [[determinant|00KDZRW4C0]] of the matrix whose columns are the coordinates of the vectors in $B$; the [[definition|0V94H674MB]] gives the details.
It is the unique alternating multilinear form on $V^n$ with value $1$ on $B$.
It changes by a fixed factor when $B$ changes, and it is nonzero exactly when the family is a basis.

## Motivation

In $\mathbb{R}^n$, the determinant of $n$ column vectors is the signed volume of the parallelotope they span.
An abstract vector space has no standard basis, so we choose a basis $B$ as the unit of volume.
The determinant in $B$ then measures signed volume in this unit.

## Notation

- $\det_B(v_1, \dots, v_n)$ is the determinant of the family $(v_1, \dots, v_n)$ in the basis $B$.
- $\det_B(B')$ is the determinant of the vectors of a second basis $B'$, in their order.
- $[v]_B$ is the [[coordinate vector|04CYQHN6MC]] of $v$ in $B$.

## Remarks

### Examples

- $\det_B(B) = 1$ for every basis $B$.
- In $\mathbb{R}^2$, $(1, 2), (3, 4)$ has determinant $-2$ in the standard basis and $-1$ in the basis $(2, 0), (0, 1)$: [[example|Q9N66CYVH4]].
- The polynomials $1 + x$, $x + x^2$, $1 + x^2$ have determinant $2$ in the basis $1, x, x^2$: [[example|XNG0N654EM]].

### Non-examples

- Two vectors in $\mathbb{R}^3$ have no determinant in a basis of $\mathbb{R}^3$: [[non-example|CECRXV7KAZ]].
- A family without a chosen basis has no determinant, since the value changes with the basis.

### Basic properties

- $\det_B$ is linear in each vector, and it is $0$ when two vectors are equal.
- Exchanging two vectors changes the sign of $\det_B$.
- [[Change of basis rule|T1WN2DHS63]]: $\det_{B'} = \det_{B'}(B) \cdot \det_B$, and $\det_B(B') \det_{B'}(B) = 1$.
- [[Basis criterion|5D1CHPV9Z3]]: over a field, $v_1, \dots, v_n$ is a basis if and only if $\det_B(v_1, \dots, v_n) \ne 0$.
- For an endomorphism $T$, $\det_B(T v_1, \dots, T v_n) = \det T \cdot \det_B(v_1, \dots, v_n)$, with the [[determinant of $T$|0X0HQYSZ0K]].

### Common errors

- Forgetting that the value depends on $B$; only the condition "nonzero" is independent of $B$.
- Using rows of coordinates in one place and columns in another; both give the same value, since $\det M^T = \det M$, but the vectors must be in the same order.
- Writing $\det_B(v) = \det_E(v) \cdot \det_E(B)$; the correct rule divides by $\det_E(B)$.

## Explanations

### L1 human

Pick a basis as the unit, and write $n$ vectors in its coordinates.
Put the coordinates side by side as the columns of a square matrix.
The determinant of this matrix is the determinant of the vectors in that basis.
It is the signed volume of their box, measured with the box of the basis as the unit.

### L2 human

In $\mathbb{R}^2$ with the standard basis $E$, $\det_E((1, 2), (3, 4)) = 1 \cdot 4 - 3 \cdot 2 = -2$.
The parallelogram of the two vectors has area $2$, and the minus sign says that the turn from the first vector to the second is clockwise.
The typical use is a quick test: $n$ vectors form a basis exactly when the determinant is nonzero.
A trap: a second basis $B$ changes the value by the factor $1/\det_E(B)$.

### L3 human

The alternating $n$-linear forms on an $n$-dimensional space form a line, and $\det_B$ is the element of this line with value $1$ on $B$.
In the language of exterior algebra, $v_1 \wedge \dots \wedge v_n = \det_B(v_1, \dots, v_n) \cdot b_1 \wedge \dots \wedge b_n$ in $\Lambda^n V$.
