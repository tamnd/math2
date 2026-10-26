---
tag: 0AEKDFCYFA
kind: definition
name: Prime factorization
aliases: [prime-decomposition, integer-factorization]
msc: [11A51]
defines: 02EKEPPJ3R
uses: [0SN0MAEKYX]
sources:
  - url: https://en.wikipedia.org/wiki/Integer_factorization
    locator: Prime decomposition
---

## Definition

Let $n$ be a positive integer.
A prime factorization of $n$ is a finite list of [[prime numbers|0SN0MAEKYX]] $p_1 \le p_2 \le \dots \le p_k$ such that $n = p_1 p_2 \cdots p_k$.
For $n = 1$, the prime factorization is the empty list, with the empty product $1$.

## Remarks

We often group equal primes and write $n = q_1^{e_1} q_2^{e_2} \cdots q_r^{e_r}$, with distinct primes $q_1 < \dots < q_r$ and exponents $e_i \ge 1$.
For example, the prime factorization of $360$ is $2, 2, 2, 3, 3, 5$, that is, $360 = 2^3 \cdot 3^2 \cdot 5$.
Each positive integer has [[a prime factorization|020K0X7HVR]], and the [[fundamental theorem of arithmetic|084HH1NDCB]] says that it is unique.

## Explanations

### L1 human

A prime factorization breaks a number into primes, which you cannot break further.
A factor tree does this: $360 = 36 \cdot 10 = (6 \cdot 6) \cdot (2 \cdot 5) = 2 \cdot 3 \cdot 2 \cdot 3 \cdot 2 \cdot 5$.
Sort the primes to get the list $2, 2, 2, 3, 3, 5$.
