---
tag: ZFNZ0M7X41
kind: definition
name: Kirby calculus
msc: [57K40, 57K30, 57R65]
defines: AVQ9WN1MDV
uses: [1A5WRCNTM3, ZA405B0Z1S, 9V11N8VVTP, 1YP4RF1QXV]
sources:
  - url: https://en.wikipedia.org/wiki/Kirby_calculus
---

## Definition

A *framed link* in $S^3$ is a [[link|1A5WRCNTM3]] $L = K_1 \cup \cdots \cup K_r$ in $S^3$ with an integer $n_i$, its framing, attached to each component $K_i$.
It determines a closed oriented $3$-manifold $M_L$ by integral [[Dehn surgery|ZA405B0Z1S]] on $L$.
It also determines a compact $4$-manifold $W_L$, obtained from $D^4$ by attaching one $2$-handle along each $K_i$ with framing $n_i$.
This is a [[handle decomposition|9V11N8VVTP]] of $W_L$, and $\partial W_L = M_L$.
*Kirby calculus* is the system of the following moves on framed links, together with isotopy of links:

1. Blow-up and blow-down: add to $L$, or remove from $L$, an unknot with framing $\pm 1$ inside a ball disjoint from the rest of $L$.
2. Handle slide: replace a component $K_i$ by a band sum of $K_i$ with a parallel copy of another component $K_j$.
   The parallel copy is taken with respect to the framing $n_j$, and the framing of the new component changes accordingly.

## Remarks

By the [[Lickorish–Wallace theorem|1YP4RF1QXV]], every closed connected oriented $3$-manifold is $M_L$ for some framed link $L$.
Kirby's theorem states that $M_L$ and $M_{L'}$ are orientation-preserving diffeomorphic if and only if $L$ and $L'$ are related by a finite sequence of the moves above.
A handle slide does not change $W_L$ up to diffeomorphism, while a blow-up replaces $W_L$ by its connected sum with $\pm \C P^2$; both leave $M_L$ unchanged.
Example: the unknot with framing $+1$ describes $S^3$ itself, since a blow-down turns it into the empty link, which describes $S^3$.
Non-example: the unknot with framing $0$ cannot be blown down, because move 1 needs framing $\pm 1$; indeed it describes $S^1 \times S^2$, which is not $S^3$.
