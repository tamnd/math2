---
tag: TFKF40Y7EY
kind: definition
name: Envy-freeness
msc: [91B32, 91B15]
defines: P3GPD0S0J7
uses: [X1X9TZ8GAR, PR11BZQQPG]
sources:
  - url: https://en.wikipedia.org/wiki/Envy-freeness
---

## Definition

Let $C$ be a set of resources and $N = \set{1, \dots, n}$ a finite set of agents.
Each agent $i$ has a valuation $V_i$ that assigns a value $V_i(X)$ to each admissible piece $X \subseteq C$.
An allocation $(X_1, \dots, X_n)$ of $C$, as in [[fair division|X1X9TZ8GAR]], is *envy-free* if
$$V_i(X_i) \ge V_i(X_j) \quad \text{for all } i, j \in N.$$
Agent $i$ *envies* agent $j$ when $V_i(X_j) > V_i(X_i)$.

## Remarks

Example: let $C = [0, 1]$ and let $V_1, V_2$ be [[measures|PR11BZQQPG]] with densities $1$ and $2x$.
For $X_1 = [0, 1/2]$ and $X_2 = (1/2, 1]$: $V_1(X_1) = V_1(X_2) = 1/2$ and $V_2(X_2) = 3/4 > 1/4 = V_2(X_1)$, so the allocation is envy-free.

Non-example: for $X_1 = [0, 3/4]$ and $X_2 = (3/4, 1]$: $V_2(X_2) = 1 - 9/16 = 7/16$ and $V_2(X_1) = 9/16$.
Agent $2$ envies agent $1$, so the allocation is not envy-free.

For indivisible goods, $(X_1, \dots, X_n)$ is *envy-free up to one good* if, whenever $i$ envies $j$, removing some single good from $X_j$ removes the envy.
