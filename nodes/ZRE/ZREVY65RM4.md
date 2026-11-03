---
tag: ZREVY65RM4
kind: concept
name: Mirror descent
msc: [90C25, 65K05]
sources:
  - url: https://en.wikipedia.org/wiki/Mirror_descent
same_as:
  wikidata: Q111939494
  wikipedia: Mirror descent
---

## Summary

Mirror descent is a first-order method for convex optimization.
It replaces the Euclidean distance of [[gradient descent|12317R8RTJ]] by a Bregman divergence adapted to the feasible set.
It was introduced by Nemirovski and Yudin.
With the negative entropy on the probability [[simplex|YX1DJK2QAG]] it gives multiplicative updates.
For subgradients bounded entrywise, its error bounds on the simplex grow like $\sqrt{\ln n}$ in the dimension $n$, not like $\sqrt{n}$.
It is a basic tool of online learning and large-scale optimization.

## Explanations

### L1 human

Gradient descent measures distances with the usual ruler, as if all directions were alike.
On some sets, such as the set of probability vectors, a different notion of distance fits better.
Mirror descent maps the point to a "mirror" space, takes the gradient step there, and maps back.
On probability vectors this turns subtracting the gradient into multiplying each weight by $e^{-\eta g_i}$ and renormalising, so weights stay positive and sum to $1$.
