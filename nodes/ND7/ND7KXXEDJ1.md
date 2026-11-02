---
tag: ND7KXXEDJ1
kind: definition
name: Lindelöf summation
msc: ["40G10"]
defines: B505P3MKTZ
uses: [8X25Q4XYMN, 0JH4MN4K1C, 0909PWZR62]
sources:
  - url: https://en.wikipedia.org/wiki/Divergent_series
---

## Definition

Let $\sum_{n \ge 0} a_n$ be a [[series|0JH4MN4K1C]] of complex numbers.
For $h > 0$ put
$$L(h) = a_0 + \sum_{n \ge 1} n^{-hn} a_n$$
whenever this series converges.
The series $\sum a_n$ is *Lindelöf summable* to $s$ if $L(h)$ is defined for every $h > 0$ and the [[one-sided limit|0909PWZR62]] $\lim_{h \to 0^+} L(h)$ equals $s$.

## Remarks

Example: let $\sum a_n$ converge to $s$.
For fixed $h > 0$ the factors $n^{-hn} = e^{-hn \ln n}$ decrease in $n \ge 1$ and lie in $(0, 1]$.
By Abel's partial summation, $L(h)$ converges, and the tails of $L(h)$ are bounded by the tails of $\sum a_n$ uniformly in $h$.
Since each factor tends to $1$ as $h \to 0^+$, one gets $L(h) \to s$, so the series is Lindelöf summable to its sum.

Non-example: for $1 + 1 + 1 + \cdots$, $L(h) = 1 + \sum_{n \ge 1} n^{-hn}$ is defined for every $h > 0$.
For each $N$, $L(h) \ge 1 + \sum_{n=1}^{N} n^{-hn} \to N + 1$ as $h \to 0^+$.
So $L(h) \to +\infty$, and the second condition fails.
