---
tag: ZHNZJGE738
kind: definition
name: Globally hyperbolic spacetime
msc: ["53C50", "83C05"]
defines: PZGHVCQB13
uses: [BY4QYYS788, KZWG5F0TSB, EKA74X1SYS, G49G4R1K04]
sources:
  - url: https://en.wikipedia.org/wiki/Globally_hyperbolic_spacetime
---

## Definition

Let $(M, g)$ be a time-oriented [[Lorentzian manifold|BY4QYYS788]], with causal futures and pasts $J^\pm(p)$ as in the [[causal structure|KZWG5F0TSB]].
$(M, g)$ is *globally hyperbolic* if

1. it is strongly causal (one of the [[causality conditions|EKA74X1SYS]]), and
2. for all $p, q \in M$ the set $J^+(p) \cap J^-(q)$ is compact.

## Remarks

The set $J^+(p) \cap J^-(q)$ is called a causal diamond.
Bernal and Sánchez showed that clause 1 can be weakened to "causal", that is, no closed causal curve, without changing the class.
Global hyperbolicity is equivalent to the existence of a Cauchy surface, by a theorem of Geroch.

Example: in [[Minkowski space|G49G4R1K04]], $J^+(p) \cap J^-(q)$ is empty, a single point, a null segment, or a closed bounded double cone, so it is compact in every case.
Minkowski space is also strongly causal, so it is globally hyperbolic.

Non-example: let $M$ be Minkowski space with the origin removed, and take $p = (-1, 0, 0, 0)$ and $q = (1, 0, 0, 0)$.
The diamond $J^+(p) \cap J^-(q)$ is the closed double cone minus its centre, which is not compact.
So clause 2 fails, although the spacetime is still strongly causal.
Anti-de Sitter space is another standard non-example: it is strongly causal, but light rays reach its conformal boundary in finite time.
