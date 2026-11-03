---
tag: E1E5ABP89W
kind: statement
role: theorem
name: s-cobordism theorem
msc: [57R80, 57Q10]
uses: [56YF8W9NXP, S1XK3HXHFX, T8BVGPPSZP]
about: [T8BVGPPSZP]
sources:
  - url: https://en.wikipedia.org/wiki/H-cobordism
---

## Statement

Let $n \ge 5$.
Let $W$ be a compact connected smooth $(n+1)$-manifold whose boundary is a disjoint union $\partial W = M_0 \sqcup M_1$ of closed $n$-manifolds.
Assume that both inclusions $M_i \hookrightarrow W$ are homotopy equivalences.
Let $\pi = \pi_1(M_0)$ be the [[fundamental group|S1XK3HXHFX]], let $\operatorname{Wh}(\pi)$ be its [[Whitehead group|8SY3AC4KW3]], and let $\tau(W, M_0) \in \operatorname{Wh}(\pi)$ be the [[Whitehead torsion|4QMDFYEK3T]] of the inclusion $M_0 \hookrightarrow W$.

1. $W$ is diffeomorphic to $M_0 \times [0, 1]$ relative to $M_0$ if and only if $\tau(W, M_0) = 0$.
2. For every closed connected $n$-manifold $M_0$ with fundamental group $\pi$ and every $\tau \in \operatorname{Wh}(\pi)$, there is such an h-cobordism $W$ with $\tau(W, M_0) = \tau$.
3. Two such h-cobordisms on $M_0$ are diffeomorphic relative to $M_0$ if and only if they have the same torsion.

## Remarks

The theorem is due independently to Barden, Mazur and Stallings.
The same statements hold for PL manifolds, and for topological manifolds by work of Kirby and Siebenmann.
Idea of the proof: as for the [[h-cobordism theorem|56YF8W9NXP]], take a handle decomposition and cancel handles.
Now the handle chain complex is a free based complex over $\Z[\pi]$, and the obstruction to cancelling all handles is exactly its torsion in $\operatorname{Wh}(\pi)$.

The theorem at work: $\operatorname{Wh}(1) = 0$, which gives back the h-cobordism theorem, and $\operatorname{Wh}(\Z^k) = 0$ by the [[computation for free abelian groups|KFG1HBX1NK]].
So every h-cobordism of dimension at least $6$ on a torus is a product.
For $\pi = \Z/5$ the Whitehead group is infinite cyclic, so a closed $5$-manifold with this fundamental group carries h-cobordisms that are not products.

## Explanations

### L1 human

The h-cobordism theorem needs the manifolds to have no nontrivial loops.
The s-cobordism theorem drops this hypothesis and says exactly what can go wrong.
There is one algebraic invariant, the Whitehead torsion, and the bigger manifold is a cylinder exactly when this invariant vanishes.

### L2 human

The theorem explains why surgery theory works with simple homotopy equivalences: an h-cobordism with zero torsion is an s-cobordism, and s-cobordant manifolds of dimension at least $5$ are diffeomorphic.
It is one input of the [[surgery exact sequence|Q7C480HQ9J]], where the structure set is formed up to this relation.
Whitehead torsion is computed from algebraic K-theory, since $\operatorname{Wh}(\pi)$ is a quotient of $K_1(\Z[\pi])$.
Classical examples come from lens spaces, whose distinction up to simple homotopy uses Reidemeister torsion.
