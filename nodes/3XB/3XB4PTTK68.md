---
tag: 3XB4PTTK68
kind: definition
name: Minimal surface equation
msc: [35J93, 53A10]
defines: 3GV2E2YTZX
uses: [7X9N9H3RK6, 0ABK9V9Y64, 0MWV6ZTK6S, 41X0YW2R9N]
sources:
  - url: https://en.wikipedia.org/wiki/Minimal_surface
---

## Definition

Let $n \ge 1$ and let $\Omega \subseteq \R^n$ be an open set.
Consider a twice continuously differentiable function $u \colon \Omega \to \R$.
The *minimal surface equation* on $\Omega$ is the [[quasilinear|7X9N9H3RK6]] equation
$$\operatorname{div} \left( \frac{\nabla u}{\sqrt{1 + \abs{\nabla u}^2}} \right) = 0.$$
Here $\nabla u$ is the [[gradient|0ABK9V9Y64]] and $\operatorname{div}$ is the [[divergence|0MWV6ZTK6S]].

## Remarks

Expanding the divergence gives the equivalent form
$$(1 + \abs{\nabla u}^2) \Delta u - \sum_{i,j=1}^n \partial_i u \, \partial_j u \, \partial_i \partial_j u = 0.$$
For $n = 2$ this is $(1 + u_y^2) u_{xx} - 2 u_x u_y u_{xy} + (1 + u_x^2) u_{yy} = 0$.
A function solves it exactly when the mean curvature of its graph in $\R^{n+1}$ is zero, that is, when the graph is a [[minimal surface|41X0YW2R9N]].
Example: Scherk's function $u(x, y) = \log(\cos y) - \log(\cos x)$ on the square $\abs{x}, \abs{y} < \pi/2$ is a solution.
Here $u_x = \tan x$, $u_y = -\tan y$, $u_{xx} = \sec^2 x$, $u_{yy} = -\sec^2 y$ and $u_{xy} = 0$, so the left side is $\sec^2 y \sec^2 x - \sec^2 x \sec^2 y = 0$.
Non-example: $u(x, y) = x^2 + y^2$ is not a solution, since at the origin $\nabla u = 0$ and the left side equals $\Delta u = 4$.
