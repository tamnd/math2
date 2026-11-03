---
tag: 5K8P0H8XJT
kind: definition
name: Arrow–Debreu model
msc: [91B50, 91B24]
defines: SVGN7R3RDY
uses: [HGMHZSM0XQ, YTBPB52K27, JGP0Q56FRY]
sources:
  - url: https://en.wikipedia.org/wiki/Arrow%E2%80%93Debreu_model
---

## Definition

An *Arrow–Debreu economy* (private ownership economy) with $L$ goods, $I$ consumers and $J$ firms consists of:

1. for each consumer $i$, a consumption set $X_i \subseteq \R^L$, a [[preference relation|JGP0Q56FRY]] $\succsim_i$ on $X_i$ and an endowment $\omega_i \in \R^L$;
2. for each firm $j$, a production set $Y_j \subseteq \R^L$, whose elements are plans with positive entries for outputs and negative entries for inputs;
3. shares $\theta_{ij} \ge 0$, the part of firm $j$ owned by consumer $i$, with $\sum_{i} \theta_{ij} = 1$ for each $j$.

An *equilibrium* of this economy is a price vector $p \in \R^L$, $p \ne 0$, plans $y_j^* \in Y_j$ and bundles $x_i^* \in X_i$ such that:

1. each $y_j^*$ maximizes profit: $p \cdot y_j^* \ge p \cdot y_j$ for all $y_j \in Y_j$;
2. each $x_i^*$ is a $\succsim_i$-best element of the budget set $\set{x \in X_i : p \cdot x \le p \cdot \omega_i + \sum_{j} \theta_{ij} \, p \cdot y_j^*}$;
3. markets clear: $\sum_i x_i^* = \sum_i \omega_i + \sum_j y_j^*$.

## Remarks

Example: with no firms ($J = 0$), $X_i = \R^L_+$ and $\omega_i \in \R^L_+$, the model is an [[exchange economy|HGMHZSM0XQ]], and an equilibrium is a [[competitive equilibrium|YTBPB52K27]].
For two consumers with utility $\sqrt{x y}$ and endowments $(1, 0)$ and $(0, 1)$, the prices $(1, 1)$ and the bundles $(1/2, 1/2)$ for both consumers satisfy all three equilibrium clauses.

Non-example: take one consumer with endowment $(1, 0)$ of labour and food, who likes only food, and one firm with $Y = \set{(-a, b) : 0 \le b \le a}$, owned by the consumer.
At prices $(1, 2)$ the firm can earn $2b - a = a > 0$ by choosing $b = a$, without bound, so no plan maximizes profit and clause 1 fails.
At prices $(1, 1)$ the plan $(-1, 1)$ has zero profit, which is the maximum, and with the bundle $(0, 1)$ all three clauses hold.

In the full model, a good is a physical commodity at a given date, place and state of the world, so one set of prices covers all future contingencies.
Conditions under which an equilibrium exists are given in the [[existence theorem for competitive equilibrium|FNMV35HB1E]].
