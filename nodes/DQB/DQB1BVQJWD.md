---
tag: DQB1BVQJWD
kind: definition
name: Tangent bundle
msc: [58A05]
defines: WY6K3P4YCG
uses: [F45VQ47GPV, 0V33BNKZ9S]
sources:
  - url: https://en.wikipedia.org/wiki/Tangent_bundle
---

## Definition

Let $M$ be a [[smooth manifold|F45VQ47GPV]] of dimension $n$, and let $C^\infty(M)$ be the algebra of [[smooth functions|0V33BNKZ9S]] $M \to \R$.
For $p \in M$, a *tangent vector* at $p$ is a linear map $v \colon C^\infty(M) \to \R$ such that $v(fg) = f(p)\, v(g) + g(p)\, v(f)$ for all $f, g \in C^\infty(M)$; that is, a derivation at $p$.
The tangent vectors at $p$ form a real vector space $T_pM$, the *tangent space* at $p$.
The *tangent bundle* of $M$ is the disjoint union
$$TM = \bigsqcup_{p \in M} T_pM = \set{(p, v) : p \in M, \ v \in T_pM},$$
with the projection $\pi \colon TM \to M$, $\pi(p, v) = p$.
Let $(U, (x^1, \ldots, x^n))$ be a chart of $M$.
$TM$ has a unique smooth structure in which each such chart gives a chart on $\pi^{-1}(U)$, namely
$$(p, v) \mapsto \big(x^1(p), \ldots, x^n(p), v^1, \ldots, v^n\big), \qquad v = \sum_{i=1}^n v^i \left.\frac{\partial}{\partial x^i}\right|_p.$$

## Remarks

Each $T_pM$ has dimension $n$, with basis $\partial/\partial x^1|_p, \ldots, \partial/\partial x^n|_p$ for any chart around $p$, so $TM$ is a smooth manifold of dimension $2n$.
For $M = \R^n$ a single chart covers everything, and $T\R^n = \R^n \times \R^n$.
For the circle $S^1$, the vector field $\partial/\partial\theta$ is nowhere zero, and $TS^1$ is diffeomorphic to $S^1 \times \R$.

The tangent bundle of $S^2$ is not isomorphic, as a vector bundle, to the product $S^2 \times \R^2$.
By the hairy ball theorem every tangent vector field on $S^2$ vanishes somewhere, while $S^2 \times \R^2$ has nowhere zero sections.

Other common definitions of $T_pM$ use equivalence classes of curves through $p$, or vectors in coordinates that change by the Jacobian matrix; they give isomorphic spaces.

## Explanations

### L1 human

The tangent bundle is the set of all pairs made of a point of the manifold and a tangent vector at that point.
