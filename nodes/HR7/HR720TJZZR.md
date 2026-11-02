---
tag: HR720TJZZR
kind: problem
name: Linear-quadratic regulator
msc: [49N10, 93C05, 49N35]
uses: [T3V6ZNAMDN, Y4V154JWR7, 01MMVW8CKC, 0KX66CZMBB, GGZV75ZZMV]
about: [T3V6ZNAMDN]
sources:
  - url: https://en.wikipedia.org/wiki/Linear–quadratic_regulator
same_as:
  wikidata: Q2520550
  wikipedia: Linear–quadratic regulator
history:
  posed_by: "Rudolf E. Kálmán"
  first_stated: "1960"
---

## Problem

Let $A$ be a real $n \times n$ matrix and $B$ a real $n \times m$ matrix.
Let $Q$ and $F$ be symmetric [[positive semidefinite|01MMVW8CKC]] $n \times n$ matrices, and let $R$ be a symmetric [[positive definite|0KX66CZMBB]] $m \times m$ matrix.
Let $T > 0$ and $x_0 \in \R^n$.
The *finite-horizon linear-quadratic regulator problem* is to minimize
$$J(u) = \int_0^T \big( x(t)^{T} Q x(t) + u(t)^{T} R u(t) \big) \, dt + x(T)^{T} F x(T)$$
over all controls $u \in L^2([0, T]; \R^m)$, where $x$ solves $x' = A x + B u$, $x(0) = x_0$.

## Remarks

The problem is solved.
Let $P$ be the solution of the [[Riccati differential equation|Y4V154JWR7]] $-P' = A^{T} P + P A - P B R^{-1} B^{T} P + Q$ with $P(T) = F$.
Then the unique optimal control is given by the linear feedback $u^*(t) = -R^{-1} B^{T} P(t) x^*(t)$, and the optimal cost is $x_0^{T} P(0) x_0$.
The proof completes the square: along any trajectory, $\frac{d}{dt} (x^{T} P x) = -x^{T} Q x - u^{T} R u + (u + R^{-1} B^{T} P x)^{T} R (u + R^{-1} B^{T} P x)$.
Integrating from $0$ to $T$ gives $J(u) = x_0^{T} P(0) x_0 + \int_0^T \abs{R^{1/2}(u + R^{-1} B^{T} P x)}^2 \, dt$, which is smallest exactly for the feedback above.
For the infinite horizon $T = \infty$ and $F = 0$, assume $(A, B)$ stabilizable and $(C, A)$ detectable, where $Q = C^{T} C$.
Then the [[algebraic Riccati equation|GGZV75ZZMV]] $A^{T} P + P A - P B R^{-1} B^{T} P + Q = 0$ has a unique symmetric positive semidefinite solution $P$.
The feedback $u = -R^{-1} B^{T} P x$ is optimal and makes the closed loop asymptotically stable.

## Explanations

### L1 human

The linear-quadratic regulator steers a linear system toward zero while keeping both the deviation and the control effort small.
The cost charges squares of both, weighted by the matrices $Q$ and $R$.
The answer is remarkably simple: the best control is a fixed matrix times the current state, computed once from a Riccati equation.
It is one of the most used results of control theory, from aircraft autopilots to robots.
