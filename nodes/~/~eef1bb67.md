---
tag: ~eef1bb67
kind: definition
name: Submodule
msc: [16D10]
defines: ~047aa607
uses: [~89d9b1b1]
sources:
  - url: https://en.wikipedia.org/wiki/Module_(mathematics)
    locator: Submodules and homomorphisms
---

## Definition

Let $R$ be a ring with identity element and let $M$ be a left [[module|~4b7b3b49]] over $R$.
A *submodule* of $M$ is a subset $N \subseteq M$ such that:

1. $N$ is a subgroup of the abelian group $(M, +)$.
2. $rx \in N$ for all $r \in R$ and $x \in N$.

## Remarks

A submodule is a module over $R$ with the restricted operations.
The submodules of $R$, as a left module over itself, are the left ideals of $R$.
The $\Z$-submodules of an abelian group are its subgroups, and over a field the submodules are the [[subspaces|~92144797]].
Intersections and sums of submodules are submodules.

## Explanations

### L1 human

A submodule is a module inside a bigger module.
It contains the sums and the scalar multiples of its elements.
For example, the even integers are a submodule of $\Z$ over $\Z$.
