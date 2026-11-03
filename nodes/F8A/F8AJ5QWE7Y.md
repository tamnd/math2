---
tag: F8AJ5QWE7Y
kind: definition
name: Bondi mass
msc: ["83C40", "83C30", "83C35"]
defines: XYFKKJM9FD
uses: [D1SYF8F8RQ, 3HTF65XMF7, JSQ840425F]
sources:
  - url: https://en.wikipedia.org/wiki/Mass_in_general_relativity
---

## Definition

Let $(M, g)$ be a vacuum spacetime that is [[asymptotically flat|3HTF65XMF7]] at future null infinity.
Assume that near null infinity it has Bondi–Sachs coordinates $(u, r, x^A)$, with $x^A$ coordinates on the unit [[sphere|JSQ840425F]] $S^2$, in which
$$g = -\frac{V}{r} e^{2\beta} \, du^2 - 2 e^{2\beta} \, du \, dr + r^2 h_{AB} \bigl( dx^A - U^A du \bigr) \bigl( dx^B - U^B du \bigr).$$
Here $\det(h_{AB})$ equals the determinant of the round metric of $S^2$, and $V, \beta, U^A, h_{AB}$ are functions of all coordinates.
Assume the asymptotic expansion
$$\frac{V}{r} = 1 - \frac{2 \mathcal{M}(u, x^A)}{r} + O(r^{-2}) \quad \text{as } r \to \infty.$$
The function $\mathcal{M}$ is the *mass aspect*.
In units with $G = 1$, the *Bondi mass* at retarded time $u$ is
$$m_B(u) = \frac{1}{4\pi} \int_{S^2} \mathcal{M}(u, x^A) \, d\Omega,$$
where $d\Omega$ is the area element of the unit sphere.

## Remarks

The Einstein equations give the *Bondi mass-loss formula* $\frac{d m_B}{du} = -\frac{1}{4\pi} \int_{S^2} \abs{N}^2 \, d\Omega \le 0$.
Here $N$ is the news function, the $u$-derivative of the leading part of the shear of the outgoing light cones, with a normalisation fixed by the convention.
Example: the Schwarzschild metric in outgoing Eddington–Finkelstein coordinates, $g = -(1 - 2M/r) \, du^2 - 2 \, du \, dr + r^2 d\Omega^2$, has this form with $\beta = U^A = 0$ and $V/r = 1 - 2M/r$.
So $\mathcal{M} = M$ and $m_B(u) = M$ for all $u$; here $N = 0$, in agreement with the mass-loss formula.
Non-example: Minkowski space in coordinates $(t, r, \theta, \varphi)$ is not in Bondi–Sachs form, since the coefficient of $dr^2$ is $1$ and not $0$.
After the change $u = t - r$ it is, with $V/r = 1$, so its Bondi mass is $0$.

## Explanations

### L1 human

The Bondi mass is the mass that distant observers assign to a system at a given retarded time, after the waves emitted earlier have gone.
