---
tag: 8AH8QSQ1H0
kind: definition
name: Rationalizability
msc: [91A26, 91A10]
defines: MJEBSVPNN3
uses: [5MZTZRC3CZ, P01KKHB155, QS6VCNJK60, 9BF72YM075]
sources:
  - url: https://en.wikipedia.org/wiki/Rationalizable_strategy
---

## Definition

Let $G = (N, (S_i), (u_i))$ be a finite [[normal-form game|5MZTZRC3CZ]].
Define sets $R_i^k \subseteq S_i$ by induction on $k \ge 0$.

1. $R_i^0 = S_i$ for each $i \in N$.
2. $R_i^{k+1}$ is the set of $s_i \in R_i^k$ such that $s_i$ is a [[best response|QS6VCNJK60]] to some profile $\sigma_{-i}$.
3. In clause 2, each $\sigma_j$ with $j \ne i$ is a [[mixed strategy|P01KKHB155]] with support in $R_j^k$.

A pure strategy $s_i$ is *rationalizable* if $s_i \in R_i^k$ for all $k$.

## Remarks

The sets decrease and $S_i$ is finite, so they become constant after finitely many steps; each final set is nonempty.
Example: in the prisoner's dilemma $C$ is never a best response, so $R_i^1 = \set{D}$ and only $D$ is rationalizable.
Non-example: in the same game $C$ is not rationalizable, since it fails clause 2 already at $k = 0$.
For two players the rationalizable strategies are exactly those that survive iterated elimination of [[strictly dominated|9BF72YM075]] strategies, where domination by mixed strategies is allowed.
With three or more players the two sets can differ, because the beliefs in clause 3 are independent across opponents.
