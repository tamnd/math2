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
We try to form "$\R^2 / S$" with the rule $u \sim v$ when $u - v \in S$, and we check where it fails.

1. $S$ is not a [[subspace|0EPTJA5QV4]], since $(0, 0) \notin S$.
2. Reflexivity fails: $(0, 0) - (0, 0) = (0, 0) \notin S$, so $(0, 0) \not\sim (0, 0)$.
3. Symmetry fails: $(0, 1) - (0, 0) = (0, 1) \in S$, so $(0, 1) \sim (0, 0)$, but $(0, 0) - (0, 1) = (0, -1) \notin S$.
4. Transitivity fails: $(0, 2) \sim (0, 1)$ and $(0, 1) \sim (0, 0)$, but $(0, 2) - (0, 0) = (0, 2) \notin S$.
5. So $\sim$ is not an equivalence relation, and there are no classes to form a [[quotient space|0SVR29SV1V]].

## Remarks

The translates $v + S$ do cover the plane by the horizontal lines $y = c$.
But these are exactly the cosets of the subspace $L = \R(1, 0)$ parallel to $S$, so the meaningful quotient is $\R^2 / L$.
The rule "$v + S = w + S$ if and only if $v - w \in S$" fails: $(0, 0) + S = (5, 0) + S$, while $(5, 0) - (0, 0) \notin S$.
A second failure, for a set that contains $0$: with $T$ the union of the two axes, $(1, 0) \sim 0$ and $0 \sim (0, 1)$, but $(1, 0) - (0, 1) = (1, -1) \notin T$.

## Explanations

### L1 human

To divide by a set, the set must contain $0$ and be closed under the operations.
A line that misses the origin fails the first test.

### L2 human

Each axiom of an equivalence relation matches one property of a subspace.
Reflexivity needs $0 \in S$, symmetry needs $-S \subseteq S$, and transitivity needs $S + S \subseteq S$.
The line $y = 1$ fails all three.
