---
tag: ~d13ac5fd
kind: statement
role: corollary
name: Dimension of the orthogonal complement
msc: [15A03, 46C05]
uses: [~d832fdcd, ~a94fe0ae]
sources:
  - url: https://en.wikipedia.org/wiki/Orthogonal_complement
    locator: Finite dimensions
---

## Statement

Let $V$ be a finite-dimensional inner product space over $\R$ or $\C$, and let $W$ be a subspace of $V$.
Then
$$\dim W + \dim W^\perp = \dim V,$$
where $W^\perp$ is the [[orthogonal complement|~dc8d80e7]] of $W$.

## Remarks

It follows from $V = W \oplus W^\perp$.
For example, in $\R^3$, a line has a plane as orthogonal complement: $1 + 2 = 3$.
For a real matrix, it gives $\rank A + \dim \ker A = n$ once more, because $\ker A$ is the orthogonal complement of the row space.

## Explanations

### L1 human

A subspace and its orthogonal complement share the dimensions of the space.
If $W$ uses $k$ directions, then $W^\perp$ uses the remaining $n - k$ directions.
