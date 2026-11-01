---
tag: K9BPYVQNZ9
kind: definition
name: Conformal modulus
msc: [30C75, 30C62]
defines: 2FQAKBVBX5
uses: [HX72KT9D0G, 01ZQQDCERP, 0C28RT5BG7, 0BVHZXWKCD, 0AJ0YVK743]
sources:
  - url: https://en.wikipedia.org/wiki/Extremal_length
---

## Definition

Let $\Omega \subseteq \C$ be an [[open set|01ZQQDCERP]], and let $\Gamma$ be a family of locally [[rectifiable curves|0C28RT5BG7]] in $\Omega$.
A Borel measurable function $\rho \colon \Omega \to [0, \infty]$ is *admissible* for $\Gamma$ if $\int_\gamma \rho \, \abs{dz} \ge 1$ for every $\gamma \in \Gamma$.
The *conformal modulus* of $\Gamma$ is
$$M(\Gamma) = \inf_{\rho} \int_\Omega \rho(x + iy)^2 \, dx\, dy \in [0, \infty],$$
the infimum taken over all admissible $\rho$.

## Remarks

The modulus is the reciprocal of the [[extremal length|HX72KT9D0G]]: $M(\Gamma) = 1/\lambda(\Gamma)$, with $1/0 = \infty$ and $1/\infty = 0$.
It is invariant under conformal maps of $\Omega$.
Example: for an [[annulus|0AJ0YVK743]] $\set{r < \abs{z} < R}$ and the family $\Gamma$ of curves in it that join the two boundary circles, $\rho(z) = \frac{1}{\abs{z}\log(R/r)}$ is admissible, and $M(\Gamma) = \frac{2\pi}{\log(R/r)}$.
The check of the lower bound integrates the inequality $\int_r^R \rho(te^{i\theta})\, dt \ge 1$ over $\theta$ and applies the Cauchy–Schwarz inequality.
Non-example: $\rho = \frac{1}{2\abs{z}\log(R/r)}$ is not admissible, since along a radial segment its integral is $\frac{1}{2}$.
A quadrilateral is a Jordan domain $Q$ with four marked boundary points, which cut the boundary into four sides.
Its modulus is the modulus of the family of curves in $Q$ that join one pair of opposite sides.
Map $Q$ conformally onto a rectangle $(0, a) \times (0, b)$, with the marked points at the corners and the chosen sides vertical; then the modulus is $b/a$.
Conventions for ring domains differ: the modulus of $\set{r < \abs{z} < R}$ is often defined as $\frac{1}{2\pi}\log(R/r)$, which is the extremal length of the family above, or as $\log(R/r)$.
