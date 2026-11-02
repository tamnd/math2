---
tag: T6DDZTB360
kind: definition
name: Discrete Poisson equation
msc: [39A14, 65N06, 35J05]
defines: 6EEAEDWXZ2
uses: [ZN30Y1ZDB6, 0EPAT51DXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Discrete_Poisson_equation
---

## Definition

Let $h > 0$ and let $\Omega \subset \Z^2$ be a finite set of grid points.
Let $\partial \Omega$ be the set of points of $\Z^2 \setminus \Omega$ at distance $1$ from some point of $\Omega$.
Let $f \colon \Omega \to \R$ and $g \colon \partial \Omega \to \R$ be given [[functions|0EPAT51DXQ]].
The *discrete Poisson equation* with Dirichlet boundary values is the problem of finding $u \colon \Omega \cup \partial \Omega \to \R$ such that
$$\frac{u(i+1, j) + u(i-1, j) + u(i, j+1) + u(i, j-1) - 4u(i, j)}{h^2} = f(i, j) \quad \text{for all } (i, j) \in \Omega,$$
and $u = g$ on $\partial \Omega$.
The left side is $h^{-2}$ times the [[discrete Laplace operator|ZN30Y1ZDB6]] of $u$ at $(i, j)$.

## Remarks

Example: let $\Omega = \set{(0, 0)}$, $h = 1$, $g = 0$ on the four neighbours and $f(0, 0) = -4$.
The equation reads $0 + 0 + 0 + 0 - 4u(0, 0) = -4$, so $u(0, 0) = 1$ is the solution.

Non-example: the function with $u(0,0) = 0$ and $u = 0$ on $\partial\Omega$ satisfies the boundary condition but gives $0 \ne -4$ on the left, so it is not a solution.

For a finite $\Omega$, the problem has exactly one solution for all $f$ and $g$; this follows from the discrete maximum principle.
Ordering the unknowns gives a linear system $A \mathbf{u} = \mathbf{b}$, where $A$ is sparse, symmetric and negative definite.
On a rectangle the matrix has a block tridiagonal form with $-4$ on the diagonal, before scaling by $h^{-2}$.
The same definition works in $\Z^d$ with $2d$ neighbours and $-2d$ in place of $-4$.
