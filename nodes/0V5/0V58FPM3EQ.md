---
tag: 0V58FPM3EQ
kind: definition
name: Minimal polynomial
msc: [15A18]
defines: 03NDVCSHSB
uses: [052M4SX57M]
sources:
  - url: https://en.wikipedia.org/wiki/Minimal_polynomial_(linear_algebra)
    locator: Formal definition
---

## Definition

Let $F$ be a field, let $V$ be a finite-dimensional vector space over $F$, and let $T \colon V \to V$ be an endomorphism.
The *minimal polynomial* of $T$ is the monic polynomial $m_T \in F[x]$ of least degree with $m_T(T) = 0$.
It is the monic generator of the ideal of [[annihilating polynomials|0PBN8VEKY8]] of $T$.
The minimal polynomial of a square matrix is defined in the same way.

## Remarks

The minimal polynomial exists and is unique.
It [[divides each annihilating polynomial|0VTAD25A3G]], in particular the [[characteristic polynomial|0VSSPAFM2C]].
For $I_2$, the minimal polynomial is $x - 1$; for $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$, it is $(x - 1)^2$.
Similar matrices have the same minimal polynomial.

## Explanations

### L1 human

The minimal polynomial is the shortest polynomial relation that a matrix satisfies.
All other relations are multiples of it.
Its roots are exactly the eigenvalues of the matrix.
