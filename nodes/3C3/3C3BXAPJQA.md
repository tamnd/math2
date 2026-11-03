---
tag: 3C3BXAPJQA
kind: statement
role: theorem
name: Alfvén's frozen-in flux theorem
msc: [76W05, 76X05]
uses: [ZSA13P8P81, T8JWCBK9M6, 0AKRKVHW94, 0NF6GQNXMY, 0MWV6ZTK6S]
about: [ZSA13P8P81]
sources:
  - url: https://en.wikipedia.org/wiki/Alfvén's_theorem
same_as:
  wikidata: Q25303782
  wikipedia: Alfvén's theorem
---

## Statement

Let $\Omega \subseteq \R^3$ be open, and let $\mathbf{u}$ and $\mathbf{B}$ be smooth vector fields on $\Omega \times [0, T]$.
Assume that they satisfy the ideal induction equation and the divergence constraint
$$\frac{\partial \mathbf{B}}{\partial t} = \nabla \times (\mathbf{u} \times \mathbf{B}), \qquad \nabla \cdot \mathbf{B} = 0.$$
Let $\phi_t$ be the flow map of $\mathbf{u}$, so that $t \mapsto \phi_t(a)$ is the path of the fluid particle that starts at $a$.
Let $S$ be a compact oriented smooth surface with boundary, and let $S_t = \phi_t(S)$ stay in $\Omega$ for $t \in [0, T]$.
Then the magnetic flux
$$\Phi(t) = \int_{S_t} \mathbf{B}(x, t) \cdot \mathbf{n} \, dA$$
is constant on $[0, T]$.

## Remarks

The proof uses the transport formula for the flux through a moving surface:
$$\frac{d\Phi}{dt} = \int_{S_t} \left( \partial_t \mathbf{B} - \nabla \times (\mathbf{u} \times \mathbf{B}) + \mathbf{u} \, (\nabla \cdot \mathbf{B}) \right) \cdot \mathbf{n} \, dA,$$
which follows from [[Stokes' theorem|0AKRKVHW94]] applied to the boundary of $S_t$.
Under the hypotheses the integrand vanishes.
A consequence is that field lines are material lines: a curve tangent to $\mathbf{B}$ at time $0$ stays tangent to $\mathbf{B}$ when it is carried by the flow.
The same equation is satisfied by the vorticity of an ideal barotropic fluid, and the theorem then becomes [[Kelvin's circulation theorem|BWMB87Q6DM]] together with [[Helmholtz's theorems on vortices|D2KCKEP0N4]].
If the magnetic diffusivity $\eta$ is positive, the induction equation gains the term $\eta \Delta \mathbf{B}$ and the flux is no longer conserved.
Field lines can then diffuse through the fluid and change their connections.

## Explanations

### L1 human

In a perfectly conducting fluid, magnetic field lines are glued to the fluid.
Draw a small loop in the fluid and count how much magnetic field goes through it.
As the fluid moves, the loop moves and deforms, but the amount of field through it never changes.
This is why the Sun's moving surface can twist and pile up its magnetic field.

### L2 human

The theorem is the main qualitative fact of [[ideal MHD|ZSA13P8P81]].
It says that the topology of the field lines cannot change in an ideal flow, so linked or knotted flux tubes stay linked or knotted.
It also gives a Lagrangian formula: in the compressible case, $\mathbf{B}/\rho$ is transported like a line element, that is, $\mathbf{B}(\phi_t(a), t)/\rho(\phi_t(a), t) = D\phi_t(a) \, \mathbf{B}(a, 0)/\rho(a, 0)$.
Stretching of fluid elements thus amplifies the field, which is the starting point of dynamo theory.
Breaking the theorem needs resistivity, and the resulting change of topology is magnetic reconnection.
