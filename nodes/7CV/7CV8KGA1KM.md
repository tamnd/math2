---
tag: 7CV8KGA1KM
kind: definition
name: Semimodular lattice
msc: [06C10, 06B05]
defines: C1NET23GG0
uses: [WH4SFAACAS, J2T75ATRV5, 4HHDPZ4BDY]
sources:
  - url: https://en.wikipedia.org/wiki/Semimodular_lattice
---

## Definition

Let $L$ be a [[lattice|WH4SFAACAS]] with [[join and meet|J2T75ATRV5]] $\vee$ and $\wedge$.
Write $x \lessdot y$ when $y$ [[covers|4HHDPZ4BDY]] $x$, that is, $x < y$ and no $z \in L$ satisfies $x < z < y$.
The lattice $L$ is *semimodular*, or *upper semimodular*, if for all $a, b \in L$,
$$a \wedge b \lessdot a \implies b \lessdot a \vee b.$$
Dually, $L$ is *lower semimodular* if $b \lessdot a \vee b$ implies $a \wedge b \lessdot a$ for all $a, b \in L$.

## Remarks

Every [[modular lattice|QX7WZ92QAK]] is both upper and lower semimodular, because in a modular lattice the intervals $[a \wedge b, a]$ and $[b, a \vee b]$ are isomorphic.

Example: the [[lattice of partitions|9RP82GD0Q4]] of a finite set, ordered by refinement with the coarser partition above, is upper semimodular.
If a partition $a$ covers $a \wedge b$, then $a$ arises from $a \wedge b$ by merging two blocks.
Then $a \vee b$ arises from $b$ by merging the two blocks of $b$ that contain these two blocks.
These blocks of $b$ are different, since otherwise $a \le b$ and $a = a \wedge b$; so $b \lessdot a \vee b$.
For a set of $4$ or more elements, this lattice is not modular.

Non-example: the [[pentagon lattice N5|DHC8TZXGYS]] with $0 < a < c < 1$ and $b$ incomparable to $a$ and $c$.
Apply the condition to the pair $(b, a)$: $b \wedge a = 0$ and $0 \lessdot b$, but $a < c < 1 = a \vee b$, so $a \lessdot a \vee b$ fails.

For a finite lattice, upper semimodularity holds if and only if the lattice is graded with a rank function $r$ satisfying $r(a) + r(b) \ge r(a \wedge b) + r(a \vee b)$ for all $a, b$.
