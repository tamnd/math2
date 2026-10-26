---
tag: 0DBTE6HVBD
kind: statement
role: proposition
name: Matrix of the adjoint is the conjugate transpose
msc: [15A04, 47A05]
uses: [0ST8QF9T3T, 0EX045E2BP, 0YYMY95FWS, 0FWJ0VW561]
sources:
  - url: https://en.wikipedia.org/wiki/Conjugate_transpose
    locator: Properties
---

## Statement

Let $V$ and $W$ be finite-dimensional inner product spaces over $\R$ or $\C$, with [[orthonormal bases|0S9GGTR0EX]] $B$ and $C$.
Let $T \colon V \to W$ be a linear map.
Then the matrix of the [[adjoint|0R9NMSM1ZP]] is
$$[T^*]_{B,C} = \left([T]_{C,B}\right)^*,$$
where $^*$ on the right is the [[conjugate transpose|0DXKE10PHF]]. Here $[\,\cdot\,]$ is the [[matrix of a linear map|0YQSGNYE3K]].

## Remarks

Over $\R$, the matrix of $T^*$ is the transpose of the matrix of $T$.
The statement needs orthonormal bases; in other bases, the Gram matrices of the bases appear in the formula.
The proof compares entries: both are $\langle T(b_j), c_i \rangle$, up to conjugation.

## Explanations

### L1 human

In orthonormal coordinates, taking the adjoint of a map means taking the conjugate transpose of its matrix.
This makes the abstract adjoint easy to compute.
In other bases, the rule is more complicated.
