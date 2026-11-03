---
tag: J6KA8R1H5Z
kind: statement
role: theorem
name: Fundamental theorems of welfare economics
msc: [91B15, 91B50]
uses: [YTBPB52K27, JREVYHFY4T, HGMHZSM0XQ, JGP0Q56FRY, 02AS45T3H9]
about: [YTBPB52K27, JREVYHFY4T]
sources:
  - url: https://en.wikipedia.org/wiki/Fundamental_theorems_of_welfare_economics
same_as:
  wikidata: Q467205
  wikipedia: Fundamental theorems of welfare economics
---

## Statement

Let an [[exchange economy|HGMHZSM0XQ]] have $L$ goods and $I$ consumers with consumption sets $\R^L_+$, [[preference relations|JGP0Q56FRY]] $\succsim_i$ and endowments $\omega_i$, with total endowment $\bar\omega = \sum_i \omega_i$.
An allocation is feasible if $x_i \in \R^L_+$ for all $i$ and $\sum_i x_i = \bar\omega$.

1. (First welfare theorem.) Suppose that every $\succsim_i$ is locally nonsatiated. If $(p, x)$ is a [[competitive equilibrium|YTBPB52K27]], then the allocation $x$ is [[Pareto efficient|JREVYHFY4T]] among feasible allocations.
2. (Second welfare theorem.) Suppose that every $\succsim_i$ is continuous, convex and strongly monotone. Let $x^*$ be a Pareto efficient feasible allocation with $x^*_{i\ell} > 0$ for all $i$ and $\ell$. Replace the endowments by $\omega'_i = x^*_i$. Then there is a price vector $p$ with all entries positive such that $(p, x^*)$ is a competitive equilibrium of the new economy.

## Remarks

First theorem: suppose a feasible $y$ Pareto dominates $x$.
For each $i$ with $y_i \succsim_i x_i$, local nonsatiation gives $p \cdot y_i \ge p \cdot \omega_i$, and for the $j$ with $y_j \succ_j x_j$, optimality gives $p \cdot y_j > p \cdot \omega_j$.
Summing, $p \cdot \sum_i y_i > p \cdot \bar\omega$, which contradicts $\sum_i y_i = \bar\omega$.

Second theorem: the set of aggregate bundles $\sum_i y_i$ with $y_i \succ_i x^*_i$ for every $i$ is [[convex|02AS45T3H9]], as a sum of convex sets.
It does not contain $\bar\omega$, since $x^*$ is Pareto efficient.
A separating hyperplane between this set and $\bar\omega$ gives the price vector $p$.
Redistributing endowments to $x^*_i$ is the same as a lump-sum transfer of wealth $p \cdot x^*_i - p \cdot \omega_i$ to consumer $i$.

Example: with two consumers of utility $\sqrt{x y}$ and total endowment $(1, 1)$, the efficient allocation $x^*_1 = (1/4, 1/4)$, $x^*_2 = (3/4, 3/4)$ is supported by $p = (1, 1)$.

Convexity is needed in the second theorem.
Suppose one consumer has nonconvex preferences.
An efficient allocation can then be a point where that consumer's better set lies on no single side of any line through it.
Then no prices make it an equilibrium.
The first theorem needs no convexity, but it fails with externalities or with agents who do not take prices as given.

## Explanations

### L1 human

The first theorem says that a competitive market wastes nothing: once prices clear all markets, no reshuffling of goods can make someone better off without making someone worse off.
The second theorem says that any efficient outcome, however the cake is shared, can be reached by a market.
One first moves wealth between people and then lets them trade.
Together they separate the question of efficiency, which markets can handle, from the question of fairness, which is about the starting point.

### L2 human

The first theorem is the precise form of the invisible hand and is purely algebraic.
The second rests on convexity and a separating hyperplane, the same tool as in duality theory for convex optimization.
Both are stated for the [[Arrow–Debreu model|SVGN7R3RDY]] with production too, where firms maximize profit and production sets are convex in the second theorem.
Their failures guide the study of market failures: externalities, public goods, market power, and asymmetric information as in the [[market for lemons|2P8CK5HD0E]].
