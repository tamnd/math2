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

A linear subspace is a subset of a vector space that contains the zero vector and that sums and scalar multiples cannot leave.
Let $F$ be a field and let $V$ be a [[vector space|05EGHEQZAW]] over $F$.
A *linear subspace* of $V$ is a subset $W \subseteq V$ with these three properties:

1. $0 \in W$.
2. If $u, v \in W$, then $u + v \in W$.
3. If $a \in F$ and $v \in W$, then $av \in W$.

## Notation

We write $W \le V$, or $W \subseteq V$ when the context makes clear that $W$ is a subspace.
In Mathlib, `Submodule R M` is defined for a module over a semiring, and for a field it is exactly this notion.

## Remarks

Conditions 2 and 3 make the two operations of $V$ restrict to maps $W \times W \to W$ and $F \times W \to W$.
With these maps $W$ is a vector space over $F$, because the axioms that are identities hold already in $V$; the [[subspace test|Z5XKYXTC0K]] proves this.

Condition 1 is there to rule out the empty set.
The empty set satisfies conditions 2 and 3, since there are no vectors to test, but a vector space must have a zero vector.
For a nonempty $W$, condition 1 follows from condition 3: pick any $w \in W$, and then $0w = 0$ lies in $W$ by the [[first consequences of the axioms|5E4VBC0A4H]].
So many books replace condition 1 by "$W$ is nonempty".

For example, the line $\{(t, 2t) : t \in \mathbb{R}\}$ in $\mathbb{R}^2$ satisfies all three conditions, since $(0, 0)$ is the point with $t = 0$ and $(s, 2s) + a(t, 2t) = (s + at, 2(s + at))$.
The line $\{(t, 2t + 1) : t \in \mathbb{R}\}$ fails condition 1, because $2t + 1 = 0$ forces $t = -\tfrac{1}{2}$, and then the first entry is $-\tfrac{1}{2}$, not $0$.
The concept page on [[subspaces|00YC1D652K]] has more examples and a failure of each condition.

## Explanations

### L1 human

A subspace is a smaller vector space inside a bigger one.
It contains the origin, and you cannot leave it by adding two of its vectors or by stretching one of them.
In space, the subspaces are the origin, the lines and planes through the origin, and the whole space.

### L2 human

Each condition can fail while the other two hold.
The line $y = 1$ in $\mathbb{R}^2$ is closed under neither operation and misses the origin, so it is not a good test of condition 1 alone.
The empty set is: it satisfies conditions 2 and 3 and fails only condition 1.
The cross of the two axes fails only condition 2, since $(1, 0) + (0, 1) = (1, 1)$ is on neither axis.
The first quadrant fails only condition 3, since $(-1)(1, 1) = (-1, -1)$ leaves it.
