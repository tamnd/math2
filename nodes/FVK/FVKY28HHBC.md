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

Let $F$ be a field, let $V$ be a vector space over $F$, and let $U_1, \dots, U_k$ be [[subspaces|0EPTJA5QV4]] of $V$ with $k \ge 2$.
The following conditions are equivalent.

1. The [[sum|0RMKABS2S5]] $U_1 + \cdots + U_k$ is [[direct|041JTZCK9Q]].
2. If $u_1 + \cdots + u_k = 0$ with $u_i \in U_i$ for each $i$, then $u_i = 0$ for each $i$.
3. For each $i = 2, \dots, k$, we have $U_i \cap (U_1 + \cdots + U_{i-1}) = \{0\}$.
4. For each $i = 1, \dots, k$, we have $U_i \cap \sum_{j \ne i} U_j = \{0\}$.

## Remarks

### Why each hypothesis is needed

- Condition 3 needs the whole earlier sum, not only the earlier subspaces one by one. For [[three lines in the plane|FRMQ1JB4RB]], each pairwise intersection is $\{0\}$, but the third line lies in the sum of the first two.
- The subspaces must be subspaces of one space $V$, so that their sum is defined. For spaces that are not inside a common space, one uses the [[external direct sum|0S7W6EG32V]].

### Consequences

- Pairwise zero intersections are necessary for a direct sum, but they are not sufficient when $k \ge 3$.
- A sum of subspaces is direct if and only if, for each choice of a basis in each $U_i$, the union of the bases is linearly independent.
- In finite dimension, the sum is direct if and only if $\dim(U_1 + \cdots + U_k) = \dim U_1 + \cdots + \dim U_k$.
- If $U_1 + \cdots + U_k$ is direct, then so is the sum of any subfamily.

### Converse

The statement is an equivalence.
Condition 3 is the efficient test: it needs $k - 1$ intersections, and the subspaces can be added one at a time.

### Generalizations

- For an infinite family $(U_i)_{i \in I}$, the sum is direct if and only if each $U_i$ meets the sum of the others only in $0$. Mathlib calls such a family independent and states the criterion for `DirectSum.IsInternal`.
- The same criteria hold for submodules of a module over a ring.

## History

The criterion with the sum of the other subspaces is standard in textbooks since Halmos's *Finite-Dimensional Vector Spaces*.
The warning about pairwise intersections is a classical exercise, for example in Axler's *Linear Algebra Done Right*.

## Explanations

### L1 human

For many subspaces, it is not enough that each two of them share only $0$.
Each subspace must share only $0$ with everything built from the others.
Three different lines in a plane fail this test, because any two of them already fill the plane.

### L2 human

We test $U_1 = \R(1, 0, 0)$, $U_2 = \R(0, 1, 0)$ and $U_3 = \R(1, 1, 1)$ in $\R^3$ with condition 3.

1. $U_2 \cap U_1 = \{0\}$, since $(0, b, 0) = (a, 0, 0)$ forces $a = b = 0$.
2. $U_1 + U_2$ is the $xy$-plane. A vector $t(1, 1, 1)$ lies in it only for $t = 0$, so $U_3 \cap (U_1 + U_2) = \{0\}$.
3. So the sum is direct, and $\R^3 = U_1 \oplus U_2 \oplus U_3$, since the dimensions add up to $3$.

The trap is to check only $U_1 \cap U_2$, $U_1 \cap U_3$ and $U_2 \cap U_3$.

### L3 human

Condition 2 says that the addition map from the [[external direct sum|0S7W6EG32V]] $U_1 \oplus \cdots \oplus U_k$ to $V$ is injective.
Condition 3 is the same statement proved by induction on $k$, one summand at a time.
In lattice terms, a family of subspaces is independent when each member is disjoint from the join of the others.
The subspace lattice is modular but not distributive, which is why pairwise disjointness is not enough.
