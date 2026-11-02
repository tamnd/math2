---
tag: N6AFVYBY2Z
kind: definition
name: Rounding
msc: [65G50, 65Y04]
defines: 5NPVX29Y0C
uses: [08GR54CKEA, 0C4JS9RF5M]
sources:
  - url: https://en.wikipedia.org/wiki/Rounding
---

## Definition

Let $F \subseteq \R$ be unbounded above and below, with only finitely many elements in each bounded interval.
An example is the set $\Z$ of [[integers|0C4JS9RF5M]].
For $x \in \R$ let $x^- = \max \set{f \in F : f \le x}$ and $x^+ = \min \set{f \in F : f \ge x}$.
A *rounding* to $F$ is a map $\mathrm{rd} \colon \R \to F$ with $\mathrm{rd}(x) \in \set{x^-, x^+}$ for every $x$.
The standard roundings are:

1. *rounding down*: $\mathrm{rd}(x) = x^-$;
2. *rounding up*: $\mathrm{rd}(x) = x^+$;
3. *rounding toward zero*: $\mathrm{rd}(x) = x^-$ if $x \ge 0$ and $x^+$ if $x < 0$;
4. *rounding to nearest*: $\mathrm{rd}(x)$ is the element of $\set{x^-, x^+}$ closest to $x$. When $x$ is exactly halfway, a tie rule decides, such as *ties to even* or *ties away from zero*.

## Remarks

Example: for $F = \Z$, rounding down is the [[floor function|08GR54CKEA]], rounding up is the ceiling function, and rounding to nearest with ties to even sends $2.5 \mapsto 2$, $3.5 \mapsto 4$ and $2.7 \mapsto 3$.
Check for $2.7$: $x^- = 2$, $x^+ = 3$, and $\abs{2.7 - 3} = 0.3 < 0.7 = \abs{2.7 - 2}$.
Non-example: the map $x \mapsto \floor{x} - 1$ is not a rounding to $\Z$, since $\floor{2.7} - 1 = 1 \notin \set{2, 3}$.
Each of the four standard roundings is monotone: $x \le y$ implies $\mathrm{rd}(x) \le \mathrm{rd}(y)$.
An arbitrary rounding need not be monotone, since it may choose $x^+$ for one point and $x^-$ for a larger point of the same gap.
For floating-point numbers, $F$ is extended by the subnormal numbers and by $\pm \infty$ to cover overflow.
