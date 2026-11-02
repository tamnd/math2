---
tag: SGVQ5ZMEGE
kind: definition
name: Completely monotone function
msc: [26A48, 44A10]
defines: VJ1NCNTEHD
uses: [0V33BNKZ9S, 04TKTF8KDK]
sources:
  - url: https://en.wikipedia.org/wiki/Bernstein%27s_theorem_on_monotone_functions
---

## Definition

Let $f \colon (0, \infty) \to \R$ be [[infinitely differentiable|0V33BNKZ9S]], and let $f^{(k)}$ be its [[derivative of order $k$|04TKTF8KDK]], with $f^{(0)} = f$.
The function $f$ is *completely monotone* if
$$(-1)^k f^{(k)}(x) \ge 0$$
for every integer $k \ge 0$ and every $x > 0$.

## Remarks

Example: $f(x) = 1/x$ is completely monotone, since $f^{(k)}(x) = (-1)^k k! \, x^{-k-1}$ and so $(-1)^k f^{(k)}(x) = k! \, x^{-k-1} > 0$.
Non-example: $g(x) = e^{-x^2}$ satisfies the conditions for $k = 0$ and $k = 1$, but $g''(x) = (4 x^2 - 2) e^{-x^2} < 0$ for $0 < x < 1/\sqrt{2}$, so the condition fails for $k = 2$.
Sums, products and positive multiples of completely monotone functions are completely monotone.
The same definition is used on other open intervals; on $[0, \infty)$ one also asks that $f$ be continuous at $0$.
The function $f$ is completely monotone on $(0, \infty)$ if and only if $x \mapsto f(-x)$ is [[absolutely monotonic|QQSPWH4NG9]] on $(-\infty, 0)$.
