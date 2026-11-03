---
tag: T7E2V0WWZV
kind: definition
name: Upper critical dimension
msc: [82B27, 82B28]
defines: BRYCFH5RB2
uses: [SQ41AZGZ2P, 1DGJYHG10E, R0KGM32QN6]
sources:
  - url: https://en.wikipedia.org/wiki/Critical_dimension
---

## Definition

Consider a family of models indexed by the dimension $d \ge 1$ of space, such as the nearest-neighbour [[Ising model|R0KGM32QN6]] on $\Z^d$, each with a critical point.
The *upper critical dimension* $d_u$ of the family is the smallest number with the following property.
For every $d > d_u$, the [[critical exponents|SQ41AZGZ2P]] of the model in dimension $d$ equal the values given by [[mean-field theory|1DGJYHG10E]].

## Remarks

Example: for the Ising model, mean-field theory gives $\beta = 1/2$, $\gamma = 1$, $\delta = 3$, $\nu = 1/2$ and $\eta = 0$, and $d_u = 4$.
A heuristic check is the hyperscaling relation $d\nu = 2 - \alpha$: with $\nu = 1/2$ and $\alpha = 0$ it holds exactly at $d = 4$.

Non-example: $d_u = 3$ fails for the Ising family, since the three-dimensional Ising model has $\beta \approx 0.326 \ne 1/2$.

The *lower critical dimension* $d_l$ is the largest $d$ at which there is no ordered phase at any positive temperature.
It is $1$ for the Ising model and $2$ for models with a continuous symmetry, by the [[Mermin–Wagner theorem|5C0QQFXSD7]].
Percolation has $d_u = 6$.
