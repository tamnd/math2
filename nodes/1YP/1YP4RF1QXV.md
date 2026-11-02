---
tag: 1YP4RF1QXV
kind: statement
role: theorem
name: Lickorish–Wallace theorem
msc: [57K30, 57K10]
uses: [ZA405B0Z1S, R20TB2KEQQ, 1A5WRCNTM3]
about: [ZA405B0Z1S, R20TB2KEQQ]
sources:
  - url: https://en.wikipedia.org/wiki/Lickorish%E2%80%93Wallace_theorem
same_as:
  wikidata: Q17125544
  wikipedia: Lickorish–Wallace theorem
---

## Statement

Let $M$ be a closed connected orientable [[3-manifold|R20TB2KEQQ]].
Then there is a [[link|1A5WRCNTM3]] $L \subset S^3$ such that $M$ is homeomorphic to the result of integral [[Dehn surgery|ZA405B0Z1S]] on $L$.
Moreover, $L$ can be chosen so that each component is unknotted and each surgery coefficient is $+1$ or $-1$.

## Remarks

Wallace and Lickorish proved the theorem independently, by different methods.
Idea of Lickorish's proof: write $M$ as a [[Heegaard splitting|EDE9919B5R]] whose gluing map differs from that of a standard splitting of $S^3$ by a homeomorphism of the Heegaard surface.
By the [[Dehn–Lickorish theorem|BG3EH18KRE]], this homeomorphism is isotopic to a product of Dehn twists.
Each Dehn twist can be realised by a $\pm 1$ surgery on a copy of its curve pushed slightly off the surface into $S^3$, and such a copy is unknotted.

The theorem at work: $S^2 \times S^1$ is $0$-surgery on the unknot, and the lens space $L(p, 1)$ is integral surgery with coefficient $\pm p$ on the unknot, depending on the orientation convention.
The theorem implies that every closed orientable $3$-manifold bounds a compact orientable $4$-manifold, obtained from the $4$-ball by attaching $2$-handles along $L$.

## Explanations

### L1 human

Every closed orientable $3$-dimensional space can be built from the $3$-sphere by a finite number of drill-and-refill operations along circles.
The circles can even be taken unknotted, each refilled with a single twist.
So $3$-manifolds can be drawn as pictures of links with numbers attached.

### L2 human

The theorem is the starting point of the description of $3$-manifolds by framed links, and of [[Kirby calculus|AVQ9WN1MDV]], which says when two framed links give the same manifold.
Quantum invariants of $3$-manifolds, such as the Witten–Reshetikhin–Turaev invariants, are defined from link invariants through such surgery presentations.
Its $4$-dimensional reading, that every $3$-manifold bounds a $4$-manifold built with $2$-handles, connects it with the vanishing of the oriented cobordism group in dimension $3$.
