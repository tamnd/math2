---
tag: RQBNA1ZRJW
kind: definition
name: Bang–bang control
msc: [49J15, 93C15]
defines: GK1Z3Q1WRZ
uses: [ZPDTVZQN5K, 02AS45T3H9, 0R6EWFKRCF]
sources:
  - url: https://en.wikipedia.org/wiki/Bang–bang_control
---

## Definition

Let $x' = f(x, u)$ be a [[control system|ZPDTVZQN5K]] whose control set $U \subseteq \R^m$ is a compact [[convex set|02AS45T3H9]], for example a box $\prod_{i=1}^m [a_i, b_i]$ with $a_i < b_i$.
An admissible control $u \colon [0, T] \to U$ is *bang–bang* if $u(t)$ is an extreme point of $U$ for almost every $t \in [0, T]$.
For a box, this means $u_i(t) \in \set{a_i, b_i}$ for each $i$ and almost every $t$.
The times at which $u$ jumps between extreme points are its switching times.

## Remarks

Example: for $U = [-1, 1]$, the control $u(t) = 1$ on $[0, 1)$ and $u(t) = -1$ on $[1, 2]$ is bang–bang, with one switching time $t = 1$.
For the double integrator $x_1' = x_2$, $x_2' = u$ starting at rest at $x_1 = -1$, it brings the state to rest at $x_1 = 0$ at time $2$, and this is the minimum time with $\abs{u} \le 1$.
Non-example: $u(t) = \sin t$ on $[0, \pi]$ with $U = [-1, 1]$ is not bang–bang, since $\abs{u(t)} < 1$ except at $t = \pi / 2$.
Consider a linear system $x' = A x + B u$ whose control set $U$ is a compact convex polytope.
The bang–bang principle says that every state reachable at time $T$ is also reachable at time $T$ by a bang–bang control.
