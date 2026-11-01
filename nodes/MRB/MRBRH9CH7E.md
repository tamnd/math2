---
tag: MRBRH9CH7E
kind: definition
name: Filter
msc: [54A20, "03E05"]
defines: 15PF73BKY6
uses: [00E0YZCERH, 0ZCY0Z80B6, 0CQHFPGJ45]
sources:
  - url: https://en.wikipedia.org/wiki/Filter_(mathematics)
---

## Definition

Let $X$ be a set.
A *filter* on $X$ is a family $\mathcal{F}$ of subsets of $X$ such that:

1. $X \in \mathcal{F}$.
2. $\emptyset \notin \mathcal{F}$.
3. If $A \in \mathcal{F}$ and $A \subseteq B \subseteq X$, then $B \in \mathcal{F}$.
4. If $A \in \mathcal{F}$ and $B \in \mathcal{F}$, then $A \cap B \in \mathcal{F}$.

## Remarks

Some authors, and Mathlib, drop clause 2.
Then the only family that satisfies clauses 1, 3 and 4 and contains $\emptyset$ is the [[power set|00E0YZCERH]] of $X$.
A filter in the sense above is then called a *proper* filter.

Example: for a point $x$ of a [[topological space|0CQHFPGJ45]] $X$, the [[neighbourhoods|0ZCY0Z80B6]] of $x$ form a filter $\mathcal{N}(x)$, the *neighbourhood filter* of $x$.
Clause 2 holds because each neighbourhood contains $x$, and clause 4 holds because the intersection of two neighbourhoods is a neighbourhood.

Example: on an infinite set $X$, the sets with finite complement form a filter, the *Fréchet filter*.
Clause 2 holds because $X$ is infinite, and clause 4 holds because the union of two finite sets is finite.

Example: for $a \in X$, the family $\set{A \subseteq X : a \in A}$ is a filter, the *principal filter* at $a$.

Non-example: on $\N$, the family of sets that contain $0$ or contain $1$ satisfies clauses 1, 2 and 3.
It fails clause 4: it contains $\set{0}$ and $\set{1}$, but not $\set{0} \cap \set{1} = \emptyset$.

A nonempty family $\mathcal{B}$ of nonempty subsets of $X$ is a *filter base* if the intersection of any two members contains a member.
The supersets of members of a filter base form a filter.
