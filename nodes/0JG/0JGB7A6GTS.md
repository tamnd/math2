---
tag: 0JGB7A6GTS
kind: definition
name: Rank of a linear map
msc: ["15A03", "15A04"]
topics: [9080WQTZ3M]
audience: ug1
defines: 0ZZXSBTR4J
uses: [0JB228DCWB, 05G2G0P224]
sources:
  - url: https://en.wikipedia.org/wiki/Rank_(linear_algebra)
    locator: lead section
  - book: isbn:9780134860244
    locator: Section 2.1
inventory: [J89PWVW5GR]
---

## Definition

The rank of a linear map is the dimension of the set of its outputs.

Let $F$ be a field, let $V$ and $W$ be vector spaces over $F$, and let $T \colon V \to W$ be a [[linear map|0RJF668P1T]] with finite-dimensional image.
The *rank* of $T$ is
$$\rank T = \dim \im T,$$
the [[dimension|05G2G0P224]] of the [[image|0JB228DCWB]] of $T$.

## Notation

Other notations are $\operatorname{rk} T$ and $r(T)$.

## Remarks

The one condition is that the image is finite-dimensional, so that its dimension is a number.
This holds whenever $V$ is finite-dimensional, since the image of a basis of $V$ spans $\im T$.
For infinite-dimensional images, the same formula defines the rank as a cardinal.

For example, the map $\R^3 \to \R^3$, $(x, y, z) \mapsto (x, y, 0)$, has the $xy$-plane as image, so its rank is $2$.
A failing case for the condition is the identity of the space $\R[x]$ of all polynomials, whose image $\R[x]$ has no finite basis, so it has no finite rank.

For the map $x \mapsto Ax$ of a matrix $A$, the rank is the [[rank of the matrix|0ZC9YTXZRY]] $A$.
The [[concept page|0ZZXSBTR4J]] has more examples and the main properties.

## Explanations

### L1 human

The rank of a linear map counts the dimensions of its output.
A map from space onto a plane has rank $2$, and a map onto a line has rank $1$.

### L2 human

For $T(x, y, z) = (x + y, \; x + y)$ from $\R^3$ to $\R^2$, each value is $(x + y)\,(1, 1)$.
So the image is the line spanned by $(1, 1)$, and $\rank T = 1$.
Watch out: the answer is not $2$, even though the target is $\R^2$.
