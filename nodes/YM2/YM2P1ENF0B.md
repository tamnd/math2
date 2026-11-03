---
tag: YM2P1ENF0B
kind: concept
name: Hamilton's principal function
msc: [70H20, 49L12]
sources:
  - url: https://en.wikipedia.org/wiki/Hamilton%E2%80%93Jacobi_equation
---

## Summary

Fix a starting point and a starting time.
Hamilton's principal function $S(q, t)$ is the [[action|T0WAGV4KP4]] of the true motion from there to the position $q$ at the time $t$.
As a function of the endpoint, it solves the [[Hamilton–Jacobi equation|5TRXQKP7DY]] $\partial_t S + H(q, \nabla_q S, t) = 0$.
Its gradient in $q$ is the final momentum, so the single function $S$ encodes a whole family of motions.
In many texts, the name also covers a complete solution of the Hamilton–Jacobi equation used as a [[generating function|NXK6HD49NZ]].
See the [[definition|JAZWC031S4]].

## Explanations

### L1 human

Fix a starting place and a starting time.
For each place $q$ and later time $t$, let the system move along its true path from the start to $q$, arriving at time $t$.
Add up the action along the way.
The result is a number $S(q, t)$ for each endpoint.
For a free particle of mass $m$ starting at $q_0$ at time $0$, the path is a straight line at constant speed, and $S = m (q - q_0)^2 / (2t)$.
The slope of $S$ in $q$ is the momentum $m (q - q_0)/t$ with which the particle arrives.
