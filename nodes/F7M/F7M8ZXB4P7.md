---
about:
- 0W02QESPJQ
kind: statement
msc:
- 15B10
name: An orthogonal matrix is invertible with inverse its transpose
role: proposition
sources:
- url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section6-3.xml#L1851
  locator: src/section6-3.xml:1851
tag: F7M8ZXB4P7
uses:
- 0W02QESPJQ
- 0EB9N0S33C
---

## Statement

Let $Q$ be an [[orthogonal matrix|0W02QESPJQ]]. Then $Q$ is an [[invertible matrix|0EB9N0S33C]], and its inverse is the transpose of $Q$, that is, $Q^{-1} = Q^T$.

## Remarks

Here an orthogonal matrix is a square matrix whose columns are orthonormal. The entries of $Q^T Q$ are the dot products of the columns of $Q$. These are $1$ on the diagonal and $0$ off it. So $Q^T Q = I$, and for a square matrix this means $Q^T$ is the inverse of $Q$.
