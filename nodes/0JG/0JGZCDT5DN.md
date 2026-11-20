---
tag: 0JGZCDT5DN
kind: example
name: Space of polynomials
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
instance_of: [000AYPA9AJ]
uses: [05EGHEQZAW, N2EY1EVPRB]
sources:
  - url: https://en.wikipedia.org/wiki/Polynomial_ring
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Examples_of_vector_spaces
    locator: Polynomial vector spaces
  - book: isbn:9783031410253
    locator: Section 2A
---

## Example

Let $F$ be a field.
A [[polynomial|N2EY1EVPRB]] over $F$ is an expression $p = a_0 + a_1 x + \cdots + a_d x^d$ with $a_k \in F$; two polynomials are equal when all their coefficients agree.
Let $F[x]$ be the set of all polynomials.
For $n \ge 0$, let $P_n(F)$ be the set of polynomials of degree at most $n$, with the zero polynomial included.
Addition and scalar multiplication act on coefficients: the coefficient of $x^k$ in $p + q$ is $a_k + b_k$, and in $cp$ it is $ca_k$.

1. Closure in $F[x]$: a sum and a scalar multiple of polynomials are polynomials.
2. Closure in $P_n(F)$: if $p$ and $q$ have no terms above $x^n$, then neither have $p + q$ and $cp$.
3. The axioms: a polynomial is determined by its sequence of coefficients $(a_0, a_1, \dots)$, which has only finitely many nonzero terms. The operations act entry by entry on these sequences, so each axiom reduces to a rule of $F$, as in the [[coordinate space|713F6AM1X1]].
4. The zero vector is the zero polynomial, and $-p$ has coefficients $-a_k$.

So $F[x]$ and $P_n(F)$ are [[vector spaces|000AYPA9AJ]] over $F$, and $P_n(F)$ is a [[subspace|00YC1D652K]] of $F[x]$.

The monomials $1, x, x^2, \dots, x^n$ form a [[basis|0KCQ9Y3QKA]] of $P_n(F)$.

5. Spanning: each $p \in P_n(F)$ is $a_0 \cdot 1 + a_1 x + \cdots + a_n x^n$ by definition.
6. Independence: if $c_0 + c_1 x + \cdots + c_n x^n$ is the zero polynomial, then all its coefficients are $0$, by the definition of equality.

So $\dim P_n(F) = n + 1$.
In the same way, all monomials $1, x, x^2, \dots$ form a basis of $F[x]$, so $F[x]$ has countably infinite dimension; see [[the dimension of a polynomial ring|T35XFF5AY3]].

## Remarks

The set of polynomials of degree exactly $n \ge 1$ is not a subspace: it does not contain $0$, and $x^n + (-x^n + 1) = 1$ leaves it.
Some books write $\mathcal{P}_n(F)$ for $P_n(F)$, and some use the polynomials of degree less than $n$, which form a space of dimension $n$.
Other bases of $P_2(\R)$ are $1, x - 1, (x - 1)^2$ and the Lagrange polynomials at three points; changing the basis changes the coordinates, not the space.
[[Differentiation|0SS770NS8B]] is a linear map from $P_n(F)$ to $P_{n-1}(F)$ for $n \ge 1$.
The space $F[x]$ is not finite-dimensional: finitely many polynomials have a largest degree $d$, and $x^{d + 1}$ is not in their span.

## Explanations

### L1 human

Polynomials can be added and scaled, and the result is again a polynomial.
So they form a vector space.
A polynomial $3 + 2x - x^2$ is the same data as the list of coefficients $(3, 2, -1)$.
That is why the polynomials of degree at most $2$ behave like $\R^3$.

### L2 human

We check that $1, x - 1, (x - 1)^2$ span $P_2(\R)$ by writing $p = x^2$ in terms of them.

1. Write $x = (x - 1) + 1$.
2. Then $x^2 = ((x - 1) + 1)^2 = (x - 1)^2 + 2(x - 1) + 1$.
3. Check by expanding: $(x^2 - 2x + 1) + (2x - 2) + 1 = x^2$.

The typical use is to turn questions about polynomials, such as interpolation, into linear systems for the coefficients.
A trap: over a finite field, a polynomial is not the same as the function it defines.
Over $\mathbb{F}_2$, the polynomial $x^2 + x$ is nonzero, but its value at $0$ and at $1$ is $0$.

### L3 human

The space $F[x]$ is the free vector space on the countable set of monomials, and it is also a ring and an $F$-algebra.
Its dimension $\aleph_0$ makes it the simplest infinite-dimensional space; its dual space is the space $F[[x]]$ of formal power series, which has uncountable dimension.
The filtration $P_0 \subset P_1 \subset P_2 \subset \cdots$ by degree is used for operators such as differentiation, which lower the degree.
