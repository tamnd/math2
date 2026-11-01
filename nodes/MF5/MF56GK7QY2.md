---
tag: MF56GK7QY2
kind: statement
role: theorem
name: Nested intervals theorem
msc: [26A03]
uses: [0TK8Y3J5RW, 0AXWET80YW, 0BTMQ04556, 0EZBG8SKJM, E3CPZNJZNG]
about: [08J2M1JYAG]
sources:
  - url: https://en.wikipedia.org/wiki/Nested_intervals
---

## Statement

For each $n \ge 1$, let $a_n \le b_n$ be real numbers and let $I_n = [a_n, b_n]$ be the closed [[interval|0TK8Y3J5RW]].
Assume that $I_{n+1} \subseteq I_n$ for all $n \ge 1$.
Then the intersection $\bigcap_{n \ge 1} I_n$ is not empty.
If moreover $b_n - a_n \to 0$, then the intersection consists of exactly one point.

## Remarks

The left endpoints $a_n$ increase and are bounded above by $b_1$.
By the [[completeness axiom|0AXWET80YW]], they have a [[supremum|0BTMQ04556]] $s$.
Each $b_m$ is an upper bound of all $a_n$, so $a_n \le s \le b_m$ for all $n$ and $m$, and $s$ lies in every $I_n$.
If two points $s < t$ lie in every $I_n$, then $b_n - a_n \ge t - s > 0$ for all $n$, so the lengths cannot tend to $0$.

Each hypothesis is needed.
The open intervals $(0, 1/n)$ are nested and nonempty, but no real number lies in all of them.
The closed unbounded sets $[n, \infty)$ are nested, but their intersection is empty.
Over $\Q$, the intervals $\{q \in \Q : a_n \le q \le b_n\}$ with $a_n, b_n$ the decimal approximations of $\sqrt 2$ from below and above have empty intersection.

The theorem is the case $X = \R$ of [[Cantor's intersection theorem|0EZBG8SKJM]].

## Explanations

### L1 human

Take a closed interval, then a smaller closed interval inside it, then a smaller one inside that, and so on forever.
Some point stays inside all of them.
If the lengths shrink to zero, the intervals close in on a single point.
For example, the intervals $[0, 1/n]$ all contain $0$, and $0$ is the only common point.

### L2 human

The theorem is one form of the [[completeness of the real numbers|E3CPZNJZNG]], and in an Archimedean ordered field it is equivalent to the least-upper-bound property.
It drives bisection proofs: halve an interval, keep a half with a desired property, and repeat.
This is how one proves the Bolzano–Weierstrass theorem and the intermediate value theorem, and how Cantor showed that $\R$ is uncountable.
