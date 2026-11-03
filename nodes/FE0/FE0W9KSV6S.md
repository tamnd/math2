---
tag: FE0W9KSV6S
kind: statement
role: proposition
name: Non-uniqueness of potential field inversion
msc: [86A22, 31B20, 35R30]
uses: [DCMFQ01QGS, 0E0B6RA8K0, PCMW7KN5P4]
about: [DCMFQ01QGS, PCMW7KN5P4]
sources:
  - url: https://en.wikipedia.org/wiki/Inverse_problem
---

## Statement

Let $\Omega \subset \R^3$ be a nonempty bounded open set and let $G > 0$.
For a bounded measurable density $\rho$ supported in $\overline{\Omega}$, let
$$V_\rho(x) = G \int_\Omega \frac{\rho(y)}{\norm{x - y}}\, dy$$
be its [[Newtonian potential|DCMFQ01QGS]].
Then the map $\rho \mapsto V_\rho|_{\R^3 \setminus \overline{\Omega}}$ is not injective.
More precisely, let $\varphi \ne 0$ be a smooth function with compact support in $\Omega$, and let $\Delta$ be the [[Laplacian|0E0B6RA8K0]].
Then the density $\rho = \Delta\varphi$ is nonzero and $V_\rho = 0$ on $\R^3 \setminus \overline{\Omega}$.

## Remarks

Since $\Delta_y (1/\norm{x - y}) = -4\pi\,\delta_x$, two integrations by parts give $V_{\Delta\varphi} = -4\pi G\varphi$ on all of $\R^3$, and $\varphi$ vanishes outside its support.
If $\rho = \Delta\varphi$ were $0$, then $\varphi$ would be harmonic with compact support, hence $0$.
So adding $\Delta\varphi$ to any density changes the body but not its exterior gravity field: gravity data alone cannot determine the density.
Example: by the [[shell theorem|20SAJR6J3Y]], a homogeneous ball of mass $M$ has the same field outside it as a thin homogeneous spherical shell of mass $M$ with the same centre.
Uniqueness returns under extra hypotheses.
For instance, P. S. Novikov proved a uniqueness theorem for bodies of the same known constant density.
If two such bodies are star-shaped with respect to a common point and have the same exterior potential, they coincide.
The same non-uniqueness holds for magnetic fields, since they are also governed by the Laplace equation outside the sources.

## Explanations

### L1 human

Gravity measured outside a body does not tell you exactly what is inside.
Many different arrangements of mass, such as a solid ball and a hollow shell of the same mass, pull on the outside world in exactly the same way.
This is why geophysicists who interpret gravity maps must add extra information, such as rock densities or the shape of a layer, before they can say what lies underground.

### L2 human

This is the basic obstruction in the [[inverse problem|PCMW7KN5P4]] of potential theory.
The kernel of the forward map contains all Laplacians of compactly supported test functions, an infinite-dimensional space.
For square-integrable densities on a regular domain, the exterior field determines only the orthogonal projection of $\rho$ onto the harmonic functions in $L^2(\Omega)$.
Inversions usually choose one solution by regularisation, for example the one of minimal norm.
Related results are the uniqueness theorems for the exterior Dirichlet problem and the [[geodetic boundary value problem|1F4S3G1R6J]].
They recover the field from boundary data but say nothing about the sources inside.
