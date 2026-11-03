---
tag: HGQTBHFFFJ
kind: definition
name: Kretschmann scalar
msc: ["83C75", "53C50", "53B30"]
defines: 62JFWFJ20F
uses: [GH6CXWFNDJ, JA29ETCM02]
sources:
  - url: https://en.wikipedia.org/wiki/Kretschmann_scalar
---

## Definition

Let $(M, g)$ be a [[pseudo-Riemannian manifold|GH6CXWFNDJ]] and let $R_{abcd}$ be the components of its [[Riemann curvature tensor|JA29ETCM02]] in local coordinates.
The *Kretschmann scalar* of $(M, g)$ is the smooth function
$$K = R_{abcd} R^{abcd} = g^{ae} g^{bf} g^{cg} g^{dh} R_{abcd} R_{efgh},$$
with summation over repeated indices.

## Remarks

The value of $K$ at a point does not depend on the coordinates, since it is a full contraction of tensors.

Example: for the [[Schwarzschild metric|6Y50T68WKY]] of mass $M$, in units $G = c = 1$, a computation of the curvature components gives
$$K = \frac{48 M^2}{r^6}.$$
At the horizon $r = 2M$ this is $3/(4M^4)$, which is finite, while $K \to \infty$ as $r \to 0$.

Non-example: the Ricci scalar $R = g^{ac} g^{bd} R_{abcd}$ is a different invariant.
For the Schwarzschild metric it is $0$ everywhere, so it does not detect the curvature that $K$ detects.

In a Riemannian manifold $K \ge 0$, and $K = 0$ exactly where the curvature tensor vanishes.
In a Lorentzian manifold $K$ can vanish where the curvature does not, for example in plane gravitational wave spacetimes.
