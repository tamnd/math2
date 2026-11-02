---
tag: B9FNGB5EBM
kind: definition
name: Willmore energy
msc: [53A10, 53C42]
defines: R7WFJGJBV4
uses: [6080X3FAD4, PA78NFEPCF, 0TVJZYB6SH]
sources:
  - url: https://en.wikipedia.org/wiki/Willmore_energy
---

## Definition

Let $S \subset \R^3$ be a [[compact|0TVJZYB6SH]] orientable [[regular surface|6080X3FAD4]] without boundary.
Let $H$ be its [[mean curvature|PA78NFEPCF]], $H = (k_1 + k_2)/2$ for the principal curvatures $k_1, k_2$, and let $dA$ be its area element.
The *Willmore energy* of $S$ is
$$\mathcal{W}(S) = \int_S H^2 \, dA.$$

## Remarks

For the sphere of radius $r$, one has $H^2 = 1/r^2$ and area $4\pi r^2$, so $\mathcal{W} = 4\pi$, for every $r$.
For the cylinder $x^2 + y^2 = r^2$, which is not compact, $H^2 = 1/(4r^2)$ is constant and the area is infinite, so the integral diverges.

The same formula defines $\mathcal{W}$ for a smooth immersion of a compact surface into $\R^3$; the value does not depend on the orientation, since $H^2$ does not.
Since $H^2 - K = (k_1 - k_2)^2/4$ and $\int_S K \, dA = 2\pi\chi(S)$ by the [[Gauss–Bonnet theorem|ESGEHKPD60]],
$$\mathcal{W}(S) = 2\pi\chi(S) + \frac{1}{4} \int_S (k_1 - k_2)^2 \, dA.$$
Some authors call $\int_S (H^2 - K)\, dA$ the Willmore energy; it differs from $\mathcal{W}$ by the topological constant $2\pi\chi(S)$.
For every such $S$, $\mathcal{W}(S) \ge 4\pi$, with equality exactly for round spheres.

## Explanations

### L1 human

The Willmore energy is the total of the squared mean curvature over a closed surface.
