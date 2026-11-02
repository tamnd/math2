---
tag: NM1KPS6E7Y
kind: concept
name: Givens rotation
msc: [65F25, 15A23]
specializes: [0HFREYRSZP]
sources:
  - url: https://en.wikipedia.org/wiki/Givens_rotation
same_as:
  wikidata: Q1367799
  wikipedia: Givens rotation
---

## Summary

A Givens rotation is an $n \times n$ [[orthogonal matrix|0W02QESPJQ]] that [[rotates|0HFREYRSZP]] the plane of two coordinate axes and leaves all other coordinates fixed.
With the angle chosen well, it turns one chosen entry of a vector or matrix into zero.
Because it touches only two rows, it is the tool of choice for zeroing single entries.
This is used in the [[QR decomposition|0ERWG4NXQ9]] of sparse or structured matrices and in the QR algorithm for eigenvalues.

## Explanations

### L1 human

Pick two coordinates, say the first and the third, and turn the vector inside the plane they span, keeping every other coordinate as it is.
Turning by a suitable angle makes one of the two coordinates zero, and moves all the length into the other one.
For example, rotating $(3, 4)$ clockwise by the angle whose cosine is $3/5$ gives $(5, 0)$.
Doing this entry by entry clears a matrix below its diagonal.
