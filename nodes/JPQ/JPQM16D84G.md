---
tag: JPQM16D84G
kind: definition
name: Derived set
msc: [54A05]
defines: 8ZAPAPYJFG
uses: [0CQHFPGJ45, 0E3X7TXS67, 0ZCY0Z80B6, 0QEAJB91GZ]
sources:
  - url: https://en.wikipedia.org/wiki/Derived_set_(mathematics)
---

## Definition

Let $X$ be a [[topological space|0CQHFPGJ45]] and let $A \subseteq X$.
The *derived set* of $A$ is the set $A'$ of all [[limit points|0E3X7TXS67]] of $A$.
So $x \in A'$ if and only if every [[neighbourhood|0ZCY0Z80B6]] of $x$ contains a point of $A$ different from $x$.

## Remarks

The [[closure|0QEAJB91GZ]] of $A$ is $\overline{A} = A \cup A'$.
In a [[T1 space|0NW6CH38YR]], the derived set $A'$ is always [[closed|0ZCK8DQYN1]].

Example: in $\R$, let $A = \set{1/n : n \ge 1}$.
Each $1/n$ has a neighbourhood that meets $A$ only in $1/n$, so $1/n \notin A'$.
Every interval $(-\varepsilon, \varepsilon)$ contains $1/n$ for large $n$, so $0 \in A'$.
Thus $A' = \set{0}$.

Example: the derived set of $\Q$ in $\R$ is $\R$, and the derived set of $\Z$ in $\R$ is $\emptyset$.

Non-example: in $\R$, the point $2$ is not in the derived set of $A = \set{2} \cup [3, 4]$.
The neighbourhood $(1, 5/2)$ of $2$ contains no point of $A$ other than $2$, so the condition fails.
