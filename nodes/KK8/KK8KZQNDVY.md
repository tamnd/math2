---
tag: KK8KZQNDVY
kind: definition
name: Partition of unity
msc: [58A05, 54D20]
defines: NH739XXVXK
uses: [0CQHFPGJ45, 0X3WGX95FE, 049PXYHW1T, DZ297MMGV8, F45VQ47GPV]
sources:
  - url: https://en.wikipedia.org/wiki/Partition_of_unity
---

## Definition

Let $X$ be a [[topological space|0CQHFPGJ45]].
For a function $\rho \colon X \to \R$, its support $\operatorname{supp} \rho$ is the closure of $\set{x \in X : \rho(x) \neq 0}$.
A *partition of unity* on $X$ is a family $(\rho_i)_{i \in I}$ of [[continuous functions|0X3WGX95FE]] $\rho_i \colon X \to [0, 1]$ such that:

1. the family of supports $(\operatorname{supp} \rho_i)_{i \in I}$ is [[locally finite|DZ297MMGV8]]: each point of $X$ has a neighbourhood that meets only finitely many of them;
2. $\sum_{i \in I} \rho_i(x) = 1$ for every $x \in X$.

Let $(U_i)_{i \in I}$ be an [[open cover|049PXYHW1T]] of $X$ with the same index set.
The partition of unity is *subordinate* to $(U_i)_{i \in I}$ if $\operatorname{supp} \rho_i \subset U_i$ for every $i$.
If $X$ is a [[smooth manifold|F45VQ47GPV]] and every $\rho_i$ is smooth, it is a *smooth partition of unity*.

## Remarks

Example on $\R$ with the cover $U_1 = (-\infty, 1)$ and $U_2 = (-1, \infty)$.
Let $\rho_1(x) = 1$ for $x \le -1/2$, $\rho_1(x) = 1/2 - x$ for $-1/2 \le x \le 1/2$, and $\rho_1(x) = 0$ for $x \ge 1/2$, and let $\rho_2 = 1 - \rho_1$.
Both are continuous with values in $[0, 1]$, the sum is $1$, and $\operatorname{supp} \rho_1 = (-\infty, 1/2] \subset U_1$ and $\operatorname{supp} \rho_2 = [-1/2, \infty) \subset U_2$.
Replacing the linear piece by a smooth monotone transition gives a smooth partition of unity.

Non-example: the constant functions $\rho_1 = \rho_2 = 1/4$ on $\R$ are continuous with locally finite supports, but their sum is $1/2$, so clause 2 fails.

Clause 1 makes the sum in clause 2 a finite sum near each point, so it is continuous, or smooth in the smooth case.
Every paracompact Hausdorff space has a partition of unity subordinate to any open cover.
Every smooth manifold has a smooth partition of unity subordinate to any open cover; the proof uses bump functions and second countability.

## Explanations

### L1 human

A partition of unity is a family of continuous functions with values in $[0,1]$ that add up to $1$, where near each point only finitely many of them are nonzero.
