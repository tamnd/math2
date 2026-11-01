---
tag: XT4SWG6J7N
kind: concept
name: Dirichlet process
msc: [60G57, 62G05, 62F15]
sources:
  - url: https://en.wikipedia.org/wiki/Dirichlet_process
same_as:
  wikidata: Q5280766
  wikipedia: Dirichlet process
---

## Summary

A Dirichlet process is a random [[probability measure|059TJN0NZ1]] whose values on every finite partition of the space follow a [[Dirichlet distribution|RX4CVSSRRJ]].
It depends on a concentration parameter $\alpha > 0$ and a base probability measure $H$.
It is the basic prior distribution on probability measures in nonparametric [[Bayesian inference|0JWRJX2RMP]].
Its samples are discrete measures almost surely, and the posterior after observing data is again a Dirichlet process.

## Explanations

### L1 human

A Dirichlet process draws a whole probability distribution at random.
On average the drawn distribution equals the base measure $H$, and a large $\alpha$ keeps it close to $H$.
The drawn distribution puts all its mass on countably many points, like a random histogram with infinitely many thin bars.
For example, with $H$ uniform on $[0, 1]$, the mass that a draw gives to $[0, 1/2]$ is a random number with mean $1/2$.
Drawing values from such a random distribution again and again produces ties, and the pattern of ties is the [[Chinese restaurant process|2SEF8QTYQF]].
