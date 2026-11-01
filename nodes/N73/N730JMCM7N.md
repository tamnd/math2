---
tag: N730JMCM7N
kind: definition
name: Minimal prime ideal
msc: [13A15]
defines: S2D8823P8B
uses: [0GYGHKX834, 06HC6HK0Z8, 0MYSA6MYNA]
sources:
  - url: https://en.wikipedia.org/wiki/Minimal_prime_ideal
---

## Definition

Let $R$ be a [[commutative ring|0GYGHKX834]].
A *minimal prime ideal* of $R$ is a [[prime ideal|06HC6HK0Z8]] $P$ of $R$ such that no prime ideal $Q$ of $R$ satisfies $Q \subsetneq P$.
Let $I$ be an [[ideal|0MYSA6MYNA]] of $R$.
A *minimal prime over $I$* is a prime ideal $P \supseteq I$ such that no prime ideal $Q$ satisfies $I \subseteq Q \subsetneq P$.

## Remarks

Example: in $R = k[x, y]/(xy)$ with $k$ a field, the ideal $(x)$ is a minimal prime.
It is prime because $R/(x) \cong k[y]$ is a domain.
A prime $Q \subseteq (x)$ contains $xy = 0$, so it contains $x$ or $y$, and $y \notin (x)$ forces $x \in Q$.
Non-example: $2\Z$ is prime in $\Z$, but it is not minimal, since the prime ideal $(0)$ is strictly smaller.
By Zorn's lemma, every prime ideal containing $I$ contains a minimal prime over $I$; the key point is that the intersection of a chain of prime ideals is prime.
The minimal primes over $I$ are the minimal primes of $R/I$, pulled back to $R$.
