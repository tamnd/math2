---
tag: H5H7RRQNX6
kind: concept
name: Balanced truncation
msc: [93B11, 93C05]
specializes: [D54SM8Q12V]
sources:
  - url: https://en.wikipedia.org/wiki/Model_order_reduction
---

## Summary

Balanced truncation is a method of [[model order reduction|D54SM8Q12V]] for stable linear systems.
It first changes the state coordinates so that the controllability and observability Gramians are equal and diagonal, with the [[Hankel singular values|VCPQ0B99MA]] on the diagonal.
It then keeps only the states with the largest Hankel singular values and drops the others.
The reduced model is again stable, and its error has an explicit bound in terms of the discarded Hankel singular values.

## Explanations

### L1 human

Some state directions of a system are easy to excite but hard to see in the output, others are easy to see but hard to excite.
Balancing changes coordinates so that each direction is exactly as easy to excite as to observe.
Then each direction gets a single score, its Hankel singular value, and the low scores can be cut away.
If the system has scores $1/2$ and $1/4$, cutting the second state changes the output by at most $2 \cdot 1/4 = 1/2$ in the worst-case gain.
