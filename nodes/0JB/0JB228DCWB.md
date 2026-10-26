---
tag: 0JB228DCWB
kind: definition
name: Image of a linear map
msc: [15A04]
defines: 0WSFKKT6FF
uses: [0RJF668P1T]
sources:
  - url: https://en.wikipedia.org/wiki/Image_(mathematics)
    locator: lead section
---

## Definition

Let $F$ be a field, let $V$ and $W$ be vector spaces over $F$, and let $T \colon V \to W$ be a [[linear map|0NRYHJPQG2]].
The *image* of $T$, also called the *range*, is
$$\im T = \{T(v) : v \in V\} \subseteq W.$$

## Remarks

The image is a [[linear subspace|00YC1D652K]] of $W$.
For the map $x \mapsto Ax$ of a matrix $A$, the image is the [[column space|03AJKXH1AV]] of $A$.
The map $T$ is surjective if and only if $\im T = W$.
The dimension of the image is the [[rank|0ZZXSBTR4J]] of $T$.

## Explanations

### L1 human

The image of a linear map is everything that the map can produce.
If a map sends ordinary space onto a plane, then its image is that plane.
The image is always a subspace.
