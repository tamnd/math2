---
tag: GWZN3EKEWD
kind: statement
role: theorem
name: Stallings theorem about ends of groups
msc: [20F65, "20E06", "20E08"]
uses: [082DWWXMRJ, 0GYQK9NDJF, 0X1JXT47GA, YEYERRY37K]
about: [082DWWXMRJ, YEYERRY37K]
sources:
  - url: https://en.wikipedia.org/wiki/Stallings_theorem_about_ends_of_groups
same_as:
  wikidata: Q7597316
  wikipedia: Stallings theorem about ends of groups
---

## Statement

Let $G$ be a [[finitely generated group|082DWWXMRJ]] and let $\Gamma$ be its [[Cayley graph|0GYQK9NDJF]] for a finite generating set.
For a finite set $K$ of vertices and edges of $\Gamma$, count the infinite connected components of $\Gamma \setminus K$.
The number of ends $e(G)$ is the supremum of this count over all such $K$.
It does not depend on the generating set.
Then $e(G) > 1$ if and only if one of the following holds:

1. $G$ is an amalgamated free product $A *_C B$ with $C$ finite, $C \neq A$ and $C \neq B$.
2. $G$ is an [[HNN extension|YEYERRY37K]] $A *_C$ with $C$ a finite [[subgroup|0X1JXT47GA]] of $A$.

## Remarks

The number of ends of a finitely generated group is always $0$, $1$, $2$ or $\infty$.
It is $0$ exactly for finite groups and $2$ exactly for infinite groups with an infinite cyclic subgroup of finite index.

The easy direction: if $G$ splits over a finite subgroup, then $G$ acts on the Bass–Serre tree of the splitting.
Removing a single edge of this tree separates the Cayley graph into at least two infinite parts.
The hard direction, due to Stallings, builds from a set of vertices with finite boundary in $\Gamma$ a tree on which $G$ acts with finite edge stabilisers.

Example: $\Z$ has two ends, since removing one vertex of the line leaves two rays; and $\Z$ is the HNN extension of the trivial group over the trivial subgroup.
Example: the [[free group|0KTW26C80J]] $F_2 = \Z * \Z$ is an amalgam over the trivial group, and it has infinitely many ends.
Example: $\Z^2$ has one end, since the complement of a finite set in the grid has one infinite component; so $\Z^2$ does not split over a finite subgroup.

## Explanations

### L1 human

Remove a big finite chunk from the Cayley graph of a group and count the infinite pieces that remain; the largest such count is the number of ends.
The line has two ends, the plane has one.
The theorem says that a group has more than one end exactly when it can be cut, algebraically, into two pieces glued along a finite group.
So a picture at infinity detects an algebraic splitting.

### L2 human

The theorem is a cornerstone of [[Bass–Serre theory|6M731X66RD]] and of [[geometric group theory|2T3218RXTD]].
Since the number of ends is a [[quasi-isometry|6FKYSH729T]] invariant, splitting over a finite subgroup is a quasi-isometry invariant property.
It implies that a finitely generated torsion-free group with a free subgroup of finite index is itself free.
Iterating splittings over finite groups leads to the accessibility theorem of Dunwoody for finitely presented groups.
