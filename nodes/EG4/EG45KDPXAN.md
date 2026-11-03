---
tag: EG45KDPXAN
kind: statement
role: theorem
name: Green's reciprocity theorem
msc: [78A30, 31B10]
uses: [SAEDXNM3Y1, 6XPSV47R56]
about: [SAEDXNM3Y1]
sources:
  - url: https://en.wikipedia.org/wiki/Reciprocity_(electromagnetism)
---

## Statement

Let $\rho_1, \rho_2 \colon \R^3 \to \R$ be bounded, measurable [[charge densities|6XPSV47R56]] with compact support.
Let $\varphi_1$ and $\varphi_2$ be their [[electric potentials|SAEDXNM3Y1]].
Then
$$\int_{\R^3} \rho_1(x) \, \varphi_2(x) \, dx = \int_{\R^3} \rho_2(x) \, \varphi_1(x) \, dx.$$

## Remarks

Both sides equal the double integral
$$\frac{1}{4 \pi \varepsilon_0} \iint \frac{\rho_1(x) \, \rho_2(y)}{\abs{x - y}} \, dx \, dy,$$
since the kernel $1/\abs{x - y}$ is symmetric in $x$ and $y$.
Fubini's theorem applies because $1/\abs{x - y}$ is integrable on bounded sets of $\R^3$.
Let point charges $q_i$ at $x_i$ have potential $\varphi$, and point charges $q'_j$ at $x'_j$ have potential $\varphi'$, with all points distinct.
Then the same identity reads $\sum_i q_i \varphi'(x_i) = \sum_j q'_j \varphi(x'_j)$.
Example: for one charge $q_1$ at $x_1$ and one charge $q_2$ at $x_2$, both sides equal $q_1 q_2 / (4 \pi \varepsilon_0 \abs{x_1 - x_2})$.
A version with conductors also holds, with the other conductors uncharged.
The potential at conductor $j$ due to unit charge on conductor $i$ equals the potential at $i$ due to unit charge on $j$.

## Explanations

### L1 human

The energy of distribution 2 sitting in the potential of distribution 1 equals the energy of distribution 1 sitting in the potential of distribution 2.
The interaction between two groups of charges is symmetric.
This comes from the fact that the potential of a charge at $y$, felt at $x$, depends only on the distance between $x$ and $y$.

### L2 human

Reciprocity is the electrostatic form of the symmetry of the Green's function, $G(x, y) = G(y, x)$.
It follows also from Green's second identity applied to $\varphi_1$ and $\varphi_2$.
It shows that the matrix of coefficients of potential of a system of conductors is symmetric, and hence so is the capacitance matrix.
