---
tag: WGDAZ1YY3J
kind: definition
name: Dual Radon transform
msc: [44A12, 92C55]
defines: 938SXZQS8G
uses: [VJNZJ352PC, P9CM4GQ2T0]
sources:
  - url: https://en.wikipedia.org/wiki/Radon_transform
---

## Definition

Let $n \ge 2$, let $S^{n-1}$ be the unit [[sphere|P9CM4GQ2T0]] in $\R^n$, and let $d\theta$ be its surface measure.
Let $g \colon S^{n-1} \times \R \to \C$ be continuous.
The *dual Radon transform* of $g$ is the function on $\R^n$ given by
$$(R^* g)(x) = \int_{S^{n-1}} g(\theta, x \cdot \theta)\, d\theta.$$

## Remarks

The pair $(\theta, x \cdot \theta)$ describes the hyperplane with normal $\theta$ through $x$, so $R^* g(x)$ integrates $g$ over all hyperplanes through $x$.
For $f$ continuous with compact support and $g$ continuous, Fubini's theorem gives the duality
$$\int_{S^{n-1}} \int_\R (R f)(\theta, s)\, g(\theta, s)\, ds\, d\theta = \int_{\R^n} f(x)\, (R^* g)(x)\, dx,$$
where $R$ is the [[Radon transform|VJNZJ352PC]].

Example: $g(\theta, s) = s^2$.
Then $R^* g(x) = \int_{S^{n-1}} (x \cdot \theta)^2\, d\theta = \frac{\omega_{n-1}}{n} \abs{x}^2$, where $\omega_{n-1}$ is the area of $S^{n-1}$, because the $n$ integrals $\int \theta_j^2\, d\theta$ are equal and add up to $\omega_{n-1}$.

Non-example: $R^*$ is not an inverse of $R$.
For $n = 2$ and $f$ continuous with compact support, polar coordinates give $R^* R f(x) = 2 \int_{\R^2} \frac{f(x + z)}{\abs{z}}\, dz$, a smoothed version of $f$, not $f$ itself.

Other notations are $R^\#$ and $R^t$; some authors divide by the area of the sphere.
