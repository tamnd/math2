---
tag: WCGH22X05Y
kind: statement
role: theorem
name: Momentum integral equation
msc: [76D10]
uses: [XXDE4YP722, 6DZC6HPDH2]
about: [XXDE4YP722]
sources:
  - url: https://en.wikipedia.org/wiki/Boundary_layer_thickness
---

## Statement

Let $(u, v)$ be a steady solution of the [[Prandtl boundary layer equations|XXDE4YP722]] along the wall $y = 0$.
The density is $1$, the kinematic viscosity is $\nu > 0$, and the outer speed $U(x) > 0$ is smooth on an interval.
Assume that $u \to U$ and $\partial_y u \to 0$ fast enough as $y \to \infty$ for all the integrals below to converge.
Assume also that differentiation in $x$ may be taken under them.
Let $\delta^*$ be the [[displacement thickness|6DZC6HPDH2]], $\theta$ the momentum thickness, $H = \delta^* / \theta$ the shape factor and $\tau_w = \nu \, \partial_y u(x, 0)$ the wall shear stress.
Then
$$\frac{d\theta}{dx} + (2 + H) \frac{\theta}{U} \frac{dU}{dx} = \frac{\tau_w}{U^2}.$$
Equivalently, $\frac{d}{dx}\big( U^2 \theta \big) + U \frac{dU}{dx} \delta^* = \tau_w$.

## Remarks

The proof integrates the momentum equation $u \, \partial_x u + v \, \partial_y u = U U' + \nu \, \partial_y^2 u$ over $0 < y < \infty$.
The term with $v$ is handled by writing $v = -\int_0^y \partial_x u$ from continuity and integrating by parts, and the viscous term gives $-\tau_w$.
Collecting terms gives the second form, and dividing by $U^2$ gives the first.
Example: for a flat plate, $U$ is constant and the equation says $d\theta / dx = \tau_w / U^2$: the growth of the momentum deficit equals the skin friction.
With an assumed profile shape, such as a polynomial in $y / \delta$, the equation becomes an ordinary differential equation for $\delta(x)$; this is the Kármán–Pohlhausen method.

## Explanations

### L1 human

Friction at the wall takes momentum out of the fluid.
This equation is the bookkeeping: the momentum lost by the layer as it flows downstream equals the friction at the wall, corrected by the push of the pressure.
It holds for any layer, without solving the equations in detail.

### L2 human

The momentum integral equation is due to von Kármán in 1921.
Once one guesses a profile family, it turns the boundary layer equations into a single ordinary differential equation along the wall.
Such integral methods gave useful estimates of skin friction and of separation points long before numerical solution was easy.
They are still used for turbulent layers, with empirical closures for $H$ and $\tau_w$.
It is exact for the Prandtl equations; the approximation enters only through the assumed profile.
