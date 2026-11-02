---
tag: 6TJTWQ5HCR
kind: concept
name: Newtonian kernel
msc: [31B15, 31B10]
sources:
  - url: https://en.wikipedia.org/wiki/Newtonian_potential
---

## Summary

The Newtonian kernel on $\R^n$, for $n \ge 3$, is the function $k(x, y) = \abs{x - y}^{2-n}$ of two points.
In space it is $1/\abs{x - y}$, the potential at $x$ of a unit mass at $y$ in Newton's law of gravitation.
It is a constant multiple of the [[fundamental solution of the Laplacian|BSJ8X2XRN9]] translated to the pole $y$.
Integrating it against a measure gives the Newtonian potential, the central object of classical potential theory in higher dimensions.

## Explanations

### L1 human

Put a point mass at $y$.
The Newtonian kernel tells you how strongly a point $x$ feels it.
The value is large when $x$ is close to $y$ and tends to $0$ when $x$ is far away.
In three dimensions the value is one over the distance, so doubling the distance halves the potential.
For a cloud of masses one adds up these kernels, one for each mass.
