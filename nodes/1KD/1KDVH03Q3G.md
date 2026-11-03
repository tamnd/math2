---
tag: 1KDVH03Q3G
kind: definition
name: Jeans escape
msc: [85A20, 82C40]
defines: V9DTKCD34M
uses: [3QSVWQJX11, DJGG5SN382]
sources:
  - url: https://en.wikipedia.org/wiki/Atmospheric_escape
---

## Definition

Consider a planet of mass $M$ with an atmosphere whose exobase, the level above which the gas is collisionless, lies at radius $r_c$.
Let the gas there consist of molecules of mass $m$ with number density $n_c$ and a [[Maxwell–Boltzmann distribution|3QSVWQJX11]] of velocities at temperature $T$.
Let $G$ be the gravitational constant and $k_B$ the Boltzmann constant.
*Jeans escape* is the loss of the molecules at the exobase that move upward faster than the [[escape velocity|DJGG5SN382]] $v_{\text{esc}} = \sqrt{2GM/r_c}$.
Let $v_0 = \sqrt{2 k_B T / m}$ be the most probable speed and $\lambda = v_{\text{esc}}^2 / v_0^2 = G M m / (k_B T r_c)$ the escape parameter.
The rate of escape per unit area is the *Jeans flux*
$$\Phi_J = n_c \, \frac{v_0}{2\sqrt{\pi}} \, (1 + \lambda) \, e^{-\lambda}.$$

## Remarks

Check: let $f$ be the Maxwell–Boltzmann density of velocities $v$ with total $n_c$.
Then $\Phi_J$ is the integral of $v_z f(v)$ over all velocities with $v_z > 0$ and $\abs{v} > v_{\text{esc}}$.
In spherical velocity coordinates this integral evaluates to the formula above.
Example: $\lambda$ is proportional to $m$, so a molecule four times heavier has four times the escape parameter.
For $\lambda$ of order $10$ to $20$, the factor $e^{-\lambda}$ then makes its flux many orders of magnitude smaller.
Non-example: in the hydrodynamic outflow of a heated atmosphere, $\lambda$ is small and the gas streams out as a fluid; this is not Jeans escape.
Neither are escape processes driven by ions or by photochemistry.
