---
tag: 6GGFPT1B3T
kind: definition
name: ADM energy
msc: ["83C40", "83C30", "53C21"]
defines: XQNV97Z79Q
uses: [SB7BVCZJ3F, 5HDG31YEPW, 24CP8Q56CV]
sources:
  - url: https://en.wikipedia.org/wiki/ADM_formalism
---

## Definition

Let $(\Sigma, h, K)$ be an initial data set, as in the [[initial value formulation|SB7BVCZJ3F]], with $\Sigma$ a 3-manifold and $h$ a [[Riemannian metric|5HDG31YEPW]].
Assume it is *asymptotically flat* in the following sense.
There are a compact set $C \subseteq \Sigma$, a radius $r_0$ and a diffeomorphism $\Sigma \setminus C \to \set{x \in \R^3 : \abs{x} > r_0}$.
In these coordinates, for some $q > 1/2$,
$$h_{ij} - \delta_{ij} = O(\abs{x}^{-q}), \quad \partial_k h_{ij} = O(\abs{x}^{-q-1}), \quad K_{ij} = O(\abs{x}^{-q-1}),$$
and the energy and momentum densities defined by the constraint equations are integrable.
In units with $G = 1$, the *ADM energy* and the *ADM momentum* are
$$E = \frac{1}{16\pi} \lim_{r \to \infty} \int_{\abs{x} = r} \sum_{i,j} \bigl( \partial_j h_{ij} - \partial_i h_{jj} \bigr) \nu^i \, dA,$$
$$P_i = \frac{1}{8\pi} \lim_{r \to \infty} \int_{\abs{x} = r} \sum_{j} \bigl( K_{ij} - (\operatorname{tr}_h K) \, h_{ij} \bigr) \nu^j \, dA.$$
Here $\nu = x/r$ is the Euclidean unit normal and $dA$ the Euclidean area element of the sphere.
When $E \ge \abs{P}$, the *ADM mass* is $m = \sqrt{E^2 - \abs{P}^2}$.

## Remarks

Under these decay conditions the limits exist and do not depend on the choice of asymptotic coordinates, by results of Bartnik and of Chruściel.
Example: for the spatial Schwarzschild metric $h = u^4 \delta$ with $u = 1 + m/(2r)$, one has $\partial_j h_{ij} - \partial_i h_{jj} = -2 \partial_i (u^4) \approx 4m x_i / r^3$.
Integrating against $\nu^i = x_i / r$ over the sphere of area $4\pi r^2$ gives $16\pi m$, so $E = m$.
Non-example: for a metric that tends to the flat metric only like $\abs{x}^{-q}$ with $q \le 1/2$, the limit may fail to exist or may depend on the coordinates.
The ADM energy is the value of the Hamiltonian of general relativity on the slice, which reduces to this boundary term when the constraints hold.

## Explanations

### L1 human

The ADM energy is the total energy of an isolated gravitating system, measured by how the metric approaches the flat metric at large distance.
