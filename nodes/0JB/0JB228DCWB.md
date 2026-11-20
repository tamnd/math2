---
tag: 0JB228DCWB
kind: definition
name: Image of a linear map
msc: ["15A04"]
topics: [9080WQTZ3M]
audience: ug1
defines: 0WSFKKT6FF
uses: [0RJF668P1T]
formal:
  - system: lean4
    library: mathlib
    decl: LinearMap.range
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Image_(mathematics)
    locator: lead section
  - book: isbn:9780134860244
    locator: Section 2.1
---

## Definition

Let $F$ be a field, let $V$ and $W$ be vector spaces over $F$, and let $T \colon V \to W$ be a [[linear map|0RJF668P1T]].
The *image* of $T$, also called the *range*, is the subset
$$\im T = \{T(v) : v \in V\}$$
of $W$.

## Notation

Other notations are $\operatorname{Im} T$, $T(V)$, $R(T)$ and $\operatorname{ran} T$.

## Remarks

- The image is a subset of the target $W$, and not of the source $V$.
- The map $T$ is surjective if and only if $\im T = W$.
- For the map $x \mapsto Ax$ of a matrix $A$, the image is the [[column space|03AJKXH1AV]] of $A$.
- Mathlib defines `LinearMap.range f` directly as a submodule, so the subspace property is built in.

## Explanations

### L1 human

The image of a linear map is everything that the map can produce.
If a map sends ordinary space onto a plane, then its image is that plane.

### L2 human

For $T(x, y) = (x + y,\ 2x + 2y)$ on $\R^2$, each value is $(x + y) \cdot (1, 2)$.
So $\im T$ is the line spanned by $(1, 2)$.
The vector $(1, 0)$ is not in the image, so $T(v) = (1, 0)$ has no solution.
