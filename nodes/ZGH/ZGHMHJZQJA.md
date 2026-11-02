---
tag: ZGHMHJZQJA
kind: definition
name: Parallelizable manifold
msc: [57R25, 57R22]
defines: 7WX14GWD4M
uses: [F45VQ47GPV, WY6K3P4YCG, 0299VCW1TH]
sources:
  - url: https://en.wikipedia.org/wiki/Parallelizable_manifold
---

## Definition

Let $M$ be a [[smooth manifold|F45VQ47GPV]] of dimension $n$.
A *global frame* on $M$ is a list $V_1, \dots, V_n$ of smooth [[vector fields|0299VCW1TH]] on $M$ with the following property.
For every $p \in M$, the vectors $V_1(p), \dots, V_n(p)$ form a basis of the tangent space $T_pM$.
The manifold $M$ is *parallelizable* if it has a global frame.

## Remarks

Equivalently, the [[tangent bundle|WY6K3P4YCG]] $TM$ is isomorphic, as a smooth vector bundle, to the trivial bundle $M \times \R^n$; a global frame gives the isomorphism $(p, a) \mapsto \sum_i a_i V_i(p)$.
Example: the circle $S^1 \subseteq \R^2$ is parallelizable.
The vector field $V(x, y) = (-y, x)$ is tangent to $S^1$ and nonzero at every point, so it is a global frame for the $1$-dimensional manifold $S^1$.
Every Lie group is parallelizable, by translating a basis of the tangent space at the identity.
Non-example: $S^2$ is not parallelizable.
A global frame would contain a nowhere-vanishing vector field, and by the hairy ball theorem no such field exists on $S^2$.
A parallelizable manifold is orientable, so the Möbius band is not parallelizable either.
