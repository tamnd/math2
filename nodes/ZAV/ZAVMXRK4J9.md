---
tag: ZAVMXRK4J9
kind: definition
name: Subadditive function
msc: [39B62, 26A51]
defines: 3X9DD9J3CV
uses: [0XMEM406JM, 0EPAT51DXQ, YQB2B0EXY8]
sources:
  - url: https://en.wikipedia.org/wiki/Subadditivity
---

## Definition

Let $(A, +)$ be a [[semigroup|0XMEM406JM]], for example $[0, \infty)$, $\R$ or the positive integers under addition.
A [[function|0EPAT51DXQ]] $f \colon A \to \R$ is *subadditive* if
$$f(x + y) \le f(x) + f(y) \quad \text{for all } x, y \in A.$$

## Remarks

Example: $f(x) = \sqrt{x}$ on $[0, \infty)$ is subadditive.
Check: both sides of $\sqrt{x + y} \le \sqrt{x} + \sqrt{y}$ are nonnegative, and squaring gives $x + y \le x + y + 2\sqrt{xy}$, which is true.

Non-example: $f(x) = x^2$ on $[0, \infty)$ is not subadditive, since $f(2) = 4 > 2 = f(1) + f(1)$.

The defining condition is a [[functional inequality|YQB2B0EXY8]].
A subadditive sequence is a subadditive function on the positive integers, $a_{m+n} \le a_m + a_n$.
Every concave function $f \colon [0, \infty) \to \R$ with $f(0) \ge 0$ is subadditive.
