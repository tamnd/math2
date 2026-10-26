---
tag: ~cbcbda41
kind: definition
name: One-sided derivative
aliases: [left-derivative, right-derivative]
msc: [26A24]
defines: ~ff30e2e9
uses: [~9c0b2396, ~963e8644]
sources:
  - url: https://en.wikipedia.org/wiki/Semi-differentiability
    locator: Definitions
---

## Definition

Let $f$ be a real function defined on an interval $[a, a + r)$ with $r > 0$.
The right derivative of $f$ at $a$ is the [[one-sided limit|~963e8644]]
$$f'_+(a) = \lim_{h \to 0^+} \frac{f(a + h) - f(a)}{h},$$
when it exists.
The left derivative $f'_-(a)$ is defined in the same way, for $f$ on $(a - r, a]$ and $h \to 0^-$.

## Remarks

A function on an open interval is differentiable at $a$ if and only if both one-sided derivatives exist and are equal. Their common value is the [[derivative|~9c0b2396]].
One-sided derivatives give a meaning to derivatives at the endpoints of a closed interval.
For $|x|$ at $0$, the right derivative is $1$ and the left derivative is $-1$.
Mathlib expresses them with `HasDerivWithinAt` on a half line.

## Explanations

### L1 human

A one-sided derivative only looks at one side of the point.
At a corner of a graph, the slopes from the left and from the right exist but differ.
