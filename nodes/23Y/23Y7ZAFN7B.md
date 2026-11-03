---
tag: 23Y7ZAFN7B
kind: statement
role: theorem
name: Raychaudhuri equation
msc: ["83C05", "53C50"]
uses: [CWHM6AV4G3, 4GTNM0WHDH, ENWD1YR20P, 3MCZ97SW6V, WP4YAHJ6V4]
about: [CWHM6AV4G3]
sources:
  - url: https://en.wikipedia.org/wiki/Raychaudhuri_equation
same_as:
  wikidata: Q2134013
  wikipedia: Raychaudhuri equation
---

## Statement

Let $(M, g)$ be a four-dimensional Lorentzian manifold.
Let $u$ be a smooth vector field whose integral curves form a [[congruence of timelike geodesics|CWHM6AV4G3]], so $g(u, u) = -1$ and $\nabla_u u = 0$.
Let $\theta$, $\sigma_{ab}$ and $\omega_{ab}$ be the expansion, shear and rotation of the congruence.
Let $\tau$ be proper time along the curves, and let $R_{ab}$ be the [[Ricci tensor|4GTNM0WHDH]] of $g$.
Then along each curve
$$\frac{d\theta}{d\tau} = -\frac13 \theta^2 - \sigma_{ab} \sigma^{ab} + \omega_{ab} \omega^{ab} - R_{ab} u^a u^b.$$

## Remarks

The proof differentiates $B_{ab} = \nabla_b u_a$ along $u$: using the geodesic equation and the definition of the Riemann tensor, $u^c \nabla_c B_{ab} = -B_{ac} B^c{}_b + R_{cba}{}^d u^c u_d$ in a standard convention.
Taking the trace and inserting the decomposition $B_{ab} = \frac13 \theta h_{ab} + \sigma_{ab} + \omega_{ab}$ gives the equation.

The most important consequence is focusing.
Assume $\omega_{ab} = 0$, for example for a congruence orthogonal to a spacelike hypersurface, and $R_{ab} u^a u^b \ge 0$.
By the [[Einstein field equations|3MCZ97SW6V]], the latter holds when matter satisfies the strong [[energy condition|ENWD1YR20P]].
Since $\sigma_{ab}\sigma^{ab} \ge 0$, one gets $d\theta/d\tau \le -\theta^2/3$, hence $\theta^{-1} \ge \theta_0^{-1} + \tau/3$.
So if $\theta_0 = \theta(0) < 0$, then $\theta \to -\infty$ within proper time $\tau \le 3/\abs{\theta_0}$: nearby geodesics cross.
Without the sign condition on $R_{ab} u^a u^b$, focusing need not happen, and the rotation term $+\omega_{ab}\omega^{ab}$ also works against focusing.

Example: for the radially expanding congruence $u^\mu = x^\mu / \tau$ in Minkowski space, $\theta = 3/\tau$, $\sigma = 0$, $\omega = 0$ and $R_{ab} = 0$; indeed $d\theta/d\tau = -3/\tau^2 = -\theta^2/3$.

## Explanations

### L1 human

Think of a cloud of particles falling freely.
The Raychaudhuri equation says how the volume of the cloud changes in time.
Ordinary matter makes gravity attractive, and the equation shows that it always tends to squeeze such a cloud; shear squeezes it too, and only rotation can resist.
Once a cloud starts to contract, it must collapse to zero volume in a finite time unless something else intervenes.

### L2 human

The equation is the engine of the [[Penrose–Hawking singularity theorems|WP4YAHJ6V4]]: focusing of geodesics plus a global causality argument forces some geodesic to be incomplete.
For null geodesic congruences there is an analogous equation, with $\frac12 \theta^2$ in place of $\frac13 \theta^2$.
Together with the null energy condition, it is used in the area theorem for black holes and in the theory of trapped surfaces.
In cosmology, applied to the matter flow of a homogeneous universe, it reduces to the acceleration equation of Friedmann.
