---
tag: KY9ZXCHCVX
kind: definition
name: Superadditive function
msc: [39B62, 26A51]
defines: 99VGJBCYC0
uses: [0XMEM406JM, 0EPAT51DXQ, 3X9DD9J3CV]
sources:
  - url: https://en.wikipedia.org/wiki/Superadditivity
---

## Definition

Let $(A, +)$ be a [[semigroup|0XMEM406JM]], for example $[0, \infty)$, $\R$ or the positive integers under addition.
A [[function|0EPAT51DXQ]] $f \colon A \to \R$ is *superadditive* if
$$f(x + y) \ge f(x) + f(y) \quad \text{for all } x, y \in A.$$

## Remarks

Example: $f(x) = x^2$ on $[0, \infty)$ is superadditive.
Check: $(x + y)^2 = x^2 + y^2 + 2xy \ge x^2 + y^2$, since $xy \ge 0$.

Non-example: $f(x) = \sqrt{x}$ on $[0, \infty)$ is not superadditive, since $\sqrt{2} < 2 = \sqrt{1} + \sqrt{1}$.

A function $f$ is superadditive if and only if $-f$ is [[subadditive|3X9DD9J3CV]].
Every convex function $f \colon [0, \infty) \to \R$ with $f(0) \le 0$ is superadditive.
For a superadditive sequence, $a_{m+n} \ge a_m + a_n$, the limit of $a_n / n$ exists in $(-\infty, \infty]$ and equals $\sup_n a_n / n$.
