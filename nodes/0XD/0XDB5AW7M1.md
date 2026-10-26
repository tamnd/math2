---
tag: 0XDB5AW7M1
kind: definition
name: Jacobi symbol
msc: [11A15]
defines: 0ADTQBXRMC
uses: [01J8AMV9RS, 0AEKDFCYFA]
sources:
  - url: https://en.wikipedia.org/wiki/Jacobi_symbol
    locator: Definition
---

## Definition

Let $n$ be a positive odd integer with [[prime factorization|0AEKDFCYFA]] $n = p_1^{e_1} \cdots p_k^{e_k}$, and let $a$ be an integer.
The Jacobi symbol is
$$\left(\frac{a}{n}\right) = \left(\frac{a}{p_1}\right)^{e_1} \cdots \left(\frac{a}{p_k}\right)^{e_k},$$
where each factor on the right is a [[Legendre symbol|01J8AMV9RS]].
For $n = 1$, the empty product gives $\left(\frac{a}{1}\right) = 1$.

## Remarks

For a prime $n$, the Jacobi symbol equals the Legendre symbol.
If $\left(\frac{a}{n}\right) = -1$, then $a$ is not a quadratic residue modulo $n$.
The converse fails: $\left(\frac{2}{15}\right) = \left(\frac{2}{3}\right) \left(\frac{2}{5}\right) = 1$, but $2$ is not a square modulo $15$.
The symbol is $0$ exactly when $\gcd(a, n) > 1$.

## Explanations

### L1 human

The Jacobi symbol extends the Legendre symbol from odd primes to all odd positive integers.
It multiplies the Legendre symbols for the prime factors of $n$.
Its main use is fast computation, because it obeys [[quadratic reciprocity|0YY06KP3ZQ]] without the need to factor numbers.
