---
tag: PWBQFRKR3F
kind: definition
name: Added mass
msc: [76B99]
defines: 2BS252PEJG
uses: [84K7TEWZ2Z, 470A1RJWBP, S8RG6N1PRT]
sources:
  - url: https://en.wikipedia.org/wiki/Added_mass
---

## Definition

Let $B \subset \R^3$ be a bounded rigid body with smooth boundary $S$.
Let $\Omega = \R^3 \setminus B$ be filled with an inviscid incompressible fluid of constant density $\rho$, at rest at infinity.
Suppose $B$ translates without rotation with velocity $U(t) = (U_1, U_2, U_3)$ and the flow is a [[potential flow|84K7TEWZ2Z]].
Let $n$ be the unit normal on $S$ pointing into the fluid.
For $i = 1, 2, 3$ let $\phi_i$ solve [[Laplace's equation|S8RG6N1PRT]] $\Delta \phi_i = 0$ in $\Omega$, with $\partial \phi_i / \partial n = n_i$ on $S$ and $\nabla \phi_i \to 0$ at infinity.
Then the [[velocity potential|470A1RJWBP]] is $\phi = \sum_i U_i \phi_i$, and the kinetic energy of the fluid is
$$T = \frac{\rho}{2} \int_\Omega \abs{\nabla \phi}^2 \, dV = \frac{1}{2} \sum_{i,j=1}^3 m_{ij} U_i U_j, \qquad m_{ij} = \rho \int_\Omega \nabla \phi_i \cdot \nabla \phi_j \, dV.$$
The symmetric matrix $(m_{ij})$ is the *added mass tensor* of $B$.

## Remarks

Example: a sphere of radius $a$ has $\phi_i = -\frac{a^3 x_i}{2\abs{x}^3}$, and the added mass tensor is $m_{ij} = \tfrac{1}{2}\rho \cdot \tfrac{4}{3}\pi a^3 \, \delta_{ij}$, half the mass of the displaced fluid.
Check: on $\abs{x} = a$ with $n = x/a$, $\partial \phi_i / \partial n = \frac{a^3 x_i}{\abs{x}^4} = n_i$.
Non-example: a body moving through fluid that carries its own vortices is not covered.
The flow is then not a potential flow, and the energy does not split as above.
For a body of mass $M$ accelerating in a fluid otherwise at rest, the fluid exerts the force $-\sum_j m_{ij} \, dU_j/dt$, so the body moves as if its mass matrix were $M\delta_{ij} + m_{ij}$.
The tensor is positive definite, since $\sum m_{ij} c_i c_j = \rho \int_\Omega \abs{\nabla(\sum c_i \phi_i)}^2 \, dV > 0$ for $c \neq 0$.
In two dimensions the same definition per unit length gives $\rho \pi a^2$ for a circular cylinder of radius $a$.
