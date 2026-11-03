---
tag: 2Q4KHDTNSX
kind: definition
name: Isostasy
msc: [86A60, 86A30]
defines: 7CJTGB6M0V
uses: []
sources:
  - url: https://en.wikipedia.org/wiki/Isostasy
---

## Definition

Describe the outer Earth by a density $\rho(x, z) \ge 0$, where $x$ is a horizontal position in a region $A$.
Here $z$ is depth below sea level, with $z$ negative above sea level.
Let $t(x) \le 0$ be the depth of the top of the column at $x$, so that $-t(x)$ is the surface height.
Let $g$ be the constant acceleration of gravity.
The region is in *isostatic equilibrium* with depth of compensation $D > \sup_x t(x)$ if the lithostatic pressure
$$p(x) = \int_{t(x)}^{D} \rho(x, z)\, g\, dz$$
does not depend on $x \in A$.
Equivalently, every vertical column of unit cross-section above depth $D$ has the same mass.

## Remarks

Example: take $D = 50$ km and two columns.
The first has crust of density $2.8$ g/cm$^3$ from sea level to $40$ km, over mantle of $3.3$ g/cm$^3$.
The second has $1$ km of topography and crust reaching $45.6$ km below sea level.
The masses per unit area are $2.8 \cdot 40 + 3.3 \cdot 10 = 145$ and $2.8 \cdot 46.6 + 3.3 \cdot 4.4 = 145$ (in units of $10^6\ \mathrm{kg/m^2}$), so the columns are in equilibrium.
Non-example: a load of $1$ km of rock placed on the first column without a root adds mass to it and breaks the equilibrium.
The two classical ways to achieve compensation are the [[Airy and Pratt models|9W8W6DVCPX]].
The definition is a hydrostatic idealisation; in flexural isostasy the lithosphere is an elastic plate and the load is supported over a wide region.
