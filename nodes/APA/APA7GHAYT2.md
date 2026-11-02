---
tag: APA7GHAYT2
kind: definition
name: Semiring of sets
msc: [28A05]
defines: PYH82FMXQ2
uses: [0SJ3RX9TXA, 0HBRW4E6G1, 07KVB4JSC7, 4W9NM803BB]
sources:
  - url: https://en.wikipedia.org/wiki/Ring_of_sets
---

## Definition

Let $X$ be a [[set|0SJ3RX9TXA]].
A *semiring of sets* on $X$ is a family $\mathcal{S}$ of subsets of $X$ such that:

1. $\varnothing \in \mathcal{S}$.
2. If $A, B \in \mathcal{S}$, then the [[intersection|0HBRW4E6G1]] $A \cap B$ is in $\mathcal{S}$.
3. If $A, B \in \mathcal{S}$, then there are finitely many pairwise disjoint sets $C_1, \ldots, C_n \in \mathcal{S}$ such that $A \setminus B$ is their [[union|07KVB4JSC7]] $C_1 \cup \cdots \cup C_n$.

## Remarks

The half-open intervals $[a, b)$ with $a, b \in \R$ form a semiring on $\R$, where $[a, b) = \varnothing$ when $b \le a$.
For clause 2, $[a, b) \cap [c, d) = [\max(a, c), \min(b, d))$.
For clause 3, when $c < d$, $[a, b) \setminus [c, d) = [a, \min(b, c)) \cup [\max(a, d), b)$, a union of two disjoint half-open intervals.
The open intervals $(a, b)$, together with $\varnothing$, do not form a semiring, since clause 3 fails.
Indeed $(0, 3) \setminus (1, 2) = (0, 1] \cup [2, 3)$ is not open, while a finite union of open intervals is open.
By clause 2 a semiring is a [[π-system|4W9NM803BB]].
The finite disjoint unions of members of a semiring form the smallest ring of sets that contains it.
