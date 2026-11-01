---
tag: TDQ4YBMW9C
kind: definition
name: Extremal length
msc: [30C75, 31A15]
defines: HX72KT9D0G
uses: [01ZQQDCERP, 0C28RT5BG7, 0BVHZXWKCD]
sources:
  - url: https://en.wikipedia.org/wiki/Extremal_length
---

## Definition

Let $\Omega \subseteq \C$ be an [[open set|01ZQQDCERP]], and let $\Gamma$ be a family of locally [[rectifiable curves|0C28RT5BG7]] in $\Omega$.
A *metric* on $\Omega$ is a [[Borel measurable|0BVHZXWKCD]] function $\rho \colon \Omega \to [0, \infty]$ with area
$$A(\rho) = \int_\Omega \rho(x + iy)^2 \, dx\, dy$$
satisfying $0 < A(\rho) < \infty$.
The $\rho$-length of $\Gamma$ is
$$L_\rho(\Gamma) = \inf_{\gamma \in \Gamma} \int_\gamma \rho \, \abs{dz},$$
the integral being with respect to arc length.
The *extremal length* of $\Gamma$ is
$$\lambda(\Gamma) = \sup_{\rho} \frac{L_\rho(\Gamma)^2}{A(\rho)} \in [0, \infty],$$
the supremum taken over all metrics $\rho$ on $\Omega$.

## Remarks

The value does not change if $\Omega$ is replaced by a larger open set and $\rho$ is extended by $0$.
If $f \colon \Omega \to \Omega'$ is a conformal map, then $\lambda(f(\Gamma)) = \lambda(\Gamma)$: the metric $\rho$ on $\Omega'$ pulls back to $(\rho \circ f)\abs{f'}$ with the same lengths and area.
Example: let $R = (0, a) \times (0, b)$ and let $\Gamma$ be the curves in $R$ that join the left side to the right side.
For $\rho = 1$, $L_\rho = a$ and $A(\rho) = ab$, so $\lambda(\Gamma) \ge a/b$.
For any metric, each horizontal segment gives $\int_0^a \rho(x + iy)\, dx \ge L_\rho$, so by integrating in $y$ and the Cauchy–Schwarz inequality, $b L_\rho \le \int_R \rho \le \sqrt{ab\, A(\rho)}$, and $\lambda(\Gamma) = a/b$.
Non-example: $\rho = 0$ is not a metric, since its area is $0$; it would give the meaningless ratio $0/0$.
If every curve of $\Gamma_1$ contains a curve of $\Gamma_2$, then $\lambda(\Gamma_1) \ge \lambda(\Gamma_2)$.
