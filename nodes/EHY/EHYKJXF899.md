---
tag: EHYKJXF899
kind: statement
role: theorem
name: Larmor formula
msc: [78A40, 78A35]
uses: [B6SKCGENY8, P3PK0Q02CZ, 6XPSV47R56]
about: [6XPSV47R56]
sources:
  - url: https://en.wikipedia.org/wiki/Larmor_formula
same_as:
  wikidata: Q1064493
  wikipedia: Larmor formula
---

## Statement

Let $\varepsilon_0 > 0$ be the vacuum permittivity and $c$ the speed of light.
Let a point [[charge|6XPSV47R56]] $q$ move with speed much smaller than $c$ and with acceleration $a$ at the retarded time.
Then, to leading order in the speed divided by $c$, the charge radiates the total power
$$P = \frac{q^2 \abs{a}^2}{6 \pi \varepsilon_0 c^3}.$$
To the same order, the power per unit solid angle at the angle $\theta$ from $a$ is
$$\frac{dP}{d\Omega} = \frac{q^2 \abs{a}^2 \sin^2 \theta}{16 \pi^2 \varepsilon_0 c^3}.$$

## Remarks

Proof idea: differentiate the [[Liénard–Wiechert potentials|B6SKCGENY8]] and keep only the part of the fields that decays like $1/R$ at distance $R$.
For small speed this part is $E = \frac{q}{4 \pi \varepsilon_0 c^2 R} \, n \times (n \times a)$ and $B = n \times E / c$, where $n$ is the unit vector toward the field point.
The [[Poynting vector|P3PK0Q02CZ]] then has size $\frac{q^2 \abs{a}^2 \sin^2 \theta}{16 \pi^2 \varepsilon_0 c^3 R^2}$, which gives $dP / d\Omega$.
Integrating over the sphere with $\int \sin^2 \theta \, d\Omega = 8\pi/3$ gives $P$.

Example: a charge that oscillates as $x(t) = x_0 \cos(\omega t)$ along a line has $\abs{a}^2 = x_0^2 \omega^4 \cos^2(\omega t)$.
Its average radiated power over a period is $\frac{q^2 x_0^2 \omega^4}{12 \pi \varepsilon_0 c^3}$, the power of an oscillating dipole.
The hypothesis of small speed is needed: for arbitrary speed, Liénard's generalization reads $P = \frac{q^2 \gamma^6}{6 \pi \varepsilon_0 c} \left( \abs{\dot\beta}^2 - \abs{\beta \times \dot\beta}^2 \right)$ with $\beta = v / c$ and $\gamma = (1 - \abs{\beta}^2)^{-1/2}$.

## Explanations

### L1 human

An accelerated charge sends out light, and the Larmor formula says how much power it sends.
The power grows with the square of the charge and the square of the acceleration.
No light goes out along the line of the acceleration, and most goes out at right angles to it.
A charge that moves at constant velocity does not radiate at all.

### L2 human

The formula is the basic estimate of radiation losses in classical electrodynamics: antennas, synchrotron radiation and bremsstrahlung all start from it or from its relativistic form.
It shows the failure of the classical model of the atom: an electron that circles a nucleus accelerates, so it would lose energy and fall in.
The energy carried away must be balanced by a force on the charge itself, which leads to the Abraham–Lorentz force.
