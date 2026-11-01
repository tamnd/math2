---
tag: V0E14B3DWD
kind: definition
name: Radical ideal
msc: [13A15]
defines: S4GQN5V54X
uses: [0GYGHKX834, 0MYSA6MYNA, 437YRCNYRJ]
sources:
  - url: https://en.wikipedia.org/wiki/Radical_of_an_ideal
---

## Definition

Let $R$ be a [[commutative ring|0GYGHKX834]].
An [[ideal|0MYSA6MYNA]] $I$ of $R$ is a *radical ideal* if $I = \sqrt{I}$, where $\sqrt{I}$ is the [[radical|437YRCNYRJ]] of $I$.
Equivalently, for all $r \in R$ and all integers $n \ge 1$, if $r^n \in I$ then $r \in I$.

## Remarks

Example: $6\Z$ is a radical ideal of $\Z$; if $6$ divides $r^n$, then $2$ and $3$ divide $r$, so $6$ divides $r$.
Non-example: $12\Z$ is not radical, since $6^2 \in 12\Z$ and $6 \notin 12\Z$.
Every [[prime ideal|06HC6HK0Z8]] is radical: if $r^n \in P$, primality applied $n - 1$ times gives $r \in P$.
The ideal $I$ is radical if and only if the [[quotient ring|0VFW4Y69BT]] $R/I$ is [[reduced|SZHY975FFX]].
The radical $\sqrt{J}$ of any ideal $J$ is a radical ideal.
