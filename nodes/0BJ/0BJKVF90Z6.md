---
tag: 0BJKVF90Z6
kind: definition
name: Spanning set
msc: [15A03]
defines: 088RYKAWK9
uses: [0HR573CHNM]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_span
    locator: lead section
---

## Definition

Let $F$ be a field and let $V$ be a vector space over $F$.
A subset $S \subseteq V$ is a *spanning set* of $V$, or *spans* $V$, when $\operatorname{span}(S) = V$, where $\operatorname{span}$ is the [[linear span|0DTY8B9HMS]].
Equivalently, each vector of $V$ is a linear combination of finitely many vectors of $S$.

## Remarks

The vectors $(1, 0), (0, 1), (1, 1)$ span $\R^2$, and so do $(1, 0), (0, 1)$.
A linearly independent spanning set is a [[basis|0KCQ9Y3QKA]].
[[Every spanning set contains a basis|06MRNP4BNT]].
A vector space with a finite spanning set is [[finite-dimensional|0ZHWKQMVX5]].

## Explanations

### L1 human

A spanning set is a set of building blocks from which we can make every vector of the space.
It may contain more vectors than we need.
Removing the extra vectors leaves a basis.
