---
tag: 0Y85GYEGSF
kind: statement
role: theorem
name: Existence of an orthonormal basis
msc: [15A63, 46C05]
uses: [0FWJ0VW561, 0VT6P0GNQR]
sources:
  - url: https://en.wikipedia.org/wiki/Orthonormal_basis
    locator: Existence
---

## Statement

Let $V$ be a finite-dimensional inner product space over $\R$ or $\C$.
Then $V$ has an [[orthonormal basis|0S9GGTR0EX]].
Moreover, each orthonormal family in $V$ extends to an orthonormal basis of $V$.

## Remarks

The proof applies the [[Gram–Schmidt process|0VT6P0GNQR]] to any basis of $V$.
For the extension, first extend the orthonormal family to a basis, and then apply Gram–Schmidt; it keeps the first vectors.
Hence each finite-dimensional real inner product space is isometric to $\R^n$ with the dot product.

## Explanations

### L1 human

Every finite-dimensional inner product space has a basis of perpendicular unit vectors.
We construct one with the Gram–Schmidt process.
So every such space looks like $\R^n$ or $\C^n$ with the standard inner product.
