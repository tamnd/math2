---
tag: NJSAK2QACC
kind: definition
name: Fair division
msc: [91B32, 91A06]
defines: X1X9TZ8GAR
uses: [PR11BZQQPG, 08QMKTWF9T]
sources:
  - url: https://en.wikipedia.org/wiki/Fair_division
---

## Definition

A *fair division problem* consists of:

1. a set $C$ of resources, either a measurable space (a divisible good, such as a cake) or a finite set (indivisible goods);
2. a finite set $N = \set{1, \dots, n}$ of agents;
3. for each agent $i$, a valuation $V_i$ that assigns a value $V_i(X) \ge 0$ to each admissible piece $X \subseteq C$.

Typical valuations are a [[measure|PR11BZQQPG]] on $C$, or an additive function on the subsets of a finite set.

An *allocation* is a tuple $(X_1, \dots, X_n)$ of pairwise disjoint admissible pieces whose union is $C$.
It is a [[partition|08QMKTWF9T]] of $C$ into $n$ labelled pieces, some of which may be empty.
*Fair division* is the study of allocations that satisfy fairness criteria, such as:

- *proportionality*: $V_i(X_i) \ge V_i(C)/n$ for every agent $i$;
- *envy-freeness*: $V_i(X_i) \ge V_i(X_j)$ for all agents $i, j$.

## Remarks

Example: let $C = [0, 1]$ with $n = 2$ agents, where $V_1$ is Lebesgue measure and $V_2$ has density $2x$.
The allocation $X_1 = [0, 1/2]$, $X_2 = (1/2, 1]$ gives $V_1(X_1) = 1/2$ and $V_2(X_2) = 1 - 1/4 = 3/4$, so it is proportional.

Non-example: with the same agents, the allocation $X_1 = (1/2, 1]$, $X_2 = [0, 1/2]$ gives $V_2(X_2) = 1/4 < 1/2$, so it is not proportional.

With additive valuations, envy-freeness implies proportionality: summing $V_i(X_i) \ge V_i(X_j)$ over $j$ gives $n V_i(X_i) \ge V_i(C)$.
