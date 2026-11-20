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

Let $F$ be a field, let $V$ and $W$ be vector spaces over $F$, and let $T \colon V \to W$ be a [[linear map|0RJF668P1T]] with finite-dimensional image.
The *rank* of $T$ is
$$\rank T = \dim \im T,$$
the [[dimension|05G2G0P224]] of the [[image|0JB228DCWB]] of $T$.

## Notation

Other notations are $\operatorname{rk} T$ and $r(T)$.

## Remarks

- If $V$ is finite-dimensional, then the image is finite-dimensional, so the rank is defined.
- For the map $x \mapsto Ax$ of a matrix $A$, the rank is the [[rank of the matrix|0ZC9YTXZRY]] $A$.
- For infinite-dimensional images, the same formula defines the rank as a cardinal.

## Explanations

### L1 human

The rank of a linear map counts the dimensions of its output.
A map from space onto a plane has rank $2$.

### L2 human

For $T(x, y, z) = (x + y,\ x + y)$ from $\R^3$ to $\R^2$, each value is $(x + y)\,(1, 1)$.
So the image is the line spanned by $(1, 1)$, and $\rank T = 1$.
The trap is to answer $2$ because the target is $\R^2$.
