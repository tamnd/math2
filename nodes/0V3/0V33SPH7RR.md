---
tag: 0V33SPH7RR
kind: statement
role: theorem
name: Intersection and union of subspaces
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
about: [00YC1D652K]
uses: [0EPTJA5QV4]
proofs: [ZQ6G3XW1WR]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_subspace
    locator: Operations and relations on subspaces
  - book: isbn:9783031410253
    locator: Section 1C
  - book: isbn:9780134860244
    locator: Section 1.3
---

## Statement

Let $F$ be a field, let $V$ be a vector space over $F$, and let $U$ and $W$ be [[linear subspaces|0EPTJA5QV4]] of $V$.

1. The intersection of each nonempty family of subspaces of $V$ is a subspace of $V$.
2. In particular, $U \cap W$ is a subspace, and it is the largest subspace of $V$ that is contained in both $U$ and $W$.
3. The union $U \cup W$ is a subspace if and only if $U \subseteq W$ or $W \subseteq U$.

## Remarks

### Why each hypothesis is needed

In part 1, the family must be nonempty, or we must agree that the empty intersection is $V$.
Otherwise the intersection is not defined inside $V$.
In part 3, $U$ and $W$ must be subspaces.
The sets $\set{0, (1, 0)}$ and $\set{0}$ in $\R^2$ have a union that is not a subspace, although one contains the other.

### Consequences

The intersection of all subspaces that contain a set $S$ is the smallest subspace that contains $S$; this is the [[span|0DTY8B9HMS]] of $S$.
The smallest subspace that contains $U \cup W$ is the [[sum|0JMTY8MF54]] $U + W$, not the union.
In $\R^3$, two different planes through the origin meet in a line through the origin.
Example: the planes $z = 0$ and $x = 0$ meet in the $y$-axis, and their union does not contain $(1, 0, 0) + (0, 0, 1) = (1, 0, 1)$.

### Converse

Part 3 is an equivalence.
For part 1, the converse question is when a subspace is an intersection of others.
Each proper subspace of a finite-dimensional space is an intersection of hyperplanes.

### Generalizations

The same proofs hold for submodules of a module over a ring, and for subgroups of a group.
Part 3 extends partly: over an infinite field, a vector space is not a union of finitely many proper subspaces.
Over $\mathbb{F}_2$, the plane $\mathbb{F}_2^2$ is the union of its three lines, so the field matters.

## Explanations

### L1 human

A vector that lies in two subspaces stays in both of them when we add or scale.
So the common part of two subspaces is again a subspace.
The union is different: the two axes of the plane form a cross, and $(1, 0) + (0, 1)$ leaves the cross.

### L2 human

The proof for the union uses one vector from each side.
If $u \in U$ is not in $W$ and $w \in W$ is not in $U$, then $u + w$ is in neither.
For example, with $U$ the $x$-axis and $W$ the $y$-axis in $\R^2$, take $u = (1, 0)$ and $w = (0, 1)$.
Then $u + w = (1, 1)$ is on neither axis.
