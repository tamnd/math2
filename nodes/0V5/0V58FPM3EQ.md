---
tag: 0V58FPM3EQ
kind: definition
name: Minimal polynomial
msc: ["15A18"]
topics: [6R1D6QPY3S]
audience: ug2
defines: 03NDVCSHSB
uses: [052M4SX57M, AH34SFJ8SF]
formal:
  - system: lean4
    library: mathlib
    decl: minpoly
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Minimal_polynomial_(linear_algebra)
    locator: Formal definition
  - book: isbn:9780135367971
---

## Definition

Let $F$ be a field, let $V$ be a finite-dimensional vector space over $F$, and let $T \colon V \to V$ be an endomorphism.
The *minimal polynomial* of $T$ is the monic polynomial $m_T \in F[x]$ of least degree with $m_T(T) = 0$.
Equivalently, it is the monic generator of the ideal $I_T$ of [[annihilating polynomials|0PBN8VEKY8]] of $T$.
The minimal polynomial $m_A$ of an $n \times n$ matrix $A$ over $F$ is defined in the same way, with $m_A(A) = 0$.

## Notation

Mathlib defines `minpoly F x` for an element $x$ of any $F$-algebra, and uses it for $T \in \End_F(V)$ and for $A \in M_n(F)$.
Mathlib sets `minpoly F x = 0` when no nonzero annihilating polynomial exists; in finite dimension this case does not occur.

## Remarks

The definition makes sense because of the theorem on [[annihilating polynomials|AH34SFJ8SF]].
That theorem shows that $I_T \ne 0$ in finite dimension, that $I_T$ has exactly one monic generator, and that this generator is the unique monic element of least degree.
So the two descriptions in the definition agree.
The minimal polynomial of $A$ equals that of the map $x \mapsto Ax$, because $p(A)x = p(L_A)(x)$ for every $p$.
For $I_2$, the minimal polynomial is $x - 1$; for $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$, it is $(x - 1)^2$.

## Explanations

### L1 human

The minimal polynomial is the shortest polynomial relation that a matrix satisfies, scaled so that its leading coefficient is $1$.
All other relations are multiples of it.

### L2 human

We find $m_A$ for $A = \begin{pmatrix} 3 & 0 \\ 0 & 3 \end{pmatrix}$.

1. A nonzero constant $c$ gives $cI \ne 0$, so $\deg m_A \ge 1$.
2. $A - 3I = 0$, so $x - 3$ annihilates $A$.
3. So $m_A = x - 3$, of degree $1$, while $p_A = (x - 3)^2$ has degree $2$.

A trap: $m_A$ is monic.
The polynomial $2x - 6$ also annihilates $A$, but it is not the minimal polynomial.
