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

A transvection is the matrix of a row replacement, "add $c$ times row $j$ to row $i$", and in the plane it is a shear.
In symbols, for $n \ge 2$, indices $i \ne j$ and a scalar $c$, it is $T_{ij}(c) = I_n + cE_{ij}$, where $I_n$ is the [[identity matrix|06DW9BAWB1]] and $E_{ij}$ has a single entry $1$ in position $(i, j)$.
These are the [[elementary matrices|01REXW3WWE]] of the replacement type, and they are exactly the ones that do not change the determinant.
Over a field, every matrix of determinant $1$ is a product of transvections, so they are the building blocks of the [[special linear group|0V9PMN0RBH]].
Without coordinates, a transvection of a vector space is a [[linear map|0NRYHJPQG2]] that fixes a hyperplane pointwise and moves every other vector parallel to a fixed line inside that hyperplane.

## Motivation

Gaussian elimination uses three kinds of row operations, but the row replacements do most of the work.
They also behave best: a replacement keeps the determinant, while an exchange changes its sign and a scaling multiplies it.
So it is natural to ask which matrices row replacements alone can reach, and the answer is the theorem on [[generation by transvections|YSS4XNY9RC]]: over a field, exactly the matrices of determinant $1$.

The picture in the plane explains the name shear.
The matrix $T_{12}(c) = \begin{pmatrix} 1 & c \\ 0 & 1 \end{pmatrix}$ sends $(x, y)$ to $(x + cy, y)$.
Points on the $x$-axis stay where they are, and the point at height $y$ slides sideways by $cy$, like the cards of a deck pushed at the top.
The unit square becomes a parallelogram with the same base and height, so its area stays $1$.

## Notation

Books write $T_{ij}(c)$, $E_{ij}(c)$, $e_{ij}(c)$ or $x_{ij}(c)$ for $I_n + cE_{ij}$; the symbol $x_{ij}(c)$ is common in the theory of groups of Lie type.
Some books count $T_{ij}(0) = I_n$ as a transvection, and some require $c \ne 0$.
The [[formal definition|0NMN00FNW1]] gives the matrix form over a commutative ring.
In coordinate-free form a transvection is $\tau(x) = x + \varphi(x)v$, where $\varphi$ is a nonzero linear form and $v \ne 0$ is a vector with $\varphi(v) = 0$.

## Remarks

### A first computation

Take $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ and clear the entry below the first pivot:
$$T_{21}(-3)\,A = \begin{pmatrix} 1 & 0 \\ -3 & 1 \end{pmatrix} \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} = \begin{pmatrix} 1 & 2 \\ 3 - 3 & 4 - 6 \end{pmatrix} = \begin{pmatrix} 1 & 2 \\ 0 & -2 \end{pmatrix}.$$
Check: the determinant is $4 - 6 = -2$ before and $1 \cdot (-2) = -2$ after.
The step is undone by $T_{21}(3)$, since $T_{21}(3)\,T_{21}(-3) = T_{21}(0) = I_2$.

### Examples and non-examples

The [[shear by $3$|DRW0DE4TM2]] $\begin{pmatrix} 1 & 3 \\ 0 & 1 \end{pmatrix}$ fixes the $x$-axis and moves each point parallel to it.
The matrix $\begin{pmatrix} 2 & -1 \\ 1 & 0 \end{pmatrix}$ is not of the form $T_{ij}(c)$, but it is a transvection in the coordinate-free sense, as the [[hyperplane example|66XNSFCMQ1]] shows: it fixes the line through $(1, 1)$ pointwise.
On the other side, $\operatorname{diag}(2, 1)$ also fixes a line pointwise, but it has determinant $2$ and is a dilation, as the [[non-example|Y4YPA5V3KJ]] explains.
The matrix $I_n + cE_{ii}$ with $c \ne 0$ is not a transvection either; it is the scaling $D_i(1 + c)$.

### Rules for computing

Since $E_{ij}^2 = 0$ for $i \ne j$, the transvections with the same indices add their parameters:
$$T_{ij}(a)\,T_{ij}(b) = I_n + (a + b)E_{ij} + abE_{ij}^2 = T_{ij}(a + b).$$
In particular $T_{ij}(c)^{-1} = T_{ij}(-c)$.
Each $T_{ij}(c)$ is triangular with diagonal entries $1$, so $\det T_{ij}(c) = 1$.
For distinct $i, j, k$, the commutator of two transvections is again one:
$$T_{ij}(a)\,T_{jk}(b)\,T_{ij}(-a)\,T_{jk}(-b) = T_{ik}(ab).$$
For example, $a = 2$ and $b = 5$ give $T_{13}(10)$.
This identity is one of the Steinberg relations.

### The geometric view

A transvection $\tau(x) = x + \varphi(x)v$ fixes every vector of the hyperplane $\ker\varphi$, and each difference $\tau(x) - x$ lies on the line through $v$.
Since $v$ lies in $\ker\varphi$, applying $\tau$ twice gives $\tau^2(x) = x + 2\varphi(x)v$, and so $(\tau - \id)^2 = 0$.
In a basis that starts with $v$ and continues with a vector $w$ with $\varphi(w) = 1$, followed by a basis of the rest of $\ker \varphi$, the matrix of $\tau$ is $I_n + E_{12}$.

### Watch out

A transvection and a dilation such as $\operatorname{diag}(2, 1)$ both fix a hyperplane pointwise, but only the transvection keeps areas; the dilation doubles them.
The inverse of $T_{ij}(c)$ is $T_{ij}(-c)$, not $T_{ji}(c)$ and not $T_{ij}(1/c)$.
And a row exchange is not a product of transvections, because its determinant is $-1$.

### Try it

First, compute $T_{12}(2)\,T_{12}(3)$ for $n = 2$.
Answer: $T_{12}(5) = \begin{pmatrix} 1 & 5 \\ 0 & 1 \end{pmatrix}$, by the addition rule.

Second, which line does $\begin{pmatrix} 1 & 0 \\ 4 & 1 \end{pmatrix}$ fix pointwise?
Answer: the $y$-axis, since $(0, y)$ goes to $(0, 4 \cdot 0 + y) = (0, y)$, while $(1, 0)$ goes to $(1, 4)$.

## Explanations

### L1 human

A transvection slides each point parallel to one direction, by an amount that depends on another coordinate.
A deck of cards that we push sideways is a picture of a shear.
Areas and volumes do not change, which matches the determinant $1$.

### L2 human

In elimination, every step "subtract a multiple of one row from another" is a transvection acting from the left.
So when you reduce a matrix using only such steps, you have written $EA = U$ with $E$ a product of transvections and $\det U = \det A$.
This is how the determinant of a matrix is computed by elimination when no row exchange is needed.

### L3 human

The transvections of a vector space $V$ with $\dim V \ge 2$ form a single conjugacy class in $\mathrm{GL}(V)$, by the basis of the geometric view.
Over a commutative ring $R$, the subgroup generated by the $T_{ij}(c)$ is the elementary group $E_n(R)$.
The comparison of $E_n(R)$ with $\mathrm{SL}_n(R)$ is part of algebraic K-theory, and the two groups are equal when $R$ is a field or a Euclidean domain.
For $n \ge 3$, the addition rule, the commutator rule above, and the rule that $T_{ij}(a)$ and $T_{kl}(b)$ commute when $j \ne k$ and $i \ne l$ are the defining relations of the Steinberg group $\mathrm{St}_n(R)$, which maps onto $E_n(R)$.
