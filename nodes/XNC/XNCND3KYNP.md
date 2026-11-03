---
tag: XNCND3KYNP
kind: statement
role: theorem
name: Hertzian contact stress
msc: [74M15, 74B05, 74G05]
uses: [T0R3FBPTJ2, T8ENJX1905, NWYZ9QBA84, 6W00ZECYT0]
about: [T0R3FBPTJ2]
sources:
  - url: https://en.wikipedia.org/wiki/Contact_mechanics
---

## Statement

Let two elastic spheres with radii $R_1, R_2 > 0$, [[Young's moduli|T8ENJX1905]] $E_1, E_2$ and [[Poisson's ratios|NWYZ9QBA84]] $\nu_1, \nu_2$ be pressed together by a force $F > 0$.
Assume [[linear elasticity|6W00ZECYT0]], smooth frictionless surfaces, and a contact region small compared with $R_1$ and $R_2$.
So each body is treated as an elastic half-space.
Define the effective radius $R$ and the effective modulus $E^*$ by
$$\frac{1}{R} = \frac{1}{R_1} + \frac{1}{R_2}, \qquad \frac{1}{E^*} = \frac{1 - \nu_1^2}{E_1} + \frac{1 - \nu_2^2}{E_2}.$$
Then the contact region is a disc of radius $a$ with $a^3 = 3 F R / (4 E^*)$.
Let $p_0 = 3F / (2 \pi a^2)$.
At distance $r \le a$ from the centre the contact pressure is
$$p(r) = p_0 \sqrt{1 - \frac{r^2}{a^2}}.$$
The approach $\delta$ of distant points of the two bodies satisfies $\delta = a^2 / R$, that is, $F = \tfrac{4}{3} E^* R^{1/2} \delta^{3/2}$.

## Remarks

The proof uses the fact that a pressure $p_0 \sqrt{1 - r^2/a^2}$ on a disc of an elastic half-space produces a surface displacement that is a quadratic function of $r$ inside the disc.
This matches the quadratic gap $r^2/(2R)$ between two spheres near their touching point, and the total force fixes $a$.
Integrating the pressure over the disc gives $F = \tfrac{2}{3} \pi a^2 p_0$.

Example: a steel ball of radius $10$ mm on a flat steel plate, so $R_2 = \infty$ and $R = 10$ mm.
With $E = 210$ GPa and $\nu = 0.3$ for both, $E^* \approx 115$ GPa, and a force of $100$ N gives $a \approx 0.19$ mm and $p_0 \approx 1.4$ GPa.

Friction and adhesion are ignored.
When the surfaces attract each other, the [[JKR model|98BMFJ17D9]] replaces this result.
The response $F \propto \delta^{3/2}$ is nonlinear even though the material is linear, because the contact region grows with the load.

## Explanations

### L1 human

When two balls are pressed together they touch on a small round patch, not at a point.
Hertz's result gives the size of that patch and the pressure in it.
The pressure is largest at the centre and falls to zero at the rim like the height of a dome.
The patch grows only like the cube root of the force.
This is why ball bearings and gear teeth can see very high stresses even at modest loads.

### L2 human

Hertz's solution is the model case of [[contact mechanics|T0R3FBPTJ2]], where the contact region is an unknown of the problem.
It builds on the [[Boussinesq problem|QJW6NMNXJM]] for a point load on a half-space, superposed over the contact disc.
The peak pressure $p_0$ and the subsurface shear stress it creates are used to check bearings against yield and fatigue.
The force law $F \propto \delta^{3/2}$ is used for collisions of elastic bodies.
