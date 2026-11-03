---
tag: EZG8N3H7QN
kind: statement
role: proposition
name: Interface conditions for electromagnetic fields
msc: [78A25, 35Q61]
uses: [9BWWD4QK8Y, 604T74VWDK, NJVXQZ780B, A2WZA4QA3V, 0JX86PSSA9, 0AKRKVHW94]
about: [9BWWD4QK8Y]
sources:
  - url: https://en.wikipedia.org/wiki/Interface_conditions_for_electromagnetic_fields
same_as:
  wikidata: Q6046288
  wikipedia: Interface conditions for electromagnetic fields
---

## Statement

Let $\Sigma$ be a smooth surface that separates two media, labelled $1$ and $2$.
Let $n$ be the unit normal on $\Sigma$ pointing from medium $1$ into medium $2$.
Let the fields $E$, $B$, $D$, $H$ be $C^1$ up to $\Sigma$ on each side.
Write $E_1, E_2$ and so on for their one-sided limits at points of $\Sigma$.
Let the macroscopic [[Maxwell's equations|9BWWD4QK8Y]] hold in the sense of distributions.
The sources are bounded volume densities, a free surface charge density $\sigma_f$ on $\Sigma$ and a free surface current density $K_f$ on $\Sigma$.
Then on $\Sigma$:

1. $n \cdot (D_2 - D_1) = \sigma_f$.
2. $n \cdot (B_2 - B_1) = 0$.
3. $n \times (E_2 - E_1) = 0$.
4. $n \times (H_2 - H_1) = K_f$.

## Remarks

Conditions 1 and 2 come from applying the [[divergence theorem|0JX86PSSA9]] to Gauss's laws on a thin pillbox that straddles $\Sigma$.
Conditions 3 and 4 come from applying [[Stokes' theorem|0AKRKVHW94]] to Faraday's law and the Ampère–Maxwell law on a thin rectangle that crosses $\Sigma$.
As the thickness tends to zero, the time derivative terms drop out because $\partial_t B$ and $\partial_t D$ are bounded, while the surface sources remain.
So the normal part of $B$ and the tangential part of $E$ are always continuous.
The jumps of the [[displacement field|NJVXQZ780B]] $D$ and of $H$ are given by the surface sources.

Together with the [[constitutive relations|604T74VWDK]] of the two media, these conditions fix how fields are refracted at a boundary.
Example: consider the boundary of two dielectrics with permittivities $\varepsilon_1$ and $\varepsilon_2$ and no free surface charge.
Let a static field line meet $\Sigma$ at angle $\theta_1$ to the normal and leave at angle $\theta_2$.
Condition 3 gives $\abs{E_1} \sin \theta_1 = \abs{E_2} \sin \theta_2$, and condition 1 gives $\varepsilon_1 \abs{E_1} \cos \theta_1 = \varepsilon_2 \abs{E_2} \cos \theta_2$.
Dividing, $\tan \theta_1 / \tan \theta_2 = \varepsilon_1 / \varepsilon_2$.

At a perfect conductor the time-varying fields inside vanish, and the conditions become $n \times E = 0$ and $n \cdot B = 0$ on the outside, the usual boundary conditions for metallic waveguides and cavities.

## Explanations

### L1 human

When light or a static field passes from air into glass or from glass into metal, the fields jump at the boundary.
These four rules say which parts of the fields jump and by how much.
The parts of the electric field along the surface, and the part of the magnetic field across the surface, never jump.
The other parts jump only by an amount set by charges or currents sitting on the surface.

### L2 human

Interface conditions are the jump conditions of the first-order system of Maxwell's equations, just as the Rankine–Hugoniot conditions are the jump conditions of a conservation law.
They turn problems with several media into boundary value problems on each side, coupled through $\Sigma$.
From them one derives the Fresnel equations for reflection and refraction of plane waves, and the boundary conditions used in the analysis of waveguides, resonant cavities and scattering problems.
