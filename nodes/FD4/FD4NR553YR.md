---
tag: FD4NR553YR
kind: statement
role: theorem
name: Continuity equation
msc: [76A02, 35Q35]
uses: [H27M44BV4M, 0MWV6ZTK6S, CJW50K5HZB, 0JX86PSSA9, 18KXZHVF4M]
about: [H27M44BV4M]
sources:
  - url: https://en.wikipedia.org/wiki/Continuity_equation
    locator: Fluid dynamics
---

## Statement

Let $\Omega \subseteq \R^3$ be open and let $I$ be an open interval.
Let $\rho \colon \Omega \times I \to (0, \infty)$ be the density and $\mathbf{u} \colon \Omega \times I \to \R^3$ the velocity of a fluid, both continuously differentiable.
Suppose that mass is conserved in the following sense.
For every bounded open set $V$ with smooth boundary $\partial V$, closure $\overline{V} \subseteq \Omega$ and outward unit normal $\mathbf{n}$, and for every $t \in I$,
$$\frac{d}{dt} \int_V \rho \, dV = - \oint_{\partial V} \rho \, \mathbf{u} \cdot \mathbf{n} \, dA.$$
Then at every point of $\Omega \times I$,
$$\frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \mathbf{u}) = 0,$$
or equivalently $\dfrac{D\rho}{Dt} + \rho \, \nabla \cdot \mathbf{u} = 0$, where $D/Dt$ is the [[material derivative|CJW50K5HZB]].
Conversely, this equation implies the integral law for every such $V$.

## Remarks

By the [[divergence theorem|0JX86PSSA9]], the integral law says $\int_V \left( \partial_t \rho + \nabla \cdot (\rho \mathbf{u}) \right) dV = 0$ for every small ball $V$.
The integrand is continuous, so if it were nonzero at a point it would keep its sign on a small ball around that point, and the integral would not vanish.
The second form follows from $\nabla \cdot (\rho \mathbf{u}) = \mathbf{u} \cdot \nabla \rho + \rho \, \nabla \cdot \mathbf{u}$.
Example: for constant density, the equation reduces to $\nabla \cdot \mathbf{u} = 0$, the condition of incompressible flow.
Example: the one-dimensional gas $\rho(x, t) = 1/(1 + t)$, $u(x, t) = x/(1 + t)$ satisfies it, since $\partial_t \rho = -1/(1 + t)^2$ and $\partial_x (\rho u) = 1/(1 + t)^2$.

## Explanations

### L1 human

Mass is neither created nor destroyed in a moving fluid.
So the mass inside any fixed box can only change by fluid crossing the walls of the box.
The continuity equation writes this bookkeeping rule at a single point.
If the fluid flows out of a point in all directions, the density there must drop.

### L2 human

The continuity equation is the first of the equations of motion of a fluid, next to the momentum equation and the energy equation.
It has the form of a conservation law $\partial_t \rho + \nabla \cdot \mathbf{j} = 0$ with flux $\mathbf{j} = \rho \mathbf{u}$, and the same form governs electric charge, probability in quantum mechanics and heat.
In the [[divergence|0MWV6ZTK6S]] form it couples the density to the velocity; for an incompressible fluid it becomes the constraint $\nabla \cdot \mathbf{u} = 0$ in the [[Navier–Stokes equations|18KXZHVF4M]].
The passage from the integral law to the pointwise law needs the fields to be continuously differentiable; for flows with shocks only the integral form survives.
