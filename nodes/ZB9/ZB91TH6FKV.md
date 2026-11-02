---
tag: ZB91TH6FKV
kind: statement
role: theorem
name: First and second variation of arc length
msc: [53C22, "58E10"]
uses: [7CBT4SM83Y, NSYMQMHPDN, 5FZDQQHQKM, JA29ETCM02, 0TH78S7GBZ]
about: [NSYMQMHPDN]
sources:
  - book: isbn:9783319917542
---

## Statement

Let $(M, g)$ be a [[Riemannian manifold|7CBT4SM83Y]] with Levi-Civita connection $\nabla$ and curvature $R(X, Y)Z = \nabla_X \nabla_Y Z - \nabla_Y \nabla_X Z - \nabla_{[X, Y]} Z$ (see [[Riemann curvature tensor|JA29ETCM02]]), and write $\ip{\cdot}{\cdot}$ for $g$.
Let $\gamma \colon [a, b] \to M$ be a smooth curve with $\abs{\gamma'(t)} = 1$ for all $t$.
Let $\Gamma \colon (-\varepsilon, \varepsilon) \times [a, b] \to M$ be a smooth map with $\Gamma(0, t) = \gamma(t)$, let $V(t) = \partial_s \Gamma(0, t)$ be its variation field, and let $L(s)$ be the [[length|0TH78S7GBZ]] of the curve $t \mapsto \Gamma(s, t)$.
Let $D_t$ and $D_s$ be the [[covariant derivatives|5FZDQQHQKM]] along the curves $t \mapsto \Gamma(s, t)$ and $s \mapsto \Gamma(s, t)$.

1. (First variation.) $$L'(0) = \Bigl[ \ip{V}{\gamma'} \Bigr]_{t=a}^{t=b} - \int_a^b \ip{V}{D_t \gamma'} \, dt.$$
2. (Second variation.) If $\gamma$ is a [[geodesic|NSYMQMHPDN]] and $V^\perp = V - \ip{V}{\gamma'}\gamma'$ is the normal part of $V$, then $$L''(0) = \int_a^b \Bigl( \abs{D_t V^\perp}^2 - \ip{R(V^\perp, \gamma')\gamma'}{V^\perp} \Bigr) dt + \Bigl[ \ip{D_s \partial_s \Gamma(0, t)}{\gamma'(t)} \Bigr]_{t=a}^{t=b}.$$

## Remarks

Both formulas come from differentiating $L(s) = \int_a^b \abs{\partial_t \Gamma(s, t)} \, dt$ under the integral sign, using the symmetry $D_s \partial_t \Gamma = D_t \partial_s \Gamma$ and metric compatibility, and integrating by parts.
The second formula also uses $D_s D_t W - D_t D_s W = R(\partial_s \Gamma, \partial_t \Gamma) W$ for vector fields $W$ along $\Gamma$.
For a proper variation, one with $\Gamma(s, a) = \gamma(a)$ and $\Gamma(s, b) = \gamma(b)$ for all $s$, the boundary terms vanish.
So a unit-speed curve is a critical point of length for all proper variations if and only if $D_t \gamma' = 0$, that is, it is a geodesic.
Example: assume all sectional curvatures are at least $k > 0$ and the geodesic $\gamma$ has length greater than $\pi / \sqrt{k}$.
Take $V = \sin\bigl(\pi (t - a)/(b - a)\bigr) E$, with $E$ a parallel unit normal field along $\gamma$.
Then $L''(0) < 0$, so $\gamma$ is not minimizing; this is the core of [[Myers's theorem|FPMJEX3DSJ]].
The second formula needs $\gamma$ to be a geodesic; otherwise extra terms involving $D_t \gamma'$ appear.

## Explanations

### L1 human

Wiggle a curve a little and watch how its length changes.
The first variation formula gives the rate of change: it vanishes for every wiggle that fixes the endpoints exactly when the curve is a geodesic.
The second variation formula gives the second derivative, which tells whether a geodesic is really a shortest path among nearby curves or only a saddle.
Positive curvature makes the second derivative smaller, so it pushes long geodesics to stop being shortest.

### L2 human

The integrand of the second variation, restricted to proper normal variations, is the index form of $\gamma$.
Its null space consists of the [[Jacobi fields|9AHMM41PJ3]] vanishing at the endpoints, so it is nondegenerate exactly when $\gamma(a)$ and $\gamma(b)$ are not [[conjugate|ZPXE5VSZ35]] along $\gamma$.
This is the bridge from curvature to global results such as the theorems of Myers, Synge and Cartan–Hadamard and the Morse index theorem.
Many texts state the same formulas for the energy $E = \tfrac{1}{2}\int \abs{\gamma'}^2 dt$ instead of the length; for unit-speed geodesics and proper normal variations the second variations agree.
