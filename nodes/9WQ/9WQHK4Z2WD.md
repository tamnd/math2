---
tag: 9WQHK4Z2WD
kind: proof
name: Proof that a matrix with two equal rows has determinant zero
msc: [15A15]
proves: 0K4VQB7HWR
uses: [0C3CFHDN6R]
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: As an alternating multilinear form
---

## Proof

1. Let $A$ be an $n \times n$ matrix over $K$ with rows $i \ne j$ that are equal.
2. By property 2 of the [[definition of the determinant|0C3CFHDN6R]], $\det$ vanishes on every matrix with two equal rows.
3. So $\det A = 0$.

## Idea

In this course the determinant is defined as the unique alternating multilinear function of the rows with value $1$ on the identity. Vanishing on two equal rows is the alternating property, so the claim is part of the definition.
