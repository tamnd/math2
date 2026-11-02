---
tag: 3WJFWAGKXR
kind: statement
role: theorem
name: Polar sets and Brownian hitting
msc: [60J45, 31B15, 60J65]
uses: [C95QJ7YH5T, 22735FGJV6]
about: [C95QJ7YH5T, 22735FGJV6]
sources:
  - url: https://en.wikipedia.org/wiki/Polar_set_(potential_theory)
---

## Statement

Let $d \ge 2$ and let $K \subset \R^d$ be a compact set.
For $x \in \R^d$, let $(B_t)$ be a [[Brownian motion|22735FGJV6]] in $\R^d$ started at $x$, with law $P^x$, and let $T_K = \inf\set{t > 0 : B_t \in K}$.
Then $K$ is a [[polar set|C95QJ7YH5T]] if and only if
$$P^x(T_K < \infty) = 0 \quad \text{for every } x \in \R^d.$$

## Remarks

Proof idea: the hitting probability $h(x) = P^x(T_K < \infty)$ is harmonic off $K$ and is the equilibrium potential of $K$, up to regularization.
For $d \ge 3$ it is the potential of the equilibrium measure of $K$.
It vanishes identically exactly when the Newtonian capacity of $K$ is $0$.
For $d = 2$ a similar argument, with logarithmic capacity and Brownian motion killed on leaving a large disc, applies.
Polar sets are exactly the sets of capacity zero, which gives the statement.
Example: a single point is polar for $d \ge 2$, so planar Brownian motion started away from $0$ never hits $0$.
A countable union of polar sets is polar, so planar Brownian motion almost surely avoids all points with rational coordinates, except possibly its starting point at time $0$.
A line segment in $\R^2$ is not polar, so Brownian motion hits it with positive probability.
In dimension $1$ the picture is different: Brownian motion hits every point almost surely, and only the empty set is polar.

## Explanations

### L1 human

Some sets are so thin that a random path will never touch them, even though the path wanders everywhere.
In the plane, a single point is such a set.
Polar sets in potential theory are exactly these sets that Brownian motion cannot see.

### L2 human

This is the probabilistic description of the exceptional sets of potential theory.
Statements that hold "except on a polar set", such as the boundary behaviour of Perron solutions, become statements that hold almost surely for Brownian paths.
It explains why polar sets are removable for bounded harmonic functions: Brownian motion never feels them.
In the language of Hunt processes, a set is polar for a process when the process almost surely never enters it, and this definition generalizes the classical one.
