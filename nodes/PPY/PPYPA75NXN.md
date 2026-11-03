---
tag: PPYPA75NXN
kind: statement
role: proposition
name: Roche limit
msc: [70F15, 85A05]
uses: [29WRN5J730, BXFSBB8Q46, P3760VW2WD]
about: [29WRN5J730]
sources:
  - url: https://en.wikipedia.org/wiki/Roche_limit
---

## Statement

Let a primary body be a sphere of radius $R$, mass $M$ and mean density $\rho_M$.
Let a satellite be a rigid sphere of radius $r$, mass $m$ and density $\rho_m$, held together only by its own gravity.
Let it move on a circular orbit of radius $d$ around the primary, with $r \ll d$.
Consider a loose particle on the surface of the satellite, at the point nearest to the primary.
Keep only the leading term in $r/d$ of the tidal acceleration.
Then the [[gravity|29WRN5J730]] of the satellite holds the particle if and only if $d > d_R$, where
$$d_R = r \left( \frac{2M}{m} \right)^{1/3} = R \left( \frac{2 \rho_M}{\rho_m} \right)^{1/3} \approx 1.26 \, R \left( \frac{\rho_M}{\rho_m} \right)^{1/3}.$$
The distance $d_R$ is the *Roche limit* of the rigid satellite.

## Remarks

The pull of the primary on the particle exceeds its pull on the centre of the satellite by $GM/(d - r)^2 - GM/d^2 \approx 2GMr/d^3$.
The particle stays when the self-gravity $Gm/r^2$ is larger, that is, when $d^3 > 2 (M/m) r^3$.
The second form follows from $M = \frac{4}{3}\pi R^3 \rho_M$ and $m = \frac{4}{3}\pi r^3 \rho_m$.
The limit depends only on the ratio of densities, not on the size of the satellite.

A fluid satellite deforms into an elongated shape under the tide, which lowers its self-gravity at the tips.
Roche's analysis of this case gives the larger value $d \approx 2.44 \, R (\rho_M/\rho_m)^{1/3}$.
Real moons have material strength, so small bodies can survive inside these limits; the limits apply to bodies held together by gravity alone.
The main rings of Saturn lie inside its Roche limit for icy bodies.

## Explanations

### L1 human

A moon is pulled harder on its near side than on its far side, and this difference tries to stretch it apart.
Its own gravity holds it together.
Close enough to the planet, stretching wins, and a moon made of loose rubble falls apart.
That critical distance is the Roche limit.
For a moon as dense as the planet, it lies between about one and a quarter and two and a half planet radii, depending on how rigid the moon is.

### L2 human

The computation is a comparison of the tidal acceleration, the first-order term of the gravitational field across the satellite, with the satellite's surface gravity.
A similar balance between the tide of the primary and the gravity of the satellite gives the radius of the [[Hill sphere|P3760VW2WD]] of a satellite on a [[Kepler orbit|BXFSBB8Q46]].
The same tidal effect explains why comets that pass close to a planet can break into pieces.
Refined versions include the rotation of the satellite and its fluid deformation, and they change only the numerical factor in front of $R (\rho_M/\rho_m)^{1/3}$.
