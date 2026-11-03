---
tag: 25ZMP5THH9
kind: statement
role: theorem
name: Rayleigh's inflection point criterion
msc: ["76E05"]
uses: [06MG208MGR, G0ADVS0K99, H028A17Z55]
about: [H028A17Z55]
sources:
  - url: https://en.wikipedia.org/wiki/Rayleigh's_equation_(fluid_dynamics)
---

## Statement

Consider an inviscid incompressible parallel shear flow $\mathbf{u} = (U(y), 0)$ between rigid walls $y = y_1$ and $y = y_2$, where $U$ is twice continuously differentiable on $[y_1, y_2]$.
A normal mode disturbance with stream function $\varphi(y) e^{i \alpha (x - c t)}$, where $\alpha > 0$ and $c \in \C$, satisfies the Rayleigh equation
$$(U - c)(\varphi'' - \alpha^2 \varphi) - U'' \varphi = 0, \qquad \varphi(y_1) = \varphi(y_2) = 0.$$
If this problem has a nonzero solution $\varphi$ with $\operatorname{Im} c > 0$, then $U''$ takes both positive and negative values on $(y_1, y_2)$.
In particular, a necessary condition for linear instability is that the velocity profile $U$ has an [[inflection point|06MG208MGR]] $y_s \in (y_1, y_2)$ with $U''(y_s) = 0$.

## Remarks

Write $c = c_r + i c_i$ with $c_i > 0$, so that $U - c \neq 0$ on $[y_1, y_2]$.
Divide the equation by $U - c$, multiply by the complex conjugate $\bar\varphi$ and integrate by parts using the boundary conditions:
$$\int_{y_1}^{y_2} \left( \abs{\varphi'}^2 + \alpha^2 \abs{\varphi}^2 \right) dy + \int_{y_1}^{y_2} \frac{U'' \abs{\varphi}^2}{U - c} \, dy = 0.$$
The imaginary part gives $c_i \int U'' \abs{\varphi}^2 / \abs{U - c}^2 \, dy = 0$.
If $U''$ kept one sign, this would force $U'' \abs{\varphi}^2 = 0$ everywhere, and then the real part would give $\int ( \abs{\varphi'}^2 + \alpha^2 \abs{\varphi}^2 ) \, dy = 0$, so $\varphi = 0$.

The Rayleigh equation is the limit $\mathrm{Re} \to \infty$ of the [[Orr–Sommerfeld equation|G0ADVS0K99]], that is, the linearisation of the Euler equations.
Plane Couette flow $U(y) = y$ and plane Poiseuille flow $U(y) = 1 - y^2$ have no inflection point, so they are stable in the inviscid theory.
Plane Poiseuille flow is nevertheless unstable for large finite Reynolds number, so the criterion says nothing about viscous instability.
The criterion is necessary but not sufficient.
Fjørtoft later gave a sharper necessary condition: $U''(U - U(y_s)) < 0$ somewhere in the flow.

## Explanations

### L1 human

Some layered flows are fragile and some are robust.
Rayleigh found a simple test for flows without friction.
A flow can only be unstable if its velocity profile bends one way in some places and the other way in others.
A jet or a mixing layer between two streams has such a bend, and these flows indeed break up into waves and eddies.
A flow whose profile curves the same way everywhere cannot be unstable in this frictionless model.

### L2 human

The criterion is the first result of inviscid [[hydrodynamic stability|H028A17Z55]].
Its proof is an energy-type identity: multiply the Rayleigh equation by the conjugate amplitude and integrate.
The same technique, applied to the Taylor–Goldstein equation for stratified flows, gives the Miles–Howard criterion and Howard's semicircle theorem.
Flows with an inflection point, such as the profile $U(y) = \tanh y$ of a mixing layer, are typically unstable at high Reynolds number through an inviscid mechanism.
Flows without one, such as boundary layers with a favourable pressure gradient, become unstable only through viscous effects, as Tollmien–Schlichting waves.
