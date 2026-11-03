---
tag: V56XAESDNE
kind: statement
role: fact
name: Hooke's law
msc: [74B05, 74A20]
uses: [8QS6QMJF5Z, KG2XWEMJ30, SX32X1D537, 80737NDZ4V, T8ENJX1905, NWYZ9QBA84, GQ3K59MRJP]
about: [6W00ZECYT0]
sources:
  - url: https://en.wikipedia.org/wiki/Hooke%27s_law
same_as:
  wikidata: Q170282
  wikipedia: Hooke's law
---

## Statement

Consider a linear elastic material undergoing small deformations.
At each point, the [[Cauchy stress tensor|KG2XWEMJ30]] $\sigma$ is a linear function of the [[strain tensor|8QS6QMJF5Z]] $\varepsilon$.
In components, $\sigma_{ij} = C_{ijkl} \, \varepsilon_{kl}$ with summation over repeated indices.
Here $C$ is the [[elasticity tensor|SX32X1D537]] of the material.
If the material is also isotropic, there are two constants $\lambda$ and $\mu$, the [[Lamé parameters|80737NDZ4V]], such that
$$\sigma = \lambda (\tr \varepsilon) I + 2 \mu \varepsilon,$$
where $I$ is the identity tensor.

## Remarks

Hooke's law is a constitutive law, an empirical model valid for many solids under small strains, not a theorem.
In its original one-dimensional form it says that a spring stretched by $x$ pulls back with force $F = -kx$, where $k > 0$ is the stiffness.
The isotropic form follows from the general one: a fourth-order tensor with the symmetries of $C$ that is invariant under all rotations has the form $C_{ijkl} = \lambda \delta_{ij} \delta_{kl} + \mu (\delta_{ik} \delta_{jl} + \delta_{il} \delta_{jk})$.
With [[Young's modulus|T8ENJX1905]] $E$ and [[Poisson's ratio|NWYZ9QBA84]] $\nu$ the isotropic law inverts to $\varepsilon = \frac{1 + \nu}{E} \sigma - \frac{\nu}{E} (\tr \sigma) I$.
For a bar in uniaxial tension it reduces to $\sigma_{11} = E \varepsilon_{11}$.
The law fails for large strains, near yield, and for materials such as rubber at moderate stretch.

## Explanations

### L1 human

Pull a spring twice as hard and it stretches twice as far.
Hooke's law is this rule of proportionality, extended from springs to solid materials.
In a solid, the stretching is measured by the strain and the internal force by the stress, and the law says that stress is proportional to strain.
It is what makes the theory of elastic solids linear.

### L2 human

In [[linear elasticity|6W00ZECYT0]] Hooke's law is the constitutive equation that closes the system of balance equations.
In general an anisotropic material needs up to $21$ constants, the independent entries of $C$.
Material symmetry reduces this number: cubic crystals need $3$ and isotropic materials need $2$.
Substituting the isotropic law into the equilibrium equations gives the [[Lamé equations|GQ3K59MRJP]].
