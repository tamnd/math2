---
tag: Q8FERXTZ8B
kind: statement
role: theorem
name: Banach–Stone theorem
msc: [46B04, "46E15", 46J10]
uses: [0TVJZYB6SH, 0S1FJ8VEX9, 0PARCKE8WP, 07SJXTWVQW, 0QT00PB5G2]
about: [MG3X8Y1VT4]
sources:
  - url: https://en.wikipedia.org/wiki/Banach%E2%80%93Stone_theorem
same_as:
  wikidata: Q4853767
  wikipedia: Banach–Stone theorem
---

## Statement

Let $X$ and $Y$ be [[compact|0TVJZYB6SH]] [[Hausdorff spaces|0S1FJ8VEX9]].
Let $C(X)$ and $C(Y)$ be the spaces of continuous real functions with the [[supremum norm|0PARCKE8WP]].
Let $T \colon C(X) \to C(Y)$ be a surjective [[linear isometry|07SJXTWVQW]].
Then there are a [[homeomorphism|0QT00PB5G2]] $\varphi \colon Y \to X$ and a continuous function $h \colon Y \to \set{-1, 1}$ such that
$$(T f)(y) = h(y) \, f(\varphi(y)) \quad \text{for all } f \in C(X), \ y \in Y.$$

## Remarks

The idea of the proof: the extreme points of the unit ball of the dual of $C(X)$ are the functionals $\pm \delta_x$, with $\delta_x(f) = f(x)$.
The adjoint of $T$ is an isometry of the duals and maps extreme points to extreme points.
So it sends each $\delta_y$ to $h(y) \delta_{\varphi(y)}$, and the weak-* topology makes $\varphi$ and $h$ continuous.

Example: on $X = Y = [0, 1]$, the map $(T f)(t) = -f(1 - t)$ is a surjective linear isometry.
Here $h = -1$ and $\varphi(t) = 1 - t$.

For complex scalars the same holds with $h$ a continuous function of absolute value $1$.
As a consequence, $X$ and $Y$ are homeomorphic if and only if $C(X)$ and $C(Y)$ are isometrically isomorphic.
Isometry is needed.
Let $S = \set{0} \cup \set{1/n : n \ge 1}$, a convergent sequence with its limit.
Then $C(S)$ and $C(S \times \set{1, 2})$ are linearly isomorphic, but $S$ has one limit point and $S \times \set{1, 2}$ has two.

## Explanations

### L1 human

The norm of $C(X)$ remembers the space $X$.
Every way to match $C(X)$ with $C(Y)$ that keeps distances comes from matching the points of $Y$ with the points of $X$, up to a change of sign.

### L2 human

The theorem shows that the Banach space $C(X)$, with its norm, determines the compact space $X$ up to homeomorphism.
Gelfand–Naimark theory gives a similar result for $C(X)$ as an algebra, and the Banach–Stone theorem gets it from the metric structure alone.
Without the isometry condition the result fails badly: by a theorem of Milutin, $C(X)$ is isomorphic to $C([0, 1])$ for every uncountable compact metric space $X$.
