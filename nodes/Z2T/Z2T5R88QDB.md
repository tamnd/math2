---
tag: Z2T5R88QDB
kind: concept
name: Trace operator
msc: ["46E35", 35J25]
sources:
  - url: https://en.wikipedia.org/wiki/Trace_operator
same_as:
  wikidata: Q13581708
  wikipedia: Trace operator
---

## Summary

The trace operator gives boundary values to functions in a [[Sobolev space|M4CEZ5K9HP]], which in general are only defined up to sets of measure zero.
Let $U$ be a bounded open set with $C^1$ boundary, and let $1 \le p < \infty$.
The trace operator extends the restriction $u \mapsto u|_{\partial U}$ to all of $W^{1,p}(U)$, as a bounded linear map into $L^p(\partial U)$.
It gives a precise meaning to boundary conditions such as $u = g$ on $\partial U$ for weak solutions of [[boundary value problems|TM8VQJWGHZ]].

## Explanations

### L1 human

The boundary of a region has volume zero, so the value of an $L^p$ function there is meaningless: one can change it freely.
A Sobolev function has a controlled slope, and this is enough to make its boundary values well defined in an averaged sense.
For a continuous function up to the boundary, the trace is just the restriction to the boundary.
The functions with zero trace are exactly the limits of smooth functions that vanish near the boundary.
