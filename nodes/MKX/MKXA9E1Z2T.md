---
tag: MKXA9E1Z2T
kind: statement
role: fact
name: Clausius–Duhem inequality
msc: [74A15, 80A10]
uses: [KG2XWEMJ30, Q4C55V47A8, 0MWV6ZTK6S]
about: [X01DZTS224]
sources:
  - url: https://en.wikipedia.org/wiki/Clausius%E2%80%93Duhem_inequality
same_as:
  wikidata: Q5129547
  wikipedia: Clausius–Duhem inequality
---

## Statement

Consider a continuous body with mass density $\rho > 0$ and absolute temperature $\theta > 0$.
Let $\eta$ be its specific entropy, $q$ its heat flux vector and $r$ its heat supply per unit mass, all smooth in position and time.
The Clausius–Duhem inequality requires that, at every point and time,
$$\rho \dot\eta \ge \frac{\rho r}{\theta} - \nabla \cdot \left( \frac{q}{\theta} \right),$$
where $\dot\eta$ is the material time derivative and $\nabla \cdot$ is the [[divergence|0MWV6ZTK6S]].

## Remarks

It is the local form of the second law of thermodynamics for continua.
Its integral form concerns a part $P$ of the body.
The entropy of $P$ grows at least at the rate of entropy supplied by heat sources in $P$ plus entropy carried in by heat flow across the boundary.
The divergence theorem turns this integral form into the local one.
Let $e$ be the specific internal energy and $\psi = e - \theta \eta$ the specific free energy.
With the local energy balance $\rho \dot e = \sigma : D - \nabla \cdot q + \rho r$, the inequality takes the reduced form
$$\sigma : D - \rho (\dot\psi + \eta \dot\theta) - \frac{q \cdot \nabla \theta}{\theta} \ge 0,$$
where $\sigma$ is the [[Cauchy stress tensor|KG2XWEMJ30]] and $D$ is the rate of deformation.
In the method of Coleman and Noll one requires this inequality for every possible process.
If the free energy depends on the deformation gradient and the temperature, this forces the stress and the entropy to be derivatives of the free energy.
For a rigid heat conductor it gives $q \cdot \nabla \theta \le 0$: heat flows from hot to cold.

## Explanations

### L1 human

The second law of thermodynamics says that entropy cannot be destroyed.
The Clausius–Duhem inequality writes this law at each point of a deforming material.
It says that the entropy at a point grows at least as fast as heat brings entropy in.
Engineers use it as a test: a proposed material law that would let entropy decrease in some process is rejected.

### L2 human

In continuum mechanics the balance laws of mass, momentum and energy hold for every material, and the Clausius–Duhem inequality is the extra restriction that comes from the second law.
Its main use is in the theory of [[constitutive equations|Q4C55V47A8]]: one asks which constitutive laws make the reduced inequality hold in all processes.
For thermoelastic materials this gives $\sigma$ as a derivative of $\psi$ with respect to strain, and $\eta = -\partial \psi / \partial \theta$.
For viscous and plastic materials it says that the dissipation, the left side of the reduced inequality, is never negative.
