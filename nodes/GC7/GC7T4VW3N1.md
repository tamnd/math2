---
tag: GC7T4VW3N1
kind: definition
name: Lie group action
msc: [57S20, 22F05, "22E15"]
defines: 96B4E2GPKJ
uses: [7JBRGCVJRB, F45VQ47GPV, 0WCY42EV9V, 0V33BNKZ9S]
sources:
  - url: https://en.wikipedia.org/wiki/Lie_group_action
---

## Definition

Let $G$ be a [[Lie group|7JBRGCVJRB]] with identity $e$ and let $M$ be a [[smooth manifold|F45VQ47GPV]].
A *(left) Lie group action* of $G$ on $M$ is a map $\alpha \colon G \times M \to M$, written $\alpha(g, p) = g \cdot p$, such that:

1. $e \cdot p = p$ for all $p \in M$;
2. $g \cdot (h \cdot p) = (gh) \cdot p$ for all $g, h \in G$ and $p \in M$;
3. $\alpha$ is [[smooth|0V33BNKZ9S]].

## Remarks

Clauses 1 and 2 say that $\alpha$ is a [[group action|0WCY42EV9V]]; clause 3 is the smoothness condition.
Right actions are defined in the same way with $(p \cdot h) \cdot g = p \cdot (hg)$.

Example: $SO(2)$ acts on $\R^2$ by $A \cdot v = Av$.
The identity matrix fixes every vector, $(AB)v = A(Bv)$, and the map $(A, v) \mapsto Av$ is polynomial in the entries, hence smooth.

Non-example: let $G = \R$ act on $M = \R$ by $t \cdot x = (x^3 + t)^{1/3}$, with the real cube root.
This is a group action, since $s \cdot (t \cdot x) = (x^3 + t + s)^{1/3}$, and it is continuous.
It is not smooth: the map $t \mapsto t \cdot 0 = t^{1/3}$ is not differentiable at $t = 0$.

Each $g$ acts by a diffeomorphism of $M$ with inverse given by $g^{-1}$.
