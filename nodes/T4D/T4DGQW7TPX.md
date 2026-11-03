---
tag: T4DGQW7TPX
kind: statement
role: theorem
name: Chandrasekhar–Friedman–Schutz instability
msc: [85A15, 83C35, "76E07"]
uses: [QW9QPV0HHG, JVM27J1FTF, SJ0A4TZTFR]
about: [QW9QPV0HHG, SJ0A4TZTFR]
sources:
  - url: https://en.wikipedia.org/wiki/Chandrasekhar%E2%80%93Friedman%E2%80%93Schutz_instability
same_as:
  wikidata: Q124655742
  wikipedia: Chandrasekhar–Friedman–Schutz instability
---

## Statement

Let a self-gravitating star of perfect fluid, with no viscosity, rotate uniformly with angular velocity $\Omega > 0$ about an axis.
Let $\phi$ be the azimuthal angle about this axis.
Consider a non-axisymmetric [[pulsation mode|QW9QPV0HHG]] with integer $m \ge 1$ and real frequency $\omega$.
In an inertial frame, let it depend on $\phi$ and on time $t$ through $e^{i(m\phi - \omega t)}$.

1. Suppose $0 < \omega / m < \Omega$, so the mode moves backward relative to the star but forward in the inertial frame.
   Then emission of [[gravitational waves|SJ0A4TZTFR]] makes the mode grow.
2. For every $\Omega > 0$ such modes exist for all large enough $m$.
   So every rotating star of this kind is unstable when gravitational radiation is taken into account.

## Remarks

A wave that moves forward in the inertial frame radiates positive angular momentum through gravitational waves.
A wave that moves backward relative to the fluid carries negative angular momentum in the rotating star.
Losing positive angular momentum then makes the negative angular momentum of the mode larger in size, so the amplitude grows.
In the rotating frame a backward f mode of order $m$ has a frequency $\sigma_m$ that grows roughly like $\sqrt{m}$, so its pattern speed $\sigma_m / m$ tends to $0$.
Its pattern speed in the inertial frame is $\Omega - \sigma_m / m$, which lies in $(0, \Omega)$ for $m$ large; this gives the second clause.
The growth time increases fast with $m$, so in real stars viscosity damps all but the lowest modes; without the hypothesis of zero viscosity the second clause fails.
Chandrasekhar found the effect for the Maclaurin spheroids, and Friedman and Schutz showed that it is generic.

## Explanations

### L1 human

A spinning star can ring in patterns that run around its equator.
If a pattern runs backward relative to the star but is dragged forward by the rotation, it sheds gravitational waves.
Strangely, this loss of energy and angular momentum makes the pattern stronger instead of weaker.
So rotating stars are in principle unstable because of gravitational radiation.

### L2 human

The instability is a radiation-driven secular instability, similar to the one that drives a viscous Maclaurin spheroid away from axial symmetry.
It is a candidate for limiting the spin of young neutron stars and for producing a source of gravitational waves.
Modes that are often discussed are the f modes for fast rotation and the r modes, which are governed by the Coriolis force.
Whether the instability matters in a given star depends on the competition between the growth time and the damping time due to viscosity.
