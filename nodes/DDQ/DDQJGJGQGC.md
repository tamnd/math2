---
tag: DDQJGJGQGC
kind: statement
role: theorem
name: Cartan's theorem on continuous homomorphisms
msc: ["22E15"]
uses: [7JBRGCVJRB, 9J5PQMG3HJ, 3NJGY8QSTE]
about: [7JBRGCVJRB]
sources:
  - url: https://en.wikipedia.org/wiki/Closed-subgroup_theorem
---

## Statement

Let $G$ and $H$ be real [[Lie groups|7JBRGCVJRB]].
Let $\varphi \colon G \to H$ be a [[continuous group homomorphism|9J5PQMG3HJ]].
Then $\varphi$ is smooth; in fact it is real-analytic.

## Remarks

The graph $\Gamma = \set{(g, \varphi(g)) : g \in G}$ is a subgroup of $G \times H$, and it is closed since $\varphi$ is continuous.
By the [[closed subgroup theorem|3NJGY8QSTE]], $\Gamma$ is an embedded Lie subgroup.
The projection $\Gamma \to G$ is a bijective smooth homomorphism; such a map has constant rank, so it is a diffeomorphism, and $\varphi$ is its inverse followed by the smooth projection $\Gamma \to H$.
Example: a continuous homomorphism $\varphi \colon \R \to \R$ satisfies $\varphi(x + y) = \varphi(x) + \varphi(y)$ and is therefore $\varphi(x) = cx$, which is smooth.
Continuity is necessary: using a basis of $\R$ as a vector space over $\Q$, there are additive maps $\R \to \R$ that are not continuous, hence not smooth.

## Explanations

### L1 human

For a map between Lie groups that respects the group laws, mere continuity already forces smoothness.
So the smooth structure of a Lie group adds nothing beyond its topology and group law.

### L2 human

A direct consequence is that a topological group carries at most one smooth structure making it a Lie group.
Indeed, the identity map between two such structures is a continuous homomorphism, so it is a diffeomorphism.
This is why one can speak of "the" Lie group structure of a group such as $SO(n)$.
It also means continuous representations of Lie groups on finite-dimensional spaces are automatically smooth, so their differentials give representations of the Lie algebra.
The question of which topological groups admit a Lie group structure at all is Hilbert's fifth problem.
