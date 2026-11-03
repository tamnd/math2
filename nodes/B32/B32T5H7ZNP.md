---
tag: B32T5H7ZNP
kind: statement
role: fact
name: Kraichnan's inverse cascade in two-dimensional turbulence
msc: [76F05, 76F02]
uses: [VY307F8Z0S, YQ2KYDWRD0, A3HKV3BHDR, RW0JK9VDZE]
about: [YQ2KYDWRD0]
sources:
  - url: https://en.wikipedia.org/wiki/Energy_cascade
---

## Statement

Consider statistically stationary, homogeneous and isotropic [[turbulence|VY307F8Z0S]] of an incompressible fluid in the plane.
Assume that energy is injected by a forcing that acts in a narrow band of wavenumbers around $k_f$.
Assume that energy is removed only at scales much larger than $1/k_f$, and enstrophy only at scales much smaller than $1/k_f$.
Let $E(k)$ be the energy spectrum, $\varepsilon$ the rate of energy injection and $\eta$ the rate of enstrophy injection.
Kraichnan's theory predicts two inertial ranges.

1. For $k \ll k_f$, energy flows at the constant rate $\varepsilon$ towards small wavenumbers, that is, towards large scales, and $E(k) = C \varepsilon^{2/3} k^{-5/3}$.
2. For $k \gg k_f$, enstrophy flows at the constant rate $\eta$ towards large wavenumbers, and $E(k) = C' \eta^{2/3} k^{-3}$.

Here $C$ and $C'$ are dimensionless constants.

## Remarks

The prediction rests on two invariants of the two-dimensional [[Euler equations|RW0JK9VDZE]]: the energy $\int E(k)\, dk$ and the enstrophy $\int k^2 E(k)\, dk$.
An argument of Fjørtoft treats energy at $k_f$ that moves to two other wavenumbers while both invariants are conserved.
It shows that most of the energy must go to the smaller wavenumber and most of the enstrophy to the larger one.
The two spectra then follow from dimensional analysis, as in the [[Kolmogorov 1941 theory|A3HKV3BHDR]], once $\varepsilon$ or $\eta$ is the only relevant parameter in the range.
The $k^{-3}$ law was later given a logarithmic correction.
The [[energy cascade|YQ2KYDWRD0]] in three dimensions goes the other way, from large to small scales, because enstrophy is not conserved there.
Numerical simulations and soap film experiments show the inverse cascade, with energy piling up at the largest scale of the domain unless friction removes it.

## Explanations

### L1 human

In ordinary three-dimensional turbulence big eddies break into smaller ones, and the energy ends up as heat at tiny scales.
In a flat, two-dimensional flow the opposite happens: small eddies merge into larger ones, so energy moves to large scales.
At the same time a second quantity, the mean square of the vorticity, still moves to small scales.
This helps explain why large, long-lived vortices form in thin layers of fluid such as soap films.

### L2 human

The theory is the two-dimensional analogue of Kolmogorov's theory, with one cascade for each inviscid invariant.
The slopes $-5/3$ and $-3$ come from dimensional analysis once one knows which flux is constant in each range.
The double cascade is often called the Kraichnan–Leith–Batchelor picture.
It guides the reading of large-scale atmospheric and oceanic spectra and the design of two-dimensional simulations.
