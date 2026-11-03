---
tag: HB7B9KHN2R
kind: definition
name: Dispersion of surface waves
msc: [74J15, 86A15]
defines: FCNW57HD54
uses: [28CHFPZ7WR, FMDA4DKT0M, C05DPKD4S0, X32RRM7ATM, A2E51V42RH, J2GWW1NPTC]
sources:
  - url: https://en.wikipedia.org/wiki/Surface_wave
---

## Definition

Let an isotropic elastic medium fill the half-space $z > 0$, with density and elastic moduli depending only on the depth $z$.
Its surface $z = 0$ is traction-free.
A *surface wave mode* is a solution of the elastic wave equation of the form $u(x, z, t) = f(z) e^{i(kx - \omega t)}$, with $k > 0$, $\omega > 0$ and $f(z) \to 0$ as $z \to \infty$.
Such modes exist only when $\omega$ and $k$ satisfy a [[dispersion relation|28CHFPZ7WR]], whose solutions form branches $\omega = \omega_m(k)$, $m = 0, 1, 2, \dots$.
The surface waves of a branch are *dispersive* if the [[phase velocity|FMDA4DKT0M]] $c = \omega_m(k)/k$ is not constant in $k$.
The [[group velocity|C05DPKD4S0]] of the branch is $U = d\omega_m/dk = c + k\, dc/dk$.

## Remarks

Example: a layer of thickness $h$, density $\rho_1$ and S-speed $\beta_1$ over a half-space with $\rho_2$ and $\beta_2 > \beta_1$ carries [[Love waves|A2E51V42RH]] with $\beta_1 < c < \beta_2$.
With [[shear moduli|J2GWW1NPTC]] $\mu_j = \rho_j \beta_j^2$, the dispersion relation is
$$\tan\Big(kh\sqrt{c^2/\beta_1^2 - 1}\Big) = \frac{\mu_2 \sqrt{1 - c^2/\beta_2^2}}{\mu_1 \sqrt{c^2/\beta_1^2 - 1}}.$$
As $kh \to \infty$ the fundamental branch has $c \to \beta_1$, and as $kh \to 0$ it has $c \to \beta_2$, so the waves are dispersive.
Non-example: a homogeneous half-space carries a [[Rayleigh wave|X32RRM7ATM]] whose speed is a fixed number below $\beta$, about $0.92\beta$ when $\lambda = \mu$.
The medium has no length scale, so $c$ cannot depend on $k$, and the Rayleigh wave is not dispersive.
