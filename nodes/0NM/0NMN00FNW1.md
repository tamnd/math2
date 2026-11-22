---
tag: 0NMN00FNW1
kind: definition
name: Transvection
msc: [15A23]
topics: [P8J6QR66TJ]
audience: ug1
defines: 0DTCBCKEJP
uses: [0M79HRJCRR]
formal:
  - system: lean4
    library: mathlib
    decl: Matrix.transvection
    match: variant
sources:
  - url: https://en.wikipedia.org/wiki/Shear_mapping
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Elementary_matrix
    locator: Row-addition transformations
---

## Definition

Let $R$ be a commutative ring, let $n \ge 2$, let $i \ne j$ be indices in $\{1, \dots, n\}$ and let $c \in R$.
Let $E_{ij}$ be the $n \times n$ matrix with entry $1$ in position $(i, j)$ and $0$ elsewhere.
The *transvection matrix* is
$$T_{ij}(c) = I_n + c E_{ij}.$$

## Notation

Other common symbols are $E_{ij}(c)$, $e_{ij}(c)$ and $x_{ij}(c)$.
For a vector space $V$ over a field, a *transvection* of $V$ is a linear map $\tau(x) = x + \varphi(x) v$.
Here $\varphi$ is a nonzero linear form and $v$ is a nonzero vector with $\varphi(v) = 0$.
The matrices $T_{ij}(c)$ with $c \ne 0$ are the transvections of this kind with $v = e_i$ and $\varphi(x) = c x_j$.

## Remarks

The product $T_{ij}(c) A$ adds $c$ times row $j$ of $A$ to row $i$; this is an [[elementary matrix|0M79HRJCRR]] of the row-replacement type.
Its determinant is $1$, and its inverse is $T_{ij}(-c)$.
Mathlib defines `Matrix.transvection i j c` as $1 + c E_{ij}$ for all indices $i$ and $j$, with no condition $i \ne j$.
Its lemmas add the condition $i \ne j$ when they need it.
So the binding is a variant: for $i = j$, the Mathlib matrix is the scaling $I_n + cE_{ii}$, which is not a transvection here.

## Explanations

### L1 human

A transvection slides each point parallel to one axis, by an amount that depends on another coordinate.
Areas and volumes do not change, which matches the determinant $1$.

### L2 human

For $n = 2$ there are two families: $T_{12}(c) = \begin{pmatrix} 1 & c \\ 0 & 1 \end{pmatrix}$ and $T_{21}(c) = \begin{pmatrix} 1 & 0 \\ c & 1 \end{pmatrix}$.
For example, $T_{21}(-3) \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} = \begin{pmatrix} 1 & 2 \\ 0 & -2 \end{pmatrix}$, the first step of elimination.
A trap: $c = 0$ gives $I_n$, so some books ask for $c \ne 0$.
