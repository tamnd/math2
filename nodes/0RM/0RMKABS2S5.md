---
tag: 0RMKABS2S5
kind: definition
name: Sum of subspaces
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
defines: 0JMTY8MF54
uses: [0EPTJA5QV4]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_subspace
    locator: Operations and relations on subspaces
  - book: isbn:9783031410253
    locator: Section 1C
inventory: [JN56MBD6F4]
---

## Definition

The sum of subspaces is the set of all vectors that we get by adding one vector from each subspace.
Let $F$ be a field, let $V$ be a vector space over $F$, and let $U$ and $W$ be [[linear subspaces|0EPTJA5QV4]] of $V$.
The *sum* of $U$ and $W$ is the subset of $V$
$$U + W = \{u + w : u \in U, \ w \in W\}.$$
More generally, for subspaces $U_1, \dots, U_k$ of $V$, the sum is
$$U_1 + \dots + U_k = \{u_1 + \dots + u_k : u_i \in U_i \text{ for } i = 1, \dots, k\}.$$

## Notation

Other notations are $\sum_{i = 1}^{k} U_i$ and, in lattice theory, $U \vee W$.
In Mathlib, the sum of two submodules is the supremum `U ⊔ W` in the lattice `Submodule F V`.

## Remarks

Each vector $u + w$ uses one vector of $U$ and one of $W$, and either may be $0$.
That is why $U \subseteq U + W$: every $u \in U$ is $u + 0$ with $0 \in W$.
The definition asks for subspaces because only then is the result a subspace again.
For example, the one-point sets $\{(1, 0)\}$ and $\{(0, 1)\}$ in $\mathbb{R}^2$ have the "sum" $\{(1, 1)\}$, which misses the origin.

A small case shows how the sum fills space.
For the $x$-axis $U$ and the $y$-axis $W$ in $\mathbb{R}^2$, every vector is $(a, b) = (a, 0) + (0, b)$, so $U + W = \mathbb{R}^2$.
The [[smallest subspace theorem|EDF9C7G048]] shows in general that $U + W$ is the least subspace that contains $U$ and $W$, so it equals the [[span|0DTY8B9HMS]] of $U \cup W$.
When $U \cap W = \{0\}$, each vector of the sum splits in only one way, and the sum is a [[direct sum|0XYYT5KNTX]].
The concept page on the [[sum of subspaces|0JMTY8MF54]] works out more examples and the [[dimension formula|06HTJNCMPA]].

## Explanations

### L1 human

The sum of two subspaces collects every vector that you can build by adding one vector from each.
In space, the sum of two different lines through the origin is the plane that contains both lines.

### L2 human

To test whether a vector lies in $U + W$, try to split it.
With $U$ the plane $z = 0$ and $W = \operatorname{span}((1, 1, 1))$ in $\mathbb{R}^3$, the vector $(2, 5, 3)$ splits as $(-1, 2, 0) + 3(1, 1, 1)$.
Check: $-1 + 3 = 2$, $2 + 3 = 5$ and $0 + 3 = 3$.
