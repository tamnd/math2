---
tag: KBCEHH0H7N
kind: example
name: Eady model
msc: ["76E20", 76U60, 86A10]
illustrates: [2SVQ4JN85Y]
uses: [8Z4QBWTWVR, 287Z5PMWY5, XQ82TE42FH, MT3A0DDAA8]
sources:
  - url: https://en.wikipedia.org/wiki/Eady_model
same_as:
  wikidata: Q23579953
  wikipedia: Eady model
---

## Example

Take the [[quasi-geostrophic equations|8Z4QBWTWVR]] on an [[f-plane|287Z5PMWY5]] with Coriolis parameter $f_0 > 0$ and constant [[Brunt–Väisälä frequency|XQ82TE42FH]] $N > 0$.
The fluid lies between rigid horizontal lids at $z = 0$ and $z = H$.
The basic state is the zonal flow $U(z) = \Lambda z$ with constant shear $\Lambda > 0$.
By thermal wind it has the buoyancy gradient $\partial_y B = -f_0 \Lambda$.
This is the *Eady model*.

The basic potential vorticity gradient vanishes in the interior.
So a perturbation $\psi' = \operatorname{Re}[\hat\psi(z) e^{i(kx + ly - kct)}]$ satisfies
$$\hat\psi'' - \frac{N^2 K^2}{f_0^2} \hat\psi = 0, \qquad K^2 = k^2 + l^2,$$
with the boundary conditions $(U - c) \hat\psi' - \Lambda \hat\psi = 0$ at $z = 0$ and $z = H$, which express conservation of buoyancy at the lids.
Write $\mu = N H K / f_0$ for the wavenumber scaled by the [[deformation radius|MT3A0DDAA8]] $L_d = N H / f_0$.
Solving with $\hat\psi = a \cosh(\mu z / H) + b \sinh(\mu z / H)$ gives
$$c = \frac{\Lambda H}{2} \pm \frac{\Lambda H}{\mu} \left[ \left( \frac{\mu}{2} - \coth \frac{\mu}{2} \right) \left( \frac{\mu}{2} - \tanh \frac{\mu}{2} \right) \right]^{1/2}.$$

Check of instability: $\mu / 2 > \tanh(\mu / 2)$ for all $\mu > 0$, so the bracket is negative exactly when $\mu / 2 < \coth(\mu / 2)$, that is, when $\mu < \mu_c \approx 2.399$.
For these wavenumbers $c$ has a positive imaginary part and the mode grows.
For $l = 0$ the growth rate $k \operatorname{Im} c$ equals $(f_0 \Lambda / N) \left[ (\coth \frac{\mu}{2} - \frac{\mu}{2})(\frac{\mu}{2} - \tanh \frac{\mu}{2}) \right]^{1/2}$.
It is largest at $\mu \approx 1.61$, with value about $0.31 \, f_0 \Lambda / N$, and the wavelength of the fastest mode is about $3.9 \, L_d$.
The growing modes travel at the mean speed $\Lambda H / 2$ of the flow, and their phase lines tilt westward with height.

Take $f_0 = 10^{-4}$ s$^{-1}$, $N = 10^{-2}$ s$^{-1}$, $H = 10$ km and a shear of $30$ m/s over $H$.
Then the fastest growth rate is about $0.93 \times 10^{-5}$ s$^{-1}$, an e-folding time of about $1.2$ days, at a wavelength of about $3900$ km.

## Explanations

### L1 human

The Eady model is the simplest picture of how mid-latitude storms are born.
It has a uniformly stratified layer of air between a flat ground and a flat lid, with a wind that grows steadily with height.
A wave that is not too short can grow by exchanging warm and cold air.
The fastest-growing wave is a few thousand kilometres long and grows in about a day.
These numbers match the size and growth of real weather systems surprisingly well.
