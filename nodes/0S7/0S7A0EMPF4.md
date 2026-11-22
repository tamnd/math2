---
tag: 0S7A0EMPF4
kind: definition
name: Algebraic multiplicity
msc: ["15A18"]
topics: [6R1D6QPY3S]
audience: ug2
defines: 0FY42N02DV
uses: [0ZND7NQ970, 0BZ81AJNWF]
sources:
  - url: https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors
    locator: Algebraic multiplicity
---

## Definition

The algebraic multiplicity counts how often an eigenvalue is a root of the characteristic polynomial.
Let $F$ be a field, let $V$ be a finite-dimensional vector space over $F$, and let $T \colon V \to V$ be a linear map.
Let $\lambda$ be an [[eigenvalue|0BQAA2BK3Q]] of $T$.
The *algebraic multiplicity* of $\lambda$ is the largest integer $m \ge 1$ such that $(t - \lambda)^m$ divides the [[characteristic polynomial|0J5EMJRRFM]] $p_T(t)$ in $F[t]$.
For a square matrix $A$ over $F$, the algebraic multiplicity of $\lambda$ is that of the map $x \mapsto Ax$ on $F^n$.

## Notation

Common symbols are $a(\lambda)$ and $\operatorname{am}(\lambda)$.
Mathlib writes `Polynomial.rootMultiplicity λ (Matrix.charpoly A)` for this number.

## Remarks

The finite dimension is needed so that $p_T$ exists, and the condition that $\lambda$ is an eigenvalue makes $\lambda$ a root of $p_T$, so $m \ge 1$.
A largest $m$ exists, because $p_T$ is a nonzero polynomial of degree $\dim V$, so no power of degree above $\dim V$ divides it.
Some books also set the multiplicity of a scalar that is not an eigenvalue to $0$, which is consistent with the same formula.

For the [[shear|HTAWRAC3QE]] $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ we get $p(t) = (t - 1)^2$, so $(t - 1)^2$ divides $p$ and $(t - 1)^3$ does not, and the algebraic multiplicity of $1$ is $2$.
The dimension of the eigenspace is a different number: here it is $1$, the [[geometric multiplicity|099TWVJ909]].
The multiplicities of all eigenvalues add up to at most $\dim V$, with equality exactly when $p_T$ splits over $F$.
The [[concept page|0FY42N02DV]] has the worked examples.

## Explanations

### L1 human

An eigenvalue can be a root of the characteristic polynomial several times, as $1$ is a root of $(t - 1)^2$ twice.
The algebraic multiplicity counts how many times.
For the identity matrix of size $n$, the characteristic polynomial is $(t - 1)^n$, so the eigenvalue $1$ has algebraic multiplicity $n$.
