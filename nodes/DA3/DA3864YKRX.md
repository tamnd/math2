---
tag: DA3864YKRX
kind: statement
role: fact
name: Tolman–Oppenheimer–Volkoff limit
msc: [85A15, 83C55]
uses: [3MCZ97SW6V, 4FC5XQA2RK, J8C4PN2R4H, 6Y50T68WKY]
about: [3MCZ97SW6V]
sources:
  - url: https://en.wikipedia.org/wiki/Tolman%E2%80%93Oppenheimer%E2%80%93Volkoff_limit
same_as:
  wikidata: Q1139232
  wikipedia: Tolman–Oppenheimer–Volkoff limit
---

## Statement

Consider static, spherically symmetric stars made of a perfect fluid with a given cold equation of state $P = P(\rho)$, in general relativity.
Let $m(r)$ be the gravitational mass inside the radius $r$, $G$ the gravitational constant and $c$ the speed of light.
By the [[Einstein field equations|3MCZ97SW6V]], such a star satisfies the Tolman–Oppenheimer–Volkoff equation
$$\frac{dP}{dr} = -\frac{G}{r^2} \left( \rho + \frac{P}{c^2} \right) \left( m + \frac{4 \pi r^3 P}{c^2} \right) \left( 1 - \frac{2 G m}{c^2 r} \right)^{-1}, \qquad \frac{dm}{dr} = 4 \pi r^2 \rho.$$
For the equations of state of neutron-star matter, the mass of these stars, as a function of the central density, has a largest value $M_{\mathrm{TOV}}$.
This maximum is the *Tolman–Oppenheimer–Volkoff limit*: no static, cold, non-rotating star with that equation of state has a larger mass.

## Remarks

When $P \ll \rho c^2$ and $G m \ll c^2 r$, the TOV equation reduces to Newtonian [[hydrostatic equilibrium|4FC5XQA2RK]].
The three relativistic factors all strengthen gravity, so pressure helps less than in Newtonian theory, and the mass curve reaches a maximum.
Configurations with central density beyond the maximum are unstable to radial perturbations.
Oppenheimer and Volkoff found a maximum of about $0.7$ solar masses for an ideal gas of free neutrons in 1939.
With realistic nuclear forces the value is not known exactly.
It is believed to lie roughly between $2$ and $3$ solar masses; it is at least about $2$, since neutron stars of that mass are observed.
The limit plays for neutron stars the role that the [[Chandrasekhar limit|J8C4PN2R4H]] plays for white dwarfs.

## Explanations

### L1 human

A neutron star is the collapsed core of a massive star, held up by the pressure of densely packed neutrons.
In Einstein's theory of gravity, pressure itself has weight, so squeezing the star harder can make gravity win.
Because of this there is a heaviest possible neutron star.
A collapsed core heavier than that limit cannot stop as a neutron star and becomes a black hole.

### L2 human

The TOV equation is the general-relativistic form of hydrostatic equilibrium.
For a given equation of state, one integrates it outward from a chosen central density until the pressure vanishes, which gives the mass and radius.
Varying the central density traces the mass–radius curve.
The maximum of this curve is $M_{\mathrm{TOV}}$, and its value tests models of matter at nuclear densities.
Outside the star the metric is the [[Schwarzschild metric|6Y50T68WKY]].
