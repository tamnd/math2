---
tag: 0TKYAEJ8N7
kind: object
name: Orthogonal group
msc: [15B10, 20G20]
instance_of: [G5S1M9]
uses: [0QRBVFJ50X]
sources:
  - url: https://en.wikipedia.org/wiki/Orthogonal_group
    locator: lead section
same_as:
  wikidata: Q1783179
  wikipedia: Orthogonal group
---

## Description

Let $n \ge 1$.
The *orthogonal group* is the set
$$O(n) = \{Q \in M_n(\R) : Q^T Q = I_n\}$$
of real $n \times n$ [[orthogonal matrices|0W02QESPJQ]], with matrix multiplication.
It is a subgroup of the general linear group $GL_n(\R)$.

## Remarks

It is the group of linear isometries of $\R^n$ with the dot product.
Each element has determinant $1$ or $-1$, and $\det \colon O(n) \to \{1, -1\}$ is a surjective homomorphism.
Its kernel is the [[special orthogonal group|0CGYNDCWRR]].
$O(n)$ is a compact Lie group of dimension $n(n-1)/2$.

## Explanations

### L1 human

The orthogonal group collects all rotations and reflections of $n$-dimensional space that fix the origin.
Composing two of them gives another one, and each one can be undone.
In the plane, it consists of the rotations about the origin and the reflections in lines through the origin.
