---
tag: 97GRC6YGF5
kind: definition
name: Principal bundle
msc: [55R10, 53C05]
defines: 8E37E74XVP
uses: [CX4M8K61AB, 0WCY42EV9V, F45VQ47GPV]
sources:
  - url: https://en.wikipedia.org/wiki/Principal_bundle
---

## Definition

Let $G$ be a [[Lie group|7JBRGCVJRB]] and let $M$ be a [[smooth manifold|F45VQ47GPV]].
A *principal $G$-bundle* over $M$ is a smooth [[fiber bundle|CX4M8K61AB]] $\pi \colon P \to M$ together with a smooth right [[action|0WCY42EV9V]] $P \times G \to P$, $(u, g) \mapsto u \cdot g$, such that:

1. the action preserves fibers: $\pi(u \cdot g) = \pi(u)$ for all $u \in P$ and $g \in G$;
2. every point of $M$ has an open neighbourhood $U$ and a diffeomorphism $\varphi \colon \pi^{-1}(U) \to U \times G$ with $\operatorname{pr}_1 \circ \varphi = \pi$ and $\varphi(u \cdot g) = \varphi(u) \cdot g$, where $G$ acts on $U \times G$ by $(x, h) \cdot g = (x, hg)$.

## Remarks

The product $M \times G$ with $(x, h) \cdot g = (x, hg)$ is a principal $G$-bundle, the trivial one.
The map $\R \to S^1$, $t \mapsto e^{2\pi i t}$, with $\Z$ acting by $t \cdot n = t + n$, is a principal $\Z$-bundle.
The Hopf map $S^3 \to S^2$ is a principal $U(1)$-bundle.

Non-example: the circle group acts on $S^2$ by rotations about the vertical axis.
This action preserves the fibers of the identity map $S^2 \to S^2$, but these fibers are points, not copies of the circle.
More generally, an action with a fixed point cannot be part of a principal bundle structure, because clause 2 forces $G$ to act freely.

Clause 2 implies that $G$ acts freely and transitively on each fiber.
Conversely, for a free and proper smooth action of a Lie group $G$ on a manifold $P$, the quotient map $P \to P/G$ is a principal $G$-bundle.
The same definition with topological groups and homeomorphisms gives topological principal bundles.

## Explanations

### L1 human

A principal bundle is a fiber bundle whose fibers are copies of a group, on which the group acts by right multiplication in a way compatible with local trivializations.
