---
tag: G38B7E4ESW
kind: statement
role: theorem
name: Nagell–Lutz theorem
msc: [11G05, 14H52]
uses: [427N6S6QQW, P7V1BQJPSS, 0WE2NHZJ7B, 0NCJ5WXN6Z]
about: [427N6S6QQW]
sources:
  - url: https://en.wikipedia.org/wiki/Nagell%E2%80%93Lutz_theorem
same_as:
  wikidata: Q3527132
  wikipedia: Nagell–Lutz theorem
---

## Statement

Let $a, b \in \Z$ with $D = 4a^3 + 27b^2 \ne 0$, and let $E$ be the [[elliptic curve|427N6S6QQW]] $y^2 = x^3 + ax + b$ over $\Q$.
Let $P = (x, y) \in E(\Q)$ be a point of finite [[order|0WE2NHZJ7B]] in the [[group of rational points|P7V1BQJPSS]], with $P \ne O$.
Then $x$ and $y$ are integers, and either $y = 0$ or $y^2$ divides $D$.

## Remarks

The integrality comes from a study of the denominators of points in the $p$-adic filtration: points whose coordinates have $p$ in the denominator form a torsion-free subgroup.
Divisibility follows next: if $P$ has finite order, so does $2P$, and both have integer coordinates; the duplication formula then forces $y^2 \mid D$.
The theorem gives an algorithm for the torsion subgroup: list the finitely many candidates and test each for finite order.
Example: on $y^2 = x^3 + 1$ one has $D = 27$, so a torsion point with $y \ne 0$ has $y \in \set{\pm 1, \pm 3}$.
This gives the points $(0, \pm 1)$ and $(2, \pm 3)$.
With $(-1, 0)$ and $O$ they form a cyclic group of order $6$.
The converse fails: on $y^2 = x^3 + 2$ the point $(-1, 1)$ has integer coordinates and $1 \mid 108$, but it has infinite order.
The hypothesis that $a$ and $b$ are integers is needed; any curve can be scaled to this form by $(x, y) \mapsto (u^2 x, u^3 y)$.

## Explanations

### L1 human

A rational point of finite order on such a curve is very special.
Its coordinates are whole numbers, and the $y$-coordinate is zero or has a square that divides a fixed number.
So the points of finite order can be found by a finite search.

### L2 human

The theorem was found independently by Nagell and Lutz in the 1930s.
It is the standard tool, together with reduction modulo good primes, to compute the torsion subgroup $T$ of $E(\Q)$ in [[Mordell's theorem|BZHGKN6Q3K]].
[[Mazur's torsion theorem|RQS6YHAR8N]] then lists all groups that can occur.
