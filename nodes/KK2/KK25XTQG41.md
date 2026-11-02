---
tag: KK25XTQG41
kind: definition
name: Sub-Riemannian manifold
msc: [53C17]
defines: 97NYHNBZ2D
uses: [F45VQ47GPV, WY6K3P4YCG, 68FGQEBD6J, 0NB0AWGJBW]
sources:
  - url: https://en.wikipedia.org/wiki/Sub-Riemannian_manifold
---

## Definition

Let $M$ be a connected [[smooth manifold|F45VQ47GPV]] with [[tangent bundle|WY6K3P4YCG]] $TM$.
A *sub-Riemannian manifold* is a triple $(M, H, g)$ such that:

1. $H \subseteq TM$ is a smooth subbundle, the horizontal distribution;
2. $H$ is bracket-generating: at each $p \in M$, the vector fields tangent to $H$ and their iterated [[Lie brackets|68FGQEBD6J]] span $T_pM$;
3. $g$ assigns to each $p \in M$ an [[inner product|0NB0AWGJBW]] $g_p$ on the fibre $H_p$, depending smoothly on $p$.

A horizontal curve is an absolutely continuous curve $\gamma$ with $\gamma'(t) \in H_{\gamma(t)}$ for almost every $t$.
The sub-Riemannian distance $d(p, q)$ is the infimum of $\int \sqrt{g(\gamma', \gamma')} \, dt$ over the horizontal curves from $p$ to $q$.

## Remarks

Example: the Heisenberg group is $\R^3$ with $H$ spanned by $X = \partial_x - \tfrac{y}{2} \partial_z$ and $Y = \partial_y + \tfrac{x}{2} \partial_z$, with $X, Y$ orthonormal.
Here $[X, Y] = \partial_z$, so $X, Y, [X, Y]$ span $T_p\R^3$ at each point, and clause 2 holds.

Non-example: on $\R^3$, let $H$ be spanned by $\partial_x$ and $\partial_y$.
All brackets of fields tangent to $H$ stay in $H$, so clause 2 fails; horizontal curves stay in the planes $z = \text{const}$, and points with different $z$ are at infinite distance.

When $H = TM$, the definition gives a Riemannian manifold.
Some authors do not require clause 2 in the definition and add it as a hypothesis when needed.
