---
tag: E1CA8QFEHB
kind: concept
name: Graded manifold
msc: [58A50, 58C50]
sources:
  - url: https://en.wikipedia.org/wiki/Graded_manifold
same_as:
  wikidata: Q5591875
  wikipedia: Graded manifold
---

## Summary

A graded manifold is a smooth manifold whose sheaf of functions is enlarged by anticommuting odd coordinates.
Locally its functions are smooth functions of $n$ ordinary variables with values in a Grassmann algebra on $m$ generators.
It is the algebraic form, due to Kostant and to Berezin and Leites, of a [[supermanifold|Z0SB9HQBAJ]].
Graded manifolds give a geometric home to fermionic fields and to the odd variables of the BRST and BV formalisms.

## Explanations

### L1 human

On an ordinary manifold a function of two variables $x, y$ is a number at each point.
On a graded manifold one adds symbols $\theta_1, \dots, \theta_m$ that anticommute, so $\theta_i \theta_j = -\theta_j \theta_i$ and $\theta_i^2 = 0$.
A function is then a finite sum such as $f(x) + g(x) \theta_1 + h(x) \theta_1 \theta_2$ with smooth coefficients.
The odd symbols carry no points of their own: setting all of them to zero gives back the ordinary manifold.
For example, the sections of the exterior algebra bundle of the cotangent bundle, that is the differential forms on a manifold, form a graded manifold.
