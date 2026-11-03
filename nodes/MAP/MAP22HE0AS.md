---
tag: MAP22HE0AS
kind: definition
name: Geodynamics
msc: [86A04, 86A60]
defines: V64G624N9E
uses: [KG2XWEMJ30, VP2HN86VAG, 13CB7V2YM4, GCX1B3DAJN]
sources:
  - url: https://en.wikipedia.org/wiki/Geodynamics
---

## Definition

*Geodynamics* is the study of the deformation, flow and thermal evolution of the solid Earth and its core by the methods of continuum mechanics.
Its models describe a region of the Earth by:

1. conservation of mass and momentum, with the [[Cauchy stress tensor|KG2XWEMJ30]] $\boldsymbol{\sigma}$ satisfying $\nabla \cdot \boldsymbol{\sigma} + \rho \mathbf{g} = 0$ when inertia is negligible;
2. conservation of energy, in the form of the [[heat equation|VP2HN86VAG]] with advection and internal heat sources;
3. a constitutive law linking stress to strain or strain rate, such as elastic, viscous or [[viscoelastic|GCX1B3DAJN]] behaviour, together with failure laws for brittle rock.

## Remarks

Example: mantle convection is modelled as [[Stokes flow|13CB7V2YM4]] of a viscous fluid heated from below and from within, which fits all three clauses.
Non-example: the propagation of seismic waves uses the same continuum mechanics, but with inertia kept and on time scales of seconds; it belongs to seismology rather than geodynamics.
The time scales of geodynamics range from thousands of years, for rebound after deglaciation, to billions of years, for the thermal history of the Earth.
