---
tag: FVKY28HHBC
kind: statement
role: proposition
name: Criterion for a direct sum of several subspaces
msc: ["15A03"]
topics: [QHKTJ89V6S]
audience: ug1
about: [0XYYT5KNTX]
uses: [041JTZCK9Q, 0RMKABS2S5, 0EPTJA5QV4]
sources:
  - book: isbn:9783031410253
    locator: Section 1C
  - book: isbn:9780134860244
    locator: Section 5.2
  - url: https://en.wikipedia.org/wiki/Direct_sum_of_modules
    locator: Internal direct sum
---

## Statement

A sum of several subspaces is direct when each subspace shares only the zero vector with the sum of the subspaces before it, and pairwise tests are not enough.
Let $F$ be a field, let $V$ be a vector space over $F$, and let $U_1, \dots, U_k$ be [[subspaces|0EPTJA5QV4]] of $V$ with $k \ge 2$.
The following conditions are equivalent.

1. The [[sum|0RMKABS2S5]] $U_1 + \cdots + U_k$ is [[direct|041JTZCK9Q]].
2. If $u_1 + \cdots + u_k = 0$ with $u_i \in U_i$ for each $i$, then $u_i = 0$ for each $i$.
3. For each $i = 2, \dots, k$, we have $U_i \cap (U_1 + \cdots + U_{i-1}) = \{0\}$.
4. For each $i = 1, \dots, k$, we have $U_i \cap \sum_{j \ne i} U_j = \{0\}$.

## Remarks

### Why the whole earlier sum is needed

Condition 3 compares $U_i$ with the sum $U_1 + \cdots + U_{i-1}$, not with each earlier subspace one at a time.
For [[three lines in the plane|FRMQ1JB4RB]], namely $\R(1, 0)$, $\R(0, 1)$ and $\R(1, 1)$, each pairwise intersection is $\{0\}$.
But the first two lines already span $\R^2$, so the third line lies in their sum, and the expression
$$(1, 1) = (1, 0) + (0, 1) + 0$$
competes with $0 + 0 + (1, 1)$.
So pairwise zero intersections are necessary for a direct sum, but they are not sufficient when $k \ge 3$.

### Why one common space is needed

The subspaces must lie in one space $V$, so that their sum is defined.
For spaces that are not inside a common space, the [[external direct sum|0S7W6EG32V]] builds the space in which they become summands.

### What it gives you

Condition 3 is the efficient test.
It needs $k - 1$ intersections, and you can add the subspaces one at a time, each time checking the new one against what you have so far.
For example, take $U_1 = \R(1, 0, 0)$, $U_2 = \R(0, 1, 0)$ and $U_3 = \R(1, 1, 1)$ in $\R^3$.
First, $(0, b, 0) = (a, 0, 0)$ forces $a = b = 0$, so $U_2 \cap U_1 = \{0\}$.
Next, $U_1 + U_2$ is the $xy$-plane, and $t(1, 1, 1)$ lies in it only for $t = 0$, so $U_3 \cap (U_1 + U_2) = \{0\}$.
So the sum is direct, and since $1 + 1 + 1 = 3$, it is all of $\R^3$.

Two further consequences follow from condition 2.
If the sum is direct, then so is the sum of any subfamily, because an expression of $0$ in the subfamily is an expression of $0$ in the whole family with zeros added.
And the sum is direct if and only if the list obtained by putting together a basis of each $U_i$ is linearly independent.
Watch out that this must be a list: for $U_1 = U_2 = \R(1, 0)$, the union of the two bases as a set is the independent set $\{(1, 0)\}$, while the list $(1, 0), (1, 0)$ is dependent and the sum is not direct.

### The finite-dimensional form

In finite dimension, the sum is direct if and only if
$$\dim(U_1 + \cdots + U_k) = \dim U_1 + \cdots + \dim U_k.$$
For the three lines in the plane, the left side is $2$ and the right side is $3$, which detects the failure at once.

### Generalizations

For an infinite family $(U_i)_{i \in I}$, the sum is direct if and only if each $U_i$ meets the sum of all the others only in $0$.
Mathlib calls such a family independent and relates it to `DirectSum.IsInternal`.
The same criteria hold for submodules of a module over a ring, with the same proof.

## History

The criterion has no single discoverer, and it belongs to the standard treatment of direct sums.
Textbooks such as Axler's *Linear Algebra Done Right* state condition 2 as the test for a direct sum and warn that pairwise intersections are not enough.

## Explanations

### L1 human

For many subspaces, it is not enough that each two of them share only the origin.
Each subspace must share only the origin with everything built from the others.
Three different lines through the origin in a plane fail this test.
Any two of them already fill the whole plane, so the third line adds nothing new and splittings stop being unique.

### L2 human

Here is a typical use: decide whether $U_1 = \R(1, 1, 0)$, $U_2 = \R(0, 1, 1)$ and $U_3 = \R(1, 0, -1)$ give a direct sum in $\R^3$.
The first two lines are different, so $U_1 \cap U_2 = \{0\}$.
The sum $U_1 + U_2$ is the plane of the vectors $a(1, 1, 0) + b(0, 1, 1) = (a, a + b, b)$.
The vector $(1, 0, -1)$ has this form with $a = 1$ and $b = -1$, so $U_3 \subseteq U_1 + U_2$.
Check: $(1, 1, 0) - (0, 1, 1) = (1, 0, -1)$.
So condition 3 fails at $i = 3$, and the sum is not direct, although all three pairwise intersections are $\{0\}$.
The typical use of the criterion is exactly this: add one subspace at a time and test it against the span of what you already have.

### L3 human

Condition 2 says that the addition map from the [[external direct sum|0S7W6EG32V]] $U_1 \oplus \cdots \oplus U_k$ to $V$ is injective.
Condition 3 breaks this into $k - 1$ steps, one for each new summand, which is the shape of a proof by induction on $k$.
In lattice terms, a family of subspaces is independent when each member is disjoint from the join of the others.
The lattice of subspaces is modular but not distributive, and this is why pairwise disjointness is not enough.
Eigenspaces for distinct eigenvalues always form a direct sum, and the usual proof of that fact runs through condition 2.
