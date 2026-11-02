---
tag: 6HVDTYAWX1
kind: definition
name: Complete set of orthogonal idempotents
msc: [16U40]
defines: SS8T32TMEX
uses: [0894J980RK, 0X4JKZXJ86]
sources:
  - url: https://en.wikipedia.org/wiki/Idempotent_(ring_theory)
---

## Definition

Let $R$ be a [[ring|0894J980RK]] and let $n \ge 1$ be an integer.
A *complete set of orthogonal idempotents* of $R$ is a family $e_1, \dots, e_n$ of elements of $R$ such that:

1. each $e_i$ is an [[idempotent|0X4JKZXJ86]], that is, $e_i^2 = e_i$;
2. $e_i e_j = 0$ for all $i \ne j$;
3. $e_1 + \cdots + e_n = 1$.

## Remarks

Many authors also require each $e_i$ to be nonzero.
Example: in $M_n(K)$ over a field $K$, the diagonal matrix units $E_{11}, \dots, E_{nn}$ form a complete set of orthogonal idempotents.
The check: $E_{ii} E_{jj}$ equals $E_{ii}$ if $i = j$ and $0$ otherwise, and $E_{11} + \cdots + E_{nn} = I_n$.
Non-example: in $M_2(K)$, the family consisting of $E_{11}$ alone satisfies clauses 1 and 2 but not clause 3, since $E_{11} \ne I_2$.
For any idempotent $e$, the pair $e, 1 - e$ is a complete set of orthogonal idempotents.
A complete set of orthogonal idempotents gives a decomposition $R = Re_1 \oplus \cdots \oplus Re_n$ of $R$ as a left module over itself.
