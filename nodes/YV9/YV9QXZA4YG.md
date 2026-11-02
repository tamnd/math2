---
tag: YV9QXZA4YG
kind: definition
name: Quasi-everywhere
msc: [31B15, 31A15, 31C15]
defines: 1X1WCNDA0J
uses: [W9N1TR1X8P]
sources:
  - url: https://en.wikipedia.org/wiki/Capacity_of_a_set
---

## Definition

Let $n \ge 2$, let $A \subseteq \R^n$, and let $P$ be a property that each point of $A$ may or may not have.
The property $P$ holds *quasi-everywhere* on $A$, abbreviated q.e., if the set of points of $A$ where $P$ fails has [[capacity zero|W9N1TR1X8P]].

## Remarks

Example: let $K$ be the closed unit disc in $\C$ and let $u(z) = \log \abs{z}$.
Then $u > -\infty$ quasi-everywhere on $K$, since the exceptional set $\set{0}$ is finite and so has capacity zero.

Non-example: let $u$ be the function on $\C$ with $u = 1$ on the segment $[0, 1]$ and $u = 0$ elsewhere.
Then $u = 0$ almost everywhere with respect to area, but not quasi-everywhere, because the segment has positive logarithmic capacity.

In $\R^n$ with $n \ge 3$ the capacity used is the Newtonian capacity, and in the plane it is the logarithmic capacity.
In nonlinear potential theory one speaks of $p$-quasi-everywhere, with the $p$-capacity in place of the Newtonian capacity.
