---
tag: 5GNFSQ5HK0
kind: statement
role: theorem
name: Monotonic law for multiplication of natural numbers
aliases: [monotonic-law-for-multiplication]
msc: [03F30]
uses: [0MWKJ44V5A, 0HNATXFEV5, 06J5DE801P]
sources:
  - url: https://github.com/mitchkeller/applied-combinatorics/blob/ebd95d6bd59e23c633c65cf560bcb93efa912aae/source/s_background_total-order-N.ptx#L66
    locator: source/s_background_total-order-N.ptx:66
---

## Statement

Let $m$, $n$ and $p$ be [[natural numbers|0MWKJ44V5A]], with the [[order|0HNATXFEV5]] $\le$ and the [[product|06J5DE801P]] $\cdot$.

If $m \le n$, then $mp \le np$.

If in addition $m < n$ and $p \neq 0$, then $mp < np$.

## Remarks

So multiplying both sides of an inequality by the same number keeps the inequality. The strict form needs a factor that is not zero, since $m \cdot 0 = n \cdot 0$ for all $m$ and $n$.
