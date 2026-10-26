---
tag: 02YFME3RGW
kind: definition
name: Kernel of a linear map
msc: [15A04]
defines: 0S23E6YE83
uses: [0RJF668P1T]
sources:
  - url: https://en.wikipedia.org/wiki/Kernel_(linear_algebra)
    locator: lead section
---

## Definition

Let $F$ be a field, let $V$ and $W$ be vector spaces over $F$, and let $T \colon V \to W$ be a [[linear map|0NRYHJPQG2]].
The *kernel* of $T$ is
$$\ker T = \{v \in V : T(v) = 0\}.$$

## Remarks

The kernel is a [[linear subspace|00YC1D652K]] of $V$.
[[A linear map is injective if and only if its kernel is trivial|0BJBYCGMWE]].
For the map $x \mapsto Ax$ of a matrix $A$, the kernel is the [[null space|0PHDYNR24D]] of $A$, the solution set of $Ax = 0$.
The kernel of the projection $\R^3 \to \R^2$, $(x, y, z) \mapsto (x, y)$, is the $z$-axis.

## Explanations

### L1 human

The kernel collects the vectors that the map sends to zero.
It measures how much information the map loses.
If only the zero vector goes to zero, then the map loses nothing.
