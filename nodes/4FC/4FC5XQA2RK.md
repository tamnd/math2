---
tag: 4FC5XQA2RK
kind: statement
role: proposition
name: Hydrostatic equilibrium
msc: [85A15, 85A30]
uses: [RW0JK9VDZE, DWK5N5SKTK, 29WRN5J730, ANRZZMH2Q0, 6T0BTVNMRF]
about: [SBKFDNEMFF]
sources:
  - url: https://en.wikipedia.org/wiki/Hydrostatic_equilibrium
same_as:
  wikidata: Q208641
  wikipedia: Hydrostatic equilibrium
---

## Statement

Let a fluid with density $\rho$, pressure $P$ and velocity $v$ fill a region of $\R^3$, in a gravitational potential $\Phi$.
Suppose that it obeys the [[Euler equations|RW0JK9VDZE]] $\rho (\partial_t v + (v \cdot \nabla) v) = -\nabla P - \rho \nabla \Phi$.
Suppose that the fluid is at rest, that is, $v = 0$ everywhere and at all times.

1. Then $\nabla P = -\rho \nabla \Phi$.
2. Suppose moreover that $\Phi$ solves [[Poisson's equation|DWK5N5SKTK]] $\Delta \Phi = 4 \pi G \rho$, where $G$ is the gravitational constant.
   Suppose also that the region is a ball centred at $0$, and that $\rho$, $P$ and $\Phi$ are smooth and depend only on $r = \abs{x}$.
   Let $m(r) = \int_0^r 4 \pi s^2 \rho(s) \, ds$ be the mass inside radius $r$.
   Then for $r > 0$,
   $$\frac{dP}{dr} = -\frac{G m(r) \rho(r)}{r^2}.$$

## Remarks

Part 1 is the Euler equation with $v = 0$.
For part 2, integrate Poisson's equation over the ball of radius $r$ and apply the divergence theorem.
This gives $4 \pi r^2 \Phi'(r) = 4 \pi G m(r)$, so $\Phi'(r) = G m(r)/r^2$, which is [[Newton's law of gravitation|29WRN5J730]] for the mass inside $r$.
Example: in a ball of uniform density $\rho_0$ and radius $R$ with $P(R) = 0$, integrating gives the central pressure $P(0) = \frac{2}{3} \pi G \rho_0^2 R^2$.
Example: in a thin layer near the ground with constant $g = \abs{\nabla \Phi}$, part 1 gives $dP/dz = -\rho g$, the barometric law of a column of air or water.
The hypothesis $v = 0$ is needed: in a rotating star the centrifugal term adds to $\nabla \Phi$ and the surfaces of equal pressure are no longer spheres.

## Explanations

### L1 human

A star, a planet's atmosphere or the water in a lake stays put because two forces balance at every point.
Gravity pulls each piece of fluid down, and the pressure below it is a little larger than the pressure above it, which pushes it up.
Hydrostatic equilibrium says that the drop in pressure as one goes up is exactly the weight of the fluid per unit area.
This is why the pressure at the centre of the Sun must be enormous: it carries the weight of all the layers above it.

### L2 human

In the equations of [[stellar structure|SBKFDNEMFF]], hydrostatic equilibrium is the equation for $dP/dr$.
Combined with a relation between pressure and density, such as a polytropic law $P = K \rho^{1 + 1/n}$, it reduces to a single second-order equation, the [[Lane–Emden equation|ANRZZMH2Q0]].
Multiplying by $4 \pi r^3$ and integrating over the star gives the [[virial theorem|6T0BTVNMRF]] for a self-gravitating gas: $3 \int P \, dV$ equals minus the gravitational energy.
In general relativity the equation is replaced by the Tolman–Oppenheimer–Volkoff equation, which leads to an upper bound on the mass of neutron stars.
