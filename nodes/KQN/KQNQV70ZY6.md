---
tag: KQNQV70ZY6
kind: definition
name: Strategic dominance
msc: [91A10]
defines: 9BF72YM075
uses: [5MZTZRC3CZ, P01KKHB155]
sources:
  - url: https://en.wikipedia.org/wiki/Strategic_dominance
---

## Definition

Let $G = (N, (S_i), (u_i))$ be a [[normal-form game|5MZTZRC3CZ]], let $i \in N$, and let $S_{-i}$ be the product of the $S_j$ for $j \ne i$.
Let $s_i, t_i \in S_i$.

1. $s_i$ *strictly dominates* $t_i$ if $u_i(s_i, s_{-i}) > u_i(t_i, s_{-i})$ for every $s_{-i} \in S_{-i}$.
2. $s_i$ *weakly dominates* $t_i$ if $u_i(s_i, s_{-i}) \ge u_i(t_i, s_{-i})$ for every $s_{-i} \in S_{-i}$, with strict inequality for at least one $s_{-i}$.

A strategy $t_i$ is *strictly dominated* if some strategy of $i$ strictly dominates it.
A strategy is *strictly dominant* if it strictly dominates every other strategy of $i$.

## Remarks

In a finite game one also lets a [[mixed strategy|P01KKHB155]] $\sigma_i$ dominate $t_i$, with $u_i(\sigma_i, s_{-i})$ in place of $u_i(s_i, s_{-i})$.
A pure strategy can be strictly dominated by a mixed strategy without being dominated by any pure strategy.
Example: in the prisoner's dilemma with $u_1(D, C) = 5 > 3 = u_1(C, C)$ and $u_1(D, D) = 1 > 0 = u_1(C, D)$, defection $D$ strictly dominates cooperation $C$.
Non-example: in matching pennies, $H$ is better than $T$ for player 1 against $H$ but worse against $T$.
So neither strategy dominates the other.
Iterated elimination of strictly dominated strategies gives the same result in every order of removal; for weak dominance the result can depend on the order.
