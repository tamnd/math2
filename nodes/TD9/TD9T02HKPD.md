---
tag: TD9T02HKPD
kind: definition
name: Magnus expansion
msc: [34A25, 34A30]
defines: EBV9M9C435
uses: [0K665H5V1S, 0A6QZ367GX, 0MQ24RBG93]
sources:
  - url: https://en.wikipedia.org/wiki/Magnus_expansion
---

## Definition

Let $A : [0, \infty) \to \C^{n \times n}$ be continuous, and let $Y$ be the solution of the [[linear system|0A6QZ367GX]] $Y' = A(t)\, Y$ with $Y(0) = I$.
For matrices $X, Z$ write $[X, Z] = XZ - ZX$.
The *Magnus expansion* is the series $\Omega(t) = \sum_{k \ge 1} \Omega_k(t)$ with $Y(t) = e^{\Omega(t)}$, the [[matrix exponential|0K665H5V1S]].
Its first terms are
$$\Omega_1(t) = \int_0^t A(t_1)\, dt_1, \qquad \Omega_2(t) = \frac12 \int_0^t \int_0^{t_1} [A(t_1), A(t_2)]\, dt_2\, dt_1,$$
and in general $\Omega_k$ is a sum of $k$-fold iterated integrals of nested commutators of $k$ values of $A$.
The terms are determined recursively by the differential equation $\Omega' = \sum_{j \ge 0} \frac{B_j}{j!} \operatorname{ad}_\Omega^j(A)$, $\Omega(0) = 0$, where $B_j$ are the Bernoulli numbers with $B_1 = -\tfrac12$ and $\operatorname{ad}_\Omega(X) = [\Omega, X]$.

## Remarks

The series converges, and gives the solution, when $\int_0^t \norm{A(s)}_2\, ds < \pi$, where $\norm{\cdot}_2$ is the spectral norm; this is a sufficient condition.
Example: if $A(t_1)$ and $A(t_2)$ commute for all $t_1, t_2$, all terms with $k \ge 2$ vanish and $Y(t) = \exp\left(\int_0^t A\right)$; for $A(t) = a(t) N$ with a fixed matrix $N$ and scalar $a$, this gives $Y = e^{(\int_0^t a) N}$.
Without commutation, $\exp\left(\int_0^t A\right)$ is in general not the solution, and $\Omega_2$ is the first correction.
The reason is that the derivative of $\exp(\Omega_1(t))$ need not be $A(t) \exp(\Omega_1(t))$ when $A(t)$ does not commute with $\Omega_1(t)$.
Let $A(t)$ lie in a matrix Lie algebra for all $t$, such as the skew-symmetric matrices.
Then every truncation of the series also lies in it, so its exponential lies in the corresponding group.
