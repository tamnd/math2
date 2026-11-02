---
tag: FCTRS2SS16
kind: example
name: Nested radical
msc: [40A05, 26A18]
instance_of: [B88PFYXWBK]
uses: [0VB8BFRABH, 0KN22AAW5R, 0FM6N4R0VB, 0SC8T7548D]
sources:
  - url: https://en.wikipedia.org/wiki/Nested_radical
---

## Example

The infinite nested radical
$$\sqrt{1 + \sqrt{1 + \sqrt{1 + \cdots}}}$$
is defined as the limit of the sequence $x_1 = 1$, $x_{n+1} = \sqrt{1 + x_n}$.
This is an [[infinite composition|B88PFYXWBK]] of the map $f(x) = \sqrt{1 + x}$, since $x_n = f^{\circ n}(0)$.
Its value is the [[golden ratio|0SC8T7548D]] $\varphi = \frac{1 + \sqrt5}{2}$.

Check: the sequence is increasing, since $x_2 = \sqrt2 > x_1$ and $f$ is increasing.
It is bounded above by $2$, since $x_n < 2$ gives $x_{n+1} < \sqrt3 < 2$.
By the [[monotone convergence theorem|0FM6N4R0VB]] it has a limit $L \ge 1$, and continuity of $f$ gives $L = \sqrt{1 + L}$.
So $L^2 - L - 1 = 0$, and the positive root is $L = \varphi$.

The same method gives $\sqrt{2 + \sqrt{2 + \cdots}} = 2$, from $L = \sqrt{2 + L}$.

## Explanations

### L1 human

An infinite nested radical is a square root inside a square root, again and again.
You give it a meaning by stopping after $n$ roots and letting $n$ grow.
The partial values $1, 1.414, 1.554, 1.598, \dots$ climb towards $1.618\ldots$, the golden ratio.
