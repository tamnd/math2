---
tag: ZDNBCXDGTA
kind: definition
name: Continuous lattice
msc: [06B35, 06B23]
defines: RXBD58SGXZ
uses: [D7A0ZGZT5S, RDM7J5J9HQ, 0R3H5PANRQ, 3J0BTXSCVN]
sources:
  - url: https://en.wikipedia.org/wiki/Continuous_poset
---

## Definition

Let $L$ be a [[complete lattice|D7A0ZGZT5S]], and let $\ll$ be the [[way-below relation|RDM7J5J9HQ]] on $L$.
The lattice $L$ is *continuous* if every $y \in L$ satisfies
$$y = \bigvee \set{x \in L : x \ll y},$$
where $\bigvee$ denotes the [[supremum|0R3H5PANRQ]].

## Remarks

Since $x \ll y$ implies $x \le y$, the condition says that $y$ is not larger than the supremum of the elements way below it.
Example: $L = [0, 1]$ with the usual order, where $x \ll y$ if and only if $x = 0$ or $x < y$.
For $y > 0$ the supremum of $[0, y)$ is $y$, and for $y = 0$ the set $\set{0}$ has supremum $0$.
Example: every [[algebraic lattice|3J0BTXSCVN]] is continuous, because each compact $c \le y$ satisfies $c \ll y$.
Non-example: the lattice of closed subsets of $[0, 1]$ under inclusion is complete.
But $\varnothing$ is the only element way below $[0, 1]$, so $[0, 1]$ is not the supremum of the elements way below it.
A complete lattice is continuous if and only if $\bigwedge_{j \in J} \bigvee D_j = \bigvee_{f} \bigwedge_{j \in J} f(j)$ for every family $(D_j)_{j \in J}$ of directed subsets, where $f$ runs over the choice functions with $f(j) \in D_j$.
