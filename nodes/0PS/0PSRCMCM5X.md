---
tag: 0PSRCMCM5X
kind: definition
name: Moore-Penrose inverse
msc: [15A09]
topics: [SS4EVPKT3A]
audience: ug2
defines: 0YY8VX28JR
uses: [0EX045E2BP]
sources:
  - url: https://en.wikipedia.org/wiki/Moore–Penrose_inverse
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Moore–Penrose_inverse
    locator: Existence and uniqueness
inventory: [Z0BK2ZVY1Y]
---

## Definition

Let $A$ be an $m \times n$ complex matrix, and let $^*$ be the [[conjugate transpose|0EX045E2BP]].
An $n \times m$ complex matrix $X$ is a *Moore-Penrose inverse*, or *pseudoinverse*, of $A$ when it satisfies the four Penrose conditions:

1. $A X A = A$.
2. $X A X = X$.
3. $(A X)^* = A X$.
4. $(X A)^* = X A$.

Every matrix has exactly one such $X$, so we speak of *the* Moore-Penrose inverse and write $A^+ = X$.
For real $A$, the conditions use the transpose, and $A^+$ is real.

## Notation

- $A^+$ is the common notation. Some books write $A^\dagger$.
- A matrix that satisfies only condition 1 is a generalized inverse. A matrix that satisfies conditions 1 and 2 is a generalized reflexive inverse.

## Remarks

The existence and uniqueness are a theorem, proved from the singular value decomposition; the definition only names the matrix.
The four conditions say that $AX$ and $XA$ are orthogonal projections, and that $X$ undoes $A$ on the right subspaces.
Condition 2 is needed for uniqueness: for $A = \operatorname{diag}(1, 0)$, both $X = A$ and $X = I$ satisfy conditions 1, 3 and 4.

## Explanations

### L1 human

For an invertible matrix $A$, the inverse $X = A^{-1}$ satisfies $AX = I$ and $XA = I$.
For other matrices this is impossible.
The four conditions are weaker, and they still fix exactly one matrix $X$.

### L2 human

To test whether a given $X$ is the pseudoinverse, compute $AX$ and $XA$.
Check that both are Hermitian, then check $AXA = A$ and $XAX = X$.
If one condition fails, $X$ is not the pseudoinverse.
A trap: $AX = I$ is not one of the conditions, and for a matrix with more rows than columns it never holds.
