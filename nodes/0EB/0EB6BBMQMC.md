---
tag: 0EB6BBMQMC
kind: statement
role: proposition
name: A composite number has a prime factor at most its square root
msc: [11A51]
uses: [0N3ADXHNTQ, 0S2SYHTWPY]
sources:
  - url: https://en.wikipedia.org/wiki/Trial_division
    locator: Method
---

## Statement

Let $n$ be a [[composite number|0N3ADXHNTQ]].
Then $n$ has a prime factor $p$ with $p^2 \le n$, that is, $p \le \sqrt{n}$.

## Remarks

The [[smallest prime factor|0S2SYHTWPY]] $p$ of $n$ has this property. Write $n = p m$. Then $m > 1$, and each prime factor of $m$ is at least $p$, so $m \ge p$ and $n \ge p^2$.
This result justifies [[trial division|0Z962ECCXR]]: to test whether $n > 1$ is prime, it is enough to test the primes $p \le \sqrt{n}$.
For example, $\sqrt{97} < 10$ and none of $2, 3, 5, 7$ divides $97$, so $97$ is prime.

## Explanations

### L1 human

If $n = a b$ with both factors larger than $\sqrt{n}$, then $a b > n$, which is impossible.
So one of the two factors is at most $\sqrt{n}$, and a prime factor of that factor is also at most $\sqrt{n}$.
