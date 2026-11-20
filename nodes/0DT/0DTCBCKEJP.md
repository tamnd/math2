---
tag: 0DTCBCKEJP
kind: concept
name: Transvection
aliases: [shear-matrix]
msc: [15A23]
topics: [P8J6QR66TJ]
audience: ug1
uses: [06DW9BAWB1, 01REXW3WWE, 0NRYHJPQG2]
sources:
  - url: https://en.wikipedia.org/wiki/Shear_mapping
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Elementary_matrix
    locator: Row-addition transformations
  - url: https://en.wikipedia.org/wiki/Special_linear_group
    locator: Generators and relations
---

## Summary

Let $R$ be a commutative ring, let $n \ge 2$, let $i \ne j$ and let $c \in R$.
The transvection matrix is $T_{ij}(c) = I_n + cE_{ij}$, where $I_n$ is the [[identity matrix|06DW9BAWB1]] and $E_{ij}$ has entry $1$ in position $(i, j)$ and $0$ elsewhere.
Left multiplication by $T_{ij}(c)$ adds $c$ times row $j$ to row $i$, so it is an [[elementary matrix|01REXW3WWE]] of the row-replacement type.
In coordinate-free terms, a transvection of a vector space $V$ is a [[linear map|0NRYHJPQG2]] of the form $\tau(x) = x + \varphi(x) v$.
Here $\varphi$ is a nonzero linear form and $v \ne 0$ is a vector with $\varphi(v) = 0$.
Transvections matter because they are the building blocks of the [[special linear group|0V9PMN0RBH]].
Over a field, every matrix of determinant $1$ is a product of them.

## Motivation

Gaussian elimination uses three kinds of row operations, but the row replacements do most of the work.
They do not change the determinant, while exchanges change its sign and scalings multiply it.
So the matrices of determinant $1$ should be reachable by row replacements alone, and this is the theorem on [[generation by transvections|YSS4XNY9RC]].
In the plane, $T_{12}(c) = \begin{pmatrix} 1 & c \\ 0 & 1 \end{pmatrix}$ is the horizontal shear $(x, y) \mapsto (x + cy, y)$.

## Notation

- Books write $T_{ij}(c)$, $E_{ij}(c)$, $e_{ij}(c)$ or $x_{ij}(c)$ for $I_n + cE_{ij}$. The letter $x_{ij}(c)$ is common in the theory of groups of Lie type.
- Some books count $T_{ij}(0) = I_n$ as a transvection, and some require $c \ne 0$.
- The [[formal definition|0NMN00FNW1]] gives the matrix form over a commutative ring.

## Remarks

### Examples

- The [[shear by $3$|DRW0DE4TM2]] $\begin{pmatrix} 1 & 3 \\ 0 & 1 \end{pmatrix}$ fixes the $x$-axis and moves each point parallel to it.
- The matrix $\begin{pmatrix} 2 & -1 \\ 1 & 0 \end{pmatrix}$ is a transvection in the coordinate-free sense, as the [[hyperplane example|66XNSFCMQ1]] shows; it is not of the form $T_{ij}(c)$.
- For $n = 3$, $T_{13}(5) = \begin{pmatrix} 1 & 0 & 5 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$ adds $5$ times row $3$ to row $1$.

### Non-examples

- $\operatorname{diag}(2, 1)$ is not a transvection: it fixes a line pointwise, but its determinant is $2$; see the [[non-example|Y4YPA5V3KJ]].
- $I_n + cE_{ii}$ is not a transvection for $c \ne 0$, because the indices are equal; it is the scaling $D_i(1 + c)$.
- A rotation by a quarter turn fixes no nonzero vector, so it is not a transvection.

### Basic properties

- $\det T_{ij}(c) = 1$, because $T_{ij}(c)$ is triangular with diagonal entries $1$.
- $T_{ij}(a)\, T_{ij}(b) = T_{ij}(a + b)$, since $E_{ij}^2 = 0$ for $i \ne j$. In particular $T_{ij}(c)^{-1} = T_{ij}(-c)$.
- For distinct $i, j, k$: $T_{ij}(a)\, T_{jk}(b)\, T_{ij}(-a)\, T_{jk}(-b) = T_{ik}(ab)$. For example, $a = 2$ and $b = 5$ give $T_{13}(10)$.
- A transvection $\tau$ fixes the hyperplane $\ker \varphi$ pointwise, and $\tau(x) - x$ lies in the line through $v$. In a suitable basis, its matrix is $I_n + E_{12}$.
- Over a field, the transvections generate $\mathrm{SL}_n(F)$, by the theorem on [[generation by transvections|YSS4XNY9RC]].

### History

The word transvection is used in the classical study of linear groups, for example by Dieudonné in his work on the classical groups.
The relation for $T_{ij}(a)$ and $T_{jk}(b)$ above is one of the Steinberg relations, which Steinberg used to give presentations of groups such as $\mathrm{SL}_n$.

### Common errors

- Students confuse a transvection with a dilation such as $\operatorname{diag}(2, 1)$. Both fix a hyperplane pointwise, but only the transvection has determinant $1$.
- Students invert $T_{ij}(c)$ as $T_{ji}(c)$ or $T_{ij}(1/c)$. The inverse is $T_{ij}(-c)$.

## Explanations

### L1 human

A transvection slides each point parallel to one direction, by an amount that depends on another coordinate.
A deck of cards that we push sideways is a picture of a shear.
Areas and volumes do not change, which matches the determinant $1$.

### L2 human

Worked example: let $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$.

1. $T_{21}(-3) A = \begin{pmatrix} 1 & 2 \\ 3 - 3 & 4 - 6 \end{pmatrix} = \begin{pmatrix} 1 & 2 \\ 0 & -2 \end{pmatrix}$.
2. $\det$ is unchanged: $\det A = 4 - 6 = -2$ and $\det \begin{pmatrix} 1 & 2 \\ 0 & -2 \end{pmatrix} = -2$.
3. Undo with $T_{21}(3)$: $T_{21}(3) T_{21}(-3) = T_{21}(0) = I_2$.

The typical use is elimination with row replacements only, which keeps the determinant.
A trap: a row exchange is not a product of transvections, because its determinant is $-1$.

### L3 human

In the coordinate-free form $\tau = \id_V + v \otimes \varphi$ with $\varphi(v) = 0$, the transvections of $V$ form a single conjugacy class in $\mathrm{GL}(V)$ when $\dim V \ge 2$.
The subgroup generated by the $T_{ij}(c)$ over a commutative ring $R$ is the elementary group $E_n(R)$.
The quotient $\mathrm{SL}_n(R)/E_n(R)$ is studied in algebraic K-theory, and it is trivial for fields and for Euclidean domains.
