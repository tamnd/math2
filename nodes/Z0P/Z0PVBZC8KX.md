---
tag: Z0PVBZC8KX
kind: definition
name: Zel'dovich approximation
msc: [85A40, 85A05]
defines: M8BWRDPA5Y
uses: [43949CJRF6, 0ZCSMYHTBP]
sources:
  - url: https://en.wikipedia.org/wiki/Structure_formation
---

## Definition

Consider pressureless matter in an expanding universe, described in comoving coordinates.
Label each mass element by its initial (Lagrangian) position $q \in \R^3$.
Let $x(q, t)$ be its comoving (Eulerian) position at time $t$, as in the [[Lagrangian and Eulerian description|43949CJRF6]].
Let $D(t)$ be the growing mode of linear perturbation theory, and let $\phi(q)$ be a potential such that the linear density contrast is $\delta_L(q, t) = D(t) \nabla_q^2 \phi(q)$.
The *Zel'dovich approximation* is the trajectory
$$x(q, t) = q - D(t) \, \nabla_q \phi(q).$$
The density then follows from conservation of mass:
$$\frac{\rho(x, t)}{\bar\rho} = \frac{1}{\abs{\det(\partial x / \partial q)}} = \frac{1}{\abs{(1 - D \lambda_1)(1 - D \lambda_2)(1 - D \lambda_3)}},$$
where $\det$ is the [[Jacobian determinant|0ZCSMYHTBP]].
Here $\lambda_1 \ge \lambda_2 \ge \lambda_3$ are the eigenvalues of the deformation tensor $\partial^2 \phi / \partial q_i \partial q_j$ at $q$.

## Remarks

To first order in $D$, the density formula gives $\rho/\bar\rho - 1 \approx D(\lambda_1 + \lambda_2 + \lambda_3) = \delta_L$, so the approximation agrees with linear theory.
The formula holds while the map $q \mapsto x(q, t)$ is one to one; the first time $D(t) \lambda_1(q) = 1$ is called shell crossing.

Example: in one dimension take $\phi(q) = -A \cos(kq)/k^2$ with $A > 0$.
Then $x = q - D A \sin(kq)/k$ and $\partial x/\partial q = 1 - D A \cos(kq)$, so $\rho/\bar\rho = 1/(1 - DA\cos(kq))$.
At $q = 0$ the density becomes infinite when $DA = 1$.
For plane-parallel motion such as this one, the approximation is exact up to shell crossing.

Non-example: after shell crossing the map $q \mapsto x$ folds over and several streams overlap at one point.
The formula then makes particles pass freely through each other, while real gravity binds them into a structure, so it no longer describes the dynamics.
