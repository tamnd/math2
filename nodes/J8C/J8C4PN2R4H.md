---
tag: J8C4PN2R4H
kind: statement
role: theorem
name: Chandrasekhar limit
msc: [85A15]
uses: [F1ZPTWW5SA, 9YTGKNPMCP, ANRZZMH2Q0, 4FC5XQA2RK]
about: [F1ZPTWW5SA]
sources:
  - url: https://en.wikipedia.org/wiki/Chandrasekhar_limit
same_as:
  wikidata: Q51366
  wikipedia: Chandrasekhar limit
---

## Statement

Model a white dwarf as a spherically symmetric, non-rotating ball in Newtonian [[hydrostatic equilibrium|4FC5XQA2RK]].
Suppose that its pressure is that of a cold, fully degenerate ideal electron gas, with special relativity taken into account.
Let its mass per electron be $\mu_e m_H$, with $m_H$ the mass of a hydrogen atom.
For each central density there is exactly one such equilibrium, given by a solution of [[Chandrasekhar's white dwarf equation|F1ZPTWW5SA]].
Let $\hbar$ be the reduced Planck constant, $c$ the speed of light and $G$ the gravitational constant.
Let $\theta$ be the solution of the [[Lane–Emden equation|ANRZZMH2Q0]] of index $3$, with first zero $\xi_1$, and let $\omega_3 = -\xi_1^2 \theta'(\xi_1) \approx 2.018$.
Set
$$M_{\mathrm{Ch}} = \frac{\sqrt{3\pi}}{2} \, \omega_3 \left( \frac{\hbar c}{G} \right)^{3/2} \frac{1}{(\mu_e m_H)^2}.$$
Then the mass $M$ of every such equilibrium satisfies $M < M_{\mathrm{Ch}}$.
Moreover $M$ increases with the central density, and $M \to M_{\mathrm{Ch}}$ as the central density tends to infinity.

## Remarks

At high density the electrons are ultra-relativistic, the pressure tends to $K \rho^{4/3}$, and the star tends to a [[polytrope|9YTGKNPMCP]] of index $3$.
For a polytrope of index $3$ the mass $4 \pi \alpha^3 \rho_c \, \omega_3$ does not depend on the central density $\rho_c$, since $\alpha^3$ is proportional to $\rho_c^{-1}$; this common value is $M_{\mathrm{Ch}}$.
For a white dwarf of carbon and oxygen, $\mu_e = 2$ and $M_{\mathrm{Ch}}$ is about $1.4$ solar masses.
Without special relativity the pressure stays proportional to $\rho^{5/3}$, the star is a polytrope of index $3/2$ with $M \propto \rho_c^{1/2}$, and there is no upper bound on the mass.
Real white dwarfs become unstable a little below $M_{\mathrm{Ch}}$, because of general relativity and the capture of electrons by nuclei.

## Explanations

### L1 human

A white dwarf is held up by electrons that refuse to be packed more tightly, not by heat.
Adding mass squeezes the star and makes it smaller, and the electrons move faster.
When their speed approaches the speed of light, their pressure can no longer grow fast enough to hold the extra weight.
So there is a largest possible mass for a white dwarf, about 1.4 times the mass of the Sun.

### L2 human

The limit comes from comparing two power laws.
Gravity needs a central pressure that scales like $M^{2/3} \rho^{4/3}$, and a relativistic degenerate gas supplies $K \rho^{4/3}$.
The power of $\rho$ is the same, so equilibrium fixes the mass and not the density.
A star whose core grows past the limit must collapse further, to a neutron star or a black hole, which is the start of a core-collapse supernova.
For neutron stars the analogous bound is the [[Tolman–Oppenheimer–Volkoff limit|DA3864YKRX]], which needs general relativity.
