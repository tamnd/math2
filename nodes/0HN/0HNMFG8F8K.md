---
tag: 0HNMFG8F8K
kind: statement
role: theorem
name: Eigenvectors with distinct eigenvalues are linearly independent
msc: [15A18]
uses: [0B5H4208Z9, 0EVHJFTG9Z]
sources:
  - url: https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors
    locator: Eigenspaces, geometric multiplicity, and the eigenbasis
---

## Statement

Let $F$ be a field, let $V$ be a vector space over $F$, and let $T \colon V \to V$ be a linear map.
Let $v_1, \dots, v_k$ be [[eigenvectors|0N6960W0BV]] of $T$ for eigenvalues $\lambda_1, \dots, \lambda_k$ that are pairwise distinct.
Then $v_1, \dots, v_k$ are [[linearly independent|0CRMGPAH83]].

## Remarks

The proof is by induction on $k$: apply $T - \lambda_k \id_V$ to a linear relation, and the term of $v_k$ disappears.
So the sum of the eigenspaces of $T$ for distinct eigenvalues is a direct sum.
In particular, an endomorphism of an $n$-dimensional space has at most $n$ distinct eigenvalues.

## Explanations

### L1 human

Eigenvectors for different eigenvalues point in genuinely different directions.
None of them is a combination of the others.
This is the key fact behind diagonalisation.
