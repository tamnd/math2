---
tag: WAWDA0XKQ6
kind: definition
name: Jeans length
msc: [85A30, "76E20"]
defines: KCDJ1QXTEQ
uses: [SN4J6KP03C]
sources:
  - url: https://en.wikipedia.org/wiki/Jeans_instability
---

## Definition

Let a uniform gas have density $\rho_0 > 0$ and [[sound speed|SN4J6KP03C]] $c_s > 0$, and let $G$ be the gravitational constant.
The *Jeans wavenumber* is $k_J = \sqrt{4\pi G \rho_0} / c_s$, and the *Jeans length* is
$$\lambda_J = \frac{2\pi}{k_J} = c_s \sqrt{\frac{\pi}{G \rho_0}}.$$
The *Jeans mass* is the mass of a ball of diameter $\lambda_J$ at density $\rho_0$, $M_J = \frac{4\pi}{3} \rho_0 \left( \frac{\lambda_J}{2} \right)^3$.

## Remarks

Example: if the density is multiplied by $4$ at fixed sound speed, then $\lambda_J$ is halved and $M_J = \frac{\pi}{6} \rho_0 \lambda_J^3$ is also halved, since $M_J \propto \rho_0 \cdot \rho_0^{-3/2} = \rho_0^{-1/2}$.
For an isothermal ideal gas $c_s^2 = k_B T / (\mu m_H)$, where $k_B$ is the Boltzmann constant, $T$ the temperature, $\mu$ the mean molecular weight and $m_H$ the hydrogen mass, so $\lambda_J \propto T^{1/2} \rho_0^{-1/2}$.
Non-example: the radius of a given cloud is not its Jeans length; the cloud is unstable to collapse when its size exceeds $\lambda_J$.
Several conventions differ by factors of order one, for example using the radius instead of the diameter in the Jeans mass.
