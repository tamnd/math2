---
tag: WV3PBEK76J
kind: definition
name: Pseudovariety
msc: ["08B99", "20M07"]
defines: XR4DPKX7T1
uses: [N5KE7FH6CX, WJ73XYBNE4]
sources:
  - url: https://en.wikipedia.org/wiki/Variety_(universal_algebra)
---

## Definition

Let $\sigma$ be an algebraic signature.
A class $V$ of finite $\sigma$-algebras is a *pseudovariety* if it satisfies these three conditions.

1. If $A \in V$ and $B$ is a homomorphic image of $A$, that is, isomorphic to a [[quotient algebra|N5KE7FH6CX]] of $A$, then $B \in V$.
2. If $A \in V$ and $B$ is a [[subalgebra|7CHG6SD365]] of $A$, then $B \in V$.
3. If $A_1, \ldots, A_n \in V$ with $n \ge 0$, then the [[direct product|WJ73XYBNE4]] $A_1 \times \cdots \times A_n$ is in $V$; for $n = 0$ it is the one-element algebra.

## Remarks

Example: the class of finite abelian groups is a pseudovariety.
Quotients and subgroups of finite abelian groups are finite and abelian, and so are finite products.

Non-example: the class of finite cyclic groups fails condition 3.
The product $\Z / 2\Z \times \Z / 2\Z$ is finite but not cyclic, since each of its elements has order at most $2$.

For each variety $W$, the finite members of $W$ form a pseudovariety, but not every pseudovariety arises this way.
A standard pseudovariety of semigroups is the class of finite aperiodic semigroups, those with only trivial subgroups.
By Eilenberg's variety theorem, pseudovarieties of finite monoids correspond to varieties of regular languages; aperiodic monoids correspond to star-free languages by [[Schützenberger's theorem|YSXPVN8G0D]].
