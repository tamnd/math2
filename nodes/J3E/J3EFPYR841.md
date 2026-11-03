---
tag: J3EFPYR841
kind: statement
role: theorem
name: Clairaut's theorem on gravity
msc: [86A30, 86A20, 70F15]
uses: [NE1PZM0HBN, 5Y2BWNY6MF, BSV03EAVYT]
about: [NE1PZM0HBN, 5Y2BWNY6MF]
sources:
  - url: https://en.wikipedia.org/wiki/Clairaut%27s_theorem_(gravity)
same_as:
  wikidata: Q1068385
  wikipedia: Clairaut's theorem (gravity)
---

## Statement

Let a body rotate with angular velocity $\omega$ about a fixed axis.
Assume that its outer surface is a spheroid with semi-axes $a > b$, and that it is a level surface of its [[geopotential|5Y2BWNY6MF]].
Let $f = (a - b)/a$ be its [[flattening|NE1PZM0HBN]], let $g_e$ be the gravity at the equator, and let $m = \omega^2 a / g_e$.
Then, to first order in the small quantities $f$ and $m$, the gravity at latitude $\varphi$ on the surface is
$$g(\varphi) = g_e\left(1 + \left(\tfrac{5}{2}m - f\right)\sin^2\varphi\right).$$
Equivalently, the gravity $g_p$ at the poles satisfies
$$\frac{g_p - g_e}{g_e} = \frac{5}{2}m - f.$$

## Remarks

Clairaut published the result in 1743, for a body made of nested spheroidal layers of constant density in hydrostatic equilibrium.
Stokes showed in 1849 that it holds for any internal density, provided the outer surface is a level spheroid.
To first order, the proof writes the exterior potential as $GM/r$ plus a degree $2$ zonal harmonic.
It then requires the potential plus the centrifugal term to be constant on the spheroid.
This fixes the $J_2$ coefficient in terms of $f$ and $m$, and the radial derivative gives $g(\varphi)$.
For the Earth, $m \approx 1/289$ and $f \approx 1/298$, so $\tfrac52 m - f \approx 0.0053$: gravity is about $0.5\%$ larger at the poles.
The result needs the surface to be a level surface; for an arbitrary rotating rigid body the relation between gravity and shape fails.

## Explanations

### L1 human

The theorem links two facts about the Earth: how flat it is, and how much gravity changes from equator to pole.
Spinning makes the Earth bulge and also pushes outward at the equator, both of which weaken gravity there.
Clairaut's formula says exactly how much, to first order, using the spin rate and the flattening.
Historically it let scientists find the Earth's flattening by swinging pendulums at different latitudes.

### L2 human

The centrifugal force alone lowers equatorial gravity by $g_e m\cos^2\varphi$; the rest of the variation comes from the shape of the attracting masses.
The theorem is the first-order version of the exact [[Somigliana formula|Y35VMCD5K0]] for a level ellipsoid.
It also expresses $J_2$ through $f$ and $m$, namely $J_2 \approx \tfrac{2}{3}f - \tfrac{1}{3}m$ to first order.
Higher-order versions keep terms in $f^2$, $fm$ and $m^2$.
