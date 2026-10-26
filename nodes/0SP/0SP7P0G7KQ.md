---
tag: 0SP7P0G7KQ
kind: statement
role: theorem
name: A space is the direct sum of a subspace and its orthogonal complement
msc: [46C05]
uses: [079D68S3AW, 041JTZCK9Q]
sources:
  - url: https://en.wikipedia.org/wiki/Orthogonal_complement
    locator: Properties
---

## Statement

Let $V$ be an inner product space over $\R$ or $\C$, and let $W$ be a finite-dimensional subspace of $V$.
Then
$$V = W \oplus W^\perp,$$
where $W^\perp$ is the [[orthogonal complement|0XJXTBCB2T]] of $W$ and $\oplus$ is the [[direct sum|0XYYT5KNTX]].

## Remarks

For an orthonormal basis $e_1, \dots, e_k$ of $W$, each $v \in V$ is $w + (v - w)$ with $w = \sum_i \langle v, e_i \rangle e_i \in W$ and $v - w \in W^\perp$.
The statement holds for each closed subspace of a Hilbert space.
It can fail for a subspace that is not closed in an infinite-dimensional space.

## Explanations

### L1 human

Each vector splits in exactly one way into a part in $W$ and a part perpendicular to $W$.
The part in $W$ is the shadow of the vector on $W$.
The part perpendicular to $W$ is what remains.
