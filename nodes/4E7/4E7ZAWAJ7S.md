---
tag: 4E7ZAWAJ7S
kind: definition
name: Topological index
msc: [58J20, 19K56]
defines: QDCD33CS21
uses: [P4DZM975BV, MT9P2X85V8, S8GC34D5ZG, 2YDB5089FR]
sources:
  - url: https://en.wikipedia.org/wiki/Atiyah–Singer_index_theorem
---

## Definition

Let $M$ be a closed smooth manifold, with cotangent bundle $\pi \colon T^*M \to M$.
Let $P \colon C^\infty(M; E) \to C^\infty(M; F)$ be an [[elliptic operator|MT9P2X85V8]] between complex [[vector bundles|P4DZM975BV]].
Its [[principal symbol|S8GC34D5ZG]] $\sigma(P)$ is a bundle map $\pi^* E \to \pi^* F$ that is invertible outside the zero section.
So it defines a class $[\sigma(P)]$ in the compactly supported K-theory $K(T^*M)$.
Choose a smooth embedding $i \colon M \to \R^N$.
It induces a Gysin map $i_! \colon K(T^*M) \to K(T^*\R^N) = K(\R^{2N})$, and Bott periodicity identifies $K(\R^{2N})$ with $\Z$.
The *topological index* of $P$ is the integer
$$\operatorname{t-ind} P = i_! [\sigma(P)] \in \Z.$$
It does not depend on the choice of the embedding.

## Remarks

In cohomology, the topological index is the integral over $T^*M$ of $\operatorname{ch}[\sigma(P)] \cdot \pi^* \operatorname{Td}(TM \otimes \C)$, up to a sign fixed by orientation conventions.
Here $\operatorname{ch}$ is the Chern character and $\operatorname{Td}$ is the [[Todd class|2YDB5089FR]].
Let $M$ be a closed oriented Riemannian manifold of even dimension and $P = d + d^*$ from even to odd forms.
Then the topological index is the Euler number $\langle e(TM), [M] \rangle$, which is the Euler characteristic of $M$.

Example: let $P \colon C^\infty(M; E) \to C^\infty(M; F)$ be the operator of order $0$ given by a bundle isomorphism $\phi \colon E \to F$.
Its symbol is $\pi^*\phi$, which is invertible on all of $T^*M$, so $[\sigma(P)] = 0$ in $K(T^*M)$ and $\operatorname{t-ind} P = 0$.
This agrees with the analytic index, since $P$ is bijective.

Non-example: for a non-elliptic operator, the principal symbol is not invertible at some nonzero covector.
Then $\sigma(P)$ does not define a class in $K(T^*M)$, and there is no topological index.
