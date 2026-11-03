---
tag: CME3WQDFKN
kind: definition
name: Zel'dovich pancake
msc: [85A40]
defines: H80SG13E22
uses: [M8BWRDPA5Y, GMRYG4S3G0]
sources:
  - url: https://en.wikipedia.org/wiki/Zeldovich_pancake
---

## Definition

Consider the [[Zel'dovich approximation|M8BWRDPA5Y]] $x(q, t) = q - D(t) \nabla_q \phi(q)$, with growth factor $D(t)$ increasing in $t$.
Let $\lambda_1(q)$ be the largest eigenvalue of the deformation tensor $\partial^2 \phi / \partial q_i \partial q_j$ at $q$, and assume that its maximum over $q$ is positive, attained at $q_0$.
At the time $t_0$ with $D(t_0) \lambda_1(q_0) = 1$, the factor $1 - D \lambda_1$ of the density formula vanishes at $q_0$, and the density becomes infinite there.
The *Zel'dovich pancake* is the thin sheet of high density that forms around $x(q_0, t_0)$ at and after $t_0$.
In it, matter has been compressed along the eigendirection of $\lambda_1$.
Along the two other directions it is still expanding or slowly contracting.

## Remarks

The surface where the density is formally infinite is a [[caustic|GMRYG4S3G0]] of the map $q \mapsto x(q, t)$.
For a Gaussian random initial field, three equal eigenvalues occur with probability zero, so the first collapse is generically one-dimensional.

Example: in one dimension with $\phi(q) = -A\cos(kq)/k^2$ and $A > 0$, the deformation is $\lambda_1(q) = A \cos(kq)$, which is maximal at $q_0 = 0$.
At $D = 1/A$ the density $1/(1 - DA\cos(kq))$ is infinite at $q = 0$, and in three dimensions this is a plane sheet.

Non-example: a spherically symmetric overdensity has $\lambda_1 = \lambda_2 = \lambda_3$ at its centre.
All three factors vanish at once, so it collapses to a point and does not form a pancake.
