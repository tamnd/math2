---
tag: W8VMC2C0W9
kind: definition
name: Divide and choose
msc: [91B32, 91A06]
defines: T0VDBHZW05
uses: [X1X9TZ8GAR, P3GPD0S0J7, KCVV28DH6R, PR11BZQQPG]
sources:
  - url: https://en.wikipedia.org/wiki/Divide_and_choose
---

## Definition

Let $C$ be a cake, as in [[fair cake-cutting|KCVV28DH6R]], shared by two agents.
Agent $i \in \set{1, 2}$ has a valuation $V_i$ that is a nonatomic probability [[measure|PR11BZQQPG]] on $C$.
*Divide and choose* is the following procedure.

1. Agent $1$ (the divider) partitions $C$ into two measurable pieces $P$ and $Q$ with $V_1(P) = V_1(Q) = 1/2$.
2. Agent $2$ (the chooser) takes a piece of larger value for her: $X_2 = P$ if $V_2(P) \ge V_2(Q)$, and $X_2 = Q$ otherwise.
3. Agent $1$ receives the other piece $X_1$.

## Remarks

The cut in step 1 exists because $V_1$ is nonatomic: on $C = [0, 1]$, the function $t \mapsto V_1([0, t])$ is continuous from $0$ to $1$, so it takes the value $1/2$.
The allocation is [[envy-free|P3GPD0S0J7]]: $V_1(X_1) = 1/2 = V_1(X_2)$ and $V_2(X_2) \ge V_2(X_1)$.
It is therefore proportional too, a [[fair division|X1X9TZ8GAR]] for two agents.

Example: on $C = [0, 1]$ let $V_1$ have density $1$ and $V_2$ density $2x$.
Agent $1$ cuts at $1/2$, agent $2$ values $[0, 1/2]$ at $1/4$ and $(1/2, 1]$ at $3/4$, so she takes $(1/2, 1]$.

Non-example: a cut into pieces of values $0.6$ and $0.4$ for the divider fails step 1.
The chooser may take the piece of value $0.6$ to the divider, who is left with $0.4 < 1/2$.
The chooser can do no worse than $1/2$ in any case.
