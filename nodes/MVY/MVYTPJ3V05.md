---
tag: MVYTPJ3V05
kind: definition
name: Sets of capacity zero
msc: [31B15, 31A15, 31C15]
defines: W9N1TR1X8P
uses: [0R6EWFKRCF, DBQXRTC0VN, 4YZVFGJVSZ, C95QJ7YH5T]
sources:
  - url: https://en.wikipedia.org/wiki/Capacity_of_a_set
---

## Definition

Let $n \ge 2$ and let $E \subseteq \R^n$.
For $n = 2$, identify $\R^2$ with $\C$ and let $\operatorname{cap}$ be the [[logarithmic capacity|DBQXRTC0VN]].
For $n \ge 3$, let $\operatorname{cap}$ be the Newtonian [[capacity|4YZVFGJVSZ]].
The set $E$ has *capacity zero* if $\operatorname{cap}(K) = 0$ for every [[compact set|0R6EWFKRCF]] $K \subseteq E$.

## Remarks

This is the condition that the inner capacity of $E$ vanishes.
For Borel sets it is equivalent to the vanishing of the outer capacity, by Choquet's capacitability theorem.

Example: in $\C$, a finite set $K$ has capacity zero, since every probability measure on $K$ has an atom and so has infinite logarithmic energy.
Every compact subset of a countable set is countable, and a countable compact set carries no atomless probability measure, so countable subsets of $\C$ also have capacity zero.

Non-example: the segment $[0, 1]$ in $\C$ does not have capacity zero, since it is compact with logarithmic capacity $1/4$.

A Borel set has capacity zero if and only if it is a [[polar set|C95QJ7YH5T]].
In $\R^n$, $n \ge 3$, a compact set with finite $(n-2)$-dimensional Hausdorff measure has capacity zero.
