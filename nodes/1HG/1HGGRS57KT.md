---
tag: 1HGGRS57KT
kind: definition
name: Boundary value problem
msc: [34B05, 34B15]
defines: TM8VQJWGHZ
uses: [0NT64JV96A, 07VX34QXAV, 0FXDW992DS]
sources:
  - url: https://en.wikipedia.org/wiki/Boundary_value_problem
---

## Definition

Let $a < b$ and $n \ge 1$, and let $F \colon [a, b] \times \R^{n} \to \R$ be continuous.
Let $g \colon \R^{n} \times \R^{n} \to \R^n$ be a function.
A (two-point) *boundary value problem* on $[a, b]$ is the problem of finding a function $y \in C^n([a, b])$ such that:

1. $y$ is a [[solution|07VX34QXAV]] of the [[ordinary differential equation|0NT64JV96A]] $y^{(n)}(x) = F\left( x, y(x), \ldots, y^{(n-1)}(x) \right)$ for all $x \in [a, b]$, and
2. $y$ satisfies the boundary conditions $g\left( \mathbf{y}(a), \mathbf{y}(b) \right) = 0$, where $\mathbf{y}(x) = \left( y(x), y'(x), \ldots, y^{(n-1)}(x) \right)$.

The problem is *linear* if the equation is linear in $y, \ldots, y^{(n)}$ and $g$ is affine.
A linear problem is *homogeneous* if $y = 0$ satisfies the equation and the conditions.

## Remarks

If the conditions only prescribe $\mathbf{y}(a)$, that is, $g(u, v) = u - \mathbf{y}_0$ for a fixed $\mathbf{y}_0 \in \R^n$, the problem is an [[initial value problem|0FXDW992DS]], not a boundary value problem in the proper sense.
The same name is used for systems and for partial differential equations on a domain, with conditions on its boundary.

Example: $y'' = -y$ on $[0, \frac{\pi}{2}]$ with $y(0) = 0$ and $y(\frac{\pi}{2}) = 1$, that is, $g(u, v) = (u_1, v_1 - 1)$.
The function $y = \sin x$ solves the equation, $\sin 0 = 0$ and $\sin \frac{\pi}{2} = 1$; it is the only solution, since the general solution is $c_1 \cos x + c_2 \sin x$.

Non-example of solvability: $y'' = -y$ on $[0, \pi]$ with $y(0) = 0$ and $y(\pi) = 1$ is a boundary value problem without solution.
Every solution with $y(0) = 0$ is $c \sin x$, which vanishes at $\pi$.
