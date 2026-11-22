---
tag: P6FQCVRKAD
kind: example
name: Polynomials as a direct sum of countably many lines
msc: ["15A03"]
topics: [QHKTJ89V6S]
audience: ug1
instance_of: [0S7W6EG32V]
uses: [02WZB422CE, 0Q9EZS90GY, 0XSJ25Z9M4]
sources:
  - url: https://en.wikipedia.org/wiki/Direct_sum_of_modules
    locator: Construction for vector spaces and abelian groups
  - url: https://hefferon.net/linearalgebra/
    locator: Chapter Two, Section III.4
---

## Example

Let $F$ be a field and let $F^{(\N)} = \bigoplus_{n \in \N} F$ be the [[external direct sum|02WZB422CE]] of countably many copies of $F$, indexed by $\N = \{0, 1, 2, \dots\}$.
Its vectors are the sequences $(a_0, a_1, a_2, \dots)$ with only finitely many nonzero terms.
We check that the map
$$\Phi \colon F^{(\N)} \to F[x], \qquad (a_0, a_1, a_2, \dots) \mapsto \sum_{n} a_n x^n$$
is an [[isomorphism|0XSJ25Z9M4]] onto the [[polynomial ring|0Q9EZS90GY]] $F[x]$.

1. The map $\Phi$ is well defined.
   Only finitely many $a_n$ are nonzero, so the sum is finite and is a polynomial.
2. The map $\Phi$ is linear.
   The coefficient of $x^n$ in a sum of polynomials is the sum of the coefficients, and the coefficient of $x^n$ in $c p$ is $c$ times the coefficient in $p$.
3. The map $\Phi$ is injective.
   If $\sum_n a_n x^n = 0$, then every $a_n$ is $0$, since a polynomial is zero exactly when all its coefficients are zero.
4. The map $\Phi$ is surjective.
   The polynomial $c_0 + c_1 x + \cdots + c_d x^d$ is the image of $(c_0, \dots, c_d, 0, 0, \dots)$.
5. So $\Phi$ is a bijective linear map, and $F[x] \cong F^{(\N)}$.

The canonical injection $\iota_n$ sends $a \in F$ to the sequence with $a$ in place $n$, and $\Phi$ sends that sequence to the monomial $a x^n$.
So $F[x]$ is also the [[internal direct sum|0XYYT5KNTX]] of the lines $F x^n$ for $n \ge 0$.

## Remarks

The example shows that the finite support condition of the direct sum is the same as the rule that a polynomial has finitely many terms.
The sequence $(1, 1, 1, \dots)$ is not in $F^{(\N)}$.
It corresponds to the formal power series $1 + x + x^2 + \cdots$, which lies in the [[product|0EX2HPXPJ6]] $F^{\N}$, and the product is the space $F[[x]]$ of all formal power series.
So the direct sum of countably many lines gives the polynomials, and the product gives the power series.

If we replace $\N$ by the finite set $\{0, 1, \dots, d\}$, the same map identifies $F^{d + 1}$ with the polynomials of degree at most $d$.
For a finite index set the direct sum and the product agree, so the difference between polynomials and power series appears only because $\N$ is infinite.

## Explanations

### L1 human

A polynomial is a list of coefficients that ends in zeros.
The polynomial $3 - x + 5x^3$ is the list $(3, -1, 0, 5, 0, 0, \dots)$.
Lists that end in zeros are exactly the vectors of the direct sum of countably many copies of $F$.

### L2 human

We add $3 - x + 5x^3$ and $1 + x$ through their sequences:
$$(3, -1, 0, 5, 0, \dots) + (1, 1, 0, 0, 0, \dots) = (4, 0, 0, 5, 0, \dots).$$
The result is the sequence of $4 + 5x^3$, and indeed $(3 - x + 5x^3) + (1 + x) = 4 + 5x^3$.
The monomials $1, x, x^2, \dots$ are the images $\Phi(\iota_n(1))$, and they form a basis of $F[x]$, so $F[x]$ has countable dimension.
Watch out: the same unit sequences do not span the product $F^{\N}$, because a power series with infinitely many nonzero coefficients is not a finite combination of monomials.
