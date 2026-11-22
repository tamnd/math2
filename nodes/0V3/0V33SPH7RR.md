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

The common part of any collection of subspaces is again a subspace, but the union of two subspaces almost never is.
Let $F$ be a field, let $V$ be a vector space over $F$, and let $U$ and $W$ be [[linear subspaces|0EPTJA5QV4]] of $V$.

1. For every nonempty family $(U_i)_{i \in I}$ of subspaces of $V$, the intersection $\bigcap_{i \in I} U_i$ is a subspace of $V$.
2. In particular, $U \cap W$ is a subspace of $V$, and it is the largest subspace of $V$ that is contained in both $U$ and $W$.
3. The union $U \cup W$ is a subspace of $V$ if and only if $U \subseteq W$ or $W \subseteq U$.

## Remarks

### Two planes in space

In $\mathbb{R}^3$, let $U$ be the plane $z = 0$ and $W$ the plane $x = 0$.
A vector lies in both exactly when $x = 0$ and $z = 0$, so
$$U \cap W = \{(0, y, 0) : y \in \mathbb{R}\},$$
the $y$-axis, which is a line through the origin and so a subspace.
The union behaves differently.
The vectors $(1, 0, 0) \in U$ and $(0, 0, 1) \in W$ lie in $U \cup W$, but their sum $(1, 0, 1)$ has $x \ne 0$ and $z \ne 0$, so it lies in neither plane.
This is the general pattern: two different planes through the origin of $\mathbb{R}^3$ meet in a line, and their union is not closed under addition.

### Why each hypothesis is needed

In part 1 the family must be nonempty, or we must agree that the intersection of the empty family is $V$.
Without one of the two, an empty intersection would be "every object at all", which is not a subset of $V$.

In part 3, $U$ and $W$ must be subspaces.
In $\mathbb{R}^2$ the subsets $\{0, (1, 0)\}$ and $\{0\}$ are nested, yet their union $\{0, (1, 0)\}$ is not a subspace, since $2 \cdot (1, 0)$ is missing.

### What it gives you

Part 1 lets us build the smallest subspace that contains a given set $S$: intersect all subspaces that contain $S$.
The family is nonempty, because $V$ itself contains $S$, and the result is the [[span|0DTY8B9HMS]] of $S$.
Part 3 says that the union is the wrong way to join two subspaces.
The smallest subspace that contains $U \cup W$ is the [[sum|0JMTY8MF54]] $U + W$, and for the two planes above it is all of $\mathbb{R}^3$.
In $F^n$, when $U$ and $W$ are given as solution sets of homogeneous systems, $U \cap W$ is the solution set of the two systems together.

### The converse

Part 3 is already an equivalence.
For part 1 one may ask which subspaces are intersections of others.
In a finite-dimensional space every proper subspace is an intersection of finitely many hyperplanes, that is, of subspaces of dimension $\dim V - 1$.
For example, the $y$-axis above is the intersection of the two planes $x = 0$ and $z = 0$.

### Generalizations

The same proofs work for submodules of a module and for subgroups of a group, since they use only closure.
The union of a chain $U_1 \subseteq U_2 \subseteq \dots$ of subspaces is a subspace, because any two vectors of the union lie in one $U_k$; the proofs by Zorn's lemma use this.
A stronger fact holds over an infinite field: a vector space is never the union of finitely many proper subspaces.
Over a finite field this fails, since $\mathbb{F}_2^2 = \{0, e_1, e_2, e_1 + e_2\}$ is the union of its three lines $\{0, e_1\}$, $\{0, e_2\}$ and $\{0, e_1 + e_2\}$.

## Explanations

### L1 human

A vector that lies in two subspaces stays in both of them when you add or stretch.
So the common part of two subspaces is again a subspace.
The union is different.
In the plane, the two axes form a cross, and $(1, 0) + (0, 1) = (1, 1)$ leaves the cross.

### L2 human

The proof for the union uses one vector from each side.
Suppose $u \in U$ is not in $W$, and $w \in W$ is not in $U$.
If $u + w$ were in $U$, then $w = (u + w) - u$ would be in $U$, which is false.
If $u + w$ were in $W$, then $u = (u + w) - w$ would be in $W$, which is also false.
So $u + w$ is in neither, and $U \cup W$ is not closed under addition.
With $U$ the $x$-axis and $W$ the $y$-axis in $\mathbb{R}^2$, the choice $u = (1, 0)$ and $w = (0, 1)$ gives $u + w = (1, 1)$, as in the cross.
The [[full proof|ZQ6G3XW1WR]] also treats intersections of any number of subspaces.

### L3 human

In the lattice of subspaces of $V$, the intersection is the meet, and the lattice is complete because part 1 allows any family.
The join is the sum, not the union, and this is the first sign that subspaces do not behave like subsets of a set.
The lattice is [[modular|QX7WZ92QAK]] but not distributive, as [[three lines in the plane|38AKN9MG6J]] shows.
The [[dimension formula|06HTJNCMPA]] $\dim(U + W) + \dim(U \cap W) = \dim U + \dim W$ ties the meet and the join together in finite dimension.
