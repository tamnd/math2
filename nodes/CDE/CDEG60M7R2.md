---
tag: CDEG60M7R2
kind: example
name: Bessel beam
msc: [78A40, 33C10, 35Q60]
illustrates: [MNXKTXJ35G]
uses: [CZCMRDWDYW]
sources:
  - url: https://en.wikipedia.org/wiki/Bessel_beam
same_as:
  wikidata: Q830111
  wikipedia: Bessel beam
---

## Example

Let $k > 0$ be a wave number and choose $k_r \in (0, k)$ and $k_z = \sqrt{k^2 - k_r^2}$.
Use cylindrical coordinates $(r, \varphi, z)$.
The *Bessel beam* of order $0$ is the field
$$U(r, z) = J_0(k_r r) \, e^{i k_z z},$$
where $J_0$ is the [[Bessel function of the first kind|CZCMRDWDYW]] of order $0$.
The time dependence $e^{-i\omega t}$ is omitted.

Check: $J_0$ satisfies $J_0''(s) + J_0'(s)/s + J_0(s) = 0$.
The transverse Laplacian in polar form is $\partial_r^2 + r^{-1}\partial_r$ on functions of $r$.
Applied to $J_0(k_r r)$, it gives $-k_r^2 J_0(k_r r)$.
The $z$ factor gives $\partial_z^2 e^{i k_z z} = -k_z^2 e^{i k_z z}$.
Hence $\Delta U = -(k_r^2 + k_z^2) U = -k^2 U$, and $U$ solves the [[Helmholtz equation|MNXKTXJ35G]] exactly, not only in the paraxial approximation.

The intensity $\abs{U}^2 = J_0(k_r r)^2$ does not depend on $z$, so the beam does not spread as it propagates.
It is the superposition of plane waves whose wave vectors lie on a cone of half-angle $\arcsin(k_r / k)$ around the $z$ axis.
More generally $J_\ell(k_r r) e^{i\ell\varphi} e^{i k_z z}$ is a Bessel beam of order $\ell \in \Z$.

The beam has infinite power: $J_0(s)^2$ behaves like $\frac{2}{\pi s}\cos^2(s - \pi/4)$ for large $s$, so $\int_0^\infty J_0(k_r r)^2 \, r \, dr$ diverges.
Each ring carries about the same power as the central spot.
Real Bessel-like beams, made with an axicon or an annular aperture, are therefore non-spreading only over a finite distance.

## Explanations

### L1 human

Most beams spread out as they travel, but a Bessel beam keeps a narrow bright centre over a long distance.
It is made by sending light along a cone towards the axis, so that the waves cross and interfere along a line.
Its cross-section is a bright spot surrounded by many faint rings.
The trick is that the rings carry as much energy as the centre, so a perfect Bessel beam would need infinite energy.
In practice it stays sharp over a limited range, which is useful in microscopy and for moving tiny particles.
