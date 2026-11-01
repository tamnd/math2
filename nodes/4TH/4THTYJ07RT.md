---
tag: 4THTYJ07RT
kind: definition
name: Limit point compact space
msc: [54D30]
defines: E8XKSQY76M
uses: [0CQHFPGJ45, 0E3X7TXS67, S3N3CHZV89, 0TVJZYB6SH, 0NW6CH38YR, 0VKD1TP7F3]
sources:
  - url: https://en.wikipedia.org/wiki/Limit_point_compact
---

## Definition

A [[topological space|0CQHFPGJ45]] $X$ is *limit point compact* when every infinite subset $A \subseteq X$ has a [[limit point|0E3X7TXS67]] in $X$.
Here $x \in X$ is a limit point of $A$ when every neighbourhood of $x$ contains a point of $A$ other than $x$.

## Remarks

Every [[compact|0TVJZYB6SH]] space is limit point compact, and so is every [[countably compact|S3N3CHZV89]] space.
For [[T1 spaces|0NW6CH38YR]], limit point compactness is equivalent to countable compactness.
For [[metric spaces|0VKD1TP7F3]], it is equivalent to compactness and to sequential compactness.
Other names in use are weakly countably compact and Fréchet compact.

Example: $[0, 1]$ is limit point compact.
An infinite subset contains a sequence of distinct points, which has a convergent subsequence by the Bolzano–Weierstrass theorem, and its limit is a limit point of the set.

Non-example: $\R$ is not limit point compact.
The infinite set $\Z$ has no limit point, since each $x \in \R$ has a neighbourhood $(x - 1/2, x + 1/2)$ that contains at most one integer.

Without the T1 condition, limit point compact need not imply countably compact.
Let $X = \N \times \set{0, 1}$, where $\N$ is discrete and $\set{0, 1}$ has the trivial topology.
Each nonempty subset has a limit point, since $(n, 1 - i)$ is a limit point of any set that contains $(n, i)$.
But the countable open cover by the sets $\set{n} \times \set{0, 1}$ has no finite subcover.
