---
tag: QG6TNKNQGT
kind: statement
role: fact
name: Schönberg–Chandrasekhar limit
msc: [85A15]
uses: [4FC5XQA2RK, SBKFDNEMFF, 6T0BTVNMRF]
about: [SBKFDNEMFF]
sources:
  - url: https://en.wikipedia.org/wiki/Sch%C3%B6nberg%E2%80%93Chandrasekhar_limit
same_as:
  wikidata: Q3704789
  wikipedia: Schönberg–Chandrasekhar limit
---

## Statement

Consider a star of mass $M$ in [[hydrostatic equilibrium|4FC5XQA2RK]], made of a core and an envelope.
The core has mass $M_c$, is isothermal, produces no energy, and consists of non-degenerate ideal gas with mean molecular weight $\mu_c$.
The envelope consists of ideal gas with mean molecular weight $\mu_e$.
Then an equilibrium of this kind exists only if
$$\frac{M_c}{M} \lesssim 0.37 \left( \frac{\mu_e}{\mu_c} \right)^2.$$
The largest possible ratio $M_c / M$ is the *Schönberg–Chandrasekhar limit*.

## Remarks

Let $T_c$ be the core temperature and $G$ the gravitational constant.
The [[virial theorem|6T0BTVNMRF]] applied to the core gives the pressure at its surface as a function of its mass and radius.
Over all radii this pressure has a maximum proportional to $T_c^4 / (\mu_c^4 G^3 M_c^2)$.
The envelope needs, at the edge of the core, a pressure proportional to $T_c^4 / (\mu_e^4 G^3 M^2)$.
Comparing the two gives a bound on $M_c / M$ proportional to $(\mu_e / \mu_c)^2$.
The factor $0.37$ comes from numerical models and is approximate.
Example: for a helium core, $\mu_c \approx 1.3$, under an envelope of hydrogen-rich gas with $\mu_e \approx 0.6$, the limit is about $0.37 \cdot (0.6 / 1.3)^2 \approx 0.08$, so about a tenth of the mass of the star.
The hypothesis of a non-degenerate core is necessary.
In stars of low mass the helium core becomes degenerate, its pressure no longer obeys the ideal gas law, and it can exceed this fraction.
The result was published by M. Schönberg and S. Chandrasekhar in 1942.

## Explanations

### L1 human

When a star has burnt the hydrogen in its centre, it is left with a core of helium that no longer makes energy.
Such a core can only carry a limited share of the star, about ten per cent of its mass.
If the core grows beyond this share, it can no longer hold up the rest of the star, and it contracts quickly.
This is why stars of moderate mass leave the main sequence fast and become red giants.

### L2 human

The limit explains the gap, in the Hertzsprung–Russell diagram, between the main sequence and the red giant branch for stars of a few solar masses.
When the helium core passes the limit, it contracts on the Kelvin–Helmholtz timescale, heats up and drives the envelope to expand.
The contraction ends either when helium ignites or when the core becomes degenerate.
