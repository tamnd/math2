---
tag: 2K8BZRGE8R
kind: definition
name: Representation of a Lie group
msc: ["22E45", "22E47", "22E15"]
defines: 7JA7WH92K0
uses: [7JBRGCVJRB, 0FCHE902D7, WYGRXCG2RN]
sources:
  - url: https://en.wikipedia.org/wiki/Representation_of_a_Lie_group
---

## Definition

Let $G$ be a [[Lie group|7JBRGCVJRB]] and let $V$ be a finite-dimensional vector space over $\R$ or $\C$.
A *representation* of $G$ on $V$ is a continuous group homomorphism $\pi \colon G \to \mathrm{GL}(V)$, where $\mathrm{GL}(V)$ is the [[general linear group|0FCHE902D7]] of $V$.

Let $V$ be an infinite-dimensional complex Hilbert or Banach space.
A representation of $G$ on $V$ is a homomorphism $\pi$ from $G$ to the group of bounded invertible operators on $V$.
It must be strongly continuous: $g \mapsto \pi(g) v$ is continuous from $G$ to $V$ for each $v \in V$.

## Remarks

Example: $G = \mathrm{SO}(3)$, $V = \R^3$ and $\pi(g) = g$.
The map is the inclusion of a closed subgroup of $\mathrm{GL}_3(\R)$, so it is a continuous homomorphism.

Non-example: let $f \colon \R \to \R$ be an additive map that is not linear, which exists by choosing a basis of $\R$ over $\Q$.
Then $\pi(t) = e^{f(t)}$ is a homomorphism $\R \to \mathrm{GL}_1(\R)$, but it is not continuous, so it is not a representation of the Lie group $\R$.

A continuous homomorphism of Lie groups is automatically smooth.
So a finite-dimensional representation $\pi$ has a differential $d\pi$ at the identity, which is a representation of the Lie algebra of $G$.
If $G$ is connected, $d\pi$ determines $\pi$.
A unitary representation is one where each $\pi(g)$ preserves a fixed inner product on $V$.
