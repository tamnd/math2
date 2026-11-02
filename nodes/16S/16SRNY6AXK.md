---
tag: 16SRNY6AXK
kind: definition
name: Lambert series
msc: [30B50, 11A25]
defines: HATVWNZNMR
uses: [0NM626FH6Q, 0YBDSJARWN, 0BKJT6WG96, 0C8QENHYZW, 0VV04M41AN, 09JXE6XMCC]
sources:
  - url: https://en.wikipedia.org/wiki/Lambert_series
---

## Definition

Let $(a_n)_{n \ge 1}$ be a sequence of complex numbers.
The *Lambert series* of $(a_n)$ is the [[series|0NM626FH6Q]]
$$L(q) = \sum_{n=1}^{\infty} a_n \frac{q^n}{1 - q^n},$$
considered as a function of the complex variable $q$.
Only the points $q$ with $\abs{q} < 1$ where the series converges are considered.

## Remarks

If $\abs{q} < 1$ and $\sum_n a_n q^n$ [[converges absolutely|0YBDSJARWN]], then the Lambert series converges absolutely and
$$L(q) = \sum_{m=1}^{\infty} \Big( \sum_{d \mid m} a_d \Big) q^m.$$
Check: $\frac{q^n}{1 - q^n} = \sum_{k \ge 1} q^{nk}$, and $\sum_{n, k} \abs{a_n} \abs{q}^{nk} \le \frac{1}{1 - \abs{q}} \sum_n \abs{a_n} \abs{q}^n < \infty$, so the double series may be regrouped by $m = nk$.
Example: for $a_n = 1$, the coefficient of $q^m$ is the [[number of divisors|0BKJT6WG96]] $d(m)$, so $\sum_n \frac{q^n}{1 - q^n} = \sum_m d(m) q^m$.
Example: for $a_n = \mu(n)$, the [[Möbius function|0C8QENHYZW]], the divisor sums vanish for $m > 1$, so $\sum_n \mu(n) \frac{q^n}{1 - q^n} = q$.
Example: for $a_n = \varphi(n)$, [[Euler's totient function|0VV04M41AN]], the [[divisor sum of the totient|09JXE6XMCC]] is $m$, so the Lambert series is $\sum_m m q^m = q/(1-q)^2$.
Non-example of convergence: for $a_n = n!$ and $0 < \abs{q} < 1$, the terms satisfy $\abs{a_n q^n / (1 - q^n)} \ge n! \abs{q}^n / 2$, which tends to $\infty$, so the series diverges.
