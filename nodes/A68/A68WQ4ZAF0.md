---
tag: A68WQ4ZAF0
kind: statement
role: theorem
name: Collar neighbourhood theorem
msc: [57R40, 57N40, 58A05]
uses: [F45VQ47GPV, 7DS6B2BFK8, 0KZZ70ZHXP]
about: [7DS6B2BFK8]
sources:
  - url: https://en.wikipedia.org/wiki/Collar_neighbourhood
---

## Statement

Let $M$ be a smooth [[manifold with boundary|7DS6B2BFK8]], and let $\partial M$ be its boundary.
Then there is an open neighbourhood $U$ of $\partial M$ in $M$ and a [[diffeomorphism|0KZZ70ZHXP]] $c \colon \partial M \times [0, 1) \to U$ such that $c(x, 0) = x$ for every $x \in \partial M$.

## Remarks

The map $c$, or its image $U$, is a *collar* of $\partial M$.
The idea of the proof is to choose a smooth vector field near $\partial M$ that points into $M$ along $\partial M$.
Such a field is glued from local choices with a partition of unity.
Its flow, started at the boundary points and run for short times, gives the collar.
Example: for the closed unit disc $D^2$, the map $c(x, t) = (1 - t/2) x$ is a collar $S^1 \times [0, 1) \to D^2$ of the boundary circle.
The statement also holds for topological manifolds with boundary, a result of Morton Brown.

## Explanations

### L1 human

Near its boundary, every smooth manifold with boundary looks like a product of the boundary with a short interval.
A disc near its rim looks like a thin ring, a circle times an interval.
This lets one glue manifolds along common boundary pieces and get a smooth manifold again.

### L2 human

Collars are used to glue manifolds along boundary components, for example in the composition of cobordisms and in handle attachments.
They show that $M$ is homotopy equivalent to its interior, and that $M$ with an outer collar $\partial M \times [0, 1]$ attached is diffeomorphic to $M$.
The collar theorem is the boundary analogue of the tubular neighbourhood theorem: the inward normal bundle of $\partial M$ is a trivial half-line bundle.
