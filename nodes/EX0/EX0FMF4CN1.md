---
tag: EX0FMF4CN1
kind: problem
name: Subset sum problem
msc: [68Q17, 90C27]
uses: [JGZWHWA8P8, QQRA9GBW51]
about: [JGZWHWA8P8]
sources:
  - url: https://en.wikipedia.org/wiki/Subset_sum_problem
same_as:
  wikidata: Q1154420
  wikipedia: Subset sum problem
history:
  posed_by: "Richard M. Karp"
  first_stated: "1972"
  notes: "Karp listed the decision problem as one of his 21 NP-complete problems, under the name knapsack."
---

## Problem

An input consists of integers $a_1, \dots, a_n$ and an integer $T$, written in binary.
The *subset sum problem* asks whether some set $I \subseteq \set{1, \dots, n}$ satisfies
$$\sum_{i \in I} a_i = T.$$

## Remarks

The problem lies in [[NP|QQRA9GBW51]], since the set $I$ is a certificate that can be checked by one addition per element.
It is [[NP-complete|JGZWHWA8P8]].
For nonnegative $a_i$ and $T$, dynamic programming decides it in $O(nT)$ steps.
It records which sums up to $T$ can be formed from $a_1, \dots, a_k$, for $k = 1, \dots, n$.
This bound is polynomial in the value $T$ but not in its number of digits, so the problem is only weakly NP-complete.
The meet-in-the-middle method of Horowitz and Sahni decides it in about $2^{n/2}$ steps up to polynomial factors.

Example: for $a = (3, 34, 4, 12, 5, 2)$ and $T = 9$, the answer is yes, since $4 + 5 = 9$.
For $T = 30$ the answer is no: without $34$ the total is $26$, and with $34$ every sum exceeds $30$.

## Explanations

### L1 human

Given a pile of coins of various values, can one pick some of them that add up to an exact amount?
Checking a proposed pick is easy, but there are $2^n$ ways to pick from $n$ coins.
When the values are small, a table of all reachable totals answers the question quickly.
When the values are huge numbers, no fast method is known, and the problem is NP-complete.
