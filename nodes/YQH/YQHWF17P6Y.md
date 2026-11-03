---
tag: YQHWF17P6Y
kind: definition
name: Underactuated system
msc: [70Q05, "93C10", "70E60"]
defines: RJSM2ZNV61
uses: [ZPDTVZQN5K, BCF1EX9W2M]
sources:
  - url: https://en.wikipedia.org/wiki/Underactuation
---

## Definition

Let $n, m \ge 1$.
Let $q \in \R^n$ be [[generalized coordinates|BCF1EX9W2M]] and $u \in \R^m$ the inputs.
Consider a second-order [[control system|ZPDTVZQN5K]] of the form
$$\ddot q = f_1(q, \dot q, t) + f_2(q, \dot q, t)\, u,$$
where $f_1$ takes values in $\R^n$ and $f_2$ takes values in the $n \times m$ real matrices.
The system is *fully actuated* in the state $(q, \dot q)$ at time $t$ if $\rank f_2(q, \dot q, t) = n$.
It is *underactuated* in that state at time $t$ if $\rank f_2(q, \dot q, t) < n$.
A system is called underactuated if it is underactuated in some state at some time.

## Remarks

For a mechanical system $M(q) \ddot q + c(q, \dot q) = B(q) u$ with invertible inertia matrix $M(q)$, one has $f_2 = M(q)^{-1} B(q)$, so $\rank f_2 = \rank B(q)$.
In particular, a system with $m < n$ inputs is underactuated in every state.

Example: for the pendulum on a cart, $q = (x, \theta)$ and the only input is a force on the cart, so $B = (1, 0)^T$ and $\rank f_2 = 1 < 2$.

Non-example: a planar two-link arm with a motor at each joint has $B = I_2$, so $\rank f_2 = 2 = n$ in every state, and it is fully actuated.

A system can be fully actuated in some states and underactuated in others, for instance when $B(q)$ drops rank at some configurations.
