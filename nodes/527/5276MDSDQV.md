---
tag: 5276MDSDQV
kind: concept
name: Unisolvent point set
msc: [41A05, 41A63, 65D05]
sources:
  - url: https://en.wikipedia.org/wiki/Unisolvent_point_set
same_as:
  wikidata: Q16956925
  wikipedia: Unisolvent point set
---

## Summary

Let $V$ be a finite-dimensional space of functions.
A set of points is unisolvent for $V$ when each choice of values at the points is taken by exactly one function in $V$.
It is the condition under which an interpolation problem has a unique answer.
In one variable, any $n + 1$ distinct points are unisolvent for the polynomials of degree at most $n$, which is the basis of [[polynomial interpolation|SS1YMS2NPC]].
In several variables the position of the points matters, and choosing unisolvent sets is a central problem of [[multivariate interpolation|BM703GV34G]].

## Explanations

### L1 human

A space of functions with $N$ free parameters needs $N$ conditions to fix one function.
Values at $N$ points give $N$ conditions, but they only work when the points are in a good position.
The affine functions $a + bx + cy$ on the plane have three parameters.
Three points that form a triangle fix such a function, so they are unisolvent.
Three points on one line are not: the function $x - y$ is zero at $(0, 0)$, $(1, 1)$ and $(2, 2)$, and so it can be added to any solution.
The [[definition|681HPCS6G6]] makes this precise.
