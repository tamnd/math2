---
tag: XJPVHVVKD9
kind: statement
role: theorem
name: Inclusion–exclusion formula for elements with none of the properties
msc: [05A05]
uses: [05099E1NMJ, 0FF7726C7P]
sources:
  - url: https://github.com/mitchkeller/applied-combinatorics/blob/ebd95d6bd59e23c633c65cf560bcb93efa912aae/source/s_inclusion-exclusion_statement.ptx#L41
    locator: source/s_inclusion-exclusion_statement.ptx:41
---

## Statement

Let $X$ be a finite set. Let $\mathcal{P} = \{p_1, \dots, p_m\}$ be a set of $m$ properties that each element of $X$ may or may not have.

For a subset $S \subseteq [m] = \{1, \dots, m\}$, let $N(S)$ be the number of elements of $X$ that have every property $p_i$ with $i \in S$. In particular $N(\varnothing) = |X|$.

Then the number of elements of $X$ that have none of the properties in $\mathcal{P}$ is
$$\sum_{S \subseteq [m]} (-1)^{|S|} N(S).$$

## Remarks

This is the sieve form of the [[inclusion–exclusion principle|0FF7726C7P]]. The sizes are [[cardinalities of finite sets|05099E1NMJ]].

Take $A_i$ to be the set of elements of $X$ with property $p_i$. Then $N(S)$ is the size of the intersection of the $A_i$ for $i \in S$, and the formula counts the complement of the union of the $A_i$ in $X$.
