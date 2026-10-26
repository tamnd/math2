---
tag: ~3ea98fed
kind: statement
role: theorem
name: Polar decomposition
msc: [15A23]
uses: [~df815872, ~6fa2a174]
sources:
  - url: https://en.wikipedia.org/wiki/Polar_decomposition
    locator: lead section
same_as:
  wikidata: Q2101158
  wikipedia: Polar decomposition
---

## Statement

Let $A$ be an $n \times n$ complex matrix.
Then there are a [[unitary matrix|~efbaff1b]] $U$ and a positive semidefinite Hermitian matrix $P$ with
$$A = UP.$$
The factor $P$ is unique: $P = (A^* A)^{1/2}$, the [[square root|~010c56e0]] of $A^* A$.
If $A$ is invertible, then $U$ is also unique.

## Remarks

It follows from the singular value decomposition $A = W \Sigma V^*$: take $U = W V^*$ and $P = V \Sigma V^*$.
For $n = 1$, it is the polar form $z = e^{i\theta} r$ of a complex number.
There is also a left polar decomposition $A = P' U$ with $P' = (A A^*)^{1/2}$.

## Explanations

### L1 human

Every square matrix is a stretch along perpendicular axes, followed by a rotation, possibly with a reflection.
This generalises writing a complex number as a positive length times a unit complex number.
The stretch part is always unique.
