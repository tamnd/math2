---
tag: AW57ZPYDPK
kind: proof
name: Proof of the coefficient formula for a product of power series
msc: [13F25]
proves: 0H6KWAYS87
uses: [072W67KFYK, 0M98XYVX6S]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy_product
    locator: Cauchy product of two power series
---

## Proof

1. Write $f = \sum_{m \ge 0} a_m X^m$ and $g = \sum_{m \ge 0} b_m X^m$. By the definition of the [[coefficient|0M98XYVX6S]], $a_m = [X^m] f$ and $b_m = [X^m] g$.
2. In $R[\![X]\!]$, multiplication is the Cauchy product, by the definition of [[formal power series|072W67KFYK]]. So $f g = \sum_{n \ge 0} c_n X^n$ with $c_n = \sum_{i + j = n} a_i b_j$.
3. Here the sum runs over the pairs $(i, j) \in \N^2$ with $i + j = n$. Hence $[X^n](fg) = c_n = \sum_{i+j=n} [X^i] f \cdot [X^j] g$. This is the first equality.
4. The map $i \mapsto (i, n - i)$ is a bijection from $\set{0, 1, \dots, n}$ to the set of pairs $(i, j) \in \N^2$ with $i + j = n$. Its inverse is $(i, j) \mapsto i$.
5. Reindexing the finite sum of step 3 along this bijection gives $\sum_{i+j=n} [X^i] f \cdot [X^j] g = \sum_{i=0}^{n} [X^i] f \cdot [X^{n-i}] g$. This is the second equality.

## Idea

The formula is the definition of the product, read through the coefficient maps. The second form only lists the pairs $(i, j)$ with $i + j = n$ by their first entry.
