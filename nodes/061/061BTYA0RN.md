---
tag: 061BTYA0RN
kind: statement
role: theorem
name: Lucas–Lehmer test
aliases: [lucas-lehmer-primality-test]
msc: [11Y11]
uses: [0GJBJ19NXR, 0TPW25CBN6]
sources:
  - url: https://en.wikipedia.org/wiki/Lucas%E2%80%93Lehmer_primality_test
    locator: The test
same_as:
  wikidata: Q1138992
  wikipedia: Lucas–Lehmer primality test
---

## Statement

Let $p$ be an odd prime, and let $M_p = 2^p - 1$ be the [[Mersenne number|0GJBJ19NXR]].
Define the sequence $(s_i)_{i \ge 0}$ by $s_0 = 4$ and $s_i = s_{i-1}^2 - 2$ for $i \ge 1$.
Then $M_p$ is prime if and only if $s_{p-2} \equiv 0 \pmod{M_p}$.

## Remarks

For example, take $p = 5$ and $M_5 = 31$. Modulo $31$, the sequence is $4, 14, 8, 0$, so $s_3 \equiv 0$ and $31$ is prime.
In practice, one reduces each term modulo $M_p$. Then the test needs $p - 2$ squarings of numbers with at most $p$ bits.

## History

Édouard Lucas developed the test in 1878, and Derrick Henry Lehmer proved it in 1930.

## Explanations

### L1 human

The test checks a Mersenne number for primality with a simple loop: square, subtract $2$, and reduce modulo $M_p$.
After $p - 2$ steps, the result is $0$ exactly when $M_p$ is prime.
