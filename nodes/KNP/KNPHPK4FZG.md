---
tag: KNPHPK4FZG
kind: definition
name: Galaxy two-point correlation function
msc: [85A35, 85A40, 60G55]
defines: QXPAG79AFV
uses: [YCZHYY8VE5, DT0QXJE705]
sources:
  - url: https://en.wikipedia.org/wiki/Correlation_function_(astronomy)
---

## Definition

Model the positions of galaxies in $\R^3$ as a random point process with mean number density $\bar n > 0$.
Assume that it is statistically homogeneous and isotropic, that is, its law is invariant under translations and rotations.
The *galaxy two-point correlation function* is the function $\xi \colon (0, \infty) \to [-1, \infty)$ defined as follows.
The probability of finding one galaxy in each of two small volume elements $dV_1$ and $dV_2$ at distance $r$ is
$$dP = \bar n^2 \, [1 + \xi(r)] \, dV_1 \, dV_2 .$$

## Remarks

Equivalently, $\xi(r) = \langle \delta(x) \, \delta(x + r) \rangle$, where $\delta = n/\bar n - 1$ is the contrast of the galaxy number density; it is the [[autocorrelation function|YCZHYY8VE5]] of a [[stationary|DT0QXJE705]] random field in space.
In a survey, $\xi$ is estimated from pair counts of the data (DD), of a random catalogue (RR) and cross pairs (DR).
The Landy–Szalay estimator is $(DD - 2DR + RR)/RR$, with normalised counts.
The projected version on the sky is the angular correlation function $w(\theta)$.

Example: for a Poisson process, the points in disjoint volumes are independent, so $dP = (\bar n \, dV_1)(\bar n \, dV_2)$ and $\xi(r) = 0$ for all $r$.

Non-example: if all galaxies lay in the half-space $x_1 > 0$, the pair probability would depend on where the volume elements are, not only on their distance.
The process is not homogeneous, so it has no correlation function $\xi(r)$ in this sense.
