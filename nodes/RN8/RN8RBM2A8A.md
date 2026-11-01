---
tag: RN8RBM2A8A
kind: definition
name: Stereographic projection
msc: [30A99, 51N20]
defines: AXDKKVD18N
uses: [0CDMXGPSES]
sources:
  - url: https://en.wikipedia.org/wiki/Stereographic_projection
---

## Definition

Let $S^2 = \set{(x_1, x_2, x_3) \in \R^3 : x_1^2 + x_2^2 + x_3^2 = 1}$ be the unit sphere and let $N = (0, 0, 1)$ be its north pole.
Identify the plane $x_3 = 0$ with $\C$ by $(x, y, 0) \mapsto x + iy$.
The *stereographic projection* is the map $\sigma \colon S^2 \setminus \set{N} \to \C$ defined as follows.
For $P \in S^2 \setminus \set{N}$, the point $\sigma(P)$ is where the line through $N$ and $P$ meets the plane $x_3 = 0$.
In coordinates,
$$\sigma(x_1, x_2, x_3) = \frac{x_1 + i x_2}{1 - x_3}.$$
Setting $\sigma(N) = \infty$ extends $\sigma$ to a bijection from $S^2$ onto the [[Riemann sphere|0CDMXGPSES]] $\C \cup \set{\infty}$.

## Remarks

The inverse map is
$$\sigma^{-1}(z) = \left( \frac{2 \operatorname{Re} z}{\abs{z}^2 + 1}, \frac{2 \operatorname{Im} z}{\abs{z}^2 + 1}, \frac{\abs{z}^2 - 1}{\abs{z}^2 + 1} \right).$$
Example: the south pole $(0, 0, -1)$ goes to $0/2 = 0$.
A point $(x_1, x_2, 0)$ of the equator goes to $x_1 + i x_2$, so the equator goes onto the unit circle.
Non-example: the projection from the center of the sphere onto a tangent plane is not stereographic.
It sends two antipodal points $P$ and $-P$ to the same point, so it is not injective.
The map $\sigma$ is a homeomorphism, it preserves angles, and it sends circles on $S^2$ to circles or lines in $\C$; the circles through $N$ go to lines.
Some authors project onto the plane tangent at the south pole, which multiplies $\sigma$ by $2$.
