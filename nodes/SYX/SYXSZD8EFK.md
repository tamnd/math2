---
tag: SYXSZD8EFK
kind: statement
role: theorem
name: Kantorovich–Rubinstein duality
msc: [49Q22, 60B10, 28A33]
uses: [VEY29CS26X, 584GXXY73M, 0AW1E6YTJY, 059TJN0NZ1, DWJF7ABPR1, 0R3H5PANRQ]
about: [VEY29CS26X]
sources:
  - url: https://en.wikipedia.org/wiki/Wasserstein_metric
---

## Statement

Let $(M, d)$ be a [[Polish space|584GXXY73M]].
Let $\mu$ and $\nu$ be Borel [[probability measures|059TJN0NZ1]] on $M$ with finite first moments, that is, $\int_M d(x, x_0) \, d\mu(x) < \infty$ and $\int_M d(x, x_0) \, d\nu(x) < \infty$ for some $x_0 \in M$.
Let $W_1$ be the $1$-[[Wasserstein distance|VEY29CS26X]].
Then
$$W_1(\mu, \nu) = \sup \set{ \int_M f \, d\mu - \int_M f \, d\nu },$$
where the [[supremum|0R3H5PANRQ]] is over all functions $f \colon M \to \R$ with $\abs{f(x) - f(y)} \le d(x, y)$ for all $x, y \in M$.

## Remarks

The inequality $\ge$ is easy.
For a coupling $\gamma$ and a $1$-[[Lipschitz|0AW1E6YTJY]] $f$, one has $\int f \, d\mu - \int f \, d\nu = \int (f(x) - f(y)) \, d\gamma(x, y) \le \int d(x, y) \, d\gamma(x, y)$.
The reverse inequality is a case of Kantorovich duality in optimal transport, for the cost $c(x, y) = d(x, y)$.
For this cost the dual potentials can be taken $1$-Lipschitz, with the second potential equal to $-f$.

Example: for Dirac measures $\delta_x$ and $\delta_y$, the function $f = d(\cdot, y)$ is $1$-Lipschitz and gives $f(x) - f(y) = d(x, y)$.
This matches $W_1(\delta_x, \delta_y) = d(x, y)$.

The moment condition makes all the integrals finite, since a $1$-Lipschitz $f$ satisfies $\abs{f(x)} \le \abs{f(x_0)} + d(x, x_0)$.

## Explanations

### L1 human

The cheapest cost of moving one mass distribution onto another can be computed in a second way.
One looks for a price function that changes by at most the distance between two places.
The largest difference of average prices under the two distributions equals the transport cost.

### L2 human

The duality turns a minimum over couplings into a maximum over Lipschitz functions.
It shows that $W_1(\mu, \nu)$ depends only on the signed measure $\mu - \nu$, as a dual norm for the Lipschitz seminorm.
This is the form of $W_1$ used in Wasserstein generative adversarial networks, where the Lipschitz function is a trained critic.
It is often called the Kantorovich–Rubinstein theorem.
