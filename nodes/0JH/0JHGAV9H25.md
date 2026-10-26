---
tag: 0JHGAV9H25
kind: statement
role: proposition
name: Eigenspaces of a self-adjoint operator are orthogonal
msc: [47B15, 15A18]
uses: [0MB8HQW495, 0AYEPBQMAW, 0TS7VZJBWD]
sources:
  - url: https://en.wikipedia.org/wiki/Self-adjoint_operator
    locator: Properties
---

## Statement

Let $V$ be a finite-dimensional inner product space over $\R$ or $\C$, and let $T \colon V \to V$ be a [[self-adjoint|0NEGN5CRSC]] linear map.
Let $v$ and $w$ be eigenvectors of $T$ for distinct eigenvalues $\lambda \ne \mu$.
Then $v$ and $w$ are [[orthogonal|0Y2X7P2WB7]].
So the [[eigenspaces|0G0RFPG8HR]] of $T$ for distinct eigenvalues are orthogonal to each other.

## Remarks

The proof: $\lambda \langle v, w \rangle = \langle T(v), w \rangle = \langle v, T(w) \rangle = \mu \langle v, w \rangle$, since $\mu$ is real.
So $(\lambda - \mu) \langle v, w \rangle = 0$, and $\langle v, w \rangle = 0$.

## Explanations

### L1 human

For a symmetric matrix, eigenvectors for different eigenvalues are perpendicular.
So the eigenspaces meet at right angles.
This is the first step towards an orthonormal basis of eigenvectors.
