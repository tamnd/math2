---
tag: YTR959CYMX
kind: problem
name: Time-optimal control
msc: [49J15, 49K15, 49N05]
uses: [T3V6ZNAMDN, ZPDTVZQN5K, 8M31QKB0GW, GK1Z3Q1WRZ, 7RPV2T29CF, 9NSCZ2KBEB]
about: [T3V6ZNAMDN]
sources:
  - url: https://en.wikipedia.org/wiki/Bang–bang_control
history:
  posed_by: "Donald W. Bushaw"
  first_stated: "1952"
  notes: "Bushaw studied time-optimal control of second-order systems in his 1952 thesis. Bellman, Glicksberg and Gross (1956) and Pontryagin and his school treated the general case."
---

## Problem

Let $U \subseteq \R^m$ be a nonempty compact set, and let $f \colon \R^n \times U \to \R^n$ be continuous.
Let $x_0, x_1 \in \R^n$.
For a measurable control $u \colon [0, T] \to U$, let $x$ be the trajectory of the [[control system|ZPDTVZQN5K]] $x' = f(x, u)$ with $x(0) = x_0$.
The *time-optimal control problem* is to find a final time $T^* \ge 0$ and an [[admissible control|8M31QKB0GW]] $u^*$ on $[0, T^*]$ whose trajectory satisfies $x(T^*) = x_1$.
It is required that no admissible control reaches $x_1$ at any time $T < T^*$.

## Remarks

For linear systems $x' = A x + B u$ with $U = [-1, 1]^m$ the theory is complete.
If $x_1$ can be reached from $x_0$ at some time, then a time-optimal control exists, because the reachable sets are compact and convex and depend continuously on time.
By [[Pontryagin's maximum principle|7RPV2T29CF]] a time-optimal control satisfies $u_j(t) = \sgn\big(b_j^{T} p(t)\big)$ wherever $b_j^{T} p(t) \neq 0$, where $b_j$ is the $j$-th column of $B$ and $p' = -A^{T} p$.
If each pair $(A, b_j)$ satisfies the [[Kalman rank condition|9NSCZ2KBEB]], then the time-optimal control is unique and [[bang–bang|GK1Z3Q1WRZ]] with finitely many switches.
If moreover all eigenvalues of $A$ are real, each component $u_j$ switches at most $n - 1$ times.
Example: for the double integrator $x_1' = x_2$, $x_2' = u$, $\abs{u} \le 1$, steered to the origin, the optimal control is $u = -1$ above the switching curve $x_1 = -\frac12 x_2 \abs{x_2}$ and $u = 1$ below it.
On the curve itself it is the constant that drives the state along the curve into the origin, and every optimal control switches at most once.

## Explanations

### L1 human

A time-optimal control problem asks how to bring a system from one state to another as fast as possible with limited control power.
A car that must stop at a wall in least time is an example.
For linear systems the answer is to use full power all the time, switching direction at well-chosen moments.
For the car, one accelerates fully and then brakes fully, with exactly one switch.
