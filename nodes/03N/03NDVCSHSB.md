---
tag: 03NDVCSHSB
kind: concept
name: Minimal polynomial
aliases: [minimal-polynomial-of-an-endomorphism, minimal-polynomial-of-a-matrix]
msc: ["15A18"]
topics: [6R1D6QPY3S]
audience: ug2
specializes: [0PBN8VEKY8]
uses: [0PBN8VEKY8, 0E3MV6E6MG]
sources:
  - url: https://en.wikipedia.org/wiki/Minimal_polynomial_(linear_algebra)
    locator: Formal definition
  - book: isbn:9780135367971
  - book: isbn:9783031410253
    locator: Chapter 5
same_as:
  wikidata: Q1163608
  wikipedia: Minimal polynomial (linear algebra)
---

## Summary

Let $T$ be an endomorphism of a finite-dimensional vector space $V$ over a field $F$.
The minimal polynomial $m_T$ is the monic polynomial of least degree with $m_T(T) = 0$.
It is the monic generator of the ideal of [[annihilating polynomials|0PBN8VEKY8]] of $T$, so every annihilating polynomial is a multiple of it.
Its roots in $F$ are the eigenvalues of $T$, and it divides the characteristic polynomial.
For a square matrix $A$, $m_A$ is the minimal polynomial of $x \mapsto Ax$.

## Motivation

The characteristic polynomial records the eigenvalues with their algebraic multiplicities.
The minimal polynomial records the shortest relation among the powers of $T$.
It decides whether $T$ is diagonalisable: this holds if and only if $m_T$ is a product of distinct linear factors.
It also gives $T^{-1}$ and high powers $T^k$ as polynomials in $T$ of small degree.

## Notation

The formal definition is the [[definition of the minimal polynomial|0V58FPM3EQ]].
Common symbols are $m_T$, $\mu_T$ and $\min_T$.
Mathlib writes `minpoly F T`.
The theorem on [[annihilating polynomials|~540651d7]] shows that $m_T$ exists and is unique.

## Remarks

### Examples

- [[The 3 by 3 matrix with 4 on the diagonal and 1 elsewhere|~29b91e21]]: $m_A = (x - 3)(x - 6)$, of degree $2$, while $p_A = (x - 3)^2 (x - 6)$.
- [[The shear of the plane|~919ae3c7]]: $m_A = (x - 1)^2 = p_A$.
- [[A 3 by 3 matrix with a defective eigenvalue|~5db5cf19]]: $m_A = p_A = (x - 1)(x - 2)^2$.
- [[Polynomials in a projection|~0ca6f4d2]]: a projection $P \ne 0, I$ has $m_P = x^2 - x$.
- [[Minimal polynomials of a diagonal and a nilpotent matrix|~e3d6a004]]: $\operatorname{diag}(1, 1, 2)$ has $m = (x - 1)(x - 2)$, and the $3 \times 3$ shift has $m = x^3$.

### Non-examples

- [[The identity matrix of size 2|~fe73ec25]]: $p = (x - 1)^2$ annihilates $I_2$, but it is not the minimal polynomial $x - 1$.
- A nonmonic polynomial such as $2x - 2$ annihilates $I_2$, but it is not the minimal polynomial, which is monic by definition.

### Basic properties

- $m_T$ divides every annihilating polynomial, by the theorem that the [[minimal polynomial divides every annihilating polynomial|0VTAD25A3G]].
- The roots of $m_T$ in $F$ are the eigenvalues of $T$, by the theorem that the [[eigenvalues are the roots of the minimal polynomial|0QF4ZEFG52]].
- $m_T$ divides $p_T$, by the theorem that the [[minimal polynomial divides the characteristic polynomial|093X6MN6Y6]]. So $\deg m_T \le \dim V$.
- $\dim F[T] = \deg m_T$, by the theorem on [[annihilating polynomials|~540651d7]].
- Similar matrices have the same minimal polynomial, because $p(SAS^{-1}) = S\,p(A)\,S^{-1}$.
- For $D = \operatorname{diag}(d_1, \dots, d_n)$ with distinct values $c_1, \dots, c_r$ among the $d_i$, $m_D = (x - c_1) \cdots (x - c_r)$.
- If $N^k = 0$ and $N^{k-1} \ne 0$, then $m_N = x^k$.
- $T$ is invertible if and only if $m_T(0) \ne 0$.

### History

The minimal polynomial is the monic generator of the annihilating ideal in the treatment of Hoffman and Kunze.
For a field element algebraic over a subfield, the analogous notion is the minimal polynomial of field theory.

### Common errors

- Taking $m_T = p_T$ without a check. For the identity and for the matrix with $4$ on the diagonal and $1$ elsewhere, they differ.
- Testing only the polynomial $\prod (x - \lambda_i)$ of the distinct eigenvalues. For the shear it fails, and a higher power is needed.
- Reading the exponent of $x - \lambda$ in $m_T$ as the algebraic multiplicity. It is the size of the largest Jordan block for $\lambda$.

## Explanations

### L1 human

A square matrix satisfies many polynomial equations, such as $A^2 - 5A + 6I = 0$.
The minimal polynomial is the shortest one with leading coefficient $1$.
Every other equation that the matrix satisfies is a multiple of it.
Its roots are exactly the eigenvalues of the matrix.

### L2 human

We compute the minimal polynomial of $A = \begin{pmatrix} 2 & 0 & 0 \\ 0 & 2 & 1 \\ 0 & 0 & 2 \end{pmatrix}$.

1. $p_A = (x - 2)^3$, because $A$ is triangular with diagonal $2, 2, 2$.
2. $m_A$ is monic, divides $p_A$, and has the root $2$. So $m_A$ is $x - 2$, $(x - 2)^2$ or $(x - 2)^3$.
3. $A - 2I = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix} \ne 0$, so $m_A \ne x - 2$.
4. $(A - 2I)^2 = 0$, because the only nonzero entry of $A - 2I$ is in position $(2, 3)$, and row $3$ of $A - 2I$ is zero.
5. So $m_A = (x - 2)^2$.

The typical use is the test for diagonalisability: $A$ is not diagonalisable, because $m_A$ has a repeated factor.
A trap: step 2 uses the theorem that $m_A$ divides $p_A$.
Without it, one must search among all monic polynomials.

### L3 human

The minimal polynomial is the generator of the annihilator of $V$ as a module over $F[x]$, with $x$ acting by $T$.
In the invariant factor decomposition $V \cong \bigoplus_i F[x]/(a_i)$ with $a_1 \mid a_2 \mid \cdots \mid a_k$, it is the largest invariant factor $a_k$.
The characteristic polynomial is the product $a_1 \cdots a_k$, which gives a second proof that $m_T \mid p_T$ and that $p_T \mid m_T^k$.
