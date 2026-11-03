---
tag: VB6HD8CH94
kind: definition
name: Reynolds stress
msc: [76F02, 76F55]
defines: FDQE4PF63G
uses: [V47TX9AFKF, VY307F8Z0S]
sources:
  - url: https://en.wikipedia.org/wiki/Reynolds_stress
---

## Definition

Consider a flow of an incompressible fluid with constant density $\rho$ and velocity $\mathbf{u} = (u_1, u_2, u_3)$.
Let $u_i = \bar u_i + u_i'$ be the [[Reynolds decomposition|V47TX9AFKF]] of the velocity components with respect to an averaging operation.
The *Reynolds stress tensor* is the symmetric tensor with components
$$\tau_{ij} = -\rho \, \overline{u_i' u_j'}, \qquad i, j = 1, 2, 3.$$

## Remarks

Many authors call $R_{ij} = \overline{u_i' u_j'}$ itself the Reynolds stress tensor, without the factor $-\rho$.
The matrix $(R_{ij})$ is symmetric and positive semidefinite, since $\sum_{i,j} a_i a_j R_{ij} = \overline{(a \cdot \mathbf{u}')^2} \ge 0$ for every vector $a$.
Half its trace is the turbulent kinetic energy per unit mass, $k = \frac12 \overline{u_i' u_i'}$.
The diagonal terms are normal stresses and the off-diagonal terms are shear stresses.

Example: take a turbulent channel flow with mean velocity $\bar u_1(x_2)$ increasing away from the lower wall.
Eddies moving up ($u_2' > 0$) tend to carry slow fluid ($u_1' < 0$), so $\overline{u_1' u_2'} < 0$.
Thus the shear stress $\tau_{12}$ is positive and acts like an extra friction.
Non-example: in a laminar steady flow the fluctuations vanish, so all $\tau_{ij}$ are zero; the viscous stress $\mu (\partial_j u_i + \partial_i u_j)$ is not a Reynolds stress.
