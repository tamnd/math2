---
tag: 93VXAB8JYS
kind: statement
role: theorem
name: Period three implies chaos
msc: ["37E05", 37D45]
uses: [0Q1D85B8G6, 0VGFHTM75Y, T75CZ5H47N, YBCZ9VY7SX]
about: [T75CZ5H47N]
sources:
  - url: https://en.wikipedia.org/wiki/Sharkovskii%27s_theorem
---

## Statement

Let $J \subseteq \R$ be an [[interval|0Q1D85B8G6]] and let $F \colon J \to J$ be a [[continuous map|0VGFHTM75Y]].
Suppose there is a point $a \in J$ such that $b = F(a)$, $c = F^2(a)$ and $d = F^3(a)$ satisfy $d \le a < b < c$ or $d \ge a > b > c$.
Then:

1. For every integer $k \ge 1$ there is a [[periodic point|T75CZ5H47N]] in $J$ of minimal period $k$.
2. There is an uncountable set $S \subseteq J$ that contains no periodic point and satisfies:
   - for all $p, q \in S$ with $p \neq q$, $\limsup_{n \to \infty} \abs{F^n(p) - F^n(q)} > 0$ and $\liminf_{n \to \infty} \abs{F^n(p) - F^n(q)} = 0$;
   - for every $p \in S$ and every periodic point $q \in J$, $\limsup_{n \to \infty} \abs{F^n(p) - F^n(q)} > 0$.

## Remarks

This is the theorem of Li and Yorke, from their paper "Period three implies chaos".
A point of minimal period $3$ satisfies the hypothesis after a suitable choice of $a$ on its orbit: one of the three points can serve as $a$, and then $d = a$.
The proof of part 1 uses a covering form of the intermediate value theorem.
If $F(K) \supseteq L$ for compact intervals $K, L$, then $K$ contains a compact interval mapped onto $L$, and chains of such intervals give periodic points.
Part 1 is also a special case of [[Sharkovskii's theorem|YBCZ9VY7SX]], since $3$ is first in the Sharkovskii ordering.
Example: the logistic map $F(x) = 4x(1 - x)$ on $[0, 1]$ has the period-$3$ orbit of $\sin^2(\pi/7)$, $\sin^2(2\pi/7)$, $\sin^2(4\pi/7)$, so it has points of all periods.
The interval hypothesis is necessary: the rotation of a circle by one third has period $3$ points but no fixed point.

## Explanations

### L1 human

For a continuous map of a segment of the line, one orbit of period three is enough to produce orbits of every period.
It also produces an uncountable set of orbits that wander forever without settling, coming close to each other and moving apart again and again.
The title of the paper of Li and Yorke made "chaos" a common word in mathematics.

### L2 human

The result gives an easy test for complicated dynamics in one-dimensional maps: find one point with the stated order pattern.
The set $S$ is called a scrambled set, and maps with an uncountable scrambled set are called chaotic in the sense of Li and Yorke.
The theorem says nothing about how large $S$ is in measure; for some maps with period three, almost every orbit tends to a stable periodic orbit.
