---
tag: 0RYTGBJAGN
kind: definition
name: Big O notation
aliases: [landau-big-o]
msc: [41A60]
defines: 0TGV80E6A4
sources:
  - url: https://en.wikipedia.org/wiki/Big_O_notation
    locator: Formal definition
---

## Definition

Let $f$ and $g$ be real functions defined on an interval $[x_0, \infty)$.
The notation $f(x) = O(g(x))$ as $x \to \infty$ means that there are real numbers $C > 0$ and $x_1 \ge x_0$ with
$$|f(x)| \le C |g(x)| \quad \text{for all } x \ge x_1.$$

## Remarks

The same definition works as $x \to a$, with $|x - a| < \delta$ in place of $x \ge x_1$.
If $g(x) \ne 0$ for large $x$, then $f = O(g)$ means that $f/g$ is bounded for large $x$.
For example, $3x^2 + 5x = O(x^2)$ as $x \to \infty$.
Mathlib defines it for filters, as `Asymptotics.IsBigO`.

## Explanations

### L1 human

The statement $f = O(g)$ says that $f$ grows at most as fast as $g$, up to a constant factor.
It ignores constant factors and small values of $x$.
