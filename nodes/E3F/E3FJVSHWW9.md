---
tag: E3FJVSHWW9
kind: definition
name: Phase matching
msc: [78A60]
defines: J7NEMSG2MD
uses: [4C67FMA3M7, 8CWCYQJ44T, 9VGK0SP6EQ, NM024G378A]
sources:
  - url: https://en.wikipedia.org/wiki/Nonlinear_optics
---

## Definition

Consider a three-wave process in a nonlinear medium.
[[Plane waves|NM024G378A]] of frequencies $\omega_1, \omega_2$ and wave vectors $\mathbf{k}_1, \mathbf{k}_2$ generate a wave of frequency $\omega_3 = \omega_1 + \omega_2$ and wave vector $\mathbf{k}_3$.
Here $\abs{\mathbf{k}_j} = n(\omega_j) \omega_j / c$, where $n$ is the [[refractive index|9VGK0SP6EQ]] of the mode and $c$ the speed of light in vacuum.
The *phase mismatch* is $\Delta \mathbf{k} = \mathbf{k}_1 + \mathbf{k}_2 - \mathbf{k}_3$.
The process is *phase matched* when $\Delta \mathbf{k} = \mathbf{0}$.

## Remarks

For collinear waves and an undepleted input, the generated intensity after a length $L$ is proportional to
$$L^2\, \frac{\sin^2(\Delta k L / 2)}{(\Delta k L / 2)^2},$$
which comes from $\abs{\int_0^L e^{i \Delta k z}\, dz}^2$.
It grows like $L^2$ when $\Delta k = 0$, and oscillates with period $2\pi/\abs{\Delta k}$ in $L$ otherwise; the length $L_c = \pi / \abs{\Delta k}$ is the *coherence length*.

Example: for [[second-harmonic generation|4C67FMA3M7]], $\omega_1 = \omega_2 = \omega$ and collinear phase matching means $n(2\omega) = n(\omega)$.
Take a [[birefringent|8CWCYQJ44T]] uniaxial crystal with $n_e < n_o$, the fundamental as an ordinary wave and the harmonic as an extraordinary wave.
When the birefringence exceeds the dispersion, $n_e(2\omega) \le n_o(\omega)$, and one can choose a direction where the two indices are equal.

Non-example: in an isotropic medium with normal dispersion, $n(2\omega) > n(\omega)$, so collinear second-harmonic generation is never phase matched.
