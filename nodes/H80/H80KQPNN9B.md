---
tag: H80KQPNN9B
kind: concept
name: Second-order cone programming
msc: [90C25, 90C22]
specializes: [PAPN0JNEKN]
sources:
  - url: https://en.wikipedia.org/wiki/Second-order_cone_programming
same_as:
  wikidata: Q7442977
  wikipedia: Second-order cone programming
---

## Summary

Second-order cone programming minimises a linear function under constraints of one kind.
Each constraint bounds the Euclidean norm of an affine expression by an affine function.
It is the case of [[conic optimization|PAPN0JNEKN]] where the cone is a product of second-order (Lorentz) cones.
It contains [[linear programming|VNMXB0J2KA]] and convex [[quadratic programming|ERSZ4ADRCY]], and is contained in [[semidefinite programming|2RTN2X4R2N]].
Robust linear programs, facility location and many engineering design problems are second-order cone programs.

## Explanations

### L1 human

A second-order cone constraint says that the length of some vector built linearly from the unknowns is at most some linear expression in the unknowns.
The basic set is the ice-cream cone $\set{(u, t) : \norm{u} \le t}$.
For example, "find the point $x$ in the plane closest to three given points in total distance" becomes minimising $t_1 + t_2 + t_3$ subject to $\norm{x - a_i} \le t_i$ for $i = 1, 2, 3$.
