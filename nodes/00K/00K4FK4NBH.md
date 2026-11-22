---
tag: 00K4FK4NBH
kind: definition
name: Nullity
msc: ["15A03", "15A04"]
topics: [9080WQTZ3M]
audience: ug1
defines: 0APCFW7639
uses: [02YFME3RGW, 05G2G0P224]
sources:
  - url: https://en.wikipedia.org/wiki/Kernel_(linear_algebra)
    locator: Properties
  - book: isbn:9780134860244
    locator: Section 2.1
---

## Definition

The nullity of a linear map is the dimension of the set of vectors that it sends to zero.

Let $F$ be a field, let $V$ and $W$ be vector spaces over $F$, and let $T \colon V \to W$ be a [[linear map|0RJF668P1T]] with finite-dimensional kernel.
The *nullity* of $T$ is
$$\operatorname{nullity} T = \dim \ker T,$$
the [[dimension|05G2G0P224]] of the [[kernel|02YFME3RGW]] of $T$.
The nullity of a matrix $A$ is the nullity of the map $x \mapsto Ax$, that is, the dimension of the [[null space|0PQ2GGY1QV]] of $A$.

## Notation

Other notations are $\operatorname{null} T$ and $n(T)$.

## Remarks

The one condition is that the kernel is finite-dimensional, so that its dimension is a number.
This holds whenever $V$ is finite-dimensional, since the kernel is a subspace of $V$.
For infinite-dimensional kernels, the same formula defines the nullity as a cardinal.

For example, the projection $(x, y, z) \mapsto (x, y, 0)$ has the $z$-axis as kernel, so its nullity is $1$.
A failing case for the condition is the zero map on the space $\R[x]$ of all polynomials, whose kernel $\R[x]$ has no finite basis.

For an $m \times n$ matrix, the nullity is the number of free variables of $Ax = 0$.
The [[concept page|0APCFW7639]] has more examples and the main properties.

## Explanations

### L1 human

The nullity counts the dimensions that the map crushes to zero.
The projection of space onto a plane crushes one direction, so its nullity is $1$.

### L2 human

For $A = \begin{pmatrix} 1 & 1 & 1 \end{pmatrix}$, the system $x_1 + x_2 + x_3 = 0$ has two free variables, $x_2$ and $x_3$.
The null space has basis $(-1, 1, 0)$ and $(-1, 0, 1)$, so the nullity is $2$.
Check: $-1 + 1 + 0 = 0$ and $-1 + 0 + 1 = 0$.
