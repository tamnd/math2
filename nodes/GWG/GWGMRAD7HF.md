---
tag: GWGMRAD7HF
kind: statement
role: theorem
name: Papkovich–Neuber solution
msc: [74B05, 74G05, 35Q74]
uses: [GQ3K59MRJP, 0DEB0JMN0W, NWYZ9QBA84]
about: [GQ3K59MRJP]
sources:
  - url: https://en.wikipedia.org/wiki/Papkovich%E2%80%93Neuber_solution
same_as:
  wikidata: Q7133037
  wikipedia: Papkovich–Neuber solution
---

## Statement

Let $\Omega \subseteq \R^3$ be an open set.
Consider a homogeneous isotropic linear elastic material with shear modulus $\mu > 0$ and [[Poisson's ratio|NWYZ9QBA84]] $\nu \in (-1, 1/2)$, and no body force.
Let $\psi \colon \Omega \to \R^3$ be a vector field and $\phi \colon \Omega \to \R$ a function, all of whose components are [[harmonic|0DEB0JMN0W]].
Then the displacement
$$u = \frac{1}{2\mu} \Big( 4 (1 - \nu) \psi - \nabla (x \cdot \psi + \phi) \Big)$$
solves the static [[Lamé equations|GQ3K59MRJP]] $\mu \Delta u + (\lambda + \mu) \nabla (\nabla \cdot u) = 0$ in $\Omega$, where $\lambda = 2\mu\nu/(1 - 2\nu)$.
Conversely, if $\Omega$ is convex, every solution $u$ of class $C^2$ of these equations on $\Omega$ has this form for some harmonic $\psi$ and $\phi$.

## Remarks

The direct part is a computation: $\Delta (x \cdot \psi) = 2 \nabla \cdot \psi$ for harmonic $\psi$, so $\Delta u = -\frac{1}{\mu} \nabla (\nabla \cdot \psi)$ and $\nabla \cdot u = \frac{1 - 2\nu}{\mu} \nabla \cdot \psi$.
Since $\lambda + \mu = \frac{\mu}{1 - 2\nu}$, the two terms of the Lamé operator cancel.
Example: $\psi = \frac{F}{8\pi(1 - \nu) \abs{x}}$ and $\phi = 0$ give the Kelvin solution for a point force on $\R^3 \setminus \{0\}$.
The representation is not unique: for example, adding a constant to $\phi$ does not change $u$.

## Explanations

### L1 human

The equations of linear elasticity couple the three components of the displacement in a complicated way.
The Papkovich–Neuber solution writes every displacement in terms of four harmonic functions, the same functions that describe gravitational or electric potentials.
Since harmonic functions are very well understood, this turns hard elasticity problems into potential theory problems.

### L2 human

The representation is a standard tool for three-dimensional elastostatics.
One chooses harmonic potentials adapted to the geometry, for example spherical harmonics for a sphere.
The Boussinesq solution for a normal point load on a half-space can be written in this form.
It plays for the [[Lamé equations|GQ3K59MRJP]] a role similar to that of the Helmholtz decomposition for vector fields.
