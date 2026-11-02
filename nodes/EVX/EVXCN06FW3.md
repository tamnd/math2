---
tag: EVXCN06FW3
kind: concept
name: Crystalline cohomology
msc: [14F30, 14G17]
sources:
  - url: https://en.wikipedia.org/wiki/Crystalline_cohomology
same_as:
  wikidata: Q5191431
  wikipedia: Crystalline cohomology
---

## Summary

Crystalline cohomology is a cohomology theory for varieties over a perfect field $k$ of characteristic $p > 0$.
Its values are modules over the ring $W(k)$ of [[Witt vectors|6N3X2QX4W9]].
Grothendieck proposed it and Berthelot developed it, to obtain a $p$-adic cohomology in characteristic $p$, where [[ℓ-adic cohomology|E1DVHN06CR]] with $\ell = p$ fails.
When the variety lifts to $W(k)$, it is the [[algebraic de Rham cohomology|13F5JZPDD0]] of the lift.
So it is a de Rham theory that does not depend on the choice of a lift.
It carries a Frobenius action and is a main object of $p$-adic Hodge theory.

## Explanations

### L1 human

De Rham cohomology over a field of characteristic $p$ gives vector spaces over that field, and it loses information, because differentiating $t^p$ gives $0$.
One would like to lift the variety to the $p$-adic integers, or more generally to $W(k)$, and compute de Rham cohomology there.
Lifts do not always exist and are not unique.
Crystalline cohomology computes what the answer would be from the variety alone, using all its thickenings at once.
For the projective line over $\F_p$ it gives $\Z_p$ in degrees $0$ and $2$, as the de Rham cohomology of the projective line over $\Z_p$ does.
