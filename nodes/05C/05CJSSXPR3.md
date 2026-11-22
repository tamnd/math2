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

In a space without a standard basis, we measure the signed volume of $n$ vectors by choosing a basis as the unit of volume.
The determinant of the family in that basis is the resulting number, and it is nonzero exactly when the family is itself a basis.
Let $V$ be a vector space of dimension $n \ge 1$ over a field $F$, let $B = (b_1, \dots, b_n)$ be a basis, and let $v_1, \dots, v_n \in V$.
Put the coordinate vectors $[v_1]_B, \dots, [v_n]_B$ as the columns of an $n \times n$ matrix $M$.
Then
$$\det_B(v_1, \dots, v_n) = \det M,$$
the [[determinant|00KDZRW4C0]] of $M$, as the [[formal definition|0V94H674MB]] states.
Equivalently, $\det_B$ is the unique [[alternating multilinear map|0K6CH0MT0F]] $V^n \to F$ that takes the value $1$ on $B$.

## Motivation

In $\mathbb{R}^n$ the determinant of $n$ column vectors is the signed volume of the [[parallelepiped|0SQV2VJTGY]] they span, measured against the unit cube.
A space of polynomials or of matrices has no unit cube, because it has no preferred basis.
So we choose a basis $B$ and let its parallelepiped be the unit.
Then $\det_B$ measures signed volume in this unit, and a second basis changes every value by one fixed factor.

The idea gives a test for bases that works in any space: $n$ vectors form a basis exactly when their determinant is not zero.
It also prepares the [[determinant of a linear map|0X0HQYSZ0K]], which compares the volume of $T v_1, \dots, T v_n$ with the volume of $v_1, \dots, v_n$, and the [[orientation|0QJJAQ6ZYZ]] of a real space, which is the sign of such a comparison.

## Notation

We write $\det_B(v_1, \dots, v_n)$, or $\det_B(v)$ for the family $v = (v_1, \dots, v_n)$.
For a second basis $B'$ we write $\det_B(B')$ for the determinant of its vectors in their order.
The symbol $[v]_B$ is the [[coordinate vector|04CYQHN6MC]] of $v$ in $B$.
The order of the vectors matters, because exchanging two of them changes the sign.

## Remarks

### A first computation

In $\mathbb{R}^2$ with the standard basis $E$, take $v_1 = (2, 1)$ and $v_2 = (1, 3)$.
The coordinates are the entries themselves, so
$$\det_E(v_1, v_2) = \det \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix} = 2 \cdot 3 - 1 \cdot 1 = 5.$$
The parallelogram of $v_1$ and $v_2$ has area $5$, and the sign is positive because the turn from $v_1$ to $v_2$ is counterclockwise.
In the order $v_2, v_1$ the value is $-5$.

### The same vectors in another basis

The value depends on the unit.
For $v_1 = (1, 2)$ and $v_2 = (3, 4)$, the standard basis gives $1 \cdot 4 - 3 \cdot 2 = -2$, while the basis $(2, 0), (0, 1)$, whose unit has area $2$, gives $-1$.
[[The plane example|Q9N66CYVH4]] computes both values, and the [[change of basis rule|T1WN2DHS63]] links them:
$$\det_B(v_1, \dots, v_n) = \det_B(B') \cdot \det_{B'}(v_1, \dots, v_n).$$
So the forms $\det_B$ for different bases differ only by nonzero factors, and the condition "nonzero" is the same in every basis.

### A test for bases

Over a field, $v_1, \dots, v_n$ is a basis exactly when $\det_B(v_1, \dots, v_n) \ne 0$, by the [[basis criterion|5D1CHPV9Z3]].
For the polynomials $1 + x$, $x + x^2$, $1 + x^2$ in the basis $1, x, x^2$, the determinant is $2$.
[[The polynomial example|XNG0N654EM]] shows that they form a basis over $\mathbb{Q}$ but not over $\mathbb{F}_2$, where $2 = 0$.

### The rules you can use

The form $\det_B$ is linear in each vector, because the determinant is linear in each column.
It is $0$ when two vectors are equal, and exchanging two vectors changes its sign.
For an endomorphism $T$ of $V$, it obeys
$$\det_B(T v_1, \dots, T v_n) = \det T \cdot \det_B(v_1, \dots, v_n),$$
because the coordinate matrix of the images is $[T]_B M$.

### What it is not

Two vectors in $\mathbb{R}^3$ have no determinant in a basis of $\mathbb{R}^3$, because their coordinate matrix is $3 \times 2$; [[the pair in space|CECRXV7KAZ]] checks this.
A family with no chosen basis has no determinant either, since the value changes with the basis.
Only the vanishing of the value is free of the choice.

### Watch out

The rule for a new basis divides, it does not multiply.
From $\det_E(v) = \det_E(B) \det_B(v)$ we get $\det_B(v) = \det_E(v) / \det_E(B)$.
In the plane example, $-2 / 2 = -1$ is correct, and $-2 \cdot 2 = -4$ is the wrong move.

### Try it

First, compute $\det_E((1, 1), (1, -1))$ in the standard basis of $\mathbb{R}^2$.
The answer is $1 \cdot (-1) - 1 \cdot 1 = -2$, so the two vectors form a basis with the opposite orientation.

Second, do $(1, 2, 3)$, $(4, 5, 6)$, $(7, 8, 9)$ form a basis of $\mathbb{R}^3$?
No: the third vector minus the second equals the second minus the first, so the vectors are dependent and the determinant is $0$.

## Explanations

### L1 human

Pick a basis to serve as the unit, and write $n$ vectors in its coordinates.
Put the coordinates side by side as the columns of a square matrix.
The determinant of this matrix is the determinant of the vectors in that basis.
It is the signed volume of their box, measured with the box of the basis as one unit.
For example, if the basis box is twice as large, every value becomes half as large.

### L2 human

Here is a typical use: do the vectors $(1, 1)$ and $(1, 0)$ form a basis, and what is their volume in the basis $B = ((1, 1), (0, 1))$?
First find coordinates in $B$:
$$(1, 1) = 1 \cdot (1, 1) + 0 \cdot (0, 1), \qquad (1, 0) = 1 \cdot (1, 1) - 1 \cdot (0, 1).$$
So the coordinate columns are $(1, 0)$ and $(1, -1)$, and
$$\det_B((1, 1), (1, 0)) = \det \begin{pmatrix} 1 & 1 \\ 0 & -1 \end{pmatrix} = -1.$$
The value is nonzero, so the vectors form a basis.
Check: in the standard basis the value is $1 \cdot 0 - 1 \cdot 1 = -1$, and $\det_E(B) = 1 \cdot 1 - 0 \cdot 1 = 1$, so the change of basis rule gives $-1 = 1 \cdot (-1)$.
One determinant answered both questions at once, which is the typical use.

### L3 human

The alternating $n$-linear forms on an $n$-dimensional space form a line, and $\det_B$ is the point of this line with value $1$ on $B$.
In the [[exterior algebra|0MDMZ965VE]] the same fact reads
$$v_1 \wedge \dots \wedge v_n = \det_B(v_1, \dots, v_n) \cdot b_1 \wedge \dots \wedge b_n.$$
Over a commutative ring the definition is the same for a free module of rank $n$, and a family is a basis exactly when its determinant is a unit.
In geometry a choice of $\det_B$ up to a positive factor is an orientation, and the absolute value $\lvert \det_B \rvert$ is a measure of volume, which returns in the [[volume scaling factor|RC5BTSG8T2]] of a linear map.
