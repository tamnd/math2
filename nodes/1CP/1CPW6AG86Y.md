---
tag: 1CPW6AG86Y
kind: definition
name: Homogeneous space
msc: [14M17, 14L30]
defines: 85TWR6E75P
uses: [RW85C34GQW, GH81SYAPPN, 02GK6HZYBT, 0AYMP41THN]
sources:
  - url: https://en.wikipedia.org/wiki/Homogeneous_space
---

## Definition

Let $k$ be an algebraically closed field, and let $G$ be an [[algebraic group|GH81SYAPPN]] over $k$.
A *homogeneous space* for $G$ is a nonempty variety $X$ over $k$ with an [[action|RW85C34GQW]] of $G$ such that $G(k)$ acts [[transitively|02GK6HZYBT]] on $X(k)$.

## Remarks

Let $x \in X(k)$ and let $G_x$ be its [[stabilizer|0AYMP41THN]], a closed subgroup of $G$.
The orbit map $g \mapsto g \cdot x$ induces a bijective morphism $G / G_x \to X$.
In characteristic $0$ this morphism is an isomorphism, so $X \cong G / G_x$.
In characteristic $p$ it can fail to be an isomorphism, because the orbit map need not be separable.

Example: $\mathrm{GL}_{n+1}$ acts on $\mathbb{P}^n$ by $g \cdot [v] = [g v]$.
Any nonzero vector can be sent to any other by an invertible matrix, so the action is transitive and $\mathbb{P}^n$ is a homogeneous space.

Non-example: $\mathbb{G}_m$ acts on $\mathbb{A}^1$ by $t \cdot x = t x$.
There are two orbits, $\set{0}$ and $\mathbb{A}^1 \setminus \set{0}$, so the action is not transitive.

In other settings, such as Lie groups and topological groups, a homogeneous space is a manifold or a space with a transitive action of the group.
