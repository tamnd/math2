---
tag: RF8WD9TSE7
kind: example
name: Grassmannian as classifying space
msc: [55R45, 55R15, 14M15]
instance_of: [WSZ40H5E4T]
sources:
  - url: https://en.wikipedia.org/wiki/Grassmannian
---

## Example

Let $n \ge 1$.
For $k \ge n$, let $G_n(\R^k)$ be the [[Grassmannian|CYPA882RB9]] of $n$-dimensional linear subspaces of $\R^k$.
The inclusions $\R^k \subset \R^{k+1}$ give inclusions $G_n(\R^k) \subset G_n(\R^{k+1})$, and $G_n(\R^\infty) = \bigcup_k G_n(\R^k)$ carries the weak topology of this union.
The tautological bundle
$$\gamma^n = \set{(V, v) \in G_n(\R^\infty) \times \R^\infty : v \in V}$$
is a real vector bundle of rank $n$ over $G_n(\R^\infty)$.

Let $X$ be a paracompact space.
Then $[f] \mapsto f^* \gamma^n$ is a bijection from homotopy classes of maps $X \to G_n(\R^\infty)$ to isomorphism classes of real rank $n$ bundles over $X$.
Rank $n$ real vector bundles correspond to principal $O(n)$-bundles through their bundles of orthonormal frames.
So $G_n(\R^\infty)$ is a [[classifying space|WSZ40H5E4T]] $BO(n)$ of the orthogonal group $O(n)$.
The frame bundle of $\gamma^n$ is the universal bundle; its total space is the infinite [[Stiefel manifold|W7RCXS3CHT]] $V_n(\R^\infty)$, which is contractible.

## Remarks

For $n = 1$, $G_1(\R^\infty) = \R P^\infty$, and real line bundles over a CW complex $X$ correspond to classes in $H^1(X; \Z/2\Z)$ through the first [[Stiefel–Whitney class|JQCK7A210W]].
In the same way, the complex Grassmannian $G_n(\C^\infty)$ is $BU(n)$, and $\C P^\infty = BU(1)$ classifies complex line bundles.
The cohomology ring $H^*(G_n(\R^\infty); \Z/2\Z)$ is the polynomial ring over $\Z/2\Z$ on $w_1(\gamma^n), \ldots, w_n(\gamma^n)$, which is why every mod $2$ [[characteristic class|7HACJC0JE2]] of rank $n$ bundles is a polynomial in Stiefel–Whitney classes.

## Explanations

### L1 human

A rank $n$ vector bundle over $X$ attaches an $n$-dimensional space of vectors to each point of $X$.
Place every such space inside one huge space $\R^\infty$.
Then the bundle becomes a map that sends each point of $X$ to an $n$-dimensional subspace, that is, to a point of the Grassmannian.
Conversely, any map into the Grassmannian gives a bundle: over each point of $X$, take the subspace it is sent to.
So the infinite Grassmannian lists all vector bundles of rank $n$ at once.
