---
tag: Z8R2D33WSM
kind: example
name: Hopf manifold
msc: [32J18, 32Q55]
instance_of: [JSGWAN2RJV]
uses: [J5X5ED0B2Y, 0BR3FY5Q8M, X60JG9AEQJ, ST71ZV3FES]
sources:
  - url: https://en.wikipedia.org/wiki/Hopf_manifold
same_as:
  wikidata: Q5900503
  wikipedia: Hopf manifold
---

## Example

Let $n \ge 2$ and let $\lambda \in \C$ with $0 < \abs{\lambda} < 1$.
Let $W = \C^n \setminus \set{0}$ and let $\Gamma$ be the group of maps $g_k(z) = \lambda^k z$, $k \in \Z$.
The quotient $X = W / \Gamma$ is a (classical) *Hopf manifold*, a compact [[complex manifold|JSGWAN2RJV]] of dimension $n$.

Check that $X$ is a complex manifold.
The action is free: if $\lambda^k z = z$ with $z \ne 0$, then $\lambda^k = 1$, so $k = 0$.
It is [[properly discontinuous|J5X5ED0B2Y]]: a compact $K \subset W$ lies in a shell $\set{r \le \abs{z} \le R}$ with $r > 0$.
The set $g_k(K)$ lies in $\set{\abs{\lambda}^k r \le \abs{z} \le \abs{\lambda}^k R}$, which meets $K$ for only finitely many $k$.
The maps $g_k$ are holomorphic, so the [[quotient|0BR3FY5Q8M]] inherits a complex structure.
It is compact: it is the image of the compact shell $\set{\abs{\lambda} \le \abs{z} \le 1}$.

For $\lambda$ real, the map $z \mapsto (\abs{z}, z/\abs{z})$ identifies $W$ with $(0, \infty) \times S^{2n-1}$, and $\Gamma$ acts only on the first factor.
So $X$ is diffeomorphic to $S^1 \times S^{2n-1}$; the same holds for all $\lambda$.

## Remarks

$X$ is not [[Kähler|X60JG9AEQJ]].
On a compact Kähler manifold of dimension $n$ the class of the Kähler form $\omega$ in $H^2(X; \R)$ is nonzero, since $\int_X \omega^n > 0$.
But by the Künneth formula $H^2(S^1 \times S^{2n-1}; \R) = 0$ for $n \ge 2$, because $2n - 1 \ge 3$.
Also the first [[Betti number|ST71ZV3FES]] of $X$ is $1$, an odd number, which is impossible for a compact Kähler manifold.

For $n = 1$ the same construction gives $\C^* / \lambda^\Z$, an elliptic curve, which is Kähler.
For $n = 2$ one gets the primary [[Hopf surfaces|PNFNGBXRM3]] of diagonal type.

## Explanations

### L1 human

Remove the origin from $\C^n$, and declare two points the same when one is $\lambda$ times the other.
What is left is a thick spherical shell whose inner and outer spheres are glued, which is the product of a circle and a sphere.
This simple space is a compact complex manifold that admits no Kähler metric.
So compact complex geometry is much wider than Kähler geometry, and hence than projective algebraic geometry.
