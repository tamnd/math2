---
tag: MZM1AFXY82
kind: statement
role: corollary
name: Interchange of summation order
msc: [40B05, 40A05]
uses: [WW53KG71KH, WK5V372TG3, 0W3K3QPEWT]
about: [PAXCH4FFSV]
sources:
  - url: https://en.wikipedia.org/wiki/Series_(mathematics)
---

## Statement

Let $(a_{m,n})_{m, n \in \N}$ be a [[double sequence|WK5V372TG3]] of complex numbers with
$$\sum_{m=0}^{\infty} \sum_{n=0}^{\infty} \abs{a_{m,n}} < \infty.$$
Then all the series below converge [[absolutely|0W3K3QPEWT]], and
$$\sum_{m=0}^{\infty} \sum_{n=0}^{\infty} a_{m,n} = \sum_{n=0}^{\infty} \sum_{m=0}^{\infty} a_{m,n}.$$

## Remarks

By the nonnegative case of [[Fubini's theorem for series|WW53KG71KH]], the hypothesis says that the family $(a_{m,n})$ over $\N \times \N$ is summable.
The same theorem, applied once with rows first and once with columns first, shows that both iterated sums equal the sum of the family.
The hypothesis cannot be dropped.
Let $a_{m,m} = 1$, $a_{m,m+1} = -1$ for all $m$, and $a_{m,n} = 0$ otherwise.
Each row sums to $0$, so $\sum_m \sum_n a_{m,n} = 0$.
Column $0$ sums to $1$ and every other column sums to $1 - 1 = 0$, so $\sum_n \sum_m a_{m,n} = 1$.
Example of use: with the [[Riemann zeta function|1XWBY4N0VT]], $\sum_{k \ge 2} (\zeta(k) - 1) = \sum_{k \ge 2} \sum_{n \ge 2} n^{-k}$.
Swapping the nonnegative sums gives $\sum_{n \ge 2} \sum_{k \ge 2} n^{-k} = \sum_{n \ge 2} \frac{1}{n(n-1)} = 1$.

## Explanations

### L1 human

For an infinite table of numbers, summing rows first or columns first gives the same total when the absolute values have a finite total.
Without this condition, the two orders can give different answers.

### L2 human

The result is used to swap two sums, which is one of the most common steps in analysis and number theory.
To apply it, bound the double sum of absolute values; for nonnegative terms the swap is always allowed, possibly with value $+\infty$.
The counterexample above shows why conditionally convergent double sums need care.
