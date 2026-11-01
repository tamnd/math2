---
tag: EFDBS6ZME8
kind: definition
name: Factorization of polynomials
msc: [13P05, "12E05", 12D05]
defines: JWB6B13Q8Z
uses: [0QA8CHH8MG, 0Q9EZS90GY, 00X2A9G9W3, 0BDX4MBKT4, 06YMXJMXYS]
sources:
  - url: https://en.wikipedia.org/wiki/Factorization_of_polynomials
---

## Definition

Let $K$ be a [[field|0QA8CHH8MG]] and let $f \in K[x]$ be a nonzero polynomial.
A factorization of $f$ into irreducibles is an expression
$$f = c \, p_1^{e_1} \cdots p_k^{e_k}$$
such that:

1. $c \in K$ is nonzero;
2. $p_1, \dots, p_k$ are pairwise distinct [[monic|0BDX4MBKT4]] [[irreducible polynomials|00X2A9G9W3]] in $K[x]$, with $k \ge 0$;
3. $e_1, \dots, e_k$ are positive integers.

## Remarks

Every nonzero $f$ has such a factorization, and it is unique up to the order of the factors, since $K[x]$ is a [[unique factorisation domain|06YMXJMXYS]].
The constant $c$ is the leading coefficient of $f$.
Example: over $\Q$, $2x^3 - 2x = 2 \, x (x - 1)(x + 1)$; each factor is monic of degree $1$, hence irreducible.
Non-example: $x^4 - 1 = (x^2 - 1)(x^2 + 1)$ is a factorization but not into irreducibles, since $x^2 - 1 = (x - 1)(x + 1)$ violates clause 2.
Over a unique factorisation domain $R$ such as $\Z$, a nonzero $f \in R[x]$ is its content times a primitive polynomial.
The primitive part factors into primitive irreducibles, by [[polynomial ring over a UFD is a UFD|0D6KH8Y59N]].
Over finite fields, see [[factorization over finite fields|XNE7F0BAGE]].

## Explanations

### L1 human

The definition fixes the shape of the answer: a constant times powers of different monic irreducible polynomials.
The exponents record repeated factors.
