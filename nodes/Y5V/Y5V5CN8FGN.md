---
tag: Y5V5CN8FGN
kind: definition
name: Semi-continuity
msc: [26A15, 54C08]
defines: 95BSKT0S6M
uses: [0CNQXVBHCX, 01T3TMGTTE, 0GSZ7B0CGR, 0P27W9RW0G, 0P8BA7T7S5, 0H4R3RESGV, 0VSB0XF4G7]
sources:
  - url: https://en.wikipedia.org/wiki/Semi-continuity
    locator: Definitions
---

## Definition

Let $X$ be a [[topological space|0CNQXVBHCX]], let $f \colon X \to [-\infty, \infty]$ be a function to the [[extended real line|0GSZ7B0CGR]], and let $x_0 \in X$.

1. The function $f$ is *upper semicontinuous at* $x_0$ if for each real $y > f(x_0)$ there is a [[neighbourhood|01T3TMGTTE]] $U$ of $x_0$ with $f(x) < y$ for all $x \in U$.
2. The function $f$ is *lower semicontinuous at* $x_0$ if for each real $y < f(x_0)$ there is a neighbourhood $U$ of $x_0$ with $f(x) > y$ for all $x \in U$.
3. The function $f$ is *upper* (or *lower*) *semicontinuous* if it is upper (or lower) semicontinuous at each point of $X$.

## Remarks

For $X \subseteq \R$, upper semicontinuity at $x_0$ means $\limsup_{x \to x_0} f(x) \le f(x_0)$, and lower semicontinuity means $\liminf_{x \to x_0} f(x) \ge f(x_0)$.
The function $f$ is upper semicontinuous if and only if the set $\set{x \in X : f(x) < y}$ is open for each real $y$.
It is lower semicontinuous if and only if $\set{x \in X : f(x) > y}$ is open for each real $y$.
The function $f$ is upper semicontinuous if and only if $-f$ is lower semicontinuous.
A real function is [[continuous|0P27W9RW0G]] at $x_0$ if and only if it is both upper and lower semicontinuous at $x_0$.

Example: the [[indicator function|0VSB0XF4G7]] $f = \mathbf 1_{[0, 1]}$ on $\R$ is upper semicontinuous.
The set $\set{f < y}$ is empty for $y \le 0$, is $\R \setminus [0, 1]$ for $0 < y \le 1$, and is $\R$ for $y > 1$, and each of these is open.

Non-example: the same function is not lower semicontinuous at $0$.
Take $y = 1/2 < 1 = f(0)$; each neighbourhood of $0$ contains a point $x < 0$ with $f(x) = 0 < y$.
