---
tag: JWB6B13Q8Z
kind: concept
name: Factorization of polynomials
msc: [13P05, "12E05", 12D05]
sources:
  - url: https://en.wikipedia.org/wiki/Factorization_of_polynomials
same_as:
  wikidata: Q392477
  wikipedia: Factorization of polynomials
---

## Summary

Factorization of polynomials writes a polynomial as a product of [[irreducible polynomials|03FKX7Z5DC]].
Over a field the result is unique up to order and constant factors, because $K[x]$ is a [[unique factorisation domain|0W4X9G6263]].
The answer depends on the field: $x^2 + 1$ is irreducible over $\R$ but splits over $\C$.
Computing factorizations is a central task of computer algebra, with different methods over finite fields, over $\Q$ and over number fields.

## Explanations

### L1 human

Factoring a polynomial is like factoring an integer into primes.
The irreducible polynomials play the role of the primes.
For example, over $\Q$ one has $x^4 - 1 = (x - 1)(x + 1)(x^2 + 1)$, and none of the three factors can be split further over $\Q$.
Over $\C$ the last factor splits as $(x - i)(x + i)$.
The [[definition|EFDBS6ZME8]] states the form of the result.
