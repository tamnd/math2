---
tag: ZJG1YAGANG
kind: statement
role: theorem
name: Optical theorem
msc: [78A45, 35P25, 81U05]
uses: [8BQYB8H5CT, MNXKTXJ35G, NM024G378A, 3Y0VBDXHJD]
about: [8BQYB8H5CT]
sources:
  - url: https://en.wikipedia.org/wiki/Optical_theorem
same_as:
  wikidata: Q1136262
  wikipedia: Optical theorem
---

## Statement

Let $k > 0$ be a wavenumber and let $\hat{d}$ be a unit vector in $\R^3$.
Consider a time-harmonic scalar wave with time factor $e^{-i\omega t}$ that solves the [[Helmholtz equation|MNXKTXJ35G]] $\Delta u + k^2 u = 0$ outside a bounded scatterer.
Suppose the total field is $u = u_i + u_s$, where $u_i(x) = e^{ik \hat{d} \cdot x}$ is the incident [[plane wave|NM024G378A]].
Suppose the scattered field $u_s$ has the far-field form
$$u_s(x) = f(\hat{x}) \frac{e^{ikr}}{r} + o\!\left(\frac{1}{r}\right), \qquad r = \abs{x} \to \infty, \quad \hat{x} = x / r,$$
where $f$ is the scattering amplitude.
Let $\sigma_{\mathrm{ext}}$ be the extinction cross-section.
It is the rate at which scattering and absorption take energy from the incident wave, divided by the incident energy flux per unit area.
Then
$$\sigma_{\mathrm{ext}} = \frac{4\pi}{k} \operatorname{Im} f(\hat{d}).$$
If the scatterer does not absorb, $\sigma_{\mathrm{ext}}$ equals the total scattering cross-section $\int_{S^2} \abs{f(\hat{x})}^2 \, d\Omega(\hat{x})$.

## Remarks

The proof is a balance of energy flux through a large sphere around the scatterer.
The flux of the total field splits into the flux of $u_i$, which is zero, the flux of $u_s$, and a cross term between $u_i$ and $u_s$.
For large $r$, the cross term is an oscillatory integral over the sphere, and the method of stationary phase shows that only the forward direction $\hat{x} = \hat{d}$ contributes.
This gives the term $\frac{4\pi}{k} \operatorname{Im} f(\hat{d})$.

The same identity holds for electromagnetic [[scattering|8BQYB8H5CT]], with the vector forward amplitude projected on the incident polarization.
It also holds in quantum potential scattering, where it is a consequence of the unitarity of the scattering operator.

An example is the extinction paradox.
For a large opaque sphere of radius $a$ with $ka \to \infty$, the extinction cross-section tends to $2\pi a^2$, twice the geometric cross-section.
Half of it comes from the light that hits the sphere, and the other half from the light diffracted into a narrow forward cone.

## Explanations

### L1 human

When a wave hits an obstacle, some energy is scattered in all directions and some is absorbed.
This energy must be missing from the wave that goes straight on.
The optical theorem says that one number, the amplitude of the scattered wave in the exact forward direction, already tells how much energy is lost in total.
The forward scattered wave interferes destructively with the incident wave and leaves a shadow.

### L2 human

The theorem links the far-field pattern $f$ to the total cross-section, so it is a check on any numerical scattering code.
In quantum mechanics it reads $\sigma_{\mathrm{tot}} = \frac{4\pi}{k} \operatorname{Im} f(0)$ and follows from conservation of probability.
It also constrains approximations: the [[Born approximation|3Y0VBDXHJD]] gives a real forward amplitude for a real potential, so it violates the optical theorem at first order.
