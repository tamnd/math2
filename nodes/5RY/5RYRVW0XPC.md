---
tag: 5RYRVW0XPC
kind: definition
name: Frame bundle
msc: [58A32, 53C10]
defines: F4HWTRNXAP
uses: [WY6K3P4YCG, 8E37E74XVP, 0FCHE902D7, 0KCQ9Y3QKA]
sources:
  - url: https://en.wikipedia.org/wiki/Frame_bundle
---

## Definition

Let $M$ be a smooth manifold of dimension $n$ with [[tangent bundle|WY6K3P4YCG]] $TM$.
A *frame* at $p \in M$ is an ordered [[basis|0KCQ9Y3QKA]] $e = (e_1, \ldots, e_n)$ of the tangent space $T_pM$.
The *frame bundle* of $M$ is the set
$$F(M) = \set{(p, e) : p \in M, \ e \text{ a frame at } p}.$$
It comes with the projection $\pi(p, e) = p$ and the right action of the [[general linear group|0FCHE902D7]] $GL(n, \R)$ given by
$$(p, e) \cdot g = (p, e g), \qquad (e g)_j = \sum_{i=1}^{n} g_{ij} \, e_i.$$
For a chart $(U, x)$ of $M$ and a frame $e$ at $p \in U$, let $A$ be the matrix with $e_j = \sum_i A_{ij} \, \partial/\partial x^i|_p$.
$F(M)$ carries the smooth structure for which each map $(p, e) \mapsto (p, A)$ is a diffeomorphism $\pi^{-1}(U) \to U \times GL(n, \R)$.
With this structure $F(M)$ is a [[principal|8E37E74XVP]] $GL(n, \R)$-bundle over $M$.

## Remarks

For $M = \R^n$, a frame at $p$ is the same as an invertible matrix, so $F(\R^n) = \R^n \times GL(n, \R)$.
Check of the action: $(e g) h = e (g h)$, because $((eg)h)_k = \sum_j h_{jk} \sum_i g_{ij} e_i = \sum_i (gh)_{ik} e_i$.

A tuple $(e_1, \ldots, e_n)$ of tangent vectors at $p$ that is linearly dependent, such as $e_1 = e_2$, is not a frame and is not a point of $F(M)$.

If $M$ is a Riemannian manifold, the orthonormal frames form the orthonormal frame bundle, a principal $O(n)$-bundle.
The same construction applies to any vector bundle $E$ of rank $k$ and gives a principal $GL(k, \R)$-bundle.

## Explanations

### L1 human

The frame bundle of a manifold is the set of all pairs made of a point and an ordered basis of the tangent space at that point.
