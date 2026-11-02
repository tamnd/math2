---
tag: X17RYQ4DS2
kind: definition
name: Dispersive partial differential equation
msc: [35Q55, 35Q53, 35B40]
defines: AYMJ2NFR4W
uses: [GC5BDZ6QBC, DPVM34ADZV, 0693Y2METT]
sources:
  - url: https://en.wikipedia.org/wiki/Dispersive_partial_differential_equation
---

## Definition

Let $n \ge 1$.
Consider a linear evolution [[partial differential equation|GC5BDZ6QBC]] with constant coefficients for $u \colon \R^n \times \R \to \C$.
Suppose that its plane-wave solutions $u(x, t) = e^{i(\xi \cdot x - \omega t)}$ are exactly those with $\omega = \omega_j(\xi)$ for finitely many functions $\omega_j \colon \R^n \to \C$.
These functions are the branches of the dispersion relation.
The equation is *dispersive* if:

1. each $\omega_j(\xi)$ is real for all real $\xi$, so plane waves neither grow nor decay;
2. for some $j$, the [[Hessian matrix|0693Y2METT]] of $\omega_j$ is not identically zero, so the group velocity $\nabla \omega_j(\xi)$ depends on $\xi$.

A nonlinear equation is called dispersive when its linear part is.

## Remarks

Example: the Schrödinger equation $i u_t + \Delta u = 0$ has $\omega(\xi) = \abs{\xi}^2$, which is real, with Hessian $2I \ne 0$, so it is dispersive.
The Airy equation $u_t + u_{xxx} = 0$, the linear part of the Korteweg–De Vries equation, has $\omega(\xi) = -\xi^3$, with $\omega''(\xi) = -6\xi$, so it is dispersive.
Non-example: the transport equation $u_t + c u_x = 0$ has $\omega(\xi) = c\xi$, whose second derivative vanishes, so clause 2 fails; solutions move without changing shape.
The heat equation $u_t = \Delta u$ has $\omega(\xi) = -i\abs{\xi}^2$, which is not real, so clause 1 fails; it is dissipative rather than dispersive.
The one-dimensional wave equation, with $\omega = \pm c\xi$, is not dispersive.
In dimension $n \ge 2$ the branches $\pm c\abs{\xi}$ have nonzero Hessian, so the wave equation meets clause 2, although it is often not called dispersive.
By the [[Fourier transform|DPVM34ADZV]], the solution is $\hat u(\xi, t) = e^{-i\omega(\xi) t}\hat u(\xi, 0)$ for a single branch, and a nondegenerate Hessian, as for the Schrödinger equation, is what yields decay estimates in $L^\infty$.
