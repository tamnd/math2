---
tag: HVA7TFK9XR
kind: definition
name: Topological quantum field theory
msc: [57R56, 81T45, 57K16]
defines: DAP92B80J2
uses: [7DS6B2BFK8, 702SNFQG0W, 0Z1Y7JHGBR, 05EGHEQZAW, 0RJF668P1T, 0G31VJ5YS5, 0M856Q1AMZ]
sources:
  - url: https://en.wikipedia.org/wiki/Topological_quantum_field_theory
---

## Definition

Let $n \ge 0$ be an integer and let $k$ be a field.
All manifolds below are smooth, compact and [[oriented|702SNFQG0W]].
For closed $n$-manifolds $\Sigma_0$ and $\Sigma_1$, a *cobordism* from $\Sigma_0$ to $\Sigma_1$ is an $(n+1)$-[[manifold with boundary|7DS6B2BFK8]] $M$ with an orientation-preserving [[diffeomorphism|0Z1Y7JHGBR]] $\partial M \to \overline{\Sigma_0} \sqcup \Sigma_1$.
Here $\overline{\Sigma}$ is $\Sigma$ with the opposite orientation.
An $(n+1)$-dimensional *topological quantum field theory* $Z$ over $k$ assigns two kinds of data.
To each closed $n$-manifold $\Sigma$ it assigns a finite-dimensional [[vector space|05EGHEQZAW]] $Z(\Sigma)$ over $k$.
To each cobordism $M$ from $\Sigma_0$ to $\Sigma_1$ it assigns a [[linear map|0RJF668P1T]] $Z(M) \colon Z(\Sigma_0) \to Z(\Sigma_1)$.
These data satisfy the following axioms.

1. Each orientation-preserving diffeomorphism $f \colon \Sigma \to \Sigma'$ gives a linear isomorphism $Z(f) \colon Z(\Sigma) \to Z(\Sigma')$, with $Z(f' \circ f) = Z(f') \circ Z(f)$.
   Diffeomorphic cobordisms, by a diffeomorphism compatible with the boundaries, give equal maps after these isomorphisms.
2. Let $M$ be a cobordism from $\Sigma_0$ to $\Sigma_1$, and $M'$ one from $\Sigma_1$ to $\Sigma_2$.
   Let $M' \cup_{\Sigma_1} M$ be the cobordism obtained by gluing them along $\Sigma_1$.
   Then $Z(M' \cup_{\Sigma_1} M) = Z(M') \circ Z(M)$.
3. For each $\Sigma$, the cylinder $\Sigma \times [0, 1]$ gives the identity map of $Z(\Sigma)$.
4. The empty $n$-manifold gives $Z(\emptyset) = k$, and disjoint unions give natural isomorphisms $Z(\Sigma \sqcup \Sigma') \cong Z(\Sigma) \otimes Z(\Sigma')$ under which $Z(M \sqcup M') = Z(M) \otimes Z(M')$, where $\otimes$ is the [[tensor product|0G31VJ5YS5]] over $k$.

## Remarks

A closed $(n+1)$-manifold $M$ is a cobordism from $\emptyset$ to $\emptyset$, so $Z(M)$ is a linear map $k \to k$, that is, a number $Z(M) \in k$.
By clause 1 this number is a diffeomorphism invariant of $M$.
The axioms imply that $Z(\overline{\Sigma})$ is the [[dual space|0M856Q1AMZ]] of $Z(\Sigma)$.
In the language of categories, a topological quantum field theory is a symmetric monoidal functor from the category of $(n+1)$-dimensional cobordisms to the category of vector spaces over $k$.
Example: let $n = 0$ and let $V$ be a finite-dimensional vector space.
Set $Z(+) = V$ for the positive point and $Z(-) = V^*$, and extend to finite sets of points by tensor products.
An arc from $\emptyset$ to $\set{+, -}$ gives the element of $V \otimes V^*$ that corresponds to $\id_V$, an arc from $\set{+, -}$ to $\emptyset$ gives evaluation $V \otimes V^* \to k$, and straight arcs give identities.
These choices satisfy the axioms, and the circle, which is the composite of the two arcs, gets the number $Z(S^1) = \dim V$.
Non-example: set $Z(\Sigma) = k$ for all $\Sigma$ and let every cobordism act as multiplication by $2$.
Then the cylinder $\Sigma \times [0, 1]$ gives multiplication by $2$, not the identity, so clause 3 fails.
In dimension $1 + 1$, topological quantum field theories correspond to commutative Frobenius algebras over $k$.
