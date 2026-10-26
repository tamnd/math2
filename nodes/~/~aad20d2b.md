---
tag: ~aad20d2b
kind: statement
role: theorem
name: Fibonacci numbers as sums of binomial coefficients
msc: [11B39]
uses: [~b1f658a8, ~bc16f766]
sources:
  - url: https://en.wikipedia.org/wiki/Fibonacci_sequence
    locator: Combinatorial identities
---

## Statement

Let $n$ be a natural number, and let $F_m$ be the [[Fibonacci numbers|~bc16f766]].
Then
$$F_{n+1} = \sum_{k=0}^{\lfloor n/2 \rfloor} \binom{n - k}{k}.$$

## Remarks

Example: $F_6 = \binom{5}{0} + \binom{4}{1} + \binom{3}{2} = 1 + 4 + 3 = 8$.
Combinatorial proof: $F_{n+1}$ counts the tilings of a strip of length $n$ by squares and dominoes. A tiling with $k$ dominoes has $n - k$ tiles, and $\binom{n-k}{k}$ choices fix the positions of the dominoes.
In [[Pascal's triangle|~9e20c12e]], the sum runs along a shallow diagonal.

## Explanations

### L1 human

Add the numbers of Pascal's triangle along the shallow diagonals, and you get the Fibonacci numbers.
Each term counts the ways to tile a strip with a fixed number of dominoes.
