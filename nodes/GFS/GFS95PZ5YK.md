---
tag: GFS95PZ5YK
kind: statement
role: theorem
name: Kramers–Kronig relations
msc: ["30E20", 44A15, 78A25]
uses: [0DG0Z72CQD, 0V3RDQV3ZX, 0DG10TVYPN, 01MPZXYVYF, NSCEBXM7ZM]
about: [NSCEBXM7ZM]
sources:
  - url: https://en.wikipedia.org/wiki/Kramers%E2%80%93Kronig_relations
same_as:
  wikidata: Q1424764
  wikipedia: Kramers–Kronig relations
---

## Statement

Let $H = \set{z \in \C : \operatorname{Im} z > 0}$ be the upper half-plane.
Let $\chi$ be continuous on the closure $\bar H$ and [[holomorphic|0DG0Z72CQD]] on $H$, with $\chi(z) \to 0$ as $\abs{z} \to \infty$ in $\bar H$, uniformly in the direction.
Write $\chi(\omega) = \chi_1(\omega) + i \chi_2(\omega)$ for real $\omega$, with $\chi_1$ and $\chi_2$ real.
Then for each real $\omega$,
$$\chi_1(\omega) = \frac{1}{\pi} \, \mathrm{p.v.} \int_{-\infty}^{\infty} \frac{\chi_2(\omega')}{\omega' - \omega} \, d\omega', \qquad \chi_2(\omega) = -\frac{1}{\pi} \, \mathrm{p.v.} \int_{-\infty}^{\infty} \frac{\chi_1(\omega')}{\omega' - \omega} \, d\omega'.$$
Here $\mathrm{p.v.}$ is the [[principal value|0V3RDQV3ZX]] at $\omega$ and at infinity: the limit of the integral over $\varepsilon < \abs{\omega' - \omega} < R$ as $\varepsilon \to 0$ and $R \to \infty$.

## Remarks

Proof idea: integrate $\chi(z)/(z - \omega)$ over the boundary of the half-disc of radius $R$ in $H$, with a small half-circle of radius $\varepsilon$ around $\omega$ removed.
By [[Cauchy's theorem|01MPZXYVYF]] the integral is $0$.
The big half-circle contributes at most $\pi \max \abs{\chi} \cdot R/(R - \abs{\omega}) \to 0$, and the small one tends to $-i\pi \chi(\omega)$.
So $\mathrm{p.v.} \int \frac{\chi(\omega')}{\omega' - \omega} \, d\omega' = i\pi \chi(\omega)$, and the real and imaginary parts give the two relations.
Example: $\chi(z) = \frac{1}{z + i}$ gives $\chi_1(\omega) = \frac{\omega}{\omega^2 + 1}$ and $\chi_2(\omega) = -\frac{1}{\omega^2 + 1}$, and these satisfy both relations.
In terms of the [[Hilbert transform|NSCEBXM7ZM]], each of $\chi_1$ and $\chi_2$ determines the other.

## Explanations

### L1 human

In physics, a response function such as the refractive index of a material has a real part and an imaginary part.
Causality, the fact that an effect cannot come before its cause, makes the response holomorphic in the upper half-plane of frequencies.
Then the real part and the imaginary part are not independent: each one can be computed from the other by an integral.
For example, the absorption of light at all frequencies determines the refractive index.

### L2 human

The relations are a direct consequence of Cauchy's integral formula on a half-plane.
They say that the real and imaginary parts of the boundary values of a holomorphic function on $H$ that decays at infinity are Hilbert transforms of each other.
For square-integrable boundary values, Titchmarsh's theorem makes this an equivalence with the Hardy space $H^2$ of the upper half-plane.
They are used to check measured spectra, to recover phases from amplitudes, and as dispersion relations in particle physics.
