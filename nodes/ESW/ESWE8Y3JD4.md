---
tag: ESWE8Y3JD4
kind: statement
role: proposition
name: Verlet integration
msc: [65L06, 65P10, 70-08]
uses: [0FXDW992DS, 3HGJCQBWVY]
about: [3HGJCQBWVY]
sources:
  - url: https://en.wikipedia.org/wiki/Verlet_integration
---

## Statement

Let $a \colon \R^d \to \R^d$ be twice continuously differentiable, and consider the equation $x'' = a(x)$ with $x(0) = x_0$ and $x'(0) = v_0$.
Fix a step size $h > 0$.
The Störmer–Verlet method sets $x_1 = x_0 + h v_0 + \frac{h^2}{2} a(x_0)$ and
$$x_{n+1} = 2 x_n - x_{n-1} + h^2 a(x_n), \qquad n \ge 1.$$

1. The positions $x_n$ are the same as the positions computed by the [[leapfrog method|3HGJCQBWVY]] (velocity Verlet) from $(x_0, v_0)$ with step size $h$.
2. On a bounded interval $[0, T]$, the error $\max_{nh \le T} \abs{x_n - x(nh)}$ is $O(h^2)$ as $h \to 0$.

## Remarks

The two-step formula comes from adding the Taylor expansions of $x(t + h)$ and $x(t - h)$: the odd powers cancel, and $x(t+h) - 2x(t) + x(t-h) = h^2 x''(t) + O(h^4)$.
So the local error is $O(h^4)$.
In a two-step recurrence of this kind, a local error made at one step is carried forward with a factor of size at most $O(n)$.
Summing over $n \le T/h$ steps gives a global error $O(h^2)$.
For clause 1, the leapfrog positions satisfy $x_{n+1} - x_n = h v_{n+1/2}$ and $v_{n+1/2} = v_{n-1/2} + h a(x_n)$, so $x_{n+1} - x_n = x_n - x_{n-1} + h^2 a(x_n)$, and both start from the same $x_1$.
Velocities do not appear in the two-step form; they can be recovered by $v_n \approx (x_{n+1} - x_{n-1}) / (2h)$, with error $O(h^2)$.
Example: for $x'' = 0$ the recurrence gives $x_n = x_0 + n h v_0$, the exact solution.

## Explanations

### L1 human

Verlet integration moves a particle using its last two positions and the current force.
The new position is the current one, plus the last displacement, plus a correction from the acceleration.
It is cheap, accurate to second order, and does not let energy drift away over long runs.
This is why it is the workhorse of molecular dynamics.

### L2 human

The two-step form needs only positions, which halves the storage.
Its drawbacks are that velocities are only implicit and that round-off is larger, because a small term $h^2 a$ is added to large positions.
The velocity Verlet form fixes both points and is the same method.
Its good long-time behaviour comes from it being symmetric and symplectic.
