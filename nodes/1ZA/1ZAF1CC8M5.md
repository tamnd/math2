---
tag: 1ZAF1CC8M5
kind: definition
name: Topological group structure of a vector space
msc: [46A03, 22A05]
defines: SQ6APWZBTR
sources:
  - url: https://en.wikipedia.org/wiki/Topological_group
---

## Definition

Let $\mathbb{K}$ be $\R$ or $\C$, and let $E$ be a topological vector space over $\mathbb{K}$.
The *topological group structure* of $E$ is the additive group $(E, +)$ together with the topology of $E$.
It is a commutative topological group: the maps $(x, y) \mapsto x + y$ from $E \times E$ to $E$ and $x \mapsto -x$ from $E$ to $E$ are continuous.

## Remarks

The map $x \mapsto -x$ is continuous because it is scalar multiplication by $-1$.
For each $a \in E$ the translation $x \mapsto x + a$ is a homeomorphism of $E$, with inverse $x \mapsto x - a$.
So a set $U$ is a neighbourhood of $a$ if and only if $U - a$ is a neighbourhood of $0$.
Example: $\R^n$ with its Euclidean topology is a commutative topological group under addition, since addition and negation are continuous functions of the coordinates.
Non-example: give $\R$ the topology whose open sets are $\emptyset$, $\R$ and the intervals $(a, \infty)$.
This is not a topological group, because $x \mapsto -x$ is not continuous: the preimage of $(0, \infty)$ is $(-\infty, 0)$, which is not open.
The topological group structure gives a uniform structure on $E$; a net $(x_i)$ is Cauchy when $x_i - x_j$ tends to $0$.
