---
tag: ~aca3e41d
kind: statement
role: theorem
name: Existence of an eigenvalue over an algebraically closed field
msc: [15A18]
uses: [~0aea559b, ~40b1c26d]
sources:
  - url: https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors
    locator: Eigenvalues and characteristic polynomial
---

## Statement

Let $F$ be an algebraically closed field, let $V$ be a finite-dimensional vector space over $F$ with $V \ne 0$, and let $T \colon V \to V$ be a linear map.
Then $T$ has at least one [[eigenvalue|~13fe038c]] in $F$.

## Remarks

The [[characteristic polynomial|~fab11e9c]] of $T$ has degree $\dim V \ge 1$, so it has a root in $F$.
The statement applies to $F = \C$, by the fundamental theorem of algebra.
It fails over $\R$: the rotation of $\R^2$ by $90$ degrees has no real eigenvalue.
It also fails in infinite dimensions: the map $p(x) \mapsto x\, p(x)$ on $\C[x]$ has no eigenvalue.

## Explanations

### L1 human

Over the complex numbers, every square matrix has at least one eigenvector.
The reason is that every nonconstant complex polynomial has a root.
Over the real numbers, a rotation can move every line, so no real eigenvector exists.
