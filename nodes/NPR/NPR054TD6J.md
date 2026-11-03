---
tag: NPR054TD6J
kind: definition
name: Electric displacement field
msc: [78A30, 78A25]
defines: NJVXQZ780B
uses: [YZ7Q9DP8RT, ASQAH710WN, RWHF5M1H72, 0MWV6ZTK6S]
sources:
  - url: https://en.wikipedia.org/wiki/Electric_displacement_field
---

## Definition

Let $\varepsilon_0 > 0$ be the vacuum permittivity.
Let $E$ be the [[electric field|YZ7Q9DP8RT]] in a region of $\R^3$ that may contain a dielectric with [[polarization density|ASQAH710WN]] $P$, with $P = 0$ outside the material.
The *electric displacement field* is the vector field
$$D = \varepsilon_0 E + P.$$

## Remarks

Write the total charge density as $\rho = \rho_f + \rho_b$, with free charge $\rho_f$ and bound charge $\rho_b = -\nabla \cdot P$.
Then [[Gauss's law|RWHF5M1H72]] $\varepsilon_0 \nabla \cdot E = \rho$ becomes $\nabla \cdot D = \rho_f$, where $\nabla \cdot$ is the [[divergence|0MWV6ZTK6S]].
Example: in vacuum $P = 0$, so $D = \varepsilon_0 E$, and a point charge $q$ at $0$ gives $D(x) = q x / (4 \pi \abs{x}^3)$.
In a linear isotropic medium $D = \varepsilon E$ with permittivity $\varepsilon$.
Non-example: in general $\nabla \times D \ne 0$ even in electrostatics, since $\nabla \times P$ can be nonzero, so $D$ need not be the gradient of a potential.
At an interface without free surface charge, the normal component of $D$ is continuous.
The unit of $D$ is the coulomb per square metre.
