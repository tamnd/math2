---
tag: FJ965C4QWA
kind: counterexample
name: Arens–Fort space
msc: [54G20, 54D55]
uses: [0CP5NDD21C, WMB2MAEDX4, 0W4CN9E2W5, 0S1FJ8VEX9, 0NSR9V8TED, 0QEAJB91GZ]
sources:
  - url: https://en.wikipedia.org/wiki/Arens%E2%80%93Fort_space
---

## Counterexample

Let $X = \N \times \N$, where $\N = \set{0, 1, 2, \dots}$, and call $\set{m} \times \N$ the $m$-th column.
Declare a set $U \subseteq X$ open if either $(0, 0) \notin U$, or $(0, 0) \in U$ and for all but finitely many $m$ the set $\set{m} \times \N \setminus U$ is finite.
This is the Arens–Fort space.
It is a countable [[Hausdorff|0S1FJ8VEX9]] and [[normal|0NSR9V8TED]] space.
The point $(0, 0)$ lies in the [[closure|0QEAJB91GZ]] of $X \setminus \set{(0, 0)}$.
But no sequence of points different from $(0, 0)$ [[converges|0W4CN9E2W5]] to $(0, 0)$.
So it is not a [[sequential space|WMB2MAEDX4]] and not [[first-countable|0CP5NDD21C]].

## Remarks

Every point other than $(0, 0)$ is isolated, and every open set containing $(0, 0)$ meets $X \setminus \set{(0, 0)}$, so $(0, 0)$ is in the closure.
Let $(p_k)$ be a sequence in $X \setminus \set{(0, 0)}$ with infinitely many distinct terms, and let $S$ be the set of its terms.
Suppose some column contains infinitely many points of $S$, and remove these points from $X$.
The rest of $X$ misses infinitely many points of only one column, so it is an open set containing $(0, 0)$.
Otherwise every column meets $S$ in a finite set, so $X \setminus S$ is an open set containing $(0, 0)$.
In both cases an open set around $(0, 0)$ misses infinitely many terms, so the sequence does not converge to $(0, 0)$.
A sequence with only finitely many distinct terms, all different from $(0, 0)$, stays outside the open set $X$ minus these terms.
Thus $X \setminus \set{(0, 0)}$ is sequentially closed but not closed.
An open set containing $(0, 0)$ is also closed, since its complement misses $(0, 0)$, and each $\set{x}$ with $x \ne (0, 0)$ is open and closed, so the space is regular.
A countable regular space is Lindelöf, and a regular Lindelöf space is normal; this gives normality.

## Explanations

### L1 human

Picture an infinite grid of points with one special corner point.
All grid points other than the corner are open on their own.
To be near the corner, a set must contain almost all of almost every column.
No sequence of grid points can be near the corner in this sense, yet the corner still touches the rest of the grid.
So sequences fail to detect closure in this space.
