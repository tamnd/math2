---
tag: 2YYCNFPX1F
kind: definition
name: Singular function
msc: [26A30]
defines: P5AWRD2793
uses: [0P27W9RW0G, 0F1WR9C83K]
sources:
  - url: https://en.wikipedia.org/wiki/Singular_function
---

## Definition

Let $a < b$ be real numbers and let $f \colon [a, b] \to \R$ be a function.
The function $f$ is *singular* if:

1. $f$ is [[continuous|0P27W9RW0G]] on $[a, b]$;
2. there is a set $N \subseteq [a, b]$ of Lebesgue measure $0$ such that for every $x \in [a, b] \setminus N$ the [[derivative|0F1WR9C83K]] $f'(x)$ exists and $f'(x) = 0$;
3. $f$ is not constant on $[a, b]$.

## Remarks

Example: the [[Cantor function|NPBYYK63FE]] $c$ on $[0, 1]$ is singular.
It is continuous, it is constant on each open interval removed in the construction of the Cantor set, so $c' = 0$ off the Cantor set, which has measure $0$, and $c(0) = 0 \ne 1 = c(1)$.

Non-example: the step function equal to $0$ on $[0, \frac12)$ and $1$ on $[\frac12, 1]$ satisfies clauses 2 and 3 but fails clause 1.

Conventions vary: some authors drop continuity, and some allow constants.
A singular function is never [[absolutely continuous|ZT6F4C2YHK]], since an absolutely continuous function with derivative $0$ almost everywhere is constant.
