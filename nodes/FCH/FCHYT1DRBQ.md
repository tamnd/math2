---
tag: FCHYT1DRBQ
kind: example
name: A parameter squared gives a half-line, not a line
msc: ["51N20", "97G70"]
topics: [VKVAJ94SKZ]
audience: school
not_instance_of:
  - target: 0399QFDFS8
    note: the set of the points a + t^2 d is a half-line, because t^2 takes no negative values
uses: [0399QFDFS8]
sources:
  - url: https://en.wikipedia.org/wiki/Line_(geometry)
    locator: Ray
---

## Example

Let $a = (1, 0, 0)$ and $d = (0, 1, 1)$, and let $S = \{\, a + t^2 d : t \in \mathbb{R} \,\}$.
The formula looks like the [[vector equation of a line|0399QFDFS8]], but $S$ is not a line.

1. For each $t$, the number $u = t^2$ is $\geq 0$, and each $u \geq 0$ is $t^2$ for $t = \sqrt{u}$.
2. So $S = \{\, a + u d : u \geq 0 \,\}$.
3. The point $a - d = (1, -1, -1)$ is on the line $a + u d$, at $u = -1$.
4. It is not in $S$: the second coordinate of $a + t^2 d$ is $t^2 \geq 0$, and $-1 < 0$.
5. So $S$ is only a half-line, the ray from $a$ in the direction $d$.

## Remarks

The set $\{a + t^3 d\}$ is the whole line, since $t \mapsto t^3$ takes every real value.
The set $\{a + (\sin t) d\}$ is the segment from $a - d$ to $a + d$.
A curve is a line only if its parameter runs through all of $\mathbb{R}$ along a fixed direction.

## Explanations

### L1 human

The square $t^2$ is never negative.
So the point $a + t^2 d$ can only move forward from $a$, never backward.
It covers half of the line, a ray.

### L2 human

For a line, the coefficient of $d$ must take every real value.
The map $t \mapsto t^2$ misses the negative numbers, so the backward half is missing.
A trap: the formula $a + f(t) d$ always stays on the line through $a$ in the direction $d$, but it covers the whole line only if $f$ is onto $\mathbb{R}$.
