---
tag: WT5CKAY5VD
kind: definition
name: G-structure
msc: [53C10]
defines: VYNQVZ8XVF
uses: [F45VQ47GPV, F4HWTRNXAP, 8E37E74XVP]
sources:
  - url: https://en.wikipedia.org/wiki/G-structure_on_a_manifold
---

## Definition

Let $M$ be a smooth manifold of dimension $n$, and let $F(M) \to M$ be its [[frame bundle|F4HWTRNXAP]].
It is the [[principal bundle|8E37E74XVP]] with group $\mathrm{GL}(n, \R)$ whose fibre over $p$ is the set of ordered bases of $T_pM$.
Let $G$ be a [[Lie subgroup|NM8XCPS1Q3]] of $\mathrm{GL}(n, \R)$.
A *$G$-structure* on $M$ is a principal $G$-subbundle $P \subset F(M)$.
That is, $P$ is a smooth submanifold of $F(M)$ that meets every fibre and is preserved by the right action of $G$.
Moreover $G$ acts freely and transitively on each fibre of $P$.

## Remarks

Example: a Riemannian metric $g$ gives an $\mathrm{O}(n)$-structure, the bundle of $g$-orthonormal frames.
Two orthonormal frames at $p$ differ by an orthogonal matrix, so $\mathrm{O}(n)$ acts simply transitively on each fibre.
Conversely every $\mathrm{O}(n)$-structure is the orthonormal frame bundle of exactly one Riemannian metric.
A $\set{e}$-structure is a global frame, that is, a parallelization of $M$.
Non-example: the sphere $S^2$ has no $\set{e}$-structure, since a global frame would contain a nowhere vanishing vector field, which $S^2$ does not have.
Other standard cases: $\mathrm{GL}^+(n, \R)$ gives orientations, $\mathrm{GL}(m, \C) \subset \mathrm{GL}(2m, \R)$ gives almost complex structures, and $\mathrm{Sp}(2m, \R)$ gives nondegenerate $2$-forms.
A $G$-structure is called integrable, or flat, when near each point there is a chart whose coordinate frames lie in $P$.
