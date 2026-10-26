---
tag: ~cfbb4a39
kind: statement
role: theorem
name: Fundamental theorem of symmetric polynomials
msc: ["05E05"]
uses: [~9753c486, ~71a32e63]
sources:
  - url: https://en.wikipedia.org/wiki/Elementary_symmetric_polynomial
    locator: Fundamental theorem of symmetric polynomials
---

## Statement

Let $R$ be a [[commutative ring|~79bc52c4]] and let $f \in R[x_1, \dots, x_n]$ be [[symmetric|~9753c486]].
Then there is a unique polynomial $g \in R[y_1, \dots, y_n]$ with
$$f = g(e_1, \dots, e_n),$$
where $e_1, \dots, e_n$ are the [[elementary symmetric polynomials|~71a32e63]].

## Remarks

Equivalently, the map $R[y_1, \dots, y_n] \to R[x_1, \dots, x_n]$, $y_k \mapsto e_k$, is injective, and its image is the ring of symmetric polynomials.
One proof is by induction on the leading monomial in the lexicographic order. Each step subtracts a product of the $e_k$ with the same leading monomial.
Example: $x_1^2 + x_2^2 = e_1^2 - 2 e_2$.
So a symmetric expression in the roots of a polynomial over a field $K$ is an element of $K$.

## Explanations

### L1 human

Every symmetric polynomial can be written in exactly one way using the elementary symmetric polynomials.
The coefficients stay in the same ring.
