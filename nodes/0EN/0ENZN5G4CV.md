---
tag: 0ENZN5G4CV
kind: definition
name: Normal operator
msc: [47B15, 15A04]
defines: 0C8BR8XRTR
uses: [0ST8QF9T3T, 0PTF1PTJK0]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_operator
    locator: lead section
---

## Definition

Let $V$ be a finite-dimensional inner product space over $\R$ or $\C$, and let $T \colon V \to V$ be an [[endomorphism|0J7H0YBFDJ]].
The map $T$ is *normal* when
$$T T^* = T^* T,$$
where $T^*$ is the [[adjoint|0R9NMSM1ZP]] of $T$.

## Remarks

Self-adjoint maps, skew-adjoint maps and unitary maps are normal.
$T$ is normal if and only if $\norm{T(v)} = \norm{T^*(v)}$ for all $v \in V$.
Over $\C$, normal maps are exactly the maps with an orthonormal basis of eigenvectors.

## Explanations

### L1 human

A normal map commutes with its adjoint.
This condition is weaker than self-adjoint, but it still gives perpendicular eigenvectors over $\C$.
Rotations of the plane are normal, but not self-adjoint.
