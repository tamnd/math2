---
tag: 0S7A0EMPF4
kind: definition
name: Algebraic multiplicity
msc: [15A18]
defines: 0FY42N02DV
uses: [0ZND7NQ970, 0BZ81AJNWF]
sources:
  - url: https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors
    locator: Algebraic multiplicity
---

## Definition

Let $F$ be a field, let $V$ be a finite-dimensional vector space over $F$, and let $T \colon V \to V$ be a linear map.
Let $\lambda$ be an [[eigenvalue|0BQAA2BK3Q]] of $T$.
The *algebraic multiplicity* of $\lambda$ is the largest integer $m \ge 1$ such that $(t - \lambda)^m$ divides the [[characteristic polynomial|0J5EMJRRFM]] $p_T(t)$.

## Remarks

The sum of the algebraic multiplicities of all eigenvalues is at most $\dim V$, with equality when $p_T$ splits over $F$.
For $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$, the eigenvalue $1$ has algebraic multiplicity $2$.
The algebraic multiplicity is at least the [[geometric multiplicity|099TWVJ909]].

## Explanations

### L1 human

An eigenvalue can be a root of the characteristic polynomial several times.
The algebraic multiplicity counts how many times.
For the identity matrix of size $n$, the eigenvalue $1$ has algebraic multiplicity $n$.
