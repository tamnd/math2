---
tag: RYTSV821V8
kind: concept
name: Closed-loop transfer function
msc: [93C80, 93B52, 93C05]
sources:
  - url: https://en.wikipedia.org/wiki/Closed-loop_transfer_function
same_as:
  wikidata: Q1477205
  wikipedia: Closed-loop transfer function
---

## Summary

The closed-loop transfer function is the [[transfer function|86JKV3TRFD]] from the reference input to the output of a [[feedback|7NYES2D0Z4]] loop.
For a forward path with transfer function $G$ and a feedback path with transfer function $H$ in negative feedback, it is $G/(1 + GH)$.
Its poles are the roots of the characteristic equation $1 + G(s) H(s) = 0$, with denominators cleared.
So the stability of the loop is read off from this equation.
Methods such as the root locus and the Nyquist criterion study how these poles depend on $G$ and $H$.

## Explanations

### L1 human

In a feedback loop the output is measured, passed back, and subtracted from the target.
The output then depends on itself, and solving this simple equation gives the closed-loop transfer function.
For an integrator $G(s) = 1/s$ with a constant feedback gain $H = k > 0$, it is $1/(s + k)$.
So the loop behaves like a system that settles at rate $k$: the feedback turned a system that drifts into one that settles.
