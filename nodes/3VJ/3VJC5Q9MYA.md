---
tag: 3VJC5Q9MYA
kind: concept
name: Leray–Schauder degree
msc: [47H11, 47J05, 35A01]
sources:
  - url: https://en.wikipedia.org/wiki/Leray%E2%80%93Schauder_degree
same_as:
  wikidata: Q111912958
  wikipedia: Leray–Schauder degree
---

## Summary

The Leray–Schauder degree is an integer that counts, with signs, the solutions of $u - K(u) = y$ in a bounded open set of a Banach space.
Here $K$ is a compact map.
It extends the Brouwer degree of maps between finite-dimensional spaces to this infinite-dimensional class.
It does not change under compact deformations that keep solutions away from the boundary, and a nonzero degree guarantees a solution.
This makes it a main tool to prove existence for nonlinear elliptic equations by continuation from a simpler problem.

## Explanations

### L1 human

In finite dimensions, the degree of a map counts how many times it covers a point, with orientation signs.
The degree survives deformations, so one can compute it on an easy map and transfer the answer to a hard one.
In infinite dimensions this fails for general continuous maps, but it works for maps of the form identity minus a compact map.
Such maps are close to finite-dimensional ones, because a compact map can be approximated by maps with values in finite-dimensional spaces.
For example, $u \mapsto u - K(u)$ on a ball, with $K$ small and compact, has degree $1$ at $0$, so the equation $u = K(u)$ has a solution in the ball.
