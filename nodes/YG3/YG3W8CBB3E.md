---
tag: YG3W8CBB3E
kind: concept
name: Dirichlet energy
msc: [31B05, 35A15, 49J10]
sources:
  - url: https://en.wikipedia.org/wiki/Dirichlet_energy
same_as:
  wikidata: Q5280760
  wikipedia: Dirichlet energy
---

## Summary

The Dirichlet energy of a function $u$ on a domain is $\frac12 \int \abs{\nabla u}^2 \, dx$, half the integral of the squared length of its gradient.
It measures how much the function varies.
Its critical points with fixed boundary values are the [[harmonic functions|0DEB0JMN0W]], which is the content of Dirichlet's principle.
The energy is the quadratic form behind the [[Laplacian|0E0B6RA8K0]], the Sobolev space $H^1$ and the theory of Dirichlet forms.

## Explanations

### L1 human

Think of a rubber membrane whose height over the point $x$ is $u(x)$.
For small slopes, the stretching energy of the membrane is roughly proportional to the Dirichlet energy.
A flat membrane has energy $0$, and a wrinkled one has large energy.
For example, $u(x, y) = x$ on the unit disc has gradient of length $1$ everywhere, so its energy is $\frac12$ times the area $\pi$, that is, $\pi/2$.
