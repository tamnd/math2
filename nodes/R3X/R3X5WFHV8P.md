---
tag: R3X5WFHV8P
kind: definition
name: Transport equation
msc: [35F05, 35F10, 35L02]
defines: PVD7VZJZ9B
uses: [GC5BDZ6QBC, 0ABK9V9Y64]
sources:
  - url: https://en.wikipedia.org/wiki/Advection
---

## Definition

Let $n \ge 1$ and let $b \in \R^n$ be a fixed vector.
The *transport equation* with velocity $b$ is the [[partial differential equation|GC5BDZ6QBC]]
$$\partial_t u + b \cdot \nabla u = 0$$
for $u \colon \R^n \times (0, \infty) \to \R$.
Here $\nabla u$ is the [[gradient|0ABK9V9Y64]] of $u$ in the space variable $x$.
The *initial value problem* adds the condition $u(x, 0) = g(x)$ for a given function $g \colon \R^n \to \R$.

## Remarks

For $g \in C^1(\R^n)$ the initial value problem has the unique $C^1$ solution $u(x, t) = g(x - tb)$.
The reason is that $u$ is constant along each line $s \mapsto (x + sb, t + s)$, since the derivative of $u$ along it is $\partial_t u + b \cdot \nabla u = 0$.
The inhomogeneous equation $\partial_t u + b \cdot \nabla u = f$ has the solution $u(x, t) = g(x - tb) + \int_0^t f(x + (s - t) b, s)\, ds$.
With a variable velocity field $b(x, t)$ one also calls $\partial_t u + b \cdot \nabla u = 0$ a transport equation, and $\partial_t u + \nabla \cdot (u\, b) = 0$ the continuity equation; the two agree when $\nabla \cdot b = 0$.

Example: $n = 1$, $b = 2$, $g(x) = e^{-x^2}$, and $u(x, t) = e^{-(x - 2t)^2}$.
Check: $\partial_t u = 4(x - 2t) u$ and $\partial_x u = -2(x - 2t) u$, so $\partial_t u + 2 \partial_x u = 0$, and $u(x, 0) = g(x)$.

Non-example: $u(x, t) = e^{-t} \sin x$ with $n = 1$ is not a solution for any $b$.
Indeed $\partial_t u + b\, \partial_x u = e^{-t}(-\sin x + b \cos x)$, which is not identically zero.
