---
tag: DR7Z989QPH
kind: definition
name: Polarization density
msc: [78A30, 78A25]
defines: ASQAH710WN
uses: [BANHMXD2TD, 0299VCW1TH, 0MWV6ZTK6S, SAEDXNM3Y1]
sources:
  - url: https://en.wikipedia.org/wiki/Polarization_density
---

## Definition

Let $\Omega \subseteq \R^3$ be the region filled by a dielectric material.
The *polarization density* of the material is a [[vector field|0299VCW1TH]] $P \colon \Omega \to \R^3$ with the following property.
For every small region $B \subseteq \Omega$, the [[electric dipole moment|BANHMXD2TD]] of the charges in $B$ is approximately $\int_B P(y) \, dy$.
Equivalently, $P(x)$ is the dipole moment per unit volume in small regions around $x$.
These regions are small, but still large compared with the atoms.

## Remarks

The *bound charge densities* of the material are $\rho_b = -\nabla \cdot P$ in the interior, where $\nabla \cdot$ is the [[divergence|0MWV6ZTK6S]], and $\sigma_b = P \cdot n$ on the boundary with outward unit normal $n$.
Let $\Omega$ be bounded with smooth boundary, and let $P$ be continuously differentiable up to the boundary.
Then the [[electric potential|SAEDXNM3Y1]] of the polarized body is
$$\varphi(x) = \frac{1}{4 \pi \varepsilon_0} \int_\Omega P(y) \cdot \frac{x - y}{\abs{x - y}^3} \, dy,$$
and it equals the potential of the bound charges $\rho_b$ and $\sigma_b$.
Example: a slab with constant $P = (0, 0, P_0)$ has $\rho_b = 0$ inside and surface charges $\pm P_0$ on its top and bottom faces.
Non-example: a single fixed point charge in a vacuum is not described by a polarization density, since its total charge is nonzero, while a polarization only displaces charge.
In a linear isotropic dielectric, $P = \varepsilon_0 \chi_e E$, with electric susceptibility $\chi_e$.
The unit of $P$ is the coulomb per square metre.
