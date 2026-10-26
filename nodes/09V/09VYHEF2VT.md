---
tag: 09VYHEF2VT
kind: definition
name: Orthonormal family
msc: [15A63, 46C05]
defines: 0RW9TNNT87
uses: [0TS7VZJBWD]
sources:
  - url: https://en.wikipedia.org/wiki/Orthonormality
    locator: Definition
---

## Definition

Let $V$ be an inner product space over $\R$ or $\C$, and let $I$ be a set.
A family $(e_i)_{i \in I}$ of vectors of $V$ is *orthonormal* when, for all $i, j \in I$,
$$\langle e_i, e_j \rangle = \delta_{ij},$$
where $\delta_{ij} = 1$ if $i = j$ and $\delta_{ij} = 0$ if $i \ne j$.

## Remarks

So each $e_i$ has norm $1$, and $e_i$ and $e_j$ are [[orthogonal|0Y2X7P2WB7]] for $i \ne j$.
The standard basis of $\R^n$ is orthonormal for the dot product.
The functions $t \mapsto e^{2\pi i k t}$, $k \in \Z$, are orthonormal for $\langle f, g \rangle = \int_0^1 f \bar g\, dt$.

## Explanations

### L1 human

An orthonormal family is like a set of coordinate axes: unit vectors at right angles.
Computations with such vectors are simple, because all inner products are $0$ or $1$.
They are the best bases to work with in an inner product space.
