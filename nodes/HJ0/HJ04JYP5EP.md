---
tag: HJ04JYP5EP
kind: definition
name: Hermite–Gaussian modes
msc: [78A60, 78A10, 33C45]
defines: 9NKZHQSC8A
uses: [Y0QE726BE3, 514PN8JF3A, MGACY98E9H, 53DCTAEM5M]
sources:
  - url: https://en.wikipedia.org/wiki/Gaussian_beam
---

## Definition

Let $\lambda$, $k$, $w_0$, $z_R$, $w(z)$, $R(z)$ and $\psi(z)$ be as for a [[Gaussian beam|Y0QE726BE3]], with $\psi$ the [[Gouy phase|514PN8JF3A]].
Let $H_m$ be the physicists' [[Hermite polynomial|MGACY98E9H]] of degree $m$.
For integers $m, n \ge 0$, the *Hermite–Gaussian mode* $\mathrm{HG}_{mn}$ is the field
$$u_{mn}(x, y, z) = \frac{w_0}{w} \, H_m\!\left(\frac{\sqrt2 \, x}{w}\right) H_n\!\left(\frac{\sqrt2 \, y}{w}\right) e^{-(x^2 + y^2)/w^2} \, e^{i\left(kz + \frac{k(x^2 + y^2)}{2R} - (m + n + 1)\psi\right)},$$
where $w$, $R$ and $\psi$ are evaluated at $z$.

## Remarks

Each $u_{mn}$ solves the [[paraxial wave equation|53DCTAEM5M]] for the envelope $u_{mn} e^{-ikz}$.
The mode $\mathrm{HG}_{00}$ is the Gaussian beam itself, since $H_0 = 1$.
The intensity of $\mathrm{HG}_{mn}$ vanishes on $m$ lines $x = \text{const}$ and $n$ lines $y = \text{const}$, from the real zeros of $H_m$ and $H_n$.
For each fixed $z$, the transverse profiles $u_{mn}(\cdot, \cdot, z)$ are orthogonal in $L^2(\R^2)$, and after normalisation they form an orthonormal basis.
The Gouy phase $(m + n + 1)\psi$ grows with the order $m + n$, which splits the resonance frequencies of these modes in a laser cavity.

Example: $H_1(t) = 2t$, so $\mathrm{HG}_{10}$ at the waist is $(2\sqrt2 \, x / w_0) e^{-(x^2 + y^2)/w_0^2}$.
Its intensity has two lobes separated by the dark line $x = 0$.

Non-example: the profile $x \, y^2 e^{-(x^2+y^2)/w_0^2}$ is not of the form $H_m(\sqrt2 x/w_0) H_n(\sqrt2 y/w_0) e^{-(x^2+y^2)/w_0^2}$ up to a constant, since $y^2$ is not a multiple of any $H_n(\sqrt 2 y / w_0)$.
It is a finite sum of such modes instead.
