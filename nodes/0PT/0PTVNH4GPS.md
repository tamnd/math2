---
tag: 0PTVNH4GPS
kind: concept
name: Linear congruence
msc: [11A07]
sources:
  - url: https://en.wikipedia.org/wiki/Modular_arithmetic
    locator: Advanced properties
---

## Summary

A linear congruence is a [[congruence|0TPW25CBN6]] $a x \equiv b \pmod n$, with given integers $a$ and $b$ and a positive integer $n$.
Its solutions are the integers $x$ that satisfy it.
Let $d = \gcd(a, n)$. The congruence has a solution if and only if $d \mid b$.
In this case, the solutions form exactly $d$ residue classes modulo $n$, and one residue class modulo $n / d$.

## Remarks

When $\gcd(a, n) = 1$, the unique solution modulo $n$ is $x \equiv a^{-1} b \pmod n$, where $a^{-1}$ is the [[modular multiplicative inverse|00GXTQMY8Z]] of $a$.
The congruence $a x \equiv b \pmod n$ is the same as the [[linear Diophantine equation|0R9GF3JD0K]] $a x - n y = b$.
For example, $6 x \equiv 4 \pmod{10}$ has $d = 2$. Its solutions are $x \equiv 4 \pmod 5$, that is, $x \equiv 4$ or $x \equiv 9 \pmod{10}$.

## Explanations

### L1 human

A linear congruence is a linear equation in modular arithmetic.
To solve $2 x \equiv 3 \pmod 5$, find the inverse $3$ of $2$ modulo $5$, and multiply: $x \equiv 9 \equiv 4 \pmod 5$.
Check: $2 \cdot 4 = 8 \equiv 3 \pmod 5$.
