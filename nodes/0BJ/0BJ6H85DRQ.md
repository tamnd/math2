---
tag: 0BJ6H85DRQ
kind: concept
name: Limit along different paths
aliases: [two-path-test]
msc: [26B05]
uses: [0J8Y1NCY0K, 0G7WM8DX4P]
sources:
  - url: https://en.wikipedia.org/wiki/Limit_of_a_function
    locator: Functions of more than one variable
---

## Summary

Let $f$ be a function on $D \subseteq \mathbb{R}^n$ and let $a$ be a limit point of $D$.
Let $\gamma \colon (0, 1] \to D$ be a path, for example a [[curve|0G7WM8DX4P]], with $\gamma(t) \ne a$ for each $t$ and $\gamma(t) \to a$ as $t \to 0^+$.
If $\lim_{x \to a} f(x) = L$, then $\lim_{t \to 0^+} f(\gamma(t)) = L$.
So if two such paths give different limits, or one path gives no limit, then the [[limit|0J8Y1NCY0K]] of $f$ at $a$ does not exist.

## Remarks

For $f(x, y) = xy / (x^2 + y^2)$ on $\mathbb{R}^2 \setminus \{(0, 0)\}$, the path $y = m x$ gives the limit $m / (1 + m^2)$ at the origin. This depends on $m$, so $f$ has no limit at $(0, 0)$.
Equal limits along all straight lines do not prove that the limit exists. For $f(x, y) = x^2 y / (x^4 + y^2)$, each line through the origin gives the limit $0$, but the parabola $y = x^2$ gives $1/2$.

## Explanations

### L1 human

In one variable you can approach a point only from the left or from the right.
In the plane you can approach a point along infinitely many routes: lines, parabolas, spirals.
A limit must give the same answer for every route, so one route that disagrees is enough to show that there is no limit.
