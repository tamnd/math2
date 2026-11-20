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

Let $F$ be a field, let $V$ be a vector space over $F$, and let $U$ and $W$ be [[linear subspaces|0EPTJA5QV4]] of $V$.
The *sum* of $U$ and $W$ is
$$U + W = \{u + w : u \in U, \ w \in W\}.$$
For subspaces $U_1, \dots, U_k$, the sum is $U_1 + \cdots + U_k = \{u_1 + \cdots + u_k : u_i \in U_i\}$.

## Remarks

The sum $U + W$ is a subspace, and it is the [[smallest subspace of $V$ that contains $U \cup W$|EDF9C7G048]].
The sum is the [[span|0DTY8B9HMS]] of $U \cup W$.
When $U \cap W = \{0\}$, the sum is a [[direct sum|0XYYT5KNTX]].
For finite-dimensional subspaces, [[Grassmann's formula|06HTJNCMPA]] gives $\dim(U + W) = \dim U + \dim W - \dim(U \cap W)$.
In Mathlib, the sum of two submodules is the supremum `U ⊔ W` in the lattice `Submodule F V`.

## Explanations

### L1 human

The sum of two subspaces collects every vector that we can build from one piece in each subspace.
In space, the sum of two different lines through the origin is the plane that contains both lines.
It is the smallest subspace that holds both subspaces.
