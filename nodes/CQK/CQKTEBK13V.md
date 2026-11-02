---
tag: CQKTEBK13V
kind: definition
name: Closed immersion
msc: [14A15]
defines: WWRWYSJDET
uses: [JXRKH6P1Z4, 5A35TYZD02, 0ZCK8DQYN1, 0QT00PB5G2, TB6TM6R4MD]
sources:
  - url: https://en.wikipedia.org/wiki/Closed_immersion
---

## Definition

Let $Z$ and $X$ be [[schemes|5A35TYZD02]].
A [[morphism of schemes|JXRKH6P1Z4]] $(f, f^\#) \colon Z \to X$ is a *closed immersion* if:

1. $f$ is a [[homeomorphism|0QT00PB5G2]] of $Z$ onto a [[closed subset|0ZCK8DQYN1]] of $X$;
2. the [[sheaf|TB6TM6R4MD]] map $f^\# \colon \mathcal{O}_X \to f_* \mathcal{O}_Z$ is surjective, that is, surjective on every stalk.

## Remarks

Example: for a ring $A$ and an ideal $I$, the morphism $\operatorname{Spec} A/I \to \operatorname{Spec} A$ induced by $A \to A/I$ is a closed immersion.
Its image is the closed set $V(I)$, and on the stalk at $\mathfrak{p} \supseteq I$ the map is $A_{\mathfrak p} \to (A/I)_{\mathfrak p}$, which is onto.
Every closed immersion into $\operatorname{Spec} A$ is isomorphic to one of these.
Non-example: let $k$ be a field and let $f \colon \operatorname{Spec} k[t] \to \operatorname{Spec} k[t^2, t^3]$ come from the inclusion $k[t^2, t^3] \subseteq k[t]$.
Then $f$ is a homeomorphism onto the whole space, so clause 1 holds.
Clause 2 fails at the origin: $t$ does not lie in the image of the stalk map.
Non-example: the open immersion $\operatorname{Spec} k[x, x^{-1}] \to \operatorname{Spec} k[x]$ fails clause 1, since its image $D(x)$ is not closed.
