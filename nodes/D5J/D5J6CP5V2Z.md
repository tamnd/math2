---
tag: D5J6CP5V2Z
kind: concept
name: Holomorphically convex domain
msc: ["32E05", 32T05]
sources:
  - url: https://en.wikipedia.org/wiki/Function_of_several_complex_variables
---

## Summary

An open set $D \subseteq \C^n$ is holomorphically convex if the [[holomorphically convex hull|CD6SMMZSW8]] of every compact subset of $D$ is again compact.
This is the holomorphic analogue of convexity, where hulls are taken with respect to holomorphic functions on $D$ instead of linear functions.
For domains in $\C^n$, holomorphic convexity is equivalent to being a domain of holomorphy.
On complex manifolds it is one of the conditions defining Stein manifolds.

## Explanations

### L1 human

Take any compact piece $K$ of the domain and form its hull: all points where holomorphic functions cannot beat their maximum over $K$.
In a holomorphically convex domain these hulls never creep out to the boundary.
Every convex open set in $\C^n$ has this property.
The punctured ball $\set{0 < \abs{z} < 1}$ in $\C^2$ does not: the hull of a small sphere around the origin contains points arbitrarily close to the missing origin.
