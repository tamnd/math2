---
tag: NJ1FJSNK6A
kind: concept
name: Lyapunov exponent
msc: [34D08, 37D45]
sources:
  - url: https://en.wikipedia.org/wiki/Lyapunov_exponent
same_as:
  wikidata: Q1238630
  wikipedia: Lyapunov exponent
---

## Summary

A Lyapunov exponent measures the exponential rate at which a solution of a differential equation grows or decays as time goes to infinity.
For a linear system it is the upper limit of $\frac{1}{t} \ln \norm{x(t)}$ along a nonzero solution $x$.
For a nonlinear system one applies it to the linearised equation along a trajectory, and it then measures how fast nearby trajectories separate.
A negative exponent signals contraction, related to [[Lyapunov stability|0F2SYCKDT2]], and a positive one signals sensitive dependence on initial conditions, a mark of chaos.
See the [[definition|QREYWGEH41]].

## Explanations

### L1 human

Watch how the size of a solution changes over a long time and ask for the best fitting exponential rate $e^{\lambda t}$.
That rate $\lambda$ is the Lyapunov exponent.
For the scalar equation $x' = a x$, the solution $x(t) = e^{a t} x(0)$ has exponent exactly $a$.
If two nearby starting points drift apart like $e^{\lambda t}$ with $\lambda > 0$, small errors in the start blow up quickly.
This is why weather is hard to forecast far ahead.
