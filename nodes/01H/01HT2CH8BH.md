---
tag: 01HT2CH8BH
kind: statement
role: theorem
name: Equivalence classes form a partition
msc: ["03E20"]
uses: [082RMRSY26, 09CCE86A6D]
sources:
  - url: https://en.wikipedia.org/wiki/Partition_of_a_set
    locator: Partitions and equivalence relations
---

## Statement

Let $\sim$ be an [[equivalence relation|0SGTMBEWRF]] on a set $A$.
Then the set $\{[a] \mid a \in A\}$ of [[equivalence classes|082RMRSY26]] is a [[partition|09CCE86A6D]] of $A$.

## Remarks

Each class $[a]$ is nonempty, because $a \in [a]$ by reflexivity.
If $[a]$ and $[b]$ have a common element, then $a \sim b$ by symmetry and transitivity, so $[a] = [b]$.
The left cosets of a subgroup of a [[group|G5S1M9]] form such a partition. This fact is the key step in [[Lagrange's theorem|3C53TD]].

## Explanations

### L1 human

The three properties of an equivalence relation are exactly what you need to sort elements into classes.
Reflexivity puts each element in some class.
Symmetry and transitivity stop two classes from overlapping.
