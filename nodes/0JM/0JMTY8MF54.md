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

The sum of two subspaces is the right way to join them: it collects every vector that you can build from one piece in each, and it is the smallest subspace that holds both.
For two [[subspaces|00YC1D652K]] $U$ and $W$ of a vector space $V$, the [[definition|0RMKABS2S5]] reads
$$U + W = \{u + w : u \in U, \ w \in W\}.$$
For subspaces $U_1, \dots, U_k$ the sum $U_1 + \dots + U_k$ is the set of all $u_1 + \dots + u_k$ with $u_i \in U_i$.
The sum $U + W$ is the [[smallest subspace that contains both U and W|EDF9C7G048]], so it plays the role of a join of subspaces, as the intersection $U \cap W$ plays the role of a meet.

## Motivation

We often build a space from smaller pieces: a plane from two lines, or the solutions of a differential equation from simpler solutions.
The first idea is to take the union of the pieces, but the union of two subspaces is [[usually not a subspace|0V33SPH7RR]].
Any subspace that contains $U$ and $W$ must contain each sum $u + w$, by closure under addition.
The sum of subspaces is exactly the set of these vectors, and it turns out to be a subspace already, so nothing more is needed.

Sums return throughout linear algebra.
A [[direct sum|0XYYT5KNTX]] is a sum in which every vector splits in only one way, and it is the basis of eigenspace decompositions.
The [[dimension formula|06HTJNCMPA]] $\dim(U + W) = \dim U + \dim W - \dim(U \cap W)$ measures how much two subspaces overlap.

## Notation

We write $U + W$, and for several subspaces $U_1 + \dots + U_k$ or $\sum_{i = 1}^{k} U_i$.
When every vector of the sum has only one decomposition, we write $U \oplus W$ and call the sum direct.
Lattice theory writes the sum as $U \vee W$, and Mathlib writes `U ⊔ W` for submodules.

## Remarks

### A first computation

In $\mathbb{R}^2$, let $U$ be the $x$-axis and $W$ the $y$-axis.
Every vector splits into a piece on each axis:
$$(a, b) = (a, 0) + (0, b),$$
so $U + W = \mathbb{R}^2$, although $U \cup W$ is only the cross of the two axes.
In $\mathbb{R}^3$, the lines $U = \operatorname{span}((1, 0, 0))$ and $W = \operatorname{span}((0, 1, 0))$ give $U + W = \{(a, b, 0) : a, b \in \mathbb{R}\}$, the plane $z = 0$.
So the sum of two different lines through the origin is the plane that contains them.

### Computing a sum in coordinates

The sum of two [[spans|0DTY8B9HMS]] is the span of the joined list: if $U = \operatorname{span}(u_1, \dots, u_p)$ and $W = \operatorname{span}(w_1, \dots, w_q)$, then $U + W = \operatorname{span}(u_1, \dots, u_p, w_1, \dots, w_q)$.
Take $U = \operatorname{span}((1, 0, 1), (0, 1, 1))$ and $W = \operatorname{span}((1, 1, 0))$ in $\mathbb{R}^3$.
Is $(1, 1, 0)$ already in $U$?
A vector of $U$ has the form $a(1, 0, 1) + b(0, 1, 1) = (a, b, a + b)$, and $(a, b, a + b) = (1, 1, 0)$ would need $a = b = 1$ and $a + b = 0$, which is impossible.
So the three vectors are independent, and $U + W = \mathbb{R}^3$.
Check: the matrix with rows $(1, 0, 1)$, $(0, 1, 1)$, $(1, 1, 0)$ has determinant $1 \cdot (0 - 1) - 0 + 1 \cdot (0 - 1) = -2 \ne 0$.
If instead $W = \operatorname{span}((1, 1, 2))$, then $(1, 1, 2) = (1, 0, 1) + (0, 1, 1)$ lies in $U$, and $U + W = U$.

### More than two subspaces

The sum of $U_1, \dots, U_k$ can be built one step at a time, since $U_1 + U_2 + U_3 = (U_1 + U_2) + U_3$.
For an infinite family $(U_i)_{i \in I}$ the sum consists of the finite sums $u_{i_1} + \dots + u_{i_m}$, because a vector space has no infinite sums.
[[Three lines in the plane|38AKN9MG6J]] show the new feature of three pieces: the lines spanned by $(1, 0)$, $(0, 1)$ and $(1, 1)$ meet pairwise only in $0$, but their sum is the plane of dimension $2$, not $3$.

### What it is not

The sum is not the union.
For the two axes of $\mathbb{R}^2$, the vector $(1, 1)$ lies in the sum but not in the union.
The same formula for sets that are not subspaces gives no subspace: for $A = \{(1, 0)\}$ and $B = \{(0, 1)\}$ the set $A + B = \{(1, 1)\}$ does not contain $0$.

### The rules you can use

The sum is a subspace that contains $U$ and $W$ and lies in every subspace that contains both; this is the [[statement on the smallest subspace|EDF9C7G048]].
So $U + W = \operatorname{span}(U \cup W)$.
The sum is commutative and associative, and $U + \{0\} = U$ and $U + U = U$, because $U$ is closed under addition.
More generally, $U + W = W$ exactly when $U \subseteq W$.
The subspaces of $V$ form a lattice, with $+$ as join and $\cap$ as meet, and it obeys the modular law: if $U \subseteq X$, then $X \cap (U + W) = U + (X \cap W)$.
The distributive law fails, as the three lines show.

### Watch out

A vector of $U + W$ can have many decompositions $u + w$.
In $\mathbb{R}^3$, with $U$ the plane $z = 0$ and $W$ the plane $x = 0$, the vector $(1, 1, 1)$ equals $(1, 1, 0) + (0, 0, 1)$ and also $(1, 0, 0) + (0, 1, 1)$.
Decompositions are unique exactly when $U \cap W = \{0\}$, and then the sum is direct.
For three or more subspaces, pairwise intersections $\{0\}$ are not enough: in the three lines, $(1, 1) = (1, 0) + (0, 1) + 0$ and also $(1, 1) = 0 + 0 + (1, 1)$.

### History

The dimension formula for $U + W$ and $U \cap W$ carries the name of Grassmann, whose *Ausdehnungslehre* of 1844 worked with sums of quantities of this kind.

### Try it

First, find $U + W$ for the lines $U = \operatorname{span}((1, 2))$ and $W = \operatorname{span}((2, 4))$ in $\mathbb{R}^2$.
Since $(2, 4) = 2 \cdot (1, 2)$, the two lines are equal, and $U + W = U$.

Second, in the space $P_2(\mathbb{R})$ of polynomials of degree at most $2$, what is the sum of the constants and the multiples of $x^2$?
It is $\{a + cx^2 : a, c \in \mathbb{R}\}$, and the polynomial $x$ is not in it.

## Explanations

### L1 human

The sum of two subspaces collects every vector that you can build by adding one vector from each.
In space, take two different lines through the origin.
Walking some distance along the first line and then some distance along the second, you can reach every point of the plane that contains both lines.
So the sum of the two lines is that plane, and it is the smallest flat piece through the origin that holds both lines.

### L2 human

Here is a typical problem: let $U$ be the plane $z = 0$ in $\mathbb{R}^3$ and $W = \operatorname{span}((1, 1, 1))$; find $U + W$ and $U \cap W$.
To split a vector $(a, b, c)$, first take $c$ times $(1, 1, 1)$ to fix the last entry, and then put the rest in $U$:
$$(a, b, c) = (a - c, \ b - c, \ 0) + c(1, 1, 1).$$
So $U + W = \mathbb{R}^3$.
A vector $t(1, 1, 1)$ of $W$ lies in $U$ only when its last entry $t$ is $0$, so $U \cap W = \{0\}$.
Check with the dimension formula: $\dim U + \dim W - \dim(U \cap W) = 2 + 1 - 0 = 3$, which is $\dim \mathbb{R}^3$.
Since the intersection is $0$, the split above is the only one, and $\mathbb{R}^3 = U \oplus W$.
This is the typical use of a sum: to break each vector into simpler pieces, and to test with the intersection whether the pieces are unique.

### L3 human

The subspaces of $V$ form a [[complete lattice|D7A0ZGZT5S]], with the sum as join and the intersection as meet, and this lattice is [[modular|QX7WZ92QAK]].
The sum $U + W$ is the image of the linear map $U \times W \to V$, $(u, w) \mapsto u + w$, from the [[external direct sum|0S7W6EG32V]], and its kernel $\{(x, -x) : x \in U \cap W\}$ is a copy of $U \cap W$; rank-nullity then gives the dimension formula.
A subspace $W$ with $U + W = V$ and $U \cap W = \{0\}$ is a [[complement|0M83V17KHX]] of $U$, and complements exist but are not unique.
The same construction gives sums of submodules of a module and products $NM$ of normal subgroups of a group.
