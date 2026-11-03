---
tag: ZJ6WC1J9X5
kind: statement
role: proposition
name: Count of integers up to n divisible by a set of primes dividing n
msc: [11A25]
uses: [0SN0MAEKYX, 096PW7Q014]
sources:
  - url: https://github.com/mitchkeller/applied-combinatorics/blob/ebd95d6bd59e23c633c65cf560bcb93efa912aae/source/s_inclusion-exclusion_euler-phi.ptx#L56
    locator: source/s_inclusion-exclusion_euler-phi.ptx:56
---

## Statement

Let $n \ge 2$ be an integer and let $k \ge 1$. Let $p_1, \dots, p_k$ be distinct [[prime numbers|0SN0MAEKYX]], each of which [[divides|096PW7Q014]] $n$.

Then exactly $\dfrac{n}{p_1 p_2 \cdots p_k}$ of the integers in $\{1, 2, \dots, n\}$ are divisible by every one of $p_1, \dots, p_k$.

## Remarks

Let $P = p_1 \cdots p_k$. Distinct primes are pairwise coprime, so an integer is divisible by all of them if and only if it is divisible by $P$. Since each $p_i$ divides $n$ and the primes are distinct, $P$ divides $n$. The multiples of $P$ in $\{1, \dots, n\}$ are $P, 2P, \dots, (n/P)P$, which gives $n/P$ numbers.

For example, with $n = 30$ and the primes $2$ and $3$, the numbers are $6, 12, 18, 24, 30$, and $30/6 = 5$.

This count is the term for each intersection of sets in the inclusion-exclusion proof of the formula for Euler's totient function.
