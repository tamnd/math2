---
tag: 47DYWZTQMC
kind: definition
name: External ray
msc: [37F20, 37F10]
defines: CNX4KVMDJQ
uses: [YBBDYHBADD, WDZFV2ACXR, 5M4S7P04GR, 1G0B73WPX8, 0YYT36R4YD]
sources:
  - url: https://en.wikipedia.org/wiki/External_ray
---

## Definition

Let $P$ be a monic [[polynomial|1G0B73WPX8]] of degree $d \ge 2$ whose filled Julia set $K$ is connected.
Let $\overline{\mathbb{D}}$ be the closed unit disc.
By [[Böttcher's theorem|YBBDYHBADD]] there is a unique [[conformal map|0YYT36R4YD]] $\varphi \colon \C \setminus K \to \C \setminus \overline{\mathbb{D}}$ with $\varphi(z)/z \to 1$ as $z \to \infty$.
It satisfies $\varphi(P(z)) = \varphi(z)^d$.
For $\theta \in \R/\Z$, the *external ray of angle* $\theta$ is
$$R_\theta = \varphi^{-1}\big(\set{r e^{2\pi i \theta} : r > 1}\big).$$
The ray $R_\theta$ *lands* at $z_0 \in \partial K$ if $\varphi^{-1}(r e^{2\pi i \theta}) \to z_0$ as $r \to 1^+$.

## Remarks

The relation $\varphi \circ P = \varphi^d$ gives $P(R_\theta) = R_{d\theta}$.
Example: for $P(z) = z^2$, $K$ is the closed unit disc and $\varphi$ is the identity.
So $R_\theta$ is the half-line $\set{r e^{2\pi i \theta} : r > 1}$, and it lands at $e^{2\pi i \theta}$.
Non-example: for $P(z) = z^2$, the spiral $\set{r e^{2\pi i (\theta + \log r)} : r > 1}$ is not an external ray, since $\varphi$ maps it to a curve whose angle varies.
Douady and Hubbard showed that every ray with a rational angle lands, at a periodic or preperiodic point of the [[Julia set|5M4S7P04GR]].
For the [[quadratic family|WDZFV2ACXR]], external rays of the Mandelbrot set are defined in the same way, with the conformal map from its complement onto $\C \setminus \overline{\mathbb{D}}$.
