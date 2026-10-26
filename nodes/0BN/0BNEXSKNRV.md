---
tag: 0BNEXSKNRV
kind: definition
name: Polynomial of an endomorphism
msc: [15A04, 15A54]
defines: 0E3MV6E6MG
uses: [0PTF1PTJK0]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_polynomial
    locator: lead section
---

## Definition

Let $F$ be a field, let $V$ be a vector space over $F$, and let $T \colon V \to V$ be an [[endomorphism|0J7H0YBFDJ]].
Let $p(x) = c_0 + c_1 x + \cdots + c_d x^d$ be a polynomial in $F[x]$.
The *value of $p$ at $T$* is the endomorphism
$$p(T) = c_0 \id_V + c_1 T + c_2 T^2 + \cdots + c_d T^d,$$
where $T^k$ is the composition of $k$ copies of $T$.
For an $n \times n$ matrix $A$, $p(A) = c_0 I_n + c_1 A + \cdots + c_d A^d$ in the same way.

## Remarks

The map $p \mapsto p(T)$ is a homomorphism of algebras $F[x] \to \End_F(V)$: $(p + q)(T) = p(T) + q(T)$ and $(pq)(T) = p(T) q(T)$.
In particular, any two polynomials in $T$ commute.
If $T(v) = \lambda v$, then $p(T)(v) = p(\lambda) v$.

## Explanations

### L1 human

We can put a matrix into a polynomial, because matrices can be added, scaled and multiplied.
The constant term becomes a multiple of the identity matrix.
For example, if $p(x) = x^2 - 3x + 2$, then $p(A) = A^2 - 3A + 2I$.
