---
tag: KRF21D5QVT
kind: statement
role: theorem
name: Kirchhoff's law of thermal radiation
msc: [80A21, 78A40, 80A10]
uses: [VETMCF1NQ5, A2RMYX8A65, S6XR2K4N8G, 5EKTEE00FZ]
about: [VETMCF1NQ5, S6XR2K4N8G]
sources:
  - url: https://en.wikipedia.org/wiki/Kirchhoff%27s_law_of_thermal_radiation
same_as:
  wikidata: Q911035
  wikipedia: Kirchhoff's law of thermal radiation
---

## Statement

Let a body be in [[thermodynamic equilibrium|5EKTEE00FZ]] with the radiation around it at absolute temperature $T$.
For a wavelength $\lambda$ and a direction $(\theta, \phi)$, let $\varepsilon_\lambda(\lambda, \theta, \phi, T)$ be its spectral directional [[emissivity|VETMCF1NQ5]].
Let $\alpha_\lambda(\lambda, \theta, \phi, T)$ be its spectral directional absorptivity, the fraction of incident radiation of that wavelength and direction that it absorbs.
Then
$$\varepsilon_\lambda(\lambda, \theta, \phi, T) = \alpha_\lambda(\lambda, \theta, \phi, T)$$
for every wavelength and direction.

## Remarks

Proof idea: place the body inside a closed cavity with walls at temperature $T$.
In equilibrium the radiation in the cavity is [[black-body radiation|A2RMYX8A65]], independent of the walls.
By the second law of thermodynamics and detailed balance, the body must emit at each wavelength and direction exactly what it absorbs there.
Since it absorbs $\alpha_\lambda$ times the black-body radiance and emits $\varepsilon_\lambda$ times it, the two fractions agree.

The equality of total hemispherical values $\varepsilon = \alpha$ needs more.
It holds, for example, when the surface is grey and diffuse, or when the incident radiation is black-body radiation at the temperature of the body.
A white paint absorbs little sunlight but emits strongly in the infrared, so its total absorptivity for sunlight differs from its total emissivity at room temperature.

Gustav Kirchhoff stated the law in 1859.

## Explanations

### L1 human

A good absorber of light is a good emitter, and a poor absorber is a poor emitter, colour by colour.
A black object heats up fast in the sun and also cools fast by radiation at night.
A shiny metal surface absorbs little and so also radiates little, which is why thermos flasks are silvered.

### L2 human

The law means a surface needs only one radiative property per wavelength and direction, not two.
Combined with the fact that absorptivity is at most $1$, it shows that no body emits more than a black body at the same temperature.
It is the basis of the grey-body model used in enclosure radiation calculations.
