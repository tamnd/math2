---
tag: 0VC4DVE7DQ
kind: statement
role: theorem
name: Euler's theorem
aliases: [fermat-euler-theorem, euler-totient-theorem]
msc: [11A07]
uses: [0VV04M41AN, 0TPW25CBN6, 0GFKP8F8AG]
sources:
  - url: https://en.wikipedia.org/wiki/Euler%27s_theorem
    locator: lead section
same_as:
  wikidata: Q193910
  wikipedia: Euler's theorem
---

## Statement

Let $n$ be a positive integer and let $a$ be an integer [[coprime|0GFKP8F8AG]] to $n$.
Then $a^{\varphi(n)} \equiv 1 \pmod n$, where $\varphi$ is [[Euler's totient function|0VV04M41AN]].

## Remarks

When $n = p$ is prime, $\varphi(p) = p - 1$, and the result is [[Fermat's little theorem|0M25PRN3WQ]].
A proof uses [[Lagrange's theorem|3C53TD]]: the group $(\mathbb{Z}/n\mathbb{Z})^\times$ has order $\varphi(n)$, by the [[number of invertible residues modulo n|06RJWZCG95]].
The result lets us reduce exponents. If $\gcd(a, n) = 1$ and $k \equiv l \pmod{\varphi(n)}$, then $a^k \equiv a^l \pmod n$.
For example, $\varphi(10) = 4$, so $7^{4} \equiv 1 \pmod{10}$, and the last digit of $7^{222}$ is the last digit of $7^2 = 49$, that is, $9$.

## History

Euler proved the theorem in 1763.

## Explanations

### L1 human

Powers of $a$ modulo $n$ repeat in a cycle, and the cycle comes back to $1$.
Euler's theorem gives one exponent that always brings $a$ back to $1$, namely $\varphi(n)$.
For $n = 12$ and $a = 5$: $\varphi(12) = 4$ and $5^4 = 625 = 52 \cdot 12 + 1$.
