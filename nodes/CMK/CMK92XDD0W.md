---
tag: CMK92XDD0W
kind: definition
name: Willmore flow
msc: ["53E40", "53A05"]
defines: MSRAD0X7H4
uses: [R7WFJGJBV4, PA78NFEPCF, SQVQ5DQT6W, F4NWZNTRMD]
sources:
  - url: https://en.wikipedia.org/wiki/Willmore_energy
---

## Definition

Let $\Sigma$ be a closed oriented surface and let $T > 0$.
Let $f \colon \Sigma \times [0, T) \to \R^3$ be a smooth family of immersions, and write $f_t = f(\cdot, t)$.
For each $t$, let $\nu$ be the unit normal of $f_t$.
Let $H = \tfrac{1}{2}(\kappa_1 + \kappa_2)$ be the [[mean curvature|PA78NFEPCF]] of $f_t$ with respect to $\nu$, so that the mean curvature vector is $2H\nu$.
Let $K$ be the [[Gaussian curvature|SQVQ5DQT6W]] of $f_t$.
Let $\Delta$ be the [[Laplace–Beltrami operator|F4NWZNTRMD]] of the metric induced by $f_t$.
The family is a solution of the *Willmore flow* if
$$\frac{\partial f}{\partial t} = -\left(\Delta H + 2H\left(H^2 - K\right)\right) \nu.$$

## Remarks

The right side is minus the $L^2$ gradient of the [[Willmore energy|R7WFJGJBV4]] $W(f_t) = \int_\Sigma H^2 \, dA$, so $W(f_t)$ does not increase.
Example: the constant family of a round sphere of radius $r$ is a solution.
Indeed $H = \pm 1/r$ is constant, so $\Delta H = 0$, and $H^2 - K = 1/r^2 - 1/r^2 = 0$, so the right side vanishes.
Non-example: the spheres of radius $1 + t$ do not form a solution, since the right side vanishes for each of them but the surfaces move.
A surface for which $\Delta H + 2H(H^2 - K) = 0$ is a Willmore surface; these are exactly the stationary solutions.
The equation is of fourth order and parabolic, so the maximum principle fails and convexity need not be preserved.
