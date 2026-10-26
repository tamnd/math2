---
tag: ~d53ee0ce
kind: example
name: Space of matrices
msc: [15A03]
instance_of: [~d0f609e9]
uses: [~a2759ca2, ~712e2ef6, ~d3699095]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_(mathematics)
    locator: lead section
---

## Example

Let $F$ be a field and let $m, n \ge 1$.
The set $M_{m \times n}(F)$ of $m \times n$ [[matrices|~52f4e417]] over $F$ is a [[vector space|~d0f609e9]] over $F$, with [[matrix addition|~517d197f]] and [[scalar multiplication|~9ac848e3]].
Its zero vector is the [[zero matrix|~348187b5]].
The matrices $E_{ij}$, with entry $1$ in position $(i, j)$ and $0$ elsewhere, form a basis, so $\dim M_{m \times n}(F) = mn$.

## Remarks

The map that lists the entries of a matrix row by row is a linear isomorphism $M_{m \times n}(F) \to F^{mn}$.
The space $M_{m \times n}(F)$ is isomorphic to the [[space of linear maps|~0acf07d9]] from $F^n$ to $F^m$.
The symmetric $n \times n$ matrices form a subspace of dimension $n(n+1)/2$.

## Explanations

### L1 human

Matrices of one fixed size can be added and scaled, so they form a vector space.
A $2 \times 2$ matrix holds four numbers, so this space has dimension $4$.
It is $F^4$ written as a square instead of a row.
