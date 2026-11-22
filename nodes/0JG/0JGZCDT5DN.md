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
A [[polynomial|N2EY1EVPRB]] over $F$ is an expression $p = a_0 + a_1 x + \dots + a_d x^d$ with coefficients $a_k \in F$, and two polynomials are equal when all their coefficients agree.
Let $F[x]$ be the set of all polynomials over $F$, and for $n \ge 0$ let $P_n(F)$ be the set of polynomials of degree at most $n$, the zero polynomial included.
Addition and scalar multiplication act on coefficients: the coefficient of $x^k$ in $p + q$ is $a_k + b_k$, and in $cp$ it is $c a_k$.
For example, in $P_2(\mathbb{R})$,
$$(1 + 2x) + 3(x - x^2) = 1 + 5x - 3x^2.$$
We check that these sets are [[vector spaces|000AYPA9AJ]] and that $P_n(F)$ has dimension $n + 1$.

1. Closure in $F[x]$: a sum and a scalar multiple of polynomials are again polynomials.
2. Closure in $P_n(F)$: if $p$ and $q$ have no terms above $x^n$, then neither have $p + q$ and $cp$.
3. The axioms: a polynomial is the same data as its sequence of coefficients $(a_0, a_1, a_2, \dots)$, with only finitely many nonzero terms. The operations act entry by entry on these sequences, so each axiom of the [[definition|05EGHEQZAW]] reduces to a rule of $F$, as in the [[coordinate space|713F6AM1X1]].
4. Zero and negatives: the zero vector is the zero polynomial, and $-p$ has coefficients $-a_k$.
5. Spanning: each $p \in P_n(F)$ equals $a_0 \cdot 1 + a_1 x + \dots + a_n x^n$, a combination of the monomials $1, x, \dots, x^n$.
6. Independence: if $c_0 + c_1 x + \dots + c_n x^n$ is the zero polynomial, then every $c_k = 0$, by the definition of equality of polynomials.

So $F[x]$ and $P_n(F)$ are vector spaces over $F$, and $P_n(F)$ is a [[subspace|00YC1D652K]] of $F[x]$.
By steps 5 and 6 the monomials $1, x, \dots, x^n$ form a [[basis|0KCQ9Y3QKA]] of $P_n(F)$, so $\dim P_n(F) = n + 1$.

## Remarks

### The whole polynomial space

In the same way, all the monomials $1, x, x^2, \dots$ form a basis of $F[x]$, so $F[x]$ has countably infinite dimension; see [[the dimension of a polynomial ring|T35XFF5AY3]].
No finite set spans $F[x]$.
Finitely many polynomials have a largest degree $d$, and every combination of them has degree at most $d$, so $x^{d + 1}$ is not in their span.

### Other bases and what is not a subspace

The monomials are only one basis.
Another basis of $P_2(\mathbb{R})$ is $1, x - 1, (x - 1)^2$, which is suited to questions near $x = 1$.
Changing the basis changes the coordinates of a polynomial, not the polynomial or the space.

The polynomials of degree exactly $n \ge 1$ do not form a subspace.
They do not contain $0$, and the sum $x^n + (-x^n + 1) = 1$ has degree $0$.
[[Differentiation|0SS770NS8B]] is a linear map from $P_n(F)$ to $P_{n - 1}(F)$ for $n \ge 1$, and it returns in the sub-area on linear maps.

### Watch out

Some books write $\mathcal{P}_n(F)$ for $P_n(F)$, and some use $P_n$ for the polynomials of degree less than $n$, a space of dimension $n$.
Read the convention before you quote a dimension.
Over a finite field a polynomial is not the same as the function it defines.
Over $\mathbb{F}_2$, the polynomial $x^2 + x$ is not zero, yet its values are $0^2 + 0 = 0$ and $1^2 + 1 = 0$, so it gives the zero function.

## Explanations

### L1 human

Polynomials can be added and scaled, and the result is again a polynomial.
So they form a vector space.
The polynomial $3 + 2x - x^2$ carries the same information as the list of coefficients $(3, 2, -1)$.
That is why the polynomials of degree at most $2$ behave just like $\mathbb{R}^3$.

### L2 human

We write $p = x^2$ in the basis $1, x - 1, (x - 1)^2$ of $P_2(\mathbb{R})$.
Write $x = (x - 1) + 1$ and square:
$$x^2 = \bigl((x - 1) + 1\bigr)^2 = (x - 1)^2 + 2(x - 1) + 1.$$
So the coordinates of $x^2$ in this basis are $(1, 2, 1)$, listed in the order $1, x - 1, (x - 1)^2$.
Check by expanding: $1 + (2x - 2) + (x^2 - 2x + 1) = x^2$.
The typical use is to turn a question about polynomials, such as fitting a polynomial through given points, into a linear system for the coefficients.

### L3 human

The space $F[x]$ is the free vector space on the countable set of monomials, and it is also a commutative ring and an $F$-algebra.
Its dual space is isomorphic to the space $F[[x]]$ of formal power series, by sending a functional to the series of its values on $1, x, x^2, \dots$, and this dual has uncountable dimension.
The chain $P_0 \subset P_1 \subset P_2 \subset \dots$ is a filtration by degree, and operators such as differentiation lower the degree along it.
