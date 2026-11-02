---
tag: E7TY2TPXX7
kind: statement
role: theorem
name: Faber–Krahn inequality
msc: [35P15, 49R05, 35J05]
uses: [4VD8XXQ4P3, 2Z2QVWZ262, 2GRPCP5XK9]
about: [4VD8XXQ4P3]
sources:
  - url: https://en.wikipedia.org/wiki/Rayleigh%E2%80%93Faber%E2%80%93Krahn_inequality
same_as:
  wikidata: Q7298491
  wikipedia: Rayleigh–Faber–Krahn inequality
---

## Statement

Let $n \ge 1$ and let $\Omega \subseteq \R^n$ be a nonempty bounded open set.
Let $\Omega^*$ be the open ball in $\R^n$ with the same [[Lebesgue measure|2Z2QVWZ262]] as $\Omega$.
Let $\lambda_1(\Omega)$ be the first [[Dirichlet eigenvalue|4VD8XXQ4P3]] of $\Omega$.
Then
$$\lambda_1(\Omega) \ge \lambda_1(\Omega^*).$$
Equality holds if and only if $\Omega$ is a ball up to a set of zero capacity.

## Remarks

Proof idea: let $u \ge 0$ be a first eigenfunction of $\Omega$ and let $u^*$ be its [[symmetric decreasing rearrangement|2GRPCP5XK9]], which lies in $H^1_0(\Omega^*)$.
Rearrangement keeps $\int u^2$ and does not increase $\int \abs{\nabla u}^2$, by the Pólya–Szegő inequality.
So the Rayleigh quotient of $u^*$ on $\Omega^*$ is at most $\lambda_1(\Omega)$, which bounds $\lambda_1(\Omega^*)$.

Example: in the plane, a square of side $\sqrt{\pi}$ has area $\pi$, the same as the unit disc.
Its first eigenvalue is $2\pi^2 / \pi = 2\pi \approx 6.28$.
The unit disc has $\lambda_1 = j_{0,1}^2 \approx 5.78$, where $j_{0,1}$ is the first zero of the Bessel function $J_0$.

The volume constraint is needed: dilating a ball by a factor $s$ divides $\lambda_1$ by $s^2$, so without fixing the volume there is no lower bound.

## Explanations

### L1 human

Among all drums of the same area, the round drum has the lowest fundamental tone.
This was conjectured by Lord Rayleigh and proved by Faber and Krahn.
It is a spectral analogue of the [[isoperimetric inequality|KBX8RBZ626]], which says the disc has the shortest boundary for a given area.

### L2 human

The inequality is the prototype of shape optimisation for eigenvalues.
Its proof combines the variational characterisation of $\lambda_1$ with symmetrisation, and the same method gives the Pólya–Szegő and Saint-Venant inequalities.
Related results include the Szegő–Weinberger inequality, where the ball maximises the first nonzero Neumann eigenvalue, and the Hong–Krahn–Szegő inequality for $\lambda_2$, where two equal disjoint balls are optimal.
