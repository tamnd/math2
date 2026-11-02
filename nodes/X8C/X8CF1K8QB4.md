---
tag: X8CF1K8QB4
kind: definition
name: Eikonal equation
msc: [35F21, 78A05, 35F30]
defines: HGMX1QGTAZ
uses: [5TRXQKP7DY, 0ABK9V9Y64]
sources:
  - url: https://en.wikipedia.org/wiki/Eikonal_equation
---

## Definition

Let $\Omega \subseteq \R^n$ be an open set and let $f \colon \Omega \to (0, \infty)$ be a continuous function.
The *eikonal equation* with speed $1/f$ is
$$\abs{\nabla u(x)} = f(x), \qquad x \in \Omega,$$
for an unknown function $u \colon \Omega \to \R$.
Here $\nabla u$ is the [[gradient|0ABK9V9Y64]] of $u$ and $\abs{\cdot}$ is the Euclidean norm.
It is usually completed by a boundary condition such as $u = 0$ on $\partial \Omega$.

## Remarks

It is the stationary [[Hamilton–Jacobi equation|5TRXQKP7DY]] with Hamiltonian $H(p, x) = \abs{p} - f(x)$.
In optics $f$ is the refractive index, $u$ is the optical path length, and the level sets of $u$ are the wave fronts.

Example: on $\Omega = \R^n \setminus \set{0}$ with $f = 1$, the function $u(x) = \abs{x}$ is a classical solution.
Check: $\nabla u(x) = x / \abs{x}$, which has length $1$.

Non-example: on the open unit disc $\Omega$ in $\R^2$ with $f = 1$ and $u = 0$ on the circle, there is no $C^1$ solution.
Indeed a function that is continuous on the closed disc, $C^1$ in the open disc and zero on the circle is identically $0$ or has an interior maximum or minimum.
In both cases $\nabla u = 0$ somewhere in $\Omega$, against $\abs{\nabla u} = 1$.
The function $u(x) = 1 - \abs{x}$ solves the equation except at $0$, where it is not differentiable.
Written as $\abs{\nabla u} - 1 = 0$, the problem has $1 - \abs{x}$, the distance to the boundary, as its unique [[viscosity solution|H1ERJ3T75T]].
