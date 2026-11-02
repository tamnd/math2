---
tag: ZVB7G8TGC3
kind: definition
name: Open immersion
msc: [14A15]
defines: GFC5YKSN5H
uses: [JXRKH6P1Z4, 5A35TYZD02, 02BH3MCBQB, 0QT00PB5G2]
sources:
  - url: https://en.wikipedia.org/wiki/Glossary_of_algebraic_geometry
---

## Definition

Let $U$ and $X$ be [[schemes|5A35TYZD02]].
A [[morphism of schemes|JXRKH6P1Z4]] $(f, f^\#) \colon U \to X$ is an *open immersion* if:

1. $f$ is a [[homeomorphism|0QT00PB5G2]] of $U$ onto an [[open subset|02BH3MCBQB]] $V$ of $X$;
2. the induced map $\mathcal{O}_X|_V \to f_* \mathcal{O}_U$ is an isomorphism of sheaves of rings on $V$.

Equivalently, $f$ is an isomorphism of $U$ onto the open subscheme $(V, \mathcal{O}_X|_V)$.

## Remarks

Example: for a ring $A$ and $g \in A$, the morphism $\operatorname{Spec} A_g \to \operatorname{Spec} A$ induced by $A \to A_g$ is an open immersion onto $D(g)$.
On each basic open $D(gh) \subseteq D(g)$ the sheaf map is the isomorphism $A_{gh} \cong (A_g)_h$.
Non-example: for a field $k$, let $f \colon \operatorname{Spec} k \to \operatorname{Spec} k[x]/(x^2)$ come from $k[x]/(x^2) \to k$, $x \mapsto 0$.
Both spaces are one point, so $f$ is a homeomorphism onto an open set and clause 1 holds.
Clause 2 fails: the ring map $k[x]/(x^2) \to k$ is not injective, so it is not an isomorphism.
