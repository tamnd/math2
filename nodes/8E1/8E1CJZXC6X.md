---
tag: 8E1CJZXC6X
kind: definition
name: Dynamic programming
msc: [90C39, 68W40]
defines: R3FXF08WBH
uses: [9DMSG5HAQX, 0FYX44GP92, 0QV2JS9RJ3]
sources:
  - url: https://en.wikipedia.org/wiki/Dynamic_programming
---

## Definition

A *dynamic programming* algorithm for a function $F$ consists of:

1. a finite set $S$ of subproblems with a strict [[partial order|0QV2JS9RJ3]] $\prec$ on $S$ and a target subproblem $s^* \in S$;
2. a [[recurrence|0FYX44GP92]] that gives the value $v(s)$ of each $s \in S$ as an explicit function of $s$ and of the values $v(s')$ of finitely many $s' \prec s$;
3. a guarantee that $F(\text{input}) = v(s^*)$.

The [[algorithm|9DMSG5HAQX]] computes the values $v(s)$ in an order compatible with $\prec$, bottom-up in a table or top-down with memoization.
It stores each value once and returns $v(s^*)$.
Its running time is at most the sum over $s \in S$ of the cost of evaluating the recurrence at $s$.

## Remarks

The method pays off when subproblems overlap, that is, when the same $v(s')$ is needed for many $s$.
For optimization problems, the correctness of the recurrence in clause 2 rests on the principle of optimality: an optimal solution restricted to a subproblem is optimal for that subproblem.

Example: the longest common subsequence of strings $x = x_1 \cdots x_m$ and $y = y_1 \cdots y_n$.
Take $S = \set{0, \dots, m} \times \set{0, \dots, n}$ with $(i', j') \prec (i, j)$ when $i' \le i$, $j' \le j$ and $(i', j') \ne (i, j)$, and target $(m, n)$.
Then $v(i, 0) = v(0, j) = 0$, $v(i, j) = v(i-1, j-1) + 1$ if $x_i = y_j$, and $v(i, j) = \max(v(i-1, j), v(i, j-1))$ otherwise.
The table has $(m+1)(n+1)$ entries, each computed in constant time, so the algorithm runs in time $O(mn)$, while trying all subsequences of $x$ would take time exponential in $m$.

Non-example: a recurrence in which some $v(s)$ depends on itself through a cycle of dependencies, such as $v(s) = v(s) + 1$, fails clause 2.
It would need $s \prec s$, which a strict partial order forbids, so no evaluation order makes all the inputs of such a $v(s)$ available first.
