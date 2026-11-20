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

Let $F$ be a field and let $F^{(\N)} = \bigoplus_{n \in \N} F$ be the [[external direct sum|02WZB422CE]] of countably many copies of $F$.
Its vectors are sequences $(a_0, a_1, a_2, \dots)$ with only finitely many nonzero terms.
We check that the map
$$\Phi \colon F^{(\N)} \to F[x], \qquad (a_0, a_1, a_2, \dots) \mapsto \sum_{n} a_n x^n$$
is an [[isomorphism|0XSJ25Z9M4]] onto the [[polynomial ring|0Q9EZS90GY]] $F[x]$.

1. $\Phi$ is well defined: only finitely many $a_n$ are nonzero, so the sum is a polynomial.
2. $\Phi$ is linear: the coefficients of a sum of polynomials are the sums of the coefficients, and likewise for scalar multiples.
3. $\Phi$ is injective: if $\sum_n a_n x^n = 0$, then every coefficient $a_n$ is $0$, since a polynomial is zero exactly when all its coefficients are zero.
4. $\Phi$ is surjective: the polynomial $c_0 + c_1 x + \cdots + c_d x^d$ is $\Phi(c_0, \dots, c_d, 0, 0, \dots)$.
5. So $\Phi$ is an isomorphism, and $F[x] \cong F^{(\N)}$.

The canonical injection $\iota_n$ sends $a \in F$ to the monomial $a x^n$.
So $F[x]$ is the internal direct sum of the lines $F x^n$.

## Remarks

The sequence $(1, 1, 1, \dots)$ is not in $F^{(\N)}$.
It would correspond to the formal power series $1 + x + x^2 + \cdots$, which lies in the [[product|0EX2HPXPJ6]] $F^{\N}$, identified with $F[[x]]$.
So the direct sum gives polynomials and the product gives power series.

## Explanations

### L1 human

A polynomial is a list of coefficients that ends with zeros.
That is exactly a vector of the direct sum of countably many copies of $F$.

### L2 human

For example, $3 - x + 5x^3$ corresponds to $(3, -1, 0, 5, 0, 0, \dots)$.
Adding $1 + x$, with sequence $(1, 1, 0, 0, \dots)$, gives $(4, 0, 0, 5, 0, \dots)$, which is $4 + 5x^3$.
The monomials $1, x, x^2, \dots$ correspond to the images of $1$ under the injections, and they form a basis.
