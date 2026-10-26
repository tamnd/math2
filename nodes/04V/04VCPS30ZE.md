---
tag: 04VCPS30ZE
kind: definition
name: P-adic valuation
aliases: [p-adic-order, multiplicity-of-a-prime]
msc: [11A51]
defines: 03HDF50VN4
uses: [0SN0MAEKYX, 096PW7Q014]
sources:
  - url: https://en.wikipedia.org/wiki/P-adic_valuation
    locator: Integers
---

## Definition

Let $p$ be a [[prime number|0SN0MAEKYX]] and let $n$ be a nonzero integer.
The $p$-adic valuation $\nu_p(n)$ is the largest natural number $k$ such that $p^k \mid n$.
By convention, $\nu_p(0) = \infty$.

## Remarks

For a positive integer $n$, $\nu_p(n)$ is the exponent of $p$ in the [[prime factorization|0AEKDFCYFA]] of $n$. It is $0$ when $p \nmid n$.
For example, $\nu_2(40) = 3$ and $\nu_5(40) = 1$, because $40 = 2^3 \cdot 5$.
For a nonzero rational number $a / b$, one sets $\nu_p(a / b) = \nu_p(a) - \nu_p(b)$.
The Lean library Mathlib sets $\nu_p(0) = 0$ for its function on natural numbers.

## Explanations

### L1 human

The number $\nu_p(n)$ counts how many times you can divide $n$ by $p$ and still get an integer.
For $n = 72$ and $p = 2$: $72, 36, 18, 9$, so you can divide three times, and $\nu_2(72) = 3$.
