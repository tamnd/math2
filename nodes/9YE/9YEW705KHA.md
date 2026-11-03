---
tag: 9YEW705KHA
kind: concept
name: Observability Gramian
msc: [93B07, 93C05]
sources:
  - url: https://en.wikipedia.org/wiki/Observability_Gramian
same_as:
  wikidata: Q7075420
  wikipedia: Observability Gramian
---

## Summary

The observability Gramian of a linear system $x' = Ax$, $y = Cx$ is a symmetric positive semidefinite matrix that measures how much output energy each initial state produces.
It is invertible exactly when the system is [[observable|C4HN3EAQWM]], and then the initial state can be computed from the output by a least-squares formula.
For a stable matrix $A$, the Gramian over infinite time solves a [[Lyapunov equation|92GVPZH9FT]].
It is the dual of the [[controllability Gramian|703MCKB5SZ]], and the two Gramians together are the basis of balanced model reduction.

## Explanations

### L1 human

Start the system in some state, let it run without input, and record the output.
The observability Gramian tells how loud the recording is for each starting state.
States that give a loud output are easy to tell apart; a nonzero state that gives no output at all is invisible, and then the Gramian is singular.
For $x' = 0$, $y = x$, the Gramian over time $T$ is $T$: the output is the constant $x(0)$, whose energy over $[0, T]$ is $T x(0)^2$.
