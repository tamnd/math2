---
tag: NCTEA5RXMP
kind: definition
name: Kelvin–Helmholtz instability
msc: ["76E17", "76E05"]
defines: 7PJ97MHYTP
uses: [84K7TEWZ2Z, H028A17Z55]
sources:
  - url: https://en.wikipedia.org/wiki/Kelvin–Helmholtz_instability
---

## Definition

Consider two inviscid incompressible fluids.
The lower one fills $z < 0$ with density $\rho_1$ and uniform velocity $(U_1, 0, 0)$.
The upper one fills $z > 0$ with density $\rho_2$ and uniform velocity $(U_2, 0, 0)$, where $U_2 \neq U_1$.
Gravity $g \ge 0$ acts in the direction $-z$, and the interface has surface tension $\sigma \ge 0$.
Perturb the interface to $z = \eta(x, t)$ and linearise the Euler equations, with [[potential flow|84K7TEWZ2Z]] in each layer.
At the interface, impose continuity of normal velocity and the pressure jump given by surface tension.
The *Kelvin–Helmholtz instability* is the exponential growth in time of a normal mode $\eta = \hat\eta \, e^{i(kx - \omega t)}$, $k > 0$, of this linear problem.
That is, the problem has a solution with $\operatorname{Im} \omega > 0$.

## Remarks

The normal modes satisfy the dispersion relation
$$\frac{\omega}{k} = \frac{\rho_1 U_1 + \rho_2 U_2}{\rho_1 + \rho_2} \pm \left( \frac{g}{k} \frac{\rho_1 - \rho_2}{\rho_1 + \rho_2} + \frac{\sigma k}{\rho_1 + \rho_2} - \frac{\rho_1 \rho_2 (U_1 - U_2)^2}{(\rho_1 + \rho_2)^2} \right)^{1/2}.$$
So the wavenumber $k$ is unstable exactly when
$$\rho_1 \rho_2 (U_1 - U_2)^2 > (\rho_1 + \rho_2) \left( \frac{g (\rho_1 - \rho_2)}{k} + \sigma k \right).$$

Example: with $g = 0$ and $\sigma = 0$ the condition holds for every $k > 0$, and the growth rate $\operatorname{Im} \omega = k \sqrt{\rho_1 \rho_2} \abs{U_1 - U_2} / (\rho_1 + \rho_2)$ is unbounded as $k \to \infty$.
Non-example: with $\rho_1 > \rho_2$, $\sigma > 0$, $g > 0$ and $(U_1 - U_2)^2 \le 2 (\rho_1 + \rho_2) \sqrt{g \sigma (\rho_1 - \rho_2)} / (\rho_1 \rho_2)$, no wavenumber is unstable, since the right side of the condition has minimum $2 (\rho_1 + \rho_2) \sqrt{g \sigma (\rho_1 - \rho_2)}$ over $k > 0$.

The name is also used for the instability of continuous shear layers, such as $U(z) = \tanh z$, which roll up into vortices in the same way.
