---
tag: RT1JE5V0PW
kind: statement
role: fact
name: Duhamel–Neumann law
msc: [74F05, 74B05]
uses: [V56XAESDNE, SX32X1D537, 8QS6QMJF5Z, KG2XWEMJ30, 80737NDZ4V]
about: [58ZRHE8MQK]
sources:
  - url: https://en.wikipedia.org/wiki/Thermal_stress
---

## Statement

Consider a linear elastic material with [[elasticity tensor|SX32X1D537]] $C_{ijkl}$ and symmetric tensor of thermal expansion coefficients $\alpha_{kl}$.
Let it be at a reference temperature $T_0$ where it is free of stress.
Let $\varepsilon_{kl}$ be the [[infinitesimal strain|8QS6QMJF5Z]] and $\theta = T - T_0$ a small temperature change.
Then the [[stress|KG2XWEMJ30]] is
$$\sigma_{ij} = C_{ijkl} \left(\varepsilon_{kl} - \alpha_{kl} \theta\right),$$
with summation over repeated indices.
For an isotropic material with [[Lamé parameters|80737NDZ4V]] $\lambda, \mu$ and expansion coefficient $\alpha$, so that $\alpha_{kl} = \alpha \delta_{kl}$, this reads
$$\sigma_{ij} = \lambda \varepsilon_{kk} \delta_{ij} + 2\mu \varepsilon_{ij} - (3\lambda + 2\mu) \alpha \theta \delta_{ij}.$$

## Remarks

The law says that the strain splits into an elastic part, related to stress by [[Hooke's law|V56XAESDNE]], and a thermal part $\alpha_{kl}\theta$ that produces no stress.
It follows from a free energy that is quadratic in $\varepsilon$ and $\theta$, $\psi = \tfrac12 C_{ijkl} \varepsilon_{ij} \varepsilon_{kl} - C_{ijkl} \alpha_{kl} \theta \varepsilon_{ij} + (\text{terms in } \theta \text{ only})$, through $\sigma_{ij} = \partial \psi / \partial \varepsilon_{ij}$.
Example: a bar that is free to expand has $\sigma = 0$ and strain $\alpha\theta$.
A bar of Young's modulus $E$ held at fixed length has axial strain $0$ and axial stress $-E \alpha \theta$, which is compressive when it is heated.
Since $3\lambda + 2\mu = 3K$ with $K$ the bulk modulus, the isotropic thermal term is $-3K\alpha\theta\delta_{ij}$.

## Explanations

### L1 human

Heating makes a material want to grow by a fixed fraction in every direction.
The Duhamel–Neumann law says that only the part of the strain beyond this free thermal growth causes stress, and it does so through the usual elastic constants.
So a heated part that is free to expand has no stress, while a heated part that is held in place is compressed.

### L2 human

This law is the constitutive equation of linear thermoelasticity.
Inserted into the equilibrium equations, it shows that a temperature field acts like a body force $-\nabla (3K\alpha\theta)$.
It also adds a normal boundary traction $3K\alpha\theta n$, and this is how thermal stress problems are reduced to ordinary elastic ones.
A temperature field that is linear in the coordinates produces no stress in a free, simply connected body of homogeneous isotropic material, since the thermal strain is then compatible.
