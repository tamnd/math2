---
tag: W5YGV8P9F2
kind: definition
name: Submultiplicative function
msc: [39B62]
defines: GE8MRV41R7
uses: [0XMEM406JM]
sources:
  - url: https://en.wikipedia.org/wiki/Subadditivity
---

## Definition

Let $(S, \cdot)$ be a [[semigroup|0XMEM406JM]].
A function $f \colon S \to [0, \infty)$ is *submultiplicative* if
$$f(x \cdot y) \le f(x) \, f(y) \quad \text{for all } x, y \in S.$$

## Remarks

For $S = (\N_{\ge 1}, +)$ the condition reads $a_{m+n} \le a_m a_n$ for a sequence $(a_n)_{n \ge 1}$, and one speaks of a submultiplicative sequence.
Example: on the multiplicative semigroup $(0, \infty)$, let $f(x) = x + 1$.
Then $f(xy) = xy + 1 \le xy + x + y + 1 = f(x) f(y)$, since $x, y > 0$.
Example: for a square matrix $A$ and a [[matrix norm|54T6Y6DSY4]] with $\norm{BC} \le \norm{B} \norm{C}$, the sequence $a_n = \norm{A^n}$ is submultiplicative.
Non-example: the constant function $f = 1/2$ on any semigroup fails the condition, since $1/2 > 1/4 = f(x) f(y)$.
If $f$ takes only positive values, then $f$ is submultiplicative exactly when $\log f$ satisfies $\log f(xy) \le \log f(x) + \log f(y)$.
