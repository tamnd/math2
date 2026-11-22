---
tag: E3MQ50YQNR
kind: example
name: No quotient by a line that misses the origin
msc: ["15A03"]
topics: [QHKTJ89V6S]
audience: ug1
not_instance_of:
  - target: 0BR3FY5Q8M
    note: S is the line y = 1 in R², which is not a subspace, and the relation u − v ∈ S is not reflexive since 0 is not in S
illustrates: [YYH67TQ9GV]
uses: [0SVR29SV1V, 0EPTJA5QV4]
sources:
  - url: https://en.wikipedia.org/wiki/Quotient_space_(linear_algebra)
    locator: Definition
---

## Example

Let $S = \{(x, 1) : x \in \R\}$, the line $y = 1$ in $\R^2$.
We try to form "$\R^2 / S$" with the rule $u \sim v$ when $u - v \in S$, and we check where the attempt fails.

1. The set $S$ is not a [[subspace|0EPTJA5QV4]], since $(0, 0) \notin S$.
2. Reflexivity fails.
   We have $(0, 0) - (0, 0) = (0, 0) \notin S$, so $(0, 0) \not\sim (0, 0)$.
3. Symmetry fails.
   We have $(0, 1) - (0, 0) = (0, 1) \in S$, so $(0, 1) \sim (0, 0)$.
   But $(0, 0) - (0, 1) = (0, -1) \notin S$, so $(0, 0) \not\sim (0, 1)$.
4. Transitivity fails.
   We have $(0, 2) \sim (0, 1)$ and $(0, 1) \sim (0, 0)$, since both differences are $(0, 1) \in S$.
   But $(0, 2) - (0, 0) = (0, 2) \notin S$.
5. So $\sim$ is not an equivalence relation, and there are no classes from which to build a [[quotient space|0SVR29SV1V]].

## Remarks

The translates $v + S$ still cover the plane: they are the horizontal lines $y = c$.
But these lines are exactly the cosets of the subspace $L = \R(1, 0)$, which is the line through $0$ parallel to $S$.
So the meaningful quotient is $\R^2 / L$, which is isomorphic to $\R$.
The rule "$v + S = w + S$ if and only if $v - w \in S$" fails for $S$.
For example, $(0, 0) + S$ and $(5, 0) + S$ are both the line $y = 1$, while $(5, 0) - (0, 0) = (5, 0) \notin S$.

Containing $0$ is not enough either.
Let $T$ be the union of the two coordinate axes, which contains $0$ and is closed under scalars.
Then $(1, 0) \sim (0, 0)$ and $(0, 0) \sim (0, -1)$, but $(1, 0) - (0, -1) = (1, 1) \notin T$, so transitivity fails because $T$ is not closed under addition.

## Explanations

### L1 human

To divide a space by a set, the set must contain the origin and be closed under adding and scaling.
A line that misses the origin fails the first test.
The fix is to divide by the parallel line through the origin instead.

### L2 human

Each axiom of an equivalence relation matches one property of a subspace.
Reflexivity needs $0 \in S$, symmetry needs $-s \in S$ for each $s \in S$, and transitivity needs $s + t \in S$ for all $s, t \in S$.
The line $y = 1$ fails all three: $0 \notin S$, $-(0, 1) = (0, -1) \notin S$, and $(0, 1) + (0, 1) = (0, 2) \notin S$.
So before forming any quotient, check first that you divide by a subspace.
