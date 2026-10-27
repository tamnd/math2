---
tag: 0TA7WT68RK
kind: definition
name: Carmichael number
aliases: [absolute-pseudoprime]
msc: [11A51]
defines: 060ZX7C32T
uses: [0N3ADXHNTQ, 0GFKP8F8AG, 02M2K4QH9P]
sources:
  - url: https://en.wikipedia.org/wiki/Carmichael_number
    locator: Overview
inventory: [2E902XW5E1]
---

## Definition

A Carmichael number is a [[composite number|0N3ADXHNTQ]] $n$ such that $a^{n-1} \equiv 1 \pmod n$ for each integer $a$ [[coprime|0GFKP8F8AG]] to $n$.

## Remarks

Thus a Carmichael number is a [[Fermat pseudoprime|02M2K4QH9P]] to each base coprime to it.
Korselt's criterion: a composite $n$ is a Carmichael number if and only if $n$ is square-free and $p - 1 \mid n - 1$ for each prime $p \mid n$.
The smallest Carmichael number is $561 = 3 \cdot 11 \cdot 17$. Here $2$, $10$ and $16$ divide $560$.
Alford, Granville and Pomerance proved in 1994 that there are infinitely many Carmichael numbers.

## Explanations

### L1 human

A Carmichael number behaves like a prime for the Fermat test, for each base that has no common factor with it.
So the [[Fermat primality test|0N5ZSZMYH6]] cannot detect it, unless the base shares a factor with it.
