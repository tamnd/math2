---
tag: XXRXVA6RBZ
kind: problem
name: Set cover problem
msc: [90C27, 68W25, 68Q17]
uses: [FJPER80BJC, JGZWHWA8P8, PSM6NKYJB8, 4WEVBDQ8SR, 0AHKWBQSWV]
about: [FJPER80BJC]
sources:
  - url: https://en.wikipedia.org/wiki/Set_cover_problem
same_as:
  wikidata: Q1192100
  wikipedia: Set cover problem
history:
  posed_by: "Richard M. Karp"
  first_stated: "1972"
  notes: "Karp listed the decision version among his 21 NP-complete problems in 1972, the earliest well-documented statement as a complexity problem. Covering formulations were already studied in operations research in the late 1960s."
---

## Problem

Let $U$ be a finite set, the universe, and let $S_1, \dots, S_m$ be subsets of $U$ whose union is $U$.
A *cover* is a set $C \subseteq \set{1, \dots, m}$ with $\bigcup_{j \in C} S_j = U$.
The *set cover problem* asks for a cover with the least number of elements $\abs{C}$.
In the weighted version, each $S_j$ has a cost $c_j \ge 0$, and the goal is a cover of least total cost $\sum_{j \in C} c_j$.
In the decision version, an integer $k$ is given, and the question is whether a cover with $\abs{C} \le k$ exists.

## Remarks

The decision version is [[NP-complete|JGZWHWA8P8]].
The [[vertex cover|0AHKWBQSWV]] problem is the special case where $U$ is the edge set of a graph and $S_v$ is the set of edges at a vertex $v$.
The [[greedy algorithm|PSM6NKYJB8]] repeatedly picks the set that covers the most elements not yet covered.
It returns a cover with at most $H(n) \cdot \mathrm{OPT}$ sets, where $n = \abs{U}$ and $H(n) = 1 + \frac12 + \cdots + \frac1n \le 1 + \ln n$.
So greedy is an [[approximation algorithm|4WEVBDQ8SR]] with ratio about $\ln n$.
Up to lower-order terms this is best possible: for every $\varepsilon > 0$, no polynomial-time algorithm achieves ratio $(1 - \varepsilon) \ln n$ unless $\mathrm{P} = \mathrm{NP}$.
As an integer program, set cover asks to minimize $\sum_j c_j x_j$ subject to $\sum_{j : u \in S_j} x_j \ge 1$ for all $u \in U$ and $x_j \in \set{0, 1}$.

## Explanations

### L1 human

You want to cover a list of needs with as few packages as possible, where each package covers some of the needs.
For example, with $U = \set{1, 2, 3, 4, 5}$ and sets $\set{1, 2, 3}$, $\set{2, 4}$, $\set{3, 4}$, $\set{4, 5}$, the two sets $\set{1, 2, 3}$ and $\set{4, 5}$ already cover everything.
Picking at each step the package that covers the most new needs is a good rule, though not always optimal.
The problem models choosing sites for services, tests for faults, or staff with given skills.
