---
tag: DD66THZBDX
kind: statement
role: theorem
name: Finite speed of propagation
msc: [35L05, 35L15]
uses: [5EHD2XBQDG, G8J0YQRPA3, VP2HN86VAG, 92C3S03AQZ]
about: [5EHD2XBQDG]
sources:
  - url: https://en.wikipedia.org/wiki/Wave_equation
---

## Statement

Let $n \ge 1$ and let $u \in C^2(\R^n \times [0, \infty))$ solve the [[wave equation|5EHD2XBQDG]] $u_{tt} = \Delta u$ on $\R^n \times (0, \infty)$.
Let $x_0 \in \R^n$ and $t_0 > 0$.
Suppose that $u(x, 0) = u_t(x, 0) = 0$ for all $x$ with $\abs{x - x_0} \le t_0$.
Then $u(x, t) = 0$ for all $(x, t)$ in the cone $\set{(x, t) : 0 \le t \le t_0, \ \abs{x - x_0} \le t_0 - t}$.

## Remarks

The proof uses the [[energy method|G8J0YQRPA3]] on shrinking balls.
Let $e(t) = \frac{1}{2}\int_{B(x_0, t_0 - t)} \big(u_t^2 + \abs{\nabla u}^2\big)\, dx$ for $0 \le t \le t_0$.
Differentiating, integrating by parts and using $\abs{u_t\, \partial_\nu u} \le \frac{1}{2}(u_t^2 + \abs{\nabla u}^2)$ on the boundary sphere gives $e'(t) \le 0$.
Since $e(0) = 0$, it follows that $e \equiv 0$, so $u_t$ and $\nabla u$ vanish in the cone and $u$ equals its initial value $0$ there.
For the equation $u_{tt} = c^2 \Delta u$, the same holds with the cone $\abs{x - x_0} \le c(t_0 - t)$.
Example: in one dimension, d'Alembert's formula shows directly that $u(x, t)$ depends only on the data on $[x - t, x + t]$.
By linearity, two solutions whose data agree on $B(x_0, t_0)$ agree in the cone, so a change of the data travels with speed at most $1$.
The [[heat equation|VP2HN86VAG]] has no such property: a nonnegative nonzero initial temperature with compact support gives a positive temperature everywhere at every positive time.

## Explanations

### L1 human

Waves need time to travel.
If nothing is happening in a ball of radius $t_0$ at the start, then the centre stays undisturbed until time $t_0$, because no disturbance from outside can arrive sooner.
The undisturbed region is a cone in space-time that shrinks at the wave speed.
This is the mathematical form of the fact that sound or light has a finite speed.

### L2 human

Finite speed of propagation is the characteristic feature of [[hyperbolic equations|92C3S03AQZ]], in contrast with parabolic and elliptic ones.
It gives the domain of dependence of a point, the backward cone, and the domain of influence of a region of data, the forward cone.
The energy proof works for general second-order hyperbolic equations with variable coefficients, with the cone replaced by a region bounded by characteristic surfaces.
It also proves uniqueness for the Cauchy problem and allows one to solve the problem locally and patch the local solutions together.
