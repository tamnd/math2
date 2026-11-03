---
tag: 12ZHZE3KG5
kind: statement
role: proposition
name: Bahcall–Wolf cusp
msc: [85A05]
uses: [4V8BT1ZD00, YHJ0PDNY8T, GZE6E8XQ7T, FVQWR7NS00]
about: [4V8BT1ZD00]
sources:
  - url: https://en.wikipedia.org/wiki/Bahcall%E2%80%93Wolf_cusp
same_as:
  wikidata: Q4842517
  wikipedia: Bahcall–Wolf cusp
---

## Statement

Consider a spherical system of stars of equal mass $m$ around a central [[black hole|YHJ0PDNY8T]] of mass $M \gg m$.
Inside the radius of influence the potential is close to the Kepler potential $-GM/r$.
Assume the stars there are bound to the black hole and their distribution is isotropic.
Assume the [[two-body relaxation time|GZE6E8XQ7T]] there is shorter than the age of the system.
Assume also that the black hole destroys the stars that come very close to it.
Consider the orbit-averaged [[Fokker–Planck equation|FVQWR7NS00]] in energy, with a small flux of stars towards the black hole.
Let $E < 0$ be the energy per unit mass of a star and $r$ its distance to the black hole.
Then the steady state has the distribution function $f$ and density $\rho$ given by
$$f(E) \propto \abs{E}^{1/4}, \qquad \rho(r) \propto r^{-7/4}.$$

## Remarks

The idea is that relaxation must carry a constant flux of energy outward through each radius, since the black hole absorbs stars and their binding energy at the centre.
Write $\rho \propto r^{-\gamma}$.
In the Kepler potential the velocity dispersion obeys $\sigma^2 \propto r^{-1}$, so the local relaxation time behaves as $t_r \propto \sigma^3 / \rho \propto r^{\gamma - 3/2}$.
The number of stars inside $r$ grows as $r^{3 - \gamma}$ and each carries an energy of order $GM/r$, so the energy flux scales as $r^{3 - \gamma} \cdot r^{-1} \cdot r^{3/2 - \gamma} = r^{7/2 - 2\gamma}$.
A flux independent of $r$ forces $\gamma = 7/4$; an isotropic $f(E) \propto \abs{E}^{p}$ in a Kepler potential gives $\rho \propto r^{-3/2 - p}$, hence $p = 1/4$.

The result was derived by J. N. Bahcall and R. A. Wolf in 1976.
The hypothesis of short relaxation time is needed: in a system younger than its relaxation time the inner density keeps the profile it was formed with.
With several stellar masses the heavier stars form the steepest cusp and the lighter ones form shallower ones.

## Explanations

### L1 human

Stars around a massive black hole slowly exchange energy through many weak encounters.
Over a long time this settles into a fixed pattern in which the density of stars rises towards the black hole like $r^{-7/4}$.
The cusp is a prediction for the centres of galaxies and of star clusters that host massive black holes.

### L2 human

The Bahcall–Wolf profile is the stellar-dynamics analogue of a steady flow: a constant energy flux through all radii fixes the exponent by dimensional analysis.
It is the standard reference profile in [[stellar dynamics|4V8BT1ZD00]] near black holes.
Comparing it with the star counts in the centre of the Milky Way tests whether that region is relaxed.
