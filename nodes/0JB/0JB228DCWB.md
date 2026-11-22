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

The image of a linear map is the set of all the vectors that it actually produces.

Let $F$ be a field, let $V$ and $W$ be vector spaces over $F$, and let $T \colon V \to W$ be a [[linear map|0RJF668P1T]].
The *image* of $T$, also called the *range*, is the subset
$$\im T = \{T(v) : v \in V\}$$
of $W$.

## Notation

Other notations are $\operatorname{Im} T$, $T(V)$, $R(T)$ and $\operatorname{ran} T$.

## Remarks

The definition has one condition: a vector $w \in W$ lies in $\im T$ when there is at least one $v \in V$ with $T(v) = w$.
The vector $v$ need not be unique, and the image is a subset of the target $W$, not of the source $V$.
So $T$ is surjective exactly when $\im T = W$.

For example, let $T(x, y) = (x, \; y, \; x + y)$ from $\R^2$ to $\R^3$.
The vector $(2, 3, 5)$ lies in $\im T$, since $T(2, 3) = (2, 3, 5)$.
The vector $(1, 0, 0)$ does not, since $T(x, y) = (1, 0, 0)$ would need $x = 1$, $y = 0$ and $x + y = 0$ at once.

For a matrix $A$, the image of $x \mapsto Ax$ is the [[column space|03AJKXH1AV]] of $A$.
Mathlib defines `LinearMap.range f` directly as a submodule of the target, so the subspace property is part of the definition there.
The [[concept page|0WSFKKT6FF]] has more examples and the main properties.

## Explanations

### L1 human

The image of a linear map is everything that the map can produce.
If a map sends ordinary space onto a plane, then its image is that plane.
A vector outside the image is never an output, whatever the input.

### L2 human

For $T(x, y) = (x + y, \; 2x + 2y)$ on $\R^2$, each value is $(x + y) \cdot (1, 2)$.
So $\im T$ is the line spanned by $(1, 2)$.
The vector $(1, 0)$ is not on this line, so the equation $T(v) = (1, 0)$ has no solution.
Watch out: here many inputs give the same output, for example $T(1, 0) = T(0, 1) = (1, 2)$, and this does not affect the image.
