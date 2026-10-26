---
tag: ~cbfd25d2
kind: statement
role: corollary
name: Congruence is compatible with powers
msc: [11A07]
uses: [~e79e2431, ~db3a40ac]
sources:
  - url: https://en.wikipedia.org/wiki/Modular_arithmetic
    locator: Basic properties
---

## Statement

Let $n$ be a positive integer, let $a$ and $b$ be integers, and let $k$ be a natural number.
If $a \equiv b \pmod n$, then $a^k \equiv b^k \pmod n$.

## Remarks

The proof is an induction on $k$ with [[compatibility with multiplication|~db3a40ac]].
The exponent cannot be reduced modulo $n$ in general. For example, $2^5 = 32 \equiv 2 \pmod 3$, but $2^{5 \bmod 3} = 2^2 \equiv 1 \pmod 3$.
[[Euler's theorem|~f2db875d]] tells when one can reduce the exponent, and by which modulus.

## Explanations

### L1 human

To find $10^{100} \bmod 9$, note that $10 \equiv 1 \pmod 9$.
So $10^{100} \equiv 1^{100} = 1 \pmod 9$, without a computation of the large number.
