---
tag: RC22S41ZDB
kind: definition
name: Wasserstein metric
msc: [49Q22, 60B10, 28A33]
defines: VEY29CS26X
uses: [0VKD1TP7F3, 584GXXY73M, 059TJN0NZ1, 0MXT6PRZZ6, DWJF7ABPR1, 0QF1MZ9FRG, 0ACRGYNHSR]
sources:
  - url: https://en.wikipedia.org/wiki/Wasserstein_metric
---

## Definition

Let $(M, d)$ be a separable complete metric space, that is, a [[Polish space|584GXXY73M]], and let $p \in [1, \infty)$.
Let $\mathcal{P}_p(M)$ be the set of Borel [[probability measures|059TJN0NZ1]] $\mu$ on $M$ with $\int_M d(x, x_0)^p \, d\mu(x) < \infty$ for some point $x_0 \in M$.
For $\mu, \nu \in \mathcal{P}_p(M)$, a *coupling* of $\mu$ and $\nu$ is a Borel probability measure $\gamma$ on $M \times M$ whose [[marginals|0MXT6PRZZ6]] are $\mu$ and $\nu$.
That is, $\gamma(A \times M) = \mu(A)$ and $\gamma(M \times A) = \nu(A)$ for every Borel set $A \subseteq M$.
Let $\Gamma(\mu, \nu)$ be the set of couplings.
The *$p$-Wasserstein distance* is
$$W_p(\mu, \nu) = \left( \inf_{\gamma \in \Gamma(\mu, \nu)} \int_{M \times M} d(x, y)^p \, d\gamma(x, y) \right)^{1/p}.$$

## Remarks

The condition on $\mu$ does not depend on the choice of $x_0$, by the triangle inequality.
The product measure $\mu \otimes \nu$ is always a coupling, so $\Gamma(\mu, \nu)$ is not empty and $W_p(\mu, \nu) < \infty$.
The function $W_p$ is a metric on $\mathcal{P}_p(M)$, and the infimum is attained.

Example: let $\delta_x$ be the [[Dirac measure|0ACRGYNHSR]] at $x$.
The only coupling of $\delta_x$ and $\delta_y$ is $\delta_{(x, y)}$, so $W_p(\delta_x, \delta_y) = d(x, y)$.

Non-example: on $M = \R$, the standard Cauchy distribution has $\int \abs{x} \, d\mu = \infty$.
So it does not lie in $\mathcal{P}_1(\R)$, and $W_1$ is not defined for it.

On $\R$, with distribution functions $F_\mu$ and $F_\nu$, one has $W_1(\mu, \nu) = \int_{-\infty}^{\infty} \abs{F_\mu(t) - F_\nu(t)} \, dt$.
In $\mathcal{P}_p(M)$, $W_p(\mu_n, \mu) \to 0$ if and only if $\mu_n \to \mu$ weakly and the $p$-th moments converge.

## Explanations

### L1 human

A coupling is a plan for moving the mass of $\mu$ to the mass of $\nu$.
The distance is the cost of the cheapest plan, where moving mass by $r$ costs $r^p$ per unit.
