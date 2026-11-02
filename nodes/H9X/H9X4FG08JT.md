---
tag: H9X4FG08JT
kind: definition
name: Equilibrium measure
msc: [31A15, 31B15, 30C85]
defines: 464NN2K4FZ
uses: [0R6EWFKRCF, 059TJN0NZ1, SFSRQCM3EG, DBQXRTC0VN]
sources:
  - url: https://en.wikipedia.org/wiki/Capacity_of_a_set
---

## Definition

Let $K$ be a [[compact set|0R6EWFKRCF]] in $\C$.
For a Borel [[probability measure|059TJN0NZ1]] $\mu$ on $K$, let
$$I(\mu) = \int_K \int_K \log\frac{1}{\abs{z - w}} \, d\mu(z) \, d\mu(w)$$
be its logarithmic [[energy|SFSRQCM3EG]], with values in $(-\infty, \infty]$.
Let $V(K) = \inf_\mu I(\mu)$, the infimum over all Borel probability measures $\mu$ on $K$.
Assume that $V(K) < \infty$, that is, $K$ has positive [[logarithmic capacity|DBQXRTC0VN]].
An *equilibrium measure* of $K$ is a Borel probability measure $\nu$ on $K$ with $I(\nu) = V(K)$.

## Remarks

Such a measure exists, because the probability measures on $K$ form a weak-star compact set and $I$ is lower semicontinuous for this topology.
It is unique, because the energy is strictly convex on probability measures of finite energy.
So one speaks of *the* equilibrium measure of $K$.

Example: let $K$ be the unit circle and let $\nu$ be normalized arc length $d\theta / 2\pi$.
For $\abs{z} \le 1$ the mean value $\frac{1}{2\pi} \int_0^{2\pi} \log \abs{z - e^{i\theta}} \, d\theta$ equals $\log \max(\abs{z}, 1) = 0$.
So the potential of $\nu$ vanishes on $K$, and $I(\nu) = 0 = V(K)$, which agrees with capacity $1$.

Non-example: the unit point mass $\delta_1$ is a probability measure on the unit circle, but $I(\delta_1) = \log(1/0) = \infty \ne V(K)$.

In $\R^n$ with $n \ge 3$ the same definition is used with the Newtonian kernel $\abs{x - y}^{2-n}$ in place of $\log(1/\abs{z - w})$.
