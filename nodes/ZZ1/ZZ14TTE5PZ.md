---
tag: ZZ14TTE5PZ
kind: definition
name: Radial distribution function
msc: [82B21, 82D15]
defines: FME4G0R7FQ
uses: [G1P1A0N7NZ, FPYQWE8X12, 39NMDCPCCV]
sources:
  - url: https://en.wikipedia.org/wiki/Radial_distribution_function
---

## Definition

Consider a classical system of $N$ identical particles with positions $x_1, \ldots, x_N$ in a region of volume $V$ in $\R^3$.
Let $\langle \cdot \rangle$ be the average in the [[canonical ensemble|G1P1A0N7NZ]].
The *pair density* is
$$\rho^{(2)}(y_1, y_2) = \Big\langle \sum_{i \ne j} \delta(y_1 - x_i) \, \delta(y_2 - x_j) \Big\rangle,$$
so that $\rho^{(2)}(y_1, y_2) \, d^3 y_1 \, d^3 y_2$ is the expected number of ordered pairs of distinct particles in the two volume elements.
Assume that in the [[thermodynamic limit|FPYQWE8X12]], with density $\rho = N/V$ fixed, the system is homogeneous and isotropic, so the limit of $\rho^{(2)}(y_1, y_2)$ depends only on $r = \abs{y_1 - y_2}$.
The *radial distribution function* $g$ is defined by
$$\rho^{(2)}(y_1, y_2) = \rho^2 \, g(\abs{y_1 - y_2}).$$

## Remarks

Equivalently, $4\pi r^2 \rho \, g(r) \, dr$ is the expected number of particles at distance between $r$ and $r + dr$ from a given particle.

Example: for an ideal gas the positions are independent and uniform, so $\rho^{(2)} = N(N-1)/V^2$, and $g = (N-1)/N \to 1$ in the limit.
For [[hard spheres|39NMDCPCCV]] of diameter $\sigma$, $g(r) = 0$ for $r < \sigma$, since no two centres come that close.
At low density, $g(r) \approx e^{-\beta \phi(r)}$ for a pair potential $\phi$ at inverse temperature $\beta$.

Non-example: a crystal is not homogeneous, because particles sit near lattice sites.
Its pair density depends on $y_1$ and $y_2$ separately, not only on $\abs{y_1 - y_2}$, so $g$ is not defined by this formula.
For crystals one uses the orientation average of the pair density instead.

The function $h = g - 1$ is the total correlation function, and $\rho \int (g(r) - 1) \, d^3 r$ is related to the isothermal compressibility.
