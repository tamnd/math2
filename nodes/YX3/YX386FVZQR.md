---
tag: YX386FVZQR
kind: definition
name: Loewner differential equation
msc: [30C35, 30C55]
defines: 51G4QJZ345
uses: [X6XGGH5FPW, 0X3WGX95FE, 0VHNKP1N3K]
sources:
  - url: https://en.wikipedia.org/wiki/Loewner_differential_equation
---

## Definition

Let $\mathbb{H} = \set{z \in \C : \operatorname{Im} z > 0}$ be the [[upper half-plane|X6XGGH5FPW]], and let $U \colon [0, \infty) \to \R$ be a [[continuous function|0X3WGX95FE]], the *driving function*.
The *chordal Loewner differential equation* with driving function $U$ is the initial value problem
$$\frac{\partial}{\partial t} g_t(z) = \frac{2}{g_t(z) - U(t)}, \qquad g_0(z) = z,$$
for each $z \in \overline{\mathbb{H}}$.
For each $z$, let $T_z \in (0, \infty]$ be the supremum of the times up to which the solution exists with $g_t(z) - U(t) \ne 0$; for $z = U(0)$ set $T_z = 0$.
For $t \ge 0$, the *hull* at time $t$ is $K_t = \set{z \in \mathbb{H} : T_z \le t}$.

## Remarks

For each $t$, the map $g_t$ is a [[conformal map|0VHNKP1N3K]] of $\mathbb{H} \setminus K_t$ onto $\mathbb{H}$ with the normalisation $g_t(z) = z + \frac{2t}{z} + O(\abs{z}^{-2})$ as $z \to \infty$.
The hulls $K_t$ increase with $t$, and the number $2t$ is their half-plane capacity.
Example: for $U = 0$, the equation gives $\partial_t (g_t(z)^2) = 4$, so $g_t(z) = \sqrt{z^2 + 4t}$ with the branch that maps $\mathbb{H}$ into $\mathbb{H}$.
A point $iy$ with $y > 0$ has $g_t(iy)^2 = 4t - y^2$, which reaches $0 = U(t)$ at $t = y^2/4$; so $K_t$ is the vertical segment from $0$ to $2i\sqrt{t}$.
Non-example: the translations $f_t(z) = z + t$ are conformal self-maps of $\mathbb{H}$, but they do not come from the equation, since $f_t(z) - z = t$ does not tend to $0$ at infinity.
The *radial* Loewner equation, which Loewner introduced first, is the analogue for the unit disc, with a driving function with values on the unit circle and maps normalised at $0$.

## Explanations

### L1 human

Each point of the half-plane flows according to a simple rule: it is pushed away from the moving point $U(t)$ on the real line, faster when it is closer.
A point that is pushed into $U(t)$ is swallowed and becomes part of the hull.
The equation turns a real function of time into a growing set in the plane and a family of maps that straighten it out.
