---
tag: 0ST8QF9T3T
kind: definition
name: Adjoint of a linear map
msc: [15A04, 47A05]
defines: 0R9NMSM1ZP
uses: [01EK923SKP, 0RJF668P1T]
sources:
  - url: https://en.wikipedia.org/wiki/Hermitian_adjoint
    locator: Definition for bounded operators between Hilbert spaces
---

## Definition

Let $V$ and $W$ be finite-dimensional inner product spaces over $\R$ or $\C$, and let $T \colon V \to W$ be a [[linear map|0NRYHJPQG2]].
The *adjoint* of $T$ is the unique linear map $T^* \colon W \to V$ such that
$$\langle T(v), w \rangle = \langle v, T^*(w) \rangle \qquad \text{for all } v \in V \text{ and } w \in W.$$

## Remarks

The existence and uniqueness follow from the [[Riesz representation theorem|04GYPXDXNH]].
It satisfies $(S + T)^* = S^* + T^*$, $(aT)^* = \bar a T^*$, $(ST)^* = T^* S^*$ and $T^{**} = T$.
In orthonormal bases, the matrix of $T^*$ is the [[conjugate transpose|0DXKE10PHF]] of the matrix of $T$.
It satisfies $\ker T^* = (\im T)^\perp$.

## Explanations

### L1 human

The adjoint lets us move a map from one side of an inner product to the other.
For real matrices with the dot product, the adjoint is the transpose: $(Ax) \cdot y = x \cdot (A^T y)$.
For complex matrices, it is the conjugate transpose.
