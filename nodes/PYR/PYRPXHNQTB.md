---
tag: PYRPXHNQTB
kind: statement
role: theorem
name: Positive mass theorem
msc: [53C21, 83C05, 83C40]
uses: [7CBT4SM83Y, ZHX2VYQDZ3, R9YWQS15AA]
about: [ZHX2VYQDZ3]
sources:
  - url: https://en.wikipedia.org/wiki/Positive_energy_theorem
---

## Statement

Let $(M, g)$ be a connected complete [[Riemannian manifold|7CBT4SM83Y]] of dimension $3$ that is asymptotically flat in the following sense.
There is a compact set $C \subset M$ and a diffeomorphism from $M \setminus C$ to $\R^3$ minus a closed ball.
In the coordinates $x = (x^1, x^2, x^3)$ it gives, for some $q > 1/2$,
$$g_{ij} - \delta_{ij} = O(\abs{x}^{-q}), \quad \partial_k g_{ij} = O(\abs{x}^{-q-1}), \quad \partial_k \partial_l g_{ij} = O(\abs{x}^{-q-2}),$$
and the [[scalar curvature|ZHX2VYQDZ3]] $R$ of $g$ is integrable on $M$.
Let the ADM mass of $(M, g)$ be
$$m = \frac{1}{16\pi} \lim_{r \to \infty} \int_{\abs{x} = r} \sum_{i,j=1}^{3} \bigl(\partial_i g_{ij} - \partial_j g_{ii}\bigr) \frac{x^j}{r} \, dA.$$
If $R \ge 0$ on $M$, then $m \ge 0$.
Moreover, $m = 0$ if and only if $(M, g)$ is [[isometric|R9YWQS15AA]] to Euclidean space $\R^3$.

## Remarks

The theorem was proved by Schoen and Yau in 1979 using minimal surfaces, and by Witten in 1981 using spinors and a Weitzenböck formula for the Dirac operator.
In Schoen and Yau's argument, if $m < 0$ one builds a complete stable minimal surface that is asymptotically a plane.
The stability inequality, together with $R \ge 0$ and the Gauss–Bonnet theorem, gives a contradiction.
Both methods extend to higher dimensions under extra hypotheses: dimension at most $7$ for minimal hypersurfaces, and spin manifolds for Witten's method.

Example: the Riemannian Schwarzschild metric $g = \bigl(1 + \frac{m}{2\abs{x}}\bigr)^4 \delta$ on $\R^3 \setminus \set{0}$, with $m > 0$, has scalar curvature $0$.
It has two asymptotically flat ends, as $\abs{x} \to \infty$ and as $\abs{x} \to 0$, and each has ADM mass $m$.
The theorem extends to manifolds with several such ends: each end has nonnegative mass.

Completeness is needed: for $m < 0$ the same formula on $\set{\abs{x} > -m/2}$ is scalar-flat and asymptotically flat with mass $m < 0$.
This metric is not complete, because the conformal factor vanishes at $\abs{x} = -m/2$, which lies at finite distance.

## Explanations

### L1 human

In general relativity, a space that has nonnegative energy density everywhere has nonnegative total mass, measured from far away.
The only way to have total mass zero is to have no gravity at all: flat space.

### L2 human

The Riemannian version above is the time-symmetric case of the positive energy theorem for initial data sets of the Einstein equations, where the condition $R \ge 0$ is the dominant energy condition.
The ADM mass is read off from the decay of the metric at infinity and does not depend on the chosen asymptotic coordinates.
The theorem is a basic tool in conformal geometry: Schoen used it to finish the solution of the Yamabe problem.
The Riemannian Penrose inequality is a sharper version that bounds the mass below by the area of a horizon.
