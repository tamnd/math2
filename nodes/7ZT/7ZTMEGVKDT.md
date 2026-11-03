---
tag: 7ZTMEGVKDT
kind: definition
name: Relativistic Lagrangian of a free particle
msc: [70H40, 83A05]
defines: NS4MJT699T
uses: [G49G4R1K04, YG74WHC3S9, T0WAGV4KP4, 47JMCBM3VJ]
sources:
  - url: https://en.wikipedia.org/wiki/Relativistic_Lagrangian_mechanics
---

## Definition

Let $c > 0$ be the speed of light, let $m > 0$, and fix an inertial frame of [[Minkowski space|G49G4R1K04]] with time $t$ and position $\vec x \in \R^3$.
The *relativistic Lagrangian of a free particle* of mass $m$ is the function
$$L(\vec x, \vec v) = -mc^2 \sqrt{1 - \frac{\abs{\vec v}^2}{c^2}}, \qquad \abs{\vec v} < c,$$
of the position $\vec x$ and the velocity $\vec v = d\vec x/dt$.
Its [[action|T0WAGV4KP4]] along a path $\vec x(t)$, $t_1 \le t \le t_2$, is
$$S = \int_{t_1}^{t_2} L \, dt = -mc^2 \int d\tau,$$
where $\tau$ is the [[proper time|YG74WHC3S9]] of the path.

## Remarks

The canonical momentum is $\partial L/\partial \vec v = \gamma m \vec v$ with $\gamma = 1/\sqrt{1 - \abs{\vec v}^2/c^2}$, the relativistic momentum.
The Euler–Lagrange equation is $\frac{d}{dt}(\gamma m \vec v) = 0$, so $\vec v$ is constant, as it must be for a free particle.
The energy function is $\vec v \cdot \partial L/\partial \vec v - L = \gamma m \abs{\vec v}^2 + mc^2/\gamma = \gamma m c^2$.
Example: for $\vec v = 0$, $L = -mc^2$, and the action of a particle at rest from $t_1$ to $t_2$ is $-mc^2(t_2 - t_1)$.
Non-example: the Newtonian Lagrangian $\frac12 m \abs{\vec v}^2$ is not of this form, since its action is not a multiple of the proper time.
So it is not Lorentz invariant; it is only the low-speed limit of $L + mc^2$.
In a manifestly invariant form, $S = -mc \int \sqrt{-\eta(\dot x, \dot x)} \, d\lambda$ for any parametrisation $\lambda \mapsto x(\lambda)$ of the world line, with $\eta = \operatorname{diag}(-1, 1, 1, 1)$.
Since a straight timelike world line maximises proper time, it minimises $S$ among nearby paths with the same endpoints.
