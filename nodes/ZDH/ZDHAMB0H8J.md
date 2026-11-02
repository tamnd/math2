---
tag: ZDHAMB0H8J
kind: definition
name: Manifold of smooth mappings
msc: [58D15, 46T10, 58B10]
defines: BW12J14X0Z
uses: [F45VQ47GPV, Q61VFHCH2J, Y7Z0AGY1A7, WWX7H5W1RP, 3GAA614673, EBMCFQT0JN, DQB1BVQJWD]
sources:
  - url: https://en.wikipedia.org/wiki/Banach_manifold
---

## Definition

Let $M$ be a compact [[smooth manifold|F45VQ47GPV]] without boundary and $N$ a smooth manifold, and let $C^\infty(M, N)$ be the set of smooth maps $M \to N$.
Fix a [[Riemannian metric|Q61VFHCH2J]] on $N$, and let $\pi \colon TN \to N$ be the [[tangent bundle|DQB1BVQJWD]].
Fix an open neighbourhood $V$ of the zero section in $TN$ on which the [[exponential map|Y7Z0AGY1A7]] is defined.
Choose $V$ so that $(\pi, \exp) \colon V \to N \times N$ is a diffeomorphism onto an open neighbourhood $W$ of the diagonal.
For $f \in C^\infty(M, N)$, let $\Gamma(f^* TN)$ be the space of smooth [[sections|WWX7H5W1RP]] of the pullback bundle.
These are the smooth maps $s \colon M \to TN$ with $s(x) \in T_{f(x)} N$ for all $x$.
With the topology of uniform convergence of all derivatives, $\Gamma(f^* TN)$ is a Fréchet space.
Let $U_f = \set{g \in C^\infty(M, N) : (f(x), g(x)) \in W \text{ for all } x \in M}$ and define $\varphi_f \colon U_f \to \Gamma(f^* TN)$ by
$$\varphi_f(g)(x) = (\pi, \exp)^{-1}(f(x), g(x)).$$
The *manifold of smooth mappings* is $C^\infty(M, N)$ with the smooth [[Fréchet manifold|EBMCFQT0JN]] structure given by the atlas $(U_f, \varphi_f)_{f \in C^\infty(M, N)}$.

## Remarks

Each $\varphi_f$ is a bijection onto an open subset of $\Gamma(f^* TN)$, with inverse $s \mapsto \exp \circ s$, and the chart changes are smooth.
The resulting manifold structure does not depend on the choice of the metric, its topology is the $C^\infty$ topology, and the tangent space at $f$ is $\Gamma(f^* TN)$.

Example: for $M = N = S^1 = \R / 2\pi\Z$ with the flat metric, take $V$ to be the vectors of length less than $\pi$.
For the identity map $f$, the chart sends $g$ near $f$ to the function $s$ with $g(x) = x + s(x)$ and $\abs{s(x)} < \pi$.
So near the identity, the diffeomorphisms of the circle correspond to small smooth functions on the circle.

Non-example: in the same setting, let $f$ be the constant map at a point $y$, and $g$ the constant map at the antipodal point $y + \pi$.
Then $(f(x), g(x)) = (y, y + \pi)$ is a pair at distance $\pi$, so it lies outside $W$, so $g$ is not in the chart domain $U_f$; it lies in a different chart.


When $\dim M \ge 1$ and $\dim N \ge 1$, the model spaces are Fréchet spaces that are not normable, so this atlas is not an atlas of a Banach manifold.
