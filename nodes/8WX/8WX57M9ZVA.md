---
tag: 8WX57M9ZVA
kind: example
name: Excluded point topology
msc: [54G20]
instance_of: [0CQHFPGJ45, 07SG12TQH3, 0V032VWTHD, 0TVJZYB6SH]
uses: [02BH3MCBQB, 0ZCK8DQYN1, 0NW6CH38YR, 0QEAJB91GZ, 4VSZ22TX4B]
sources:
  - url: https://en.wikipedia.org/wiki/Excluded_point_topology
same_as:
  wikidata: Q5419668
  wikipedia: Excluded point topology
---

## Example

Let $X$ be a set and let $p \in X$.
The *excluded point topology* on $X$ declares a set $U \subseteq X$ [[open|02BH3MCBQB]] if $U = X$ or $p \notin U$.
This is a topology: $\emptyset$ and $X$ are open.
A union of open sets is either $X$ or avoids $p$, and so is a finite intersection of open sets.
So $X$ is a [[topological space|0CQHFPGJ45]].

- The [[closed sets|0ZCK8DQYN1]] are $\emptyset$ and the sets that contain $p$.
- $X$ is [[compact|0TVJZYB6SH]]: the only open set that contains $p$ is $X$, so every open cover has $X$ as a member.
  Then $\set{X}$ is a finite subcover.
- $X$ is [[connected|0V032VWTHD]]: a clopen set that contains $p$ is open, hence equal to $X$.
  A clopen set that misses $p$ is closed, hence empty.
- $X$ is a [[T0 space|07SG12TQH3]]: for $x \ne p$, the open set $\set{x}$ contains $x$ but not $p$.
  For distinct $x, y \ne p$, the open set $\set{x}$ separates them.
- If $X$ has at least two points, $X$ is not a [[T1 space|0NW6CH38YR]], since every open set that contains $p$ contains all points.

The closed sets of this topology are exactly the open sets of the [[particular point topology|4VSZ22TX4B]] at $p$.

## Explanations

### L1 human

Here one point $p$ is kept out: a set is open when it avoids $p$, and the whole space is open too.
Every point other than $p$ is open by itself, so away from $p$ the space looks discrete.
The point $p$ can only be surrounded by the whole space, which is why one member of any open cover already covers the space, and the space is compact.
It is the mirror image of the particular point topology.
