---
tag: H3QX1ZFC8K
kind: concept
name: Exponential map of a Lie group
msc: ["22E60", "22E15"]
sources:
  - url: https://en.wikipedia.org/wiki/Exponential_map_(Lie_theory)
same_as:
  wikidata: Q19810382
  wikipedia: Exponential map (Lie theory)
---

## Summary

Let $G$ be a [[Lie group|7JBRGCVJRB]] with Lie algebra $\mathfrak{g} = T_eG$.
The exponential map sends $X \in \mathfrak{g}$ to the value at time $1$ of the [[one-parameter subgroup|YHA64AP1HN]] with initial velocity $X$.
For matrix groups it is the [[matrix exponential|020M04FN1H]].
It restricts to a diffeomorphism from a neighbourhood of $0$ onto a neighbourhood of the identity.
So it carries information from the Lie algebra to the group.
It is the main tool for passing between Lie groups and Lie algebras, and it differs in general from the [[exponential map|Y7Z0AGY1A7]] of Riemannian geometry.

## Explanations

### L1 human

Start at the identity of the group and move with a constant velocity $X$, in the sense that the motion is a one-parameter subgroup.
Where you are after one unit of time is $\exp(X)$.
On the circle group, with velocity $\theta$, you end at the point $e^{i\theta}$, which is the ordinary exponential function.
For a square matrix $A$, $\exp(A)$ is the series $I + A + A^2/2! + A^3/3! + \cdots$.
