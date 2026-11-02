---
tag: H5FQQWDJRV
kind: example
name: Calabi–Eckmann manifold
msc: [32Q55, 32J18, 53C55]
instance_of: [JSGWAN2RJV]
uses: [7GJ4STCNNM, 427N6S6QQW, CX4M8K61AB, X60JG9AEQJ]
sources:
  - url: https://en.wikipedia.org/wiki/Calabi%E2%80%93Eckmann_manifold
same_as:
  wikidata: Q5018296
  wikipedia: Calabi–Eckmann manifold
---

## Example

Let $p, q \ge 0$ be integers and let $\tau \in \C$ with $\operatorname{Im} \tau \ne 0$.
Let $W = (\C^{p+1} \setminus \set{0}) \times (\C^{q+1} \setminus \set{0})$, and let the additive group $\C$ act on $W$ by
$$t \cdot (u, v) = (e^{t} u, \; e^{\tau t} v).$$
The quotient $X_{p,q} = W / \C$ is a *Calabi–Eckmann manifold*, a compact [[complex manifold|JSGWAN2RJV]] of dimension $p + q + 1$.

Check that $X_{p,q}$ is diffeomorphic to $S^{2p+1} \times S^{2q+1}$: each orbit meets $S^{2p+1} \times S^{2q+1}$ in exactly one point.
Write $t = x + iy$.
The conditions $\abs{e^t u} = 1$ and $\abs{e^{\tau t} v} = 1$ read $x = -\log\abs{u}$ and $x \operatorname{Re}\tau - y \operatorname{Im}\tau = -\log\abs{v}$.
Since $\operatorname{Im}\tau \ne 0$, they have exactly one solution $(x, y)$.
The action is free and proper and is by holomorphic maps, so the quotient is a complex manifold of dimension $(p + 1) + (q + 1) - 1$.

## Remarks

The map $[u, v] \mapsto ([u], [v])$ makes $X_{p,q}$ a holomorphic [[fibre bundle|CX4M8K61AB]] over $\mathbb{CP}^p \times \mathbb{CP}^q$ (see [[complex projective space|7GJ4STCNNM]]) whose fibres are [[elliptic curves|427N6S6QQW]].
For $p = q = 0$ one gets an elliptic curve, and for $p = 0$ a [[Hopf manifold|Z8R2D33WSM]] diffeomorphic to $S^1 \times S^{2q+1}$.
For $p, q \ge 1$ the manifold $S^{2p+1} \times S^{2q+1}$ is simply connected and has $H^2 = 0$, so $X_{p,q}$ is not [[Kähler|X60JG9AEQJ]]: a compact Kähler manifold has a nonzero class in $H^2$.
So Calabi and Eckmann's construction gives simply connected compact complex manifolds that are not Kähler, for example on $S^3 \times S^3$.

## Explanations

### L1 human

A product of two odd-dimensional spheres, such as $S^3 \times S^3$, has no obvious complex structure, since neither factor is even-dimensional.
Calabi and Eckmann found one by viewing each sphere as a circle bundle over a complex projective space and combining the two circles into a complex torus.
The result is a compact complex manifold that cannot carry a Kähler metric.
