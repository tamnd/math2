---
tag: YG05CHY6Z3
kind: definition
name: Gradient wind
msc: [86A10, 76U60]
defines: C0HR875S0K
uses: [CZ1S1P465Y, 6HZRX3WSQD]
sources:
  - url: https://en.wikipedia.org/wiki/Balanced_flow
---

## Definition

Consider steady, frictionless, horizontal flow of a fluid of density $\rho > 0$ in a frame rotating with Coriolis parameter $f$.
Use natural coordinates along a streamline: the speed is $V \ge 0$ and the unit normal $\mathbf{n}$ points to the left of the flow.
Let $R$ be the signed radius of curvature of the streamline, with $R > 0$ when the centre of curvature lies to the left.
Assume that the streamlines are parallel to the isobars.
The speed $V$ is a *gradient wind* if
$$\frac{V^2}{R} + f V = -\frac{1}{\rho} \frac{\partial p}{\partial n},$$
where $\partial p / \partial n$ is the derivative of the pressure $p$ in the direction $\mathbf{n}$.

## Remarks

The three terms are the centripetal acceleration, the [[Coriolis|6HZRX3WSQD]] acceleration and the pressure gradient force per unit mass.
With the geostrophic speed $V_g = -(\rho f)^{-1} \partial p / \partial n$ of [[geostrophic balance|CZ1S1P465Y]], the balance reads $V_g / V = 1 + V / (f R)$.
Solving the quadratic gives
$$V = -\frac{f R}{2} \pm \sqrt{\frac{f^2 R^2}{4} - \frac{R}{\rho} \frac{\partial p}{\partial n}},$$
and the physical root is the one that is non-negative and tends to $V_g$ as $\abs{R} \to \infty$.

Example: in the northern hemisphere ($f > 0$), around a low the flow is anticlockwise, $R > 0$, and $V < V_g$: the wind is subgeostrophic.
With $f = 10^{-4}$ s$^{-1}$, $R = 500$ km and $V_g = 20$ m/s, the balance $V^2 + 50 V - 1000 = 0$ gives $V \approx 15.3$ m/s.

Non-example: around a high in the northern hemisphere $R < 0$, and a real solution needs $f^2 R^2 / 4 \ge (R / \rho) \, \partial p / \partial n$.
If the pressure gradient of a high is steeper than this bound, no gradient wind exists; this is why the pressure gradient near the centre of a high is weak.

When the Rossby number $V / (\abs{f} \abs{R})$ is small, the centripetal term is negligible and the gradient wind reduces to the geostrophic wind.
