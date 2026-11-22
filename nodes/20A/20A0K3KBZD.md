---
tag: 20A0K3KBZD
kind: statement
role: proposition
name: Criteria for a direct sum of two subspaces
msc: ["15A03"]
topics: [QHKTJ89V6S]
audience: ug1
about: [0XYYT5KNTX]
uses: [041JTZCK9Q, 0RMKABS2S5, 0V33SPH7RR, 0EPTJA5QV4]
formal:
  - system: lean4
    library: mathlib
    decl: Submodule.disjoint_def
    match: partial
sources:
  - url: https://en.wikipedia.org/wiki/Direct_sum_of_modules
    locator: Internal direct sum
  - book: isbn:9783031410253
    locator: Section 1C
  - book: isbn:9780134860244
    locator: Section 1.3
---

## Statement

To see whether two subspaces give unique splittings, it is enough to look at the zero vector, or at the vectors they share.
Let $F$ be a field, let $V$ be a vector space over $F$, and let $U$ and $W$ be [[subspaces|0EPTJA5QV4]] of $V$.
The following three conditions are equivalent.

1. The [[sum|0RMKABS2S5]] $U + W$ is [[direct|041JTZCK9Q]]: each vector of $U + W$ is $u + w$ with $u \in U$ and $w \in W$ in exactly one way.
2. If $u + w = 0$ with $u \in U$ and $w \in W$, then $u = 0$ and $w = 0$.
3. The [[intersection|0V33SPH7RR]] $U \cap W$ is $\{0\}$.

In particular, $V = U \oplus W$ if and only if $U + W = V$ and $U \cap W = \{0\}$.

## Remarks

### Why the sets must be subspaces

The proof subtracts two expressions and uses that the differences stay inside $U$ and inside $W$.
For subsets that are not closed under subtraction, the criterion fails.
In $\R$, the sets $U = \{0, 1, 2\}$ and $W = \{0, -1\}$ meet only in $0$, but the number $1$ has the two expressions $1 + 0$ and $2 + (-1)$.

### Why there are only two subspaces

Condition 3 looks at one intersection, and that is enough only for two subspaces.
For three subspaces, zero pairwise intersections do not give a direct sum, as [[three lines in the plane|FRMQ1JB4RB]] show: the lines through $(1, 0)$, $(0, 1)$ and $(1, 1)$ meet pairwise in $0$, but $(1, 1) = (1, 0) + (0, 1)$ gives a second expression.
The correct test for several subspaces is the [[criterion for several subspaces|FVKY28HHBC]], which compares each subspace with the sum of the others.

### What it gives you

To prove $V = U \oplus W$, you check two things: each vector is some $u + w$, and no nonzero vector lies in both subspaces.
For example, take $U = \{(x, y, z) : x + y + z = 0\}$ and $W = \R(1, 1, 1)$ in $\R^3$.
A vector $t(1, 1, 1)$ lies in $U$ when $3t = 0$, so $t = 0$, and $U \cap W = \{0\}$.
For the sum, put $m = (x + y + z)/3$ and write
$$(x, y, z) = (x - m, y - m, z - m) + m(1, 1, 1),$$
where the first part lies in $U$ because its entries add up to $x + y + z - 3m = 0$.
So $\R^3 = U \oplus W$.
In finite dimension, the [[dimension criterion|P4JG9DJ2HH]] replaces the second check by a count of dimensions.
A further consequence is that an independent family in $U$ followed by an independent family in $W$ is independent in $V$ when $U \cap W = \{0\}$.

### The condition that is not included

The three conditions say nothing about whether $U + W$ is all of $V$.
The $x$-axis and the $y$-axis in $\R^3$ satisfy all three, but their sum is the $xy$-plane; see [[the two axes in space|PAJHW0002P]].
So "$U + W = V$" is a separate condition, and both are needed for $V = U \oplus W$.

### Generalizations

The same criteria hold for submodules of a module over any ring, with the same proof, since the proof only adds, subtracts and multiplies by $-1$.
In the lattice of subspaces, $U \cap W = \{0\}$ and $U + W = V$ together say that $U$ and $W$ are complements, which Mathlib writes `IsCompl U W`.

## History

The criterion has no single discoverer.
It is the first test for a direct sum in most modern textbooks, for example in Section 1C of Axler's *Linear Algebra Done Right*.

## Explanations

### L1 human

Two subspaces give unique splittings exactly when they share only the zero vector.
Suppose they shared a nonzero vector $x$.
Then $x$ itself could be counted in the first part, as $x + 0$, or in the second part, as $0 + x$.
That is two different splittings of one vector, so uniqueness fails.

### L2 human

Here is a typical use: decide whether $U = \R(1, 2, 3)$ and $W = \{(x, y, z) : x - y + z = 0\}$ give a direct sum.
Test the vectors of $U$ in the equation of $W$.
The vector $t(1, 2, 3)$ gives $t - 2t + 3t = 2t$, which is zero only for $t = 0$.
So $U \cap W = \{0\}$, and the sum $U + W$ is direct by condition 3.
Since $\dim U + \dim W = 1 + 2 = 3$, the sum is all of $\R^3$, and $\R^3 = U \oplus W$.
Watch out: the intersection test alone shows that the sum is direct, and you need a second argument, here the count of dimensions, to see that it fills $V$.

### L3 human

Condition 2 says that the addition map $U \times W \to V$, $(u, w) \mapsto u + w$, has kernel $\{0\}$.
Condition 3 describes the same kernel, since $(u, w)$ lies in it exactly when $u = -w$, that is, when $u \in U \cap W$ and $w = -u$.
So the criteria are the familiar fact that a linear map is injective if and only if its kernel is zero.
The same view explains the generalization to several subspaces, where the addition map starts from the [[external direct sum|0S7W6EG32V]] of all of them.
