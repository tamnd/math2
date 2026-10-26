---
tag: 0S2SYHTWPY
kind: definition
name: Smallest prime factor
aliases: [least-prime-factor, minfac]
msc: [11A41]
defines: 0VMWPGGG3C
uses: [0SN0MAEKYX, 0SPBEDVNW1]
sources:
  - url: https://en.wikipedia.org/wiki/Prime_number
    locator: Trial division
---

## Definition

Let $n$ be a natural number with $n \ge 2$.
The smallest prime factor of $n$ is the smallest [[prime number|0SN0MAEKYX]] $p$ such that $p \mid n$.
It exists by the [[existence of a prime divisor|0SPBEDVNW1]].

## Remarks

The smallest prime factor of $n$ is also the smallest divisor $d$ of $n$ with $d > 1$.
The number $n$ is prime if and only if its smallest prime factor is $n$.
If $n$ is composite, its smallest prime factor $p$ satisfies $p^2 \le n$. See [[a composite number has a prime factor at most its square root|0EB6BBMQMC]].
For example, the smallest prime factor of $91 = 7 \cdot 13$ is $7$.

## Explanations

### L1 human

Divide $n$ by $2$, then by $3$, then by $4$, and so on. The first number that divides $n$ exactly is the smallest prime factor.
It is always prime, because a smaller factor of it would also divide $n$ and would come earlier.
