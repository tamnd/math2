---
tag: QGRBR04JJN
kind: concept
name: Leray–Schauder method
msc: [47H11, 45G10, 47H10]
sources:
  - url: https://en.wikipedia.org/wiki/Leray%E2%80%93Schauder_degree
---

## Summary

The Leray–Schauder method proves that a nonlinear equation $u = T(u)$ with a compact map $T$ has a solution.
It deforms the equation into one that is easy to solve.
One embeds the problem in a family $u = T(\lambda, u)$, $0 \le \lambda \le 1$, and proves an a priori bound: all solutions for all $\lambda$ lie in a fixed ball.
The [[Leray–Schauder degree|3VJC5Q9MYA]] is then the same for every $\lambda$, and a nonzero degree at $\lambda = 0$ forces a solution at $\lambda = 1$.
It is a main tool for nonlinear integral equations and for quasilinear elliptic boundary value problems.

## Explanations

### L1 human

Imagine slowly turning a knob that changes an easy equation into the hard one you care about.
Solutions move as the knob turns, but they cannot vanish into thin air unless they escape to infinity.
If one can show that no solution ever gets too large, then the solution of the easy equation must survive until the end.
The degree is the count of solutions, with signs, that stays fixed along the way.
