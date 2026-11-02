---
tag: M0SSFESZQY
kind: definition
name: Oka manifold
msc: [32Q56]
defines: NXEAT9DMWD
uses: [JSGWAN2RJV, 3MQTWKBBBT, 0R6EWFKRCF, 7AWZJNQGT2]
sources:
  - url: https://en.wikipedia.org/wiki/Stein_manifold
---

## Definition

Let $Y$ be a [[complex manifold|JSGWAN2RJV]] with a distance function $d$ that induces its topology.
The manifold $Y$ has the *convex approximation property* if the following holds for every $n \ge 1$.
Let $K \subseteq \C^n$ be a [[compact|0R6EWFKRCF]] convex set, let $U$ be an open neighbourhood of $K$, and let $f \colon U \to Y$ be a [[holomorphic map|3MQTWKBBBT]].
Then for every $\varepsilon > 0$ there is a holomorphic map $F \colon \C^n \to Y$ with $d(F(z), f(z)) < \varepsilon$ for all $z \in K$.

The manifold $Y$ is an *Oka manifold* if it has the convex approximation property.

## Remarks

The property does not depend on the choice of $d$, since any two such distances are uniformly equivalent on a compact neighbourhood of the compact set $f(K)$.
Example: $Y = \C^m$ is Oka.
A compact convex set is polynomially convex.
So by the [[Oka–Weil theorem|7AWZJNQGT2]] each component of $f$ is a uniform limit on $K$ of polynomials, and polynomial maps $F$ approximate $f$ on $K$.
Non-example: the unit disc $D \subseteq \C$ is not Oka.
Take $n = 1$, $K = \set{\abs{z} \le 1/2}$ and $f(z) = z$; any holomorphic $F \colon \C \to D$ is bounded, hence constant by Liouville's theorem, and a constant cannot be closer than $1/2$ to $z$ at both $z = 1/2$ and $z = -1/2$.
Forstnerič proved that the convex approximation property is equivalent to the full Oka principle for maps from Stein manifolds to $Y$, with approximation and interpolation; this justifies the definition.
