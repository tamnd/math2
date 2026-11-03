---
tag: GDYDF41KM8
kind: definition
name: Quasinormal mode
msc: ["83C57", "83C35", "35P25"]
defines: 8X3E8122BJ
uses: [5EHD2XBQDG]
sources:
  - url: https://en.wikipedia.org/wiki/Quasinormal_mode
---

## Definition

Let $V \colon \R \to \R$ be a smooth potential that tends to $0$ as $x \to \pm\infty$, fast enough for the limits below to make sense.
Consider the one-dimensional [[wave equation|5EHD2XBQDG]] with potential
$$\partial_t^2 \psi - \partial_x^2 \psi + V(x)\, \psi = 0, \qquad (t, x) \in \R \times \R.$$
A *quasinormal mode* is a nonzero solution of the form $\psi(t, x) = e^{-i\omega t} u(x)$ with $\omega \in \C$, such that
$$u(x) \sim e^{i\omega x} \text{ as } x \to +\infty, \qquad u(x) \sim e^{-i\omega x} \text{ as } x \to -\infty.$$
The number $\omega$ is a *quasinormal frequency*.

## Remarks

The boundary conditions say that the wave only leaves the region: outward to $x = +\infty$ and inward to $x = -\infty$.
Then $u$ satisfies $u'' + (\omega^2 - V) u = 0$, and $\omega$ is determined by the boundary conditions as in an eigenvalue problem.
If $\operatorname{Im} \omega < 0$ the mode decays in time, but $u$ grows exponentially as $x \to \pm\infty$, so it is not square integrable and $\omega$ is not an eigenvalue of a self-adjoint operator.
For this reason quasinormal frequencies are often defined as poles of the meromorphic continuation of the resolvent, also called resonances.

Example: perturbations of the Schwarzschild black hole of mass $M$ reduce, mode by mode in spherical harmonics, to this equation.
The variable $x$ is the tortoise coordinate, with the horizon at $x = -\infty$, and $V$ is the Regge–Wheeler or Zerilli potential.
The least damped gravitational mode with angular number $\ell = 2$ has $M\omega \approx 0.3737 - 0.0890\, i$ in units $G = c = 1$.

Non-example: a string of length $\pi$ with fixed ends obeys $\partial_t^2 \psi = \partial_x^2 \psi$ with $u(0) = u(\pi) = 0$.
Its modes $\sin(nx)\, e^{-int}$ have real frequencies and do not decay; they are normal modes, because no energy leaves the string, and the outgoing conditions are not satisfied.
