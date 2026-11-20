---
tag: 0JMTY8MF54
kind: concept
name: Sum of subspaces
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
specializes: [00YC1D652K]
uses: [00YC1D652K, 0EPTJA5QV4]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_subspace
    locator: Operations and relations on subspaces
  - book: isbn:9783031410253
    locator: Section 1C
  - book: isbn:9780135367971
    locator: Section 2.2
inventory: [JN56MBD6F4]
---

## Summary

Let $U$ and $W$ be [[subspaces|00YC1D652K]] of a vector space $V$.
Their sum is $U + W = \set{u + w : u \in U, \ w \in W}$; the precise statement is in the [[definition|0RMKABS2S5]].
It is the [[smallest subspace that contains $U \cup W$|~a8f7cf5b]], so it plays the role of a join, while $U \cap W$ plays the role of a meet.

## Motivation

The union of two subspaces is usually not a subspace; see [[intersection and union of subspaces|0V33SPH7RR]].
We still want a subspace that contains both pieces.
The sum adds one vector from each piece, and this is exactly what closure under addition forces.

## Notation

For subspaces $U_1, \dots, U_k$, we write $U_1 + \cdots + U_k$ or $\sum_i U_i$.
When each vector of the sum has only one decomposition, we write $U \oplus W$; see [[direct sum|0XYYT5KNTX]].

## Remarks

### Examples

1. In $\R^2$, let $U$ be the $x$-axis and $W$ the $y$-axis. Each $(a, b)$ is $(a, 0) + (0, b)$, so $U + W = \R^2$.
2. In $\R^3$, let $U = \operatorname{span}(1, 0, 0)$ and $W = \operatorname{span}(0, 1, 0)$. Then $U + W = \set{(a, b, 0)}$, the plane $z = 0$.
3. In $\R^3$, the planes $z = 0$ and $x = 0$ have sum $\R^3$, because $(a, b, c) = (a, b, 0) + (0, 0, c)$. Their intersection is the $y$-axis.
4. In each space, $U + \set{0} = U$ and $U + U = U$.
5. In $P_2(\R)$, the constants plus the multiples of $x^2$ give $\set{a + c x^2}$.

### Non-examples

1. The union of the two axes in $\R^2$ is not their sum: $(1, 1)$ lies in the sum but not in the union.
2. For the subsets $A = \set{(1, 0)}$ and $B = \set{(0, 1)}$, which are not subspaces, the set $A + B = \set{(1, 1)}$ fails condition 1 of a subspace: it does not contain $0$.

### Basic properties

1. $U + W$ is a subspace, and it is the smallest subspace that contains $U \cup W$; see [[this statement|~a8f7cf5b]].
2. $U + W = \operatorname{span}(U \cup W)$, the [[span|0DTY8B9HMS]] of the union.
3. The sum is commutative and associative, and $U \subseteq U + W$.
4. For finite-dimensional subspaces, [[Grassmann's formula|06HTJNCMPA]] gives $\dim(U + W) = \dim U + \dim W - \dim(U \cap W)$.
5. The lattice of subspaces with $+$ and $\cap$ is modular: if $U \subseteq X$, then $X \cap (U + W) = U + (X \cap W)$. It is not distributive; see [[three lines in the plane|~d4abcdaa]].

### History

Grassmann worked with the join and the meet of spans in his *Ausdehnungslehre* of 1844.
The dimension formula for $U + W$ and $U \cap W$ is named after him.
Peano gave the axiomatic definition of a vector space in 1888.

### Common errors

1. $U + W$ is not $U \cup W$, and it is usually much larger.
2. A decomposition $v = u + w$ need not be unique; it is unique for all $v$ exactly when $U \cap W = \set{0}$.
3. The sum of three subspaces does not obey the inclusion-exclusion formula for dimension; see [[three lines in the plane|~d4abcdaa]].

## Explanations

### L1 human

The sum of two subspaces collects every vector that we can build from one piece in each subspace.
In space, the sum of two different lines through the origin is the plane that contains both lines.
It is the smallest subspace that holds both subspaces.

### L2 human

To compute $U + W$ in $F^n$, take a spanning list of $U$ and a spanning list of $W$, and join the lists.
The joined list spans $U + W$.
Row reduction of the matrix with these vectors as rows then gives a basis of $U + W$.
Example: $U = \operatorname{span}((1, 1, 0))$ and $W = \operatorname{span}((0, 1, 1))$ in $\R^3$.
The two vectors are independent, so $U + W$ is the plane through $0$ that contains them, with normal vector $(1, -1, 1)$.

### L3 human

The subspaces of $V$ form a complete modular lattice, with join $+$ and meet $\cap$.
For an infinite family $(U_i)$, the sum $\sum_i U_i$ consists of the finite sums $u_{i_1} + \cdots + u_{i_k}$.
For modules, the same construction gives the sum of submodules.
