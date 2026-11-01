---
tag: MJDV3PFBRT
kind: definition
name: I-adic topology
msc: [13J10, 13B35]
defines: 2VF2TSJ3PY
uses: [0310REJJY8, 096Z9MP2ME, 0NZ8JA25WK, 0CQHFPGJ45]
sources:
  - url: https://en.wikipedia.org/wiki/I-adic_topology
---

## Definition

Let $R$ be a [[commutative ring|0310REJJY8]], let $I$ be an [[ideal|096Z9MP2ME]] of $R$, and let $M$ be an $R$-[[module|0NZ8JA25WK]].
The *$I$-adic topology* on $M$ is the following [[topology|0CQHFPGJ45]].
A subset $U \subseteq M$ is open if and only if for every $x \in U$ there is $n \ge 0$ with $x + I^n M \subseteq U$.
The $I$-adic topology on $R$ is the case $M = R$.

## Remarks

The cosets $x + I^n M$, for $x \in M$ and $n \ge 0$, form a base of this topology; each of them is open and also closed.
Addition on $M$ and multiplication $R \times M \to M$ are continuous, so $R$ becomes a topological ring and $M$ a topological module.
The topology is Hausdorff if and only if $\bigcap_n I^n M = 0$; then $d(x, y) = 2^{-\nu(x - y)}$, with $\nu(z)$ the largest $n$ such that $z \in I^n M$ and $\nu(0) = \infty$, is a metric for it.
Example: on $\Z$ with $I = (2)$, the sequence $2^n$ tends to $0$, since $2^m \in 2^n \Z$ for all $m \ge n$.
Non-example: the set $\set{0}$ is not open in $\Z$ for this topology, since no $2^n \Z$ is contained in $\set{0}$.
So the $2$-adic topology on $\Z$ is not discrete, unlike the topology that $\Z$ gets from $\R$.
