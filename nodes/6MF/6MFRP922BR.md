---
tag: 6MFRP922BR
kind: definition
name: Jacobson topology
msc: [16D60, 46J20]
defines: WFFGB4RK60
uses: [0894J980RK, M0JDQR0V5S, 0DDA6CY7GJ, 0CNQXVBHCX]
sources:
  - url: https://en.wikipedia.org/wiki/Primitive_ideal
---

## Definition

Let $R$ be a [[ring|0894J980RK]] and let $\operatorname{Prim}(R)$ be the set of its [[primitive ideals|M0JDQR0V5S]].
For a subset $S \subseteq \operatorname{Prim}(R)$, its *kernel* is $k(S) = \bigcap_{P \in S} P$, with $k(\varnothing) = R$.
For a [[two-sided ideal|0DDA6CY7GJ]] $I$ of $R$, its *hull* is $h(I) = \set{P \in \operatorname{Prim}(R) : P \supseteq I}$.
The *Jacobson topology*, or *hull-kernel topology*, on $\operatorname{Prim}(R)$ is the [[topology|0CNQXVBHCX]] whose closure operator is
$$\overline{S} = h(k(S)).$$
Equivalently, its closed sets are exactly the hulls $h(I)$ of the two-sided ideals $I$ of $R$.

## Remarks

The map $S \mapsto h(k(S))$ satisfies the Kuratowski closure axioms, so it does define a topology.
The space $\operatorname{Prim}(R)$ is $T_0$: two distinct primitive ideals $P \ne Q$ have different closures $h(P) \ne h(Q)$.
Example: for $R = \Z$ the primitive ideals are the ideals $p\Z$ with $p$ prime.
The kernel of an infinite set of them is $0$, so its closure is all of $\operatorname{Prim}(\Z)$; the closed sets are the finite sets and the whole space.
Non-example of a closed set: $\set{p\Z : p \text{ an odd prime}}$ is not closed, because its closure contains $2\Z$.
For a commutative ring $R$, the primitive ideals are the maximal ideals and the Jacobson topology is the subspace topology from the Zariski topology on the prime spectrum.
