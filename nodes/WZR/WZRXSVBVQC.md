---
tag: WZRXSVBVQC
kind: definition
name: Continuous group homomorphism
msc: [22A05]
defines: 9J5PQMG3HJ
uses: [92700QAB5Y, 0JYTG5K9Y4, 0VGFHTM75Y]
sources:
  - url: https://en.wikipedia.org/wiki/Topological_group
---

## Definition

Let $G$ and $H$ be [[topological groups|92700QAB5Y]].
A *continuous group homomorphism* from $G$ to $H$ is a map $f \colon G \to H$ such that:

1. $f$ is a [[group homomorphism|0JYTG5K9Y4]], that is, $f(xy) = f(x) f(y)$ for all $x, y \in G$;
2. $f$ is [[continuous|0VGFHTM75Y]].

## Remarks

Example: $f \colon (\R, +) \to (\C \setminus \set{0}, \cdot)$, $f(t) = e^{2\pi i t}$.
It satisfies $f(s + t) = f(s) f(t)$, and it is continuous as a composition of continuous functions.
Non-example: the identity map from $(\R, +)$ with the usual topology to $(\R, +)$ with the discrete topology.
It is a homomorphism, but the preimage of the open set $\set{0}$ is $\set{0}$, which is not open in the usual topology.
A homomorphism $f$ is continuous if and only if it is continuous at the identity $e$ of $G$.
Indeed, near a point $a$ one writes $f(x) = f(a) f(a^{-1} x)$ and uses that translations are homeomorphisms.
