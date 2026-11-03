---
tag: WTDGF7AZ35
kind: definition
name: Bulk modulus
msc: [74B05, 74A20]
defines: PPXM3HCN6Y
uses: [80737NDZ4V, 0V1EJCT8G6]
sources:
  - url: https://en.wikipedia.org/wiki/Bulk_modulus
---

## Definition

Consider a substance whose equilibrium pressure $p$ is a differentiable function $p(V)$ of its volume $V > 0$ along a given process, for example at constant temperature.
The *bulk modulus* of the substance at volume $V$ is
$$K = -V \frac{dp}{dV},$$
where $dp/dV$ is the [[derivative|0V1EJCT8G6]] of $p$.
For an isotropic linear elastic solid with [[Lamé parameters|80737NDZ4V]] $\lambda$ and $\mu$, a hydrostatic stress $\sigma = -p I$ produces the volume strain $\tr \varepsilon = -p / K$ with
$$K = \lambda + \tfrac23 \mu.$$

## Remarks

Example: an ideal gas at constant temperature has $p V = c$ for a constant $c > 0$, so $dp/dV = -c/V^2$ and $K = c/V = p$.

Non-example: for an incompressible material the volume does not change under any pressure.
So $p$ is not a function of $V$, and the definition does not apply; one says informally that $K = \infty$.

For the elastic solid, $\tr \sigma = (3\lambda + 2\mu) \tr \varepsilon$, and $\tr \sigma = -3p$ gives $\tr \varepsilon = -3p/(3\lambda + 2\mu) = -p/K$.
In terms of Young's modulus $E$ and Poisson's ratio $\nu$, $K = E / (3(1 - 2\nu))$, which tends to infinity as $\nu \to 1/2$.
The isothermal and adiabatic bulk moduli of a gas differ; for an ideal gas the adiabatic one is $\gamma p$, where $\gamma$ is the heat capacity ratio.
