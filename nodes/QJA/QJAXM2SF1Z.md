---
tag: QJAXM2SF1Z
kind: definition
name: Spectrum of a ring
msc: [14A05, 13A15]
defines: FB45BHHA2J
uses: [0310REJJY8, 00MHHZ9SNE, 8SQK7RTB63, 0VTH8KPCG2]
sources:
  - url: https://en.wikipedia.org/wiki/Spectrum_of_a_ring
---

## Definition

Let $R$ be a [[commutative ring|0310REJJY8]].
The *spectrum* of $R$ is the set
$$\operatorname{Spec} R = \set{\mathfrak p : \mathfrak p \text{ is a prime ideal of } R},$$
equipped with the [[Zariski topology|8SQK7RTB63]], whose closed sets are the sets $V(E) = \set{\mathfrak p \in \operatorname{Spec} R : E \subseteq \mathfrak p}$ for subsets $E \subseteq R$.

## Remarks

A [[ring homomorphism|0VTH8KPCG2]] $f \colon R \to A$ induces the map $\operatorname{Spec} A \to \operatorname{Spec} R$, $\mathfrak q \mapsto f^{-1}(\mathfrak q)$.
It is continuous, since the preimage of $V(E)$ is $V(f(E))$.

Example: $\operatorname{Spec} \Z$ consists of $(0)$ and the ideals $p\Z$ for the prime numbers $p$.
The spectrum of a field $k$ is a single point $(0)$.
The spectrum of $\Z/n\Z$ for $n \ge 2$ is the finite set of ideals $p\Z/n\Z$ for the primes $p$ dividing $n$.

Non-example: the ring $R$ itself is not a point of $\operatorname{Spec} R$, because a [[prime ideal|00MHHZ9SNE]] is by definition a proper ideal.
So the zero ring has empty spectrum.

Every nonzero ring has a [[maximal ideal|0PV74TR5FP]], which is prime, so $\operatorname{Spec} R \ne \emptyset$ when $R \ne 0$.
