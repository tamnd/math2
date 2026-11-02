---
tag: J5YNNKSB9P
kind: concept
name: Resolvent
msc: [47A10]
sources:
  - url: https://en.wikipedia.org/wiki/Resolvent_formalism
same_as:
  wikidata: Q1426722
  wikipedia: Resolvent formalism
---

## Summary

The resolvent of an operator $T$ is the operator-valued function $\lambda \mapsto (T - \lambda I)^{-1}$, defined on the resolvent set, the complement of the spectrum.
It is an analytic function of $\lambda$, and its singularities are exactly the points of the spectrum.
Through the resolvent, complex analysis becomes a tool of operator theory: contour integrals of the resolvent give projections and functions of $T$.

## Explanations

### L1 human

For a number $t$, the function $\lambda \mapsto 1/(t - \lambda)$ blows up only at $\lambda = t$.
The resolvent does the same for an operator: it inverts $T - \lambda I$ wherever this is possible.
Where the inverse stops existing, the resolvent has a singularity, and these points form the spectrum.
For a diagonal matrix with entries $1$ and $2$, the resolvent is the diagonal matrix with entries $1/(1 - \lambda)$ and $1/(2 - \lambda)$.
