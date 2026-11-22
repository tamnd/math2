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

The minimal polynomial of a linear map is the monic polynomial of smallest degree that annihilates the map.
Let $F$ be a field, let $V$ be a finite-dimensional vector space over $F$, and let $T \colon V \to V$ be an endomorphism.
The *minimal polynomial* of $T$ is the monic polynomial $m_T \in F[x]$ of least degree with $m_T(T) = 0$.
Equivalently, it is the monic generator of the ideal $I_T$ of [[annihilating polynomials|052M4SX57M]] of $T$.
For an $n \times n$ matrix $A$ over $F$, the minimal polynomial $m_A$ is defined in the same way, with $m_A(A) = 0$ in $M_n(F)$.

## Notation

Mathlib defines `minpoly F x` for an element $x$ of any $F$-algebra, and applies it to $T \in \operatorname{End}_F(V)$ and to $A \in M_n(F)$.
Mathlib sets `minpoly F x = 0` when $x$ has no nonzero annihilating polynomial, but in finite dimension this case does not occur.

## Remarks

Each condition in the definition has a job.
Finite dimension guarantees that some nonzero polynomial annihilates $T$, by the theorem that [[the ideal of annihilating polynomials is nonzero and principal|AH34SFJ8SF]].
Without it the definition can fail: on smooth functions the derivative has no nonzero annihilating polynomial.
The word "monic" makes the answer unique, since $x - 1$ and $2x - 2$ both annihilate the identity and have the same degree.
The same theorem shows that the monic element of least degree and the monic generator of $I_T$ are the same polynomial, so the two descriptions agree.

The minimal polynomial of a matrix $A$ equals that of the map $L_A \colon x \mapsto Ax$, because $p(A)x = p(L_A)(x)$ for every polynomial $p$ and every vector $x$.
For example, $I_2$ has minimal polynomial $x - 1$, while the shear $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ has $(x - 1)^2$, since the shear minus $I_2$ is not zero but its square is.
The [[concept page|03NDVCSHSB]] computes many more examples.

## Explanations

### L1 human

The minimal polynomial is the shortest polynomial equation that a matrix satisfies, written with leading coefficient $1$.
All the other equations that the matrix satisfies are multiples of this one.

### L2 human

To find $m_A$ for $A = \begin{pmatrix} 3 & 0 \\ 0 & 3 \end{pmatrix}$, start with the smallest degrees.
A nonzero constant $c$ gives $cI \ne 0$, so $\deg m_A \ge 1$.
In degree $1$, the polynomial $x - 3$ gives $A - 3I = 0$.
So $m_A = x - 3$, while the characteristic polynomial $(x - 3)^2$ has degree $2$.
Watch out: the polynomial $2x - 6$ also annihilates $A$, but it is not monic, so it is not the minimal polynomial.
