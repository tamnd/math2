---
tag: 2S4K8FA8QY
kind: definition
name: Field of formal Laurent series
msc: [13F25, 12J10]
defines: YZWYF7DXTW
uses: [0QA8CHH8MG, 072W67KFYK, 0VF11ZTTMD, ZYK5F0GBK6]
sources:
  - url: https://en.wikipedia.org/wiki/Formal_power_series
---

## Definition

Let $k$ be a [[field|0QA8CHH8MG]] and let $X$ be a symbol.
A *formal Laurent series* in $X$ over $k$ is a family $(a_n)_{n \in \Z}$ of elements of $k$ with the following property.
There is $N \in \Z$ with $a_n = 0$ for all $n < N$.
It is written $\sum_{n \ge N} a_n X^n$.
The set $k((X))$ of these series has the operations
$$\sum_n a_n X^n + \sum_n b_n X^n = \sum_n (a_n + b_n) X^n, \qquad \Big(\sum_n a_n X^n\Big)\Big(\sum_n b_n X^n\Big) = \sum_n \Big(\sum_{i + j = n} a_i b_j\Big) X^n.$$
With these operations $k((X))$ is a field, the *field of formal Laurent series* over $k$.

## Remarks

The inner sum $\sum_{i + j = n} a_i b_j$ is finite: if $a_i = 0$ for $i < N$ and $b_j = 0$ for $j < M$, only the pairs with $N \le i \le n - M$ contribute.
Example: $f = X - X^2$ has the inverse $g = \sum_{n \ge -1} X^n = X^{-1} + 1 + X + \cdots$; indeed $f g = (1 - X)(1 + X + X^2 + \cdots) = 1$.
Non-example: the family with $a_n = 1$ for all $n \in \Z$ is not a formal Laurent series, since no $N$ bounds its negative powers.
Its square would need the infinite sum $\sum_{i + j = 0} 1$.
The map $v(f) = \min \set{n : a_n \ne 0}$ for $f \ne 0$ is a [[discrete valuation|ZYK5F0GBK6]] on $k((X))$ with uniformizer $X$, and $k((X))$ is complete for it.
Its valuation ring is the ring $k[\![X]\!]$ of [[formal power series|072W67KFYK]], and $k((X))$ is the [[field of fractions|0VF11ZTTMD]] of $k[\![X]\!]$.
