---
tag: YSMBT6KQ4N
kind: definition
name: Lambert summation
msc: ["40G10", "11M45"]
defines: W8H1WX0JHG
uses: [8X25Q4XYMN, 0JH4MN4K1C, 0909PWZR62, 0C8QENHYZW]
sources:
  - url: https://en.wikipedia.org/wiki/Lambert_summation
---

## Definition

Let $\sum_{n \ge 1} a_n$ be a [[series|0JH4MN4K1C]] of complex numbers.
The series is *Lambert summable* to $s$ if the following two conditions hold.

1. The series $\sum_{n \ge 1} n a_n \frac{x^n}{1 - x^n}$ converges for every real $x$ with $0 < x < 1$.
2. The [[one-sided limit|0909PWZR62]]
$$\lim_{x \to 1^-} (1 - x) \sum_{n \ge 1} n a_n \frac{x^n}{1 - x^n}$$
exists and equals $s$.

## Remarks

Example: let $\mu$ be the [[Möbius function|0C8QENHYZW]] and $a_n = \mu(n)/n$.
Expanding $\frac{x^n}{1 - x^n} = \sum_{m \ge 1} x^{nm}$ and grouping by $N = nm$ gives
$$\sum_{n \ge 1} \mu(n) \frac{x^n}{1 - x^n} = \sum_{N \ge 1} x^N \sum_{d \mid N} \mu(d) = x,$$
since $\sum_{d \mid N} \mu(d)$ is $1$ for $N = 1$ and $0$ for $N > 1$.
The rearrangement is valid because the double series converges absolutely for $0 < x < 1$.
So $(1 - x) \cdot x \to 0$, and $\sum \mu(n)/n$ is Lambert summable to $0$.

Non-example: for $1 + 1 + 1 + \cdots$, the inequality $1 - x^n \le n (1 - x)$ gives $n \frac{x^n}{1 - x^n} \ge \frac{x^n}{1 - x}$.
Hence $(1 - x) \sum_{n \ge 1} n \frac{x^n}{1 - x^n} \ge \sum_{n \ge 1} x^n = \frac{x}{1 - x} \to +\infty$, and condition 2 fails.
