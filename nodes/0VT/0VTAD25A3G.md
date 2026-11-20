---
tag: 0VTAD25A3G
kind: statement
role: proposition
name: Minimal polynomial divides every annihilating polynomial
msc: ["15A18"]
topics: [6R1D6QPY3S]
audience: ug2
about: [03NDVCSHSB, 0PBN8VEKY8]
uses: [0V58FPM3EQ, 052M4SX57M]
sources:
  - url: https://en.wikipedia.org/wiki/Minimal_polynomial_(linear_algebra)
    locator: Formal definition
  - book: isbn:9780135367971
  - book: isbn:9783031410253
    locator: Chapter 5
---

## Statement

Let $F$ be a field, let $V$ be a finite-dimensional vector space over $F$, and let $T \colon V \to V$ be an endomorphism with [[minimal polynomial|03NDVCSHSB]] $m_T$.
For $p \in F[x]$, the following are equivalent.

1. $p(T) = 0$, that is, $p$ is an [[annihilating polynomial|0PBN8VEKY8]] of $T$.
2. $m_T$ divides $p$ in $F[x]$.

The same holds for an $n \times n$ matrix $A$ over $F$ and its minimal polynomial $m_A$.

## Remarks

The proof is in [[the proof by division with remainder|BRFPQM1MMW]].
The direction from 2 to 1 is direct: if $p = q m_T$, then $p(T) = q(T) m_T(T) = 0$.

### Why each hypothesis is needed

- $V$ must be finite-dimensional so that $m_T$ exists. For the derivative on $C^\infty(\R)$, only the zero polynomial annihilates, and there is no monic generator.
- The divisor must be the minimal polynomial, not an arbitrary annihilating polynomial. For $I_2$, the polynomial $x - 1$ annihilates $I_2$ but is not divisible by $(x - 1)^2$.

### Consequences

- If $A^2 = A$, then $m_A$ divides $x^2 - x$. So $m_A$ is $x$, $x - 1$ or $x^2 - x$.
- If $A^k = 0$, then $m_A = x^j$ for some $j \le k$.
- The minimal polynomial of the restriction of $T$ to an invariant subspace divides $m_T$, because $m_T$ annihilates the restriction.
- Together with the Cayley-Hamilton theorem, it gives that $m_T$ divides the characteristic polynomial. This is the theorem that the [[minimal polynomial divides the characteristic polynomial|093X6MN6Y6]].

### Generalizations

- The theorem on [[annihilating polynomials|AH34SFJ8SF]] states that $I_T = m_T \, F[x]$, which is the same fact in the language of ideals.
- For an element $a$ algebraic over a field $K$, the minimal polynomial of $a$ divides every polynomial over $K$ with root $a$. This is the field theory version.

## History

The division argument is standard in linear algebra textbooks, for example in Hoffman and Kunze.

## Explanations

### L1 human

Every polynomial that kills $T$ is a multiple of the minimal polynomial.
If a matrix satisfies $A^2 = A$, then its minimal polynomial divides $x^2 - x$.
So it is $x$, $x - 1$ or $x^2 - x$.

### L2 human

We use the theorem to find $m_A$ for $A = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$.

1. $A^2 = I$, so $x^2 - 1 = (x - 1)(x + 1)$ annihilates $A$.
2. By the theorem, $m_A$ is a monic divisor of $x^2 - 1$: one of $1$, $x - 1$, $x + 1$ and $x^2 - 1$.
3. $1(A) = I \ne 0$, $A - I \ne 0$ and $A + I \ne 0$, because $A$ is not $\pm I$.
4. So $m_A = x^2 - 1$.

The typical use is to reduce the search for $m_A$ to the finitely many monic divisors of a known annihilating polynomial.
A trap: the theorem needs $p(A) = 0$ for the whole matrix, not $p(A)v = 0$ for one vector.

### L3 human

The statement says that the kernel of evaluation $F[x] \to \End_F(V)$ is the principal ideal $(m_T)$.
The same division argument shows that $F[x]$ is a principal ideal domain.
