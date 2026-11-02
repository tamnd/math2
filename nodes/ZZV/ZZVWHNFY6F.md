---
tag: ZZVWHNFY6F
kind: statement
role: theorem
name: Stein–Tomas restriction theorem
msc: [42B10, 42B20]
uses: [SYP1ATSTTH, DPVM34ADZV, SASP14MA1Z, SQVQ5DQT6W, CG9JEATW3Q]
about: [DPVM34ADZV]
sources:
  - url: https://en.wikipedia.org/wiki/Restriction_conjecture
---

## Statement

Let $n \ge 2$ and let $S \subseteq \R^n$ be a compact smooth hypersurface, possibly with boundary, whose [[Gaussian curvature|SQVQ5DQT6W]] is nonzero at every point.
Let $\sigma$ be the surface measure on $S$, and let $\hat f$ be the [[Fourier transform|DPVM34ADZV]] of $f$.
Let
$$1 \le p \le \frac{2(n + 1)}{n + 3}.$$
Then there is a constant $C$ such that
$$\Big( \int_S \abs{\hat f(\xi)}^2 \, d\sigma(\xi) \Big)^{1/2} \le C \norm{f}_{L^p(\R^n)}$$
for every [[Schwartz function|CG9JEATW3Q]] $f$ on $\R^n$.
So the restriction map $f \mapsto \hat f|_S$ extends to a bounded operator from $L^p(\R^n)$ to $L^2(S, \sigma)$.

## Remarks

By duality, the estimate is equivalent to $\norm{\widehat{g \, d\sigma}}_{L^{p'}(\R^n)} \le C \norm{g}_{L^2(S)}$, with $1/p + 1/p' = 1$.
A $TT^*$ argument reduces this to the bound $\norm{f * \hat\sigma}_{L^{p'}} \le C^2 \norm{f}_{L^p}$.
One splits $\hat\sigma$ into dyadic pieces in $\abs{x}$.
Each piece is bounded from $L^1$ to $L^\infty$ by the [[decay of the Fourier transform of surface measure|SYP1ATSTTH]], and on $L^2$ by the size of its Fourier transform.
Interpolating these two bounds, the pieces sum when $p < 2(n+1)/(n+3)$.
Peter Tomas proved the range $p < 2(n + 1)/(n + 3)$, and Elias Stein obtained the endpoint.

Example: for the circle in $\R^2$ the range is $1 \le p \le 6/5$, and for the sphere in $\R^3$ it is $1 \le p \le 4/3$.

The exponent $2(n + 1)/(n + 3)$ is sharp for the $L^2(S)$ norm on the left.
The Knapp example takes $\hat f$ to be a smooth bump adapted to a cap of $S$ of radius $\delta$.
Such a cap lies in a slab of thickness about $\delta^2$.
Comparing both sides as $\delta \to 0$ forces $p \le 2(n+1)/(n+3)$.
Without curvature, for a flat piece of a hyperplane, no estimate with $p > 1$ holds.

## Explanations

### L1 human

For a general function in $L^p$, its Fourier transform is only defined almost everywhere, so its values on a surface of measure zero seem meaningless.
The theorem says that the Fourier transform does have a meaningful restriction to a curved surface, such as a sphere.
This holds with a norm bound when $p$ is close enough to $1$.
Curvature is what makes this work: on a flat plane, it fails.

### L2 human

This is the main known case of the [[Fourier restriction problem|FFCH15ZNZG]] with $L^2$ norm on the surface, and it is sharp in that setting.
It is used to prove Strichartz estimates for the Schrödinger and wave equations, which are restriction estimates for paraboloids and cones.
The [[restriction conjecture|9CE11G48JY]] asks for more general $L^q(S)$ norms and a larger range of $p$.
