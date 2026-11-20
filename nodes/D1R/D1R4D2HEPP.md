---
tag: D1R4D2HEPP
kind: statement
role: theorem
name: A t-norm has a residuum iff it is left-continuous
aliases: [residuum-iff-left-continuous]
msc: ["03B52", "06F05"]
topics: [WZP584JQ06]
audience: grad
about: [VR6D8JXX1W]
uses: [BHGCVPAJW0]
proofs: [BKYX7JYW9J]
sources:
  - url: https://plato.stanford.edu/entries/logic-fuzzy/
    locator: 1. Fuzzy connectives based on t-norms
  - url: https://en.wikipedia.org/wiki/T-norm
    locator: Residuum; Basic properties of residua
---

## Statement

Let $*$ be a [[t-norm|BHGCVPAJW0]].

1. $*$ has a residuum $\Rightarrow_*$ iff $*$ is left-continuous.
2. In that case the residuum is unique, and $x \Rightarrow_* y = \max \set{z \in [0, 1] : z * x \le y}$; the maximum exists.

## Remarks

### Why each hypothesis is needed

1. Left-continuity is needed: the drastic t-norm is right-continuous, and it has no residuum; see [[the drastic non-example|VK2A62AQ0F]].
2. Monotonicity is used to reduce left-continuity to the preservation of suprema of sets.
3. Completeness of $[0, 1]$ is used: the supremum of $\set{z : z * x \le y}$ must exist.

### Consequences

1. Every continuous t-norm has a residuum, in particular the three basic ones.
2. The nilpotent minimum is left-continuous but not continuous, and it has a residuum.
3. With a left-continuous t-norm, $[0, 1]$ is a residuated lattice; this is the standard semantics of [[MTL|PT5PHKJDYM]].

### Converse

Item 1 is an equivalence, and both directions are proved.

### Generalizations

In any complete lattice, a monotone binary operation has a residuum in its first argument iff it preserves all joins in that argument.

## History

SEP states the equivalence and the formula with $\max$; Wikipedia states existence and uniqueness for left-continuous t-norms and gives the formula with $\sup$.

## Explanations

### L1 human

An implication should satisfy: "$z$ and $x$ give at most $y$" exactly when "$z$ is at most ($x$ implies $y$)".
This works only when the "and" has no jump from below.

### L2 human

To compute $x \Rightarrow y$, take the largest $z$ with $z * x \le y$.
For a t-norm with a jump, this largest $z$ may fail to exist.
For the drastic t-norm at $x = 0.5$, $y = 0$, every $z < 1$ works and $z = 1$ fails.

### L3 human

For fixed $x$, the map $z \mapsto z * x$ is monotone on the complete chain $[0, 1]$.
A monotone map between complete lattices has a right adjoint iff it preserves all joins.
On a chain, preserving joins of non-empty sets is the same as left-continuity, and the join of the empty set is $0 = 0 * x$.
