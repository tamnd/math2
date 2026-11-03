---
tag: SG3RXYFQ3B
kind: example
name: Kelvin solution for a point force
msc: [74B05, 74G05, 35Q74]
illustrates: [GQ3K59MRJP]
uses: [GQ3K59MRJP, GWGMRAD7HF, 0KPHENZ5S7, 0DEB0JMN0W, NWYZ9QBA84, 80737NDZ4V]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_elasticity
---

## Example

Consider an infinite homogeneous isotropic linear elastic body filling $\R^3$, with shear modulus $\mu > 0$ and [[Poisson's ratio|NWYZ9QBA84]] $\nu \in (-1, 1/2)$.
A point force $F \in \R^3$ acts at the origin, so the body force is $F \delta_0$, where $\delta_0$ is the [[Dirac delta|0KPHENZ5S7]].
The Kelvin solution is the displacement
$$u_i(x) = \frac{1}{16 \pi \mu (1 - \nu)} \left( \frac{(3 - 4\nu) \, \delta_{ij}}{r} + \frac{x_i x_j}{r^3} \right) F_j, \qquad r = \abs{x} \ne 0,$$
with summation over $j$.
It solves the [[Lamé equations|GQ3K59MRJP]] $\mu \Delta u + (\lambda + \mu) \nabla (\nabla \cdot u) + F \delta_0 = 0$ in the sense of distributions, where $\lambda = 2\mu\nu/(1 - 2\nu)$ is the first [[Lamé parameter|80737NDZ4V]], and $u(x) \to 0$ as $\abs{x} \to \infty$.

Check away from the origin: let $\psi = \frac{F}{8\pi(1-\nu) r}$, a vector field whose components are [[harmonic|0DEB0JMN0W]] on $\R^3 \setminus \{0\}$.
Using $\nabla \frac{x \cdot F}{r} = \frac{F}{r} - \frac{(x \cdot F) x}{r^3}$, one finds $u = \frac{1}{2\mu} \big( 4(1-\nu) \psi - \nabla (x \cdot \psi) \big)$, a [[Papkovich–Neuber representation|GWGMRAD7HF]].
Since $\Delta (x \cdot \psi) = 2 \nabla \cdot \psi$, this gives $\Delta u = -\frac{1}{\mu} \nabla (\nabla \cdot \psi)$ and $\nabla \cdot u = \frac{1 - 2\nu}{\mu} \nabla \cdot \psi$.
With $\lambda + \mu = \frac{\mu}{1 - 2\nu}$, the sum $\mu \Delta u + (\lambda + \mu) \nabla (\nabla \cdot u)$ is $-\nabla (\nabla \cdot \psi) + \nabla (\nabla \cdot \psi) = 0$.
The constant in front is fixed by requiring that the tractions on every sphere centred at $0$ balance the point force $F$.
The stresses decay like $r^{-2}$.

## Explanations

### L1 human

Push on a single point deep inside a huge block of jelly.
The Kelvin solution tells how every other point of the block moves.
The displacement falls off like one over the distance, and it is larger along the line of the push than across it.
It is the elastic analogue of the field of a point charge, and more complicated solutions are built by adding up many such point forces.
