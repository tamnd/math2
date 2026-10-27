---
tag: 00BWV5CKCF
kind: statement
role: proposition
name: Finite intersection property
aliases: [compactness-via-the-finite-intersection-property]
msc: [54D30]
uses: [00R0X1WGPX, 0G5AV9Q4RR, 0P6PMJB4MA]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_intersection_property
    locator: Compactness
inventory: [HQC84QWJ4M]
---

## Statement

Let $X$ be a [[topological space|0CNQXVBHCX]] and let $K \subseteq X$.
Then $K$ is [[compact|00R0X1WGPX]] if and only if it has the property that follows.
Let $(F_i)_{i \in I}$ be a family of [[closed subsets|0G5AV9Q4RR]] of $X$ with $K \cap F_{i_1} \cap \cdots \cap F_{i_n} \neq \emptyset$ for all finitely many indices $i_1, \ldots, i_n \in I$.
Then also $K \cap \bigcap_{i \in I} F_i \neq \emptyset$.

## Remarks

A family of sets has the finite intersection property when each finite subfamily has a nonempty intersection.
Proof: take complements. The sets $X \setminus F_i$ cover $K$ if and only if $K \cap \bigcap_i F_i = \emptyset$. Then use [[compactness via open covers|0P6PMJB4MA]].
For $K = X$: a space is compact if and only if each family of closed sets with the finite intersection property has nonempty intersection.
[[Cantor's intersection theorem|0EZBG8SKJM]] is a special case.

## Explanations

### L1 human

This is the dual form of compactness, with closed sets instead of open sets.
Suppose that each finite subfamily of the closed sets has a common point in $K$. Then the whole family has a common point in $K$.
