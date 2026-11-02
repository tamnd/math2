---
tag: MAVAK2WWXK
kind: concept
name: Lyapunov–Schmidt reduction
msc: [47J15, 34C23]
sources:
  - url: https://en.wikipedia.org/wiki/Lyapunov%E2%80%93Schmidt_reduction
same_as:
  wikidata: Q6707091
  wikipedia: Lyapunov–Schmidt reduction
---

## Summary

The Lyapunov–Schmidt reduction turns a nonlinear equation $F(x, \lambda) = 0$ between infinite-dimensional spaces into an equivalent system of finitely many equations in finitely many unknowns.
It works near a solution where the derivative of $F$ is a Fredholm operator, which is close to being invertible.
The part of the equation where the derivative is invertible is solved by the [[implicit function theorem|0BXBADR94C]].
What remains is a small bifurcation equation, which describes how solutions branch as the parameter $\lambda$ varies.
See the [[definition|CC666JT89X]].

## Explanations

### L1 human

Many problems ask for the solutions of an equation that depends on a parameter, such as the shape of a beam under a load.
Usually the solution changes smoothly with the parameter, but at special values several solutions can appear.
The Lyapunov–Schmidt method splits the unknown into a few "dangerous" directions and all the others.
The other directions can be solved for, so only the few dangerous directions are left.
The problem then becomes a question about a small number of equations, which can often be solved by hand.
