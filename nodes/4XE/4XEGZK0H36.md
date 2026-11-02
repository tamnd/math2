---
tag: 4XEGZK0H36
kind: definition
name: Stieltjes function
msc: [26A48, 28A12, 26A42]
defines: WPR0NVC9PC
uses: [0A7KV2WB7A, 08J2M1JYAG]
sources:
  - url: https://en.wikipedia.org/wiki/Lebesgue%E2%80%93Stieltjes_integration
---

## Definition

A *Stieltjes function* is a function $F \colon \R \to \R$ such that:

1. $F$ is non-decreasing, that is, $F(x) \le F(y)$ whenever $x \le y$; see [[monotone function|0A7KV2WB7A]].
2. $F$ is right-continuous, that is, $F(x) = \lim_{y \to x^+} F(y)$ for every $x \in \R$.

## Remarks

Example: the floor function $F(x) = \floor{x}$ is a Stieltjes function.
It is non-decreasing, and on each interval $[n, n + 1)$ with $n \in \Z$ it is constant, so it is right-continuous at every point.
Its [[Lebesgue–Stieltjes measure|QV75XJBFCS]] puts mass $1$ at each integer.

Non-example: the ceiling function $F(x) = \ceil{x}$ is non-decreasing but is not right-continuous at the integers.
At $x = 0$ one has $F(0) = 0$, while $F(y) = 1$ for all $y \in (0, 1)$, so the limit from the right is $1 \ne F(0)$.

Every non-decreasing function has one-sided limits at every point, so right-continuity only fixes the value at the countably many jumps.
Two Stieltjes functions give the same measure exactly when they differ by a constant.
Some authors write "distribution function" for the same notion.
