---
tag: XSQX8X2YQ2
kind: concept
name: Green's function of a Markov process
msc: [60J45, 60J35, 31C15]
sources:
  - url: https://en.wikipedia.org/wiki/Green%27s_function
---

## Summary

The Green's function of a Markov process is the density of its potential kernel with respect to a reference measure.
Its value $u(x, y)$ measures how much time, on average, the process started at $x$ spends near $y$.
For Brownian motion it is a constant multiple of the classical Green's function of the Laplacian.
For a Markov chain it is the expected number of visits.

## Explanations

### L1 human

Start a random particle at $x$ and count, on average, how long it stays near another point $y$, per unit of volume.
This density is the Green's function.
For a random walk on a graph, $u(x, y)$ is simply the expected number of visits to $y$ by a walk started at $x$.
For Brownian motion in three-dimensional space, it is $1/(2\pi \abs{x - y})$, which decreases with distance as one would expect.
