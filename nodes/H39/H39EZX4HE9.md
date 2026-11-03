---
tag: H39EZX4HE9
kind: definition
name: Plane strain
msc: [74B05, 74A05]
defines: JQT1GBRYTY
uses: [8QS6QMJF5Z, X121AYEY67]
sources:
  - url: https://en.wikipedia.org/wiki/Infinitesimal_strain_theory
---

## Definition

Let $u$ be a displacement field on a region of $\R^3$ in [[infinitesimal strain theory|X121AYEY67]], and let $\varepsilon = \tfrac12 (\nabla u + (\nabla u)^T)$ be its [[strain tensor|8QS6QMJF5Z]].
Let $(x_1, x_2, x_3)$ be Cartesian coordinates.
The field $u$ is in *plane strain* with respect to the $x_1 x_2$-plane if it has the form
$$u(x_1, x_2, x_3) = \big( u_1(x_1, x_2), \; u_2(x_1, x_2), \; 0 \big).$$
Then $\varepsilon_{13} = \varepsilon_{23} = \varepsilon_{33} = 0$, and the other components depend only on $x_1$ and $x_2$.

## Remarks

Example: the shear $u = (\gamma x_2, 0, 0)$ is in plane strain, with $\varepsilon_{12} = \gamma/2$ as its only nonzero strain component.

Non-example: for an isotropic material with Poisson's ratio $\nu \ne 0$, uniaxial stress along $x_1$ produces the strain $\varepsilon_{33} = -\nu \varepsilon_{11} \ne 0$, so this state is not in plane strain with respect to the $x_1 x_2$-plane.

For an isotropic linear elastic material in plane strain, the out-of-plane stress is $\sigma_{33} = \nu (\sigma_{11} + \sigma_{22})$, which is not zero in general.
The in-plane equations of plane strain have the same form as those of plane stress, with the elastic constants changed: $E$ is replaced by $E/(1 - \nu^2)$ and $\nu$ by $\nu/(1 - \nu)$.
