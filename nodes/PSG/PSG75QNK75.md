---
tag: PSG75QNK75
kind: definition
name: Laguerre–Gaussian modes
msc: [78A60, 78A10, 33C45]
defines: 8YGCTX64MT
uses: [Y0QE726BE3, 514PN8JF3A, WAMRHWW82R, 53DCTAEM5M]
sources:
  - url: https://en.wikipedia.org/wiki/Gaussian_beam
---

## Definition

Let $\lambda$, $k$, $w_0$, $z_R$, $w(z)$, $R(z)$ and $\psi(z)$ be as for a [[Gaussian beam|Y0QE726BE3]], with $\psi$ the [[Gouy phase|514PN8JF3A]].
Use cylindrical coordinates $(r, \varphi, z)$, and let $L_p^{(\alpha)}$ be the generalised [[Laguerre polynomial|WAMRHWW82R]].
For integers $p \ge 0$ and $\ell \in \Z$, the *Laguerre–Gaussian mode* $\mathrm{LG}_{p\ell}$ is the field
$$u_{p\ell} = \frac{w_0}{w} \left(\frac{\sqrt2 \, r}{w}\right)^{\abs{\ell}} L_p^{(\abs{\ell})}\!\left(\frac{2 r^2}{w^2}\right) e^{-r^2/w^2} \, e^{i \ell \varphi} \, e^{i\left(kz + \frac{k r^2}{2R} - (2p + \abs{\ell} + 1)\psi\right)},$$
where $w$, $R$ and $\psi$ are evaluated at $z$.

## Remarks

Each $u_{p\ell}$ solves the [[paraxial wave equation|53DCTAEM5M]] for the envelope $u_{p\ell} e^{-ikz}$.
The mode $\mathrm{LG}_{00}$ is the Gaussian beam.
The number $p$ is the number of zeros of the radial factor for $r > 0$, so the intensity has $p + 1$ bright rings.
The index $\ell$ is the azimuthal index: the phase winds $\ell$ times around the axis.
For each fixed $z$ the transverse profiles are orthogonal in $L^2(\R^2)$, and after normalisation they form an orthonormal basis.
The modes of the same order $2p + \abs{\ell} = N$ are linear combinations of the Hermite–Gaussian modes with $m + n = N$, and conversely.

Example: $\mathrm{LG}_{01}$ at the waist is $(\sqrt2 \, r / w_0) e^{-r^2/w_0^2} e^{i\varphi}$, since $L_0^{(1)} = 1$.
Its intensity $2 r^2 w_0^{-2} e^{-2r^2/w_0^2}$ is a ring of radius $w_0/\sqrt2$ with a zero at the centre.

Non-example: the profile $e^{-r^2/w_0^2} e^{i\varphi}$ is not a Laguerre–Gaussian mode.
It is not continuous at $r = 0$, because its modulus tends to $1$ while its phase has no limit there.
