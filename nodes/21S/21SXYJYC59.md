---
tag: 21SXYJYC59
kind: concept
name: Convex combination
msc: [52A05, 52A20]
specializes: [0KJH6SRFZK]
sources:
  - url: https://en.wikipedia.org/wiki/Convex_combination
same_as:
  wikidata: Q2627315
  wikipedia: Convex combination
---

## Summary

A convex combination of finitely many points is a weighted sum of the points whose weights are nonnegative and add up to $1$.
It is the special kind of [[affine combination|0KJH6SRFZK]] in which no weight is negative.
The [[convex hull|0FQSDC2EQ2]] of a set is exactly the set of all convex combinations of its points.
A [[convex set|02AS45T3H9]] is a set closed under convex combinations.
So convex combinations are the basic operation of convex geometry.

## Explanations

### L1 human

Think of the weights as masses placed at the points, with total mass $1$.
The convex combination is the centre of mass of this system.
Because all masses are nonnegative, the centre of mass always lies inside the shape spanned by the points.
For example, with the points $0$ and $10$ on the real line and weights $0.3$ and $0.7$, the convex combination is $0.3 \cdot 0 + 0.7 \cdot 10 = 7$, which lies between $0$ and $10$.
