---
tag: 7WPVZZ4YFC
kind: concept
name: Tame Fréchet space
msc: [46A61, 58C15]
specializes: [3GAA614673]
sources:
  - url: https://en.wikipedia.org/wiki/Nash%E2%80%93Moser_theorem
---

## Summary

A tame Fréchet space is a graded [[Fréchet space|3GAA614673]] of a special kind.
Up to tame linear isomorphism, it is a direct summand of a space of exponentially decreasing sequences in a Banach space.

The notion is due to Richard Hamilton.
Tame spaces carry smoothing operators, and this is what the [[Nash–Moser theorem|9ZCCXT3KKP]] needs to run Newton's method with loss of derivatives.
The basic example is the space of smooth functions on a compact manifold, graded by the $C^n$ norms.

## Explanations

### L1 human

A space of smooth functions is measured by a whole ladder of norms: the size of the function, of its first derivatives, of its second derivatives, and so on.
Many natural operators, such as differential operators, cost a fixed number of rungs of this ladder.
A tame Fréchet space is one in which the ladder behaves like the ladder of weights $e^{nk}$ on a sequence $(f_k)$.
Then one can smooth an element, trading rungs in a controlled way, and this makes hard implicit function theorems possible.
