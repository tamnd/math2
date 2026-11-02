---
tag: BSJ8X2XRN9
kind: concept
name: Fundamental solution of the Laplacian
msc: [35A08, 31B10, 35J05]
specializes: [K2NK9A8M5F]
sources:
  - url: https://en.wikipedia.org/wiki/Fundamental_solution
---

## Summary

The fundamental solution of the Laplacian is a radial function $\Phi$ on $\R^n \setminus \set{0}$ with $-\Delta \Phi = \delta$, the Dirac delta at the origin.
It equals $-\frac{1}{2\pi} \log \abs{x}$ in the plane and $\frac{1}{n(n-2)\omega_n} \abs{x}^{2-n}$ in dimension $n \ge 3$, where $\omega_n$ is the volume of the unit ball.
It is the [[fundamental solution|K2NK9A8M5F]] of the Laplace operator that is used throughout potential theory, up to sign.
Convolving it with a source $f$ solves Poisson's equation, and it is the building block of Green's functions and of the Newtonian and logarithmic potentials.

## Explanations

### L1 human

Think of a single unit point charge at the origin of space.
The electrostatic potential it creates is proportional to one over the distance to the origin, and this is the fundamental solution in three dimensions.
In the plane the potential of a point source grows like the logarithm of the distance instead.
Away from the origin the function is harmonic; all of its "source" sits at the origin.
For example, in $\R^3$ it is $\Phi(x) = \frac{1}{4\pi \abs{x}}$.
