---
tag: BP3WR8NG1W
kind: concept
name: Frame operator
msc: [42C15, 47B02]
sources:
  - url: https://en.wikipedia.org/wiki/Frame_(linear_algebra)
---

## Summary

The frame operator of a frame $(f_i)$ in a [[Hilbert space|HM2HHE3J51]] sends a vector $f$ to $\sum_i \ip{f}{f_i} f_i$.
It is bounded, [[self-adjoint|0NEGN5CRSC]], [[positive|77020CY5ZW]] and [[invertible|CPAD5W1CGW]], and its spectrum lies between the frame bounds.
Its inverse gives the canonical dual frame, and so a formula that rebuilds every vector from its frame coefficients.

## Explanations

### L1 human

A frame lets one measure a vector by taking inner products with many fixed vectors.
The frame operator first measures, then adds up the fixed vectors weighted by the measurements.
For an orthonormal basis this gives back the vector itself.
For a general frame the result is distorted, but in a way that can be undone, because the operator is invertible.
For example, the three Mercedes-Benz star vectors in the plane give the frame operator $\tfrac32 I$.
