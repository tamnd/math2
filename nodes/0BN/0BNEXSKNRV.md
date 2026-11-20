---
tag: 0BNEXSKNRV
kind: definition
name: Polynomial of an endomorphism
msc: ["15A04", "15A54"]
topics: [6R1D6QPY3S]
audience: ug2
defines: 0E3MV6E6MG
uses: [0PTF1PTJK0]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_polynomial
    locator: lead section
  - book: isbn:9783031410253
    locator: Chapter 5
---

## Definition

Let $F$ be a field, let $V$ be a vector space over $F$, and let $T \colon V \to V$ be an [[endomorphism|0PTF1PTJK0]].
Let $p(x) = c_0 + c_1 x + \cdots + c_d x^d$ be a polynomial in $F[x]$.
The *value of $p$ at $T$* is the endomorphism
$$p(T) = c_0 \id_V + c_1 T + c_2 T^2 + \cdots + c_d T^d,$$
where $T^0 = \id_V$ and $T^k$ is the composition of $k$ copies of $T$.
For an $n \times n$ matrix $A$ over $F$, $p(A) = c_0 I_n + c_1 A + \cdots + c_d A^d$ in the same way.
The set of all $p(T)$ is written $F[T]$.

## Notation

Mathlib writes `Polynomial.aeval T p` for $p(T)$.
Some books write $p[T]$ or $p(T)$ with the convention $T^0 = I$ stated explicitly.

## Remarks

The map $p \mapsto p(T)$ is a homomorphism of $F$-algebras $F[x] \to \End_F(V)$: $(p + q)(T) = p(T) + q(T)$, $(cp)(T) = c\,p(T)$, $(pq)(T) = p(T) q(T)$ and $1(T) = \id_V$.
The rule for products follows from $T^j T^k = T^{j+k}$ and from the distributive laws for composition of linear maps.
In particular, any two polynomials in $T$ commute, so $F[T]$ is a commutative subalgebra of $\End_F(V)$.
If $T(v) = \lambda v$, then $T^k(v) = \lambda^k v$ by induction on $k$, so $p(T)(v) = p(\lambda) v$.
For a matrix, $p(SAS^{-1}) = S\,p(A)\,S^{-1}$, because $(SAS^{-1})^k = SA^kS^{-1}$.

## Explanations

### L1 human

We can put a matrix into a polynomial, because matrices can be added, scaled and multiplied.
The constant term becomes a multiple of the identity matrix.
For example, if $p(x) = x^2 - 3x + 2$, then $p(A) = A^2 - 3A + 2I$.

### L2 human

We compute $p(A)$ for $A = \begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix}$ and $p(x) = x^2 - x - 1$.

1. $A^2 = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}$.
2. $p(A) = A^2 - A - I = \begin{pmatrix} 1 - 0 - 1 & 1 - 1 - 0 \\ 1 - 1 - 0 & 2 - 1 - 1 \end{pmatrix} = 0$.
3. So $p$ annihilates $A$. This $p$ is the characteristic polynomial of $A$, because $\tr A = 1$ and $\det A = -1$.

A trap: the constant $-1$ becomes $-I$, not the number $-1$.
