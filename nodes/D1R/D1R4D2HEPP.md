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

A t-norm has a matching implication exactly when it has no jumps from below.

Let $*$ be a [[t-norm|BHGCVPAJW0]].

1. The t-norm $*$ has a residuum $\Rightarrow_*$ if and only if $*$ is left-continuous.
2. In that case the residuum is unique, the maximum below exists for all $x, y \in [0, 1]$, and it equals $x \Rightarrow_* y$.
   $$x \Rightarrow_* y = \max \{ z \in [0, 1] : z * x \le y \}.$$

## Remarks

### Why each hypothesis is needed

Left-continuity cannot be dropped.
The drastic t-norm is right-continuous, but it jumps from $0$ to $0.5$ as $z$ rises to $1$ in $z * 0.5$.
So the set $\{ z : z * 0.5 \le 0 \}$ is $[0, 1)$, which has no maximum, and [[the drastic non-example|VK2A62AQ0F]] concludes that there is no residuum.

Monotonicity is used to turn left-continuity into a statement about suprema.
For a monotone map on $[0, 1]$, being left-continuous is the same as sending the supremum of every nonempty set to the supremum of the image.
The completeness of $[0, 1]$ is used too, since the supremum of $\{ z : z * x \le y \}$ must exist.
On the rationals in $[0, 1]$, with $x * y = \max(0, x + y - 1)$ and with $y$ and $x$ rational, the residuum still exists, but on a chain with gaps a supremum can be missing.

### What it gives you

Every continuous t-norm has a residuum, in particular the three basic ones, whose residua are computed in [[the residua statement|7R2JBNNMT5]].
The nilpotent minimum is left-continuous but not continuous, and it still has a residuum, as [[the nilpotent minimum example|ZJX7P6TVG9]] computes.
With a left-continuous t-norm, $[0, 1]$ becomes a residuated lattice, and these are exactly the standard algebras of [[MTL|PT5PHKJDYM]].
So the theorem explains why MTL is the logic of left-continuous t-norms: they are exactly the t-norms that have an implication.

### The converse

Item 1 is an equivalence, and the proof gives both directions.
A residuum forces left-continuity, and left-continuity gives a residuum.

### Generalizations

In any complete lattice, a monotone operation has a residuum in its first argument exactly when it preserves all joins in that argument.
This is the order-theoretic form of the adjoint functor theorem, and the statement is its case for the chain $[0, 1]$.

## History

The equivalence is standard in the theory of t-norms, and it appears in Hájek's monograph of 1998 and in the monograph of Klement, Mesiar and Pap of 2000.
It is the reason why left-continuity became the standard hypothesis in residuated fuzzy logic.

## Explanations

### L1 human

An implication should satisfy one rule.
"$z$ and $x$ give at most $y$" should hold exactly when "$z$ is at most ($x$ implies $y$)".
This rule picks out a best value for "$x$ implies $y$".
The best value exists only when the "and" has no sudden jump as its inputs rise.

### L2 human

To compute $x \Rightarrow y$, take the largest $z$ with $z * x \le y$.
For the minimum at $x = 0.7$, $y = 0.4$, the set of good $z$ is computed below.

$$\{ z : \min(z, 0.7) \le 0.4 \} = [0, 0.4].$$

Its largest element is $0.4$, so $0.7 \Rightarrow_G 0.4 = 0.4$.
For the drastic t-norm at $x = 0.5$, $y = 0$, every $z < 1$ is good and $z = 1$ is not, so there is no largest element.
Watch out: the set $\{ z : z * x \le y \}$ is always an interval starting at $0$, and the only question is whether it contains its right end.

### L3 human

For fixed $x$, the map $f(z) = z * x$ is monotone on the complete chain $[0, 1]$.
A monotone map between complete lattices has a right adjoint exactly when it preserves all joins.
On a chain, preserving joins of nonempty sets is the same as left-continuity, and the join of the empty set is $0 = f(0)$.
The same pattern returns for [[residuated lattices|E337A6WVH3]] in algebraic logic, where residuation is an axiom and the existence question disappears.
