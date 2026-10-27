---
tag: 0TRNT4X7J0
kind: concept
name: Euclidean algorithm
msc: [11A05]
specializes: [023VY493K0]
sources:
  - url: https://en.wikipedia.org/wiki/Euclidean_algorithm
    locator: Procedure
same_as:
  wikidata: Q230848
  wikipedia: Euclidean algorithm
---

## Summary

The Euclidean algorithm computes the [[greatest common divisor|02WF878BH1]] of two natural numbers $a$ and $b$.
It uses two rules: $\gcd(a, 0) = a$, and $\gcd(a, b) = \gcd(b, a \bmod b)$ when $b \neq 0$.
It applies the second rule until the second number is $0$. Then the first number is the result.
The algorithm stops, because the second number gets smaller at each step.

## Remarks

The second rule is true because $a$ and $b$ have the same common divisors as $b$ and $a \bmod b$.
The number of steps is at most a constant times the number of digits of the smaller input. Lamé's theorem gives this bound.
The algorithm also works in each Euclidean domain, for example in the ring of polynomials over a field.

## Explanations

### L1 human

To find $\gcd(48, 18)$, divide again and again, and keep the divisor and the remainder.
$48 = 2 \cdot 18 + 12$, then $18 = 1 \cdot 12 + 6$, then $12 = 2 \cdot 6 + 0$.
The last nonzero remainder is $6$, so $\gcd(48, 18) = 6$.
