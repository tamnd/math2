---
tag: YBCZ9VY7SX
kind: statement
role: theorem
name: Sharkovskii's theorem
msc: ["37E15", "37E05"]
uses: [0Q1D85B8G6, 0VGFHTM75Y, T75CZ5H47N, VFZRVZ9SD8]
about: [T75CZ5H47N]
sources:
  - url: https://en.wikipedia.org/wiki/Sharkovskii%27s_theorem
same_as:
  wikidata: Q2226855
  wikipedia: Sharkovskii's theorem
---

## Statement

Order the positive integers by the *Sharkovskii ordering* $\triangleright$:
$$3 \triangleright 5 \triangleright 7 \triangleright \cdots \triangleright 2 \cdot 3 \triangleright 2 \cdot 5 \triangleright \cdots \triangleright 2^2 \cdot 3 \triangleright 2^2 \cdot 5 \triangleright \cdots \triangleright 2^3 \triangleright 2^2 \triangleright 2 \triangleright 1.$$
First come the odd numbers greater than $1$ in increasing order, then $2$ times them, then $2^2$ times them, and so on.
At the end come the powers of $2$ in decreasing order.
Let $I \subseteq \R$ be an [[interval|0Q1D85B8G6]] and let $f \colon I \to I$ be a [[continuous map|0VGFHTM75Y]].

1. If $f$ has a [[periodic point|T75CZ5H47N]] of [[minimal period|VFZRVZ9SD8]] $m$ and $m \triangleright n$, then $f$ has a periodic point of minimal period $n$.
2. Conversely, for each integer $m \ge 1$ some continuous $f \colon \R \to \R$ has a point of minimal period $m$ but none of minimal period $k$ when $k \triangleright m$.

## Remarks

The proof of part 1 uses the intermediate value theorem in the form: if $f(J) \supseteq K$ for closed intervals $J, K$, then $J$ contains a closed interval mapped onto $K$.
The points of a periodic orbit cut the interval into pieces, and a directed graph records which pieces cover which.
Cycles in this graph give periodic points of the required periods.
Example: since $3$ is the first number in the ordering, a continuous map of an interval with a point of period $3$ has points of every period.
The hypothesis that the space is an interval is necessary: the rotation of the circle by $1/3$ has every point of period $3$ and no other periods.
For a continuous map of a compact interval, the set of minimal periods is therefore of one of two kinds.
It is either a tail $\set{k : m \trianglerighteq k}$ of the ordering for some $m$, or the set of all powers of $2$.

## Explanations

### L1 human

The theorem says that the periods of a continuous map of a line segment come in a fixed order.
If a period appears, then every period further down the list appears as well.
Period $3$ is at the top of the list, so period $3$ forces all periods.
Period $1$, a fixed point, is at the bottom: it is forced by any other period.

### L2 human

The theorem is purely one-dimensional: its proof uses the order of the real line through the intermediate value theorem, and it fails on the circle and in the plane.
It refines the Li–Yorke result that period three implies chaos.
In families like the logistic map, the passage from maps with only power-of-two periods to the others is where period doubling turns into chaos.
