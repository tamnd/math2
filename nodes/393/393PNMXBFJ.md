---
tag: 393PNMXBFJ
kind: definition
name: Quasiconvex function
msc: [26B25, 26A51, 90C26]
defines: S4RMH7JQB8
uses: [05EGHEQZAW, 0K06X9QXDX, 0Y5Q8Q9WJ7]
sources:
  - url: https://en.wikipedia.org/wiki/Quasiconvex_function
---

## Definition

Let $V$ be a real [[vector space|05EGHEQZAW]], let $S \subseteq V$ be a [[convex set|0K06X9QXDX]], and let $f \colon S \to \R$ be a function.
The function $f$ is *quasiconvex* if
$$f(t x + (1 - t) y) \le \max\set{f(x), f(y)}$$
for all $x, y \in S$ and all $t \in [0, 1]$.

## Remarks

Equivalently, for each $a \in \R$ the sublevel set $\set{x \in S : f(x) \le a}$ is convex; compare [[level sets|0Y5Q8Q9WJ7]].
The function $f$ is *quasiconcave* if $-f$ is quasiconvex.
A [[convex function|0M1GJSWZDA]] is quasiconvex, because $t f(x) + (1 - t) f(y) \le \max\set{f(x), f(y)}$.

Example: $f(x) = \sqrt{\abs{x}}$ on $\R$.
Its sublevel sets are $\emptyset$ for $a < 0$ and $[-a^2, a^2]$ for $a \ge 0$, all convex.
It is not convex, since $f(1/2) = \sqrt{1/2} > 1/2 = \frac{1}{2} f(0) + \frac{1}{2} f(1)$.

Non-example: $f(x) = -x^2$ on $\R$.
With $x = -1$, $y = 1$ and $t = 1/2$, one gets $f(0) = 0 > -1 = \max\set{f(-1), f(1)}$.
