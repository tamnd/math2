---
tag: 6G8WNXTJAN
kind: problem
name: Knapsack problem
msc: [90C27, 90C10, 68Q17]
uses: [FJPER80BJC, R3FXF08WBH, JGZWHWA8P8, EX0FMF4CN1, PYMHHM5Z6F]
about: [FJPER80BJC]
sources:
  - url: https://en.wikipedia.org/wiki/Knapsack_problem
same_as:
  wikidata: Q864457
  wikipedia: Knapsack problem
history:
  posed_by: "G. B. Mathews"
  first_stated: "1897"
  notes: "Mathews studied the problem in his 1897 paper On the partition of numbers, the earliest known formulation; according to folklore the name was suggested by Tobias Dantzig. Karp listed the decision version among his 21 NP-complete problems in 1972."
---

## Problem

Let $n \ge 1$ be the number of items.
Item $i$ has a positive integer weight $w_i$ and a nonnegative value $v_i$, for $i = 1, \dots, n$.
Let $W$ be a positive integer, the capacity.
The *0-1 knapsack problem* asks for a set $S \subseteq \set{1, \dots, n}$ with $\sum_{i \in S} w_i \le W$ that makes the total value $\sum_{i \in S} v_i$ as large as possible.
In the decision version, a number $V$ is also given, and the question is whether some such $S$ has total value at least $V$.

## Remarks

The decision version is [[NP-complete|JGZWHWA8P8]].
It contains the [[subset sum problem|EX0FMF4CN1]] as the special case $v_i = w_i$ and $V = W$.
[[Dynamic programming|R3FXF08WBH]] solves the problem in $O(nW)$ steps.
Let $m(i, c)$ be the best value using only items $1, \dots, i$ with capacity $c$.
Then $m(i, c) = \max(m(i-1, c), \, v_i + m(i-1, c - w_i))$, where the second option is allowed only when $w_i \le c$.
This bound is polynomial in $W$ but not in the number of digits of $W$, so the algorithm is pseudo-polynomial.
For every $\varepsilon > 0$ there is a polynomial-time algorithm that returns a value at least $(1 - \varepsilon)$ times the optimum, by rounding the values and running a dynamic program.
In the fractional version, a part $x_i \in [0, 1]$ of each item $i$ may be taken.
That version is solved by taking items in decreasing order of $v_i / w_i$, and it is the [[linear programming relaxation|PYMHHM5Z6F]] of the 0-1 version.
Variants allow several copies of each item (the unbounded knapsack problem) or several knapsacks.

## Explanations

### L1 human

A hiker can carry at most $W$ kilograms and must choose among objects, each with a weight and a value.
The question is which objects to pack to get the most value without going over the limit.
For example, with capacity $5$ and items of weight and value $(2, 3)$, $(3, 4)$, $(4, 5)$, the best choice is the first two items, with weight $5$ and value $7$.
Many budget questions have this form: limited money or space, and options with costs and gains.
No fast method is known that always finds the best choice, but good methods exist when the numbers are not too large.
