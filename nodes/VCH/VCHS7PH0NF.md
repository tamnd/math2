---
tag: VCHS7PH0NF
kind: concept
name: Dual operator
msc: [47A05, 46B99]
specializes: [0AZ5ARP287]
sources:
  - url: https://en.wikipedia.org/wiki/Transpose_of_a_linear_map
---

## Summary

The dual operator of a bounded operator $T \colon X \to Y$ between normed spaces is the operator $T' \colon Y' \to X'$ between the continuous dual spaces given by $T'(f) = f \circ T$.
It is the analytic form of the [[dual map|0AZ5ARP287]] of linear algebra, also called the transpose or Banach space adjoint.
Many properties of $T$, such as having closed or dense range, can be read off from $T'$.

## Explanations

### L1 human

A continuous linear functional measures vectors, giving one number for each vector.
Given an operator $T$ from $X$ to $Y$, any measurement $f$ on $Y$ gives a measurement on $X$: first apply $T$, then measure with $f$.
That is the dual operator, and it goes in the opposite direction.
For a matrix acting on column vectors, the dual operator is given by the transposed matrix.
