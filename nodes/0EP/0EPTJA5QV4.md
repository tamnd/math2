---
tag: 0EPTJA5QV4
kind: definition
name: Linear subspace
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
defines: 00YC1D652K
uses: [05EGHEQZAW]
formal:
  - system: lean4
    library: mathlib
    decl: Submodule
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Linear_subspace
    locator: Definition
  - book: isbn:9783031410253
    locator: Section 1C
inventory: [5QGEM8RZJA]
---

## Definition

Let $F$ be a field and let $V$ be a [[vector space|05EGHEQZAW]] over $F$.
A *linear subspace* of $V$ is a subset $W \subseteq V$ with these three properties:

1. $0 \in W$.
2. If $u, v \in W$, then $u + v \in W$.
3. If $a \in F$ and $v \in W$, then $av \in W$.

## Remarks

With the operations of $V$, a subspace $W$ is itself a vector space over $F$; see the [[subspace test|~3900ae4c]].
Condition 1 can be replaced by "$W$ is nonempty", because $0v = 0$ then gives $0 \in W$ by condition 3.
The sets $\set{0}$ and $V$ are subspaces of $V$.
The lines through the origin are the one-dimensional subspaces of $\R^2$; a line that misses the origin is not a subspace.
The kernel and the image of a linear map are subspaces.
In Mathlib, `Submodule R M` is defined for a module over a semiring, and for a field it is exactly this notion.

## Explanations

### L1 human

A subspace is a smaller vector space inside a bigger one.
We cannot leave it by adding its vectors or by scaling them.
In space, the subspaces are the origin, the lines and planes through the origin, and the whole space.

### L2 human

Each condition can fail alone.
The line $y = 1$ fails condition 1, the union of the two axes fails condition 2, and the first quadrant fails condition 3.
Do not forget condition 1: the empty set satisfies conditions 2 and 3 but is not a subspace.
