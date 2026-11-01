---
tag: 4VSZ22TX4B
kind: example
name: Particular point topology
msc: [54G20]
instance_of: [0CQHFPGJ45, 07SG12TQH3, 0V032VWTHD]
uses: [02BH3MCBQB, 0NW6CH38YR, 0BSJSX7ME2, 0TVJZYB6SH, 0QEAJB91GZ]
sources:
  - url: https://en.wikipedia.org/wiki/Particular_point_topology
same_as:
  wikidata: Q7140510
  wikipedia: Particular point topology
---

## Example

Let $X$ be a set and let $p \in X$.
The *particular point topology* on $X$ declares a set $U \subseteq X$ [[open|02BH3MCBQB]] if $U = \emptyset$ or $p \in U$.
This is a topology: $\emptyset$ and $X$ are open.
A union of sets that contain $p$ contains $p$, and so does a finite intersection of them.
So $X$ is a [[topological space|0CQHFPGJ45]].

- $X$ is a [[T0 space|07SG12TQH3]]: let $x \ne y$, and name them so that $x \ne p$.
  Then $\set{p, y}$ is open, contains $y$, and does not contain $x$.
- If $X$ has at least two points, $X$ is not a [[T1 space|0NW6CH38YR]]: every open set that contains a point $x \ne p$ also contains $p$.
- $X$ is [[connected|0V032VWTHD]]: any two nonempty open sets meet at $p$, so $X$ is not a union of two disjoint nonempty open sets.
- The set $\set{p}$ is [[dense|0BSJSX7ME2]], since every nonempty open set contains $p$.
- $X$ is [[compact|0TVJZYB6SH]] if and only if $X$ is finite.
  Indeed, the open sets $\set{p, x}$ for $x \in X$ cover $X$, and a finite subcover exists only when $X$ is finite.

## Explanations

### L1 human

In this topology one point $p$ is special: a nonempty set is open exactly when it contains $p$.
So $p$ is "close" to every other point, and every small open set around any point must reach $p$.
This makes the space connected and lets the single point $p$ be dense.
It is a standard source of counterexamples in general topology.
