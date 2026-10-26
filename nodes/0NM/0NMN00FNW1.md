---
tag: 0NMN00FNW1
kind: definition
name: Transvection
msc: [15A23]
defines: 0DTCBCKEJP
uses: [0M79HRJCRR]
sources:
  - url: https://en.wikipedia.org/wiki/Shear_mapping
    locator: lead section
---

## Definition

Let $R$ be a commutative ring, let $n \ge 2$, let $i \ne j$ be indices in $\{1, \dots, n\}$ and let $c \in R$.
Let $E_{ij}$ be the $n \times n$ matrix with entry $1$ in position $(i, j)$ and $0$ elsewhere.
The *transvection matrix* is
$$T_{ij}(c) = I_n + c E_{ij}.$$

## Remarks

The product $T_{ij}(c) A$ adds $c$ times row $j$ of $A$ to row $i$; this is an [[elementary matrix|01REXW3WWE]] of the row-addition type.
Its determinant is $1$, and its inverse is $T_{ij}(-c)$.
Over a field, the transvections generate the [[special linear group|0V9PMN0RBH]].
In the plane, $\begin{pmatrix} 1 & c \\ 0 & 1 \end{pmatrix}$ is a horizontal shear.

## Explanations

### L1 human

A transvection slides each point parallel to one axis, by an amount that depends on another coordinate.
A deck of cards that we push sideways is a picture of a shear.
Areas and volumes do not change, which matches the determinant $1$.
