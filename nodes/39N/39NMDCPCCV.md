---
tag: 39NMDCPCCV
kind: example
name: Hard spheres
msc: [82B21, 82D15, 52C17]
illustrates: [T4FZCAQC0D]
uses: [T4FZCAQC0D, G1P1A0N7NZ]
sources:
  - url: https://en.wikipedia.org/wiki/Hard_spheres
same_as:
  wikidata: Q2435125
  wikipedia: Hard spheres
---

## Example

The *hard-sphere* fluid is a classical system of $N$ identical balls of diameter $\sigma > 0$ in a region of volume $V$ in $\R^3$.
The balls interact through the pair potential
$$\phi(r) = \begin{cases} +\infty & \text{if } r < \sigma, \\ 0 & \text{if } r \ge \sigma, \end{cases}$$
where $r$ is the distance between two centres.
In the [[canonical ensemble|G1P1A0N7NZ]] the Boltzmann factor $e^{-\beta \sum_{i<j} \phi(\abs{x_i - x_j})}$ is $1$ if no two balls overlap and $0$ otherwise.
So the configurational distribution is uniform on the set of non-overlapping configurations, for every temperature.

Check with the second virial coefficient: the [[Mayer f-function|T4FZCAQC0D]] is $f(r) = e^{-\beta\phi(r)} - 1$, equal to $-1$ for $r < \sigma$ and $0$ for $r \ge \sigma$.
Hence
$$B_2 = -\frac12 \int_{\R^3} f(\abs{x}) \, d^3 x = \frac12 \cdot \frac{4\pi}{3} \sigma^3 = \frac{2\pi \sigma^3}{3},$$
which does not depend on the temperature, and the low-density pressure is $P \approx n k_B T (1 + B_2 n)$ with $n = N/V$.

## Remarks

Because temperature only scales the momenta, the ratio $P/(n k_B T)$ is a function of the packing fraction $\eta = \pi n \sigma^3 / 6$ alone.
The packing fraction cannot exceed $\pi / (3\sqrt 2) \approx 0.7405$, the density of the densest sphere packing, by the Kepler conjecture proved by Thomas Hales.
In one dimension, hard rods of length $\sigma$ (the Tonks gas) are exactly solvable, with $P = n k_B T / (1 - n \sigma)$.
In three dimensions, computer simulations show a transition from a fluid to a crystal as the density grows, driven by entropy alone.

## Explanations

### L1 human

Think of a box of billiard balls that never attract each other and simply cannot overlap.
Every allowed arrangement is equally likely, so the physics is all about how much room the balls have.
Squeezing them leaves fewer arrangements, so they push back on the walls.
At high density the balls gain more room to jiggle by lining up in a crystal, so order can arise from crowding alone.
