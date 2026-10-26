---
tag: ~7f1c1ffe
kind: definition
name: Quotient map
msc: [15A03, 15A04]
defines: ~467a0280
uses: [~f96424b7]
sources:
  - url: https://en.wikipedia.org/wiki/Quotient_space_(linear_algebra)
    locator: Definition
---

## Definition

Let $F$ be a field, let $V$ be a vector space over $F$, and let $W$ be a subspace of $V$.
The *quotient map* is the map
$$\pi \colon V \to V / W, \qquad \pi(v) = v + W,$$
from $V$ to the [[quotient space|~d45aaac6]] $V / W$.

## Remarks

The map $\pi$ is linear and surjective, and its kernel is $W$.
Each linear map $T \colon V \to U$ with $W \subseteq \ker T$ factors through $\pi$, see [[universal property of the quotient space|~1926a1f5]].
In Mathlib, it is `Submodule.mkQ`.

## Explanations

### L1 human

The quotient map sends each vector to the class of all vectors that differ from it by an element of $W$.
It forgets exactly the information in $W$.
The vectors that it sends to zero are exactly the vectors of $W$.
