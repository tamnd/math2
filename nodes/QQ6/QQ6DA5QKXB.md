---
tag: QQ6DA5QKXB
kind: definition
name: Funk transform
msc: [44A12, 53C65, 33C55]
defines: WQPTRZYY0Y
uses: [P9CM4GQ2T0, 3F32Y21HP4, YCK709QB06]
sources:
  - url: https://en.wikipedia.org/wiki/Funk_transform
---

## Definition

Let $S^2 = \set{x \in \R^3 : \abs{x} = 1}$ be the unit [[sphere|P9CM4GQ2T0]].
For $\theta \in S^2$, let $C_\theta = \set{x \in S^2 : x \cdot \theta = 0}$ be the great circle with pole $\theta$, with its arc length measure $ds$.
Let $f \colon S^2 \to \C$ be continuous.
The *Funk transform* of $f$ is the function on $S^2$ given by
$$(F f)(\theta) = \int_{C_\theta} f(x)\, ds(x).$$

## Remarks

Since $C_{-\theta} = C_\theta$, $F f$ is even.
If $f$ is odd, $f(-x) = -f(x)$, then $F f = 0$, because $C_\theta$ is symmetric under $x \mapsto -x$.
On a [[spherical harmonic|3F32Y21HP4]] $Y_k$ of degree $k$, $F Y_k = 2\pi P_k(0)\, Y_k$, where $P_k$ is the Legendre polynomial; $P_k(0) = 0$ for odd $k$ and $P_k(0) \ne 0$ for even $k$.
Hence $F$ is injective on even continuous functions.

Example: $f = 1$ gives $F f = 2\pi$, the length of a great circle; this is the case $k = 0$, with $P_0(0) = 1$.

Example: $f(x) = x_3$ is odd, so $F f = 0$, although $f \ne 0$.

Non-example: the integral of $f$ over a small circle $\set{x \in S^2 : x \cdot \theta = c}$ with $0 < \abs{c} < 1$ is not a value of the Funk transform, which uses only circles through the center of the sphere.

The same definition works on $S^{n-1}$ with the great subspheres $S^{n-1} \cap \theta^\perp$.
