---
tag: 9ZVCJWYPB2
kind: definition
name: Moore family
msc: [06A15]
defines: 80GQXWM7BV
uses: [0BC7KX51Z8, 0839XNQXDK]
sources:
  - url: https://en.wikipedia.org/wiki/Closure_operator
---

## Definition

Let $X$ be a set and let $\mathcal{M}$ be a family of subsets of $X$, that is, a subset of the [[power set|0BC7KX51Z8]] of $X$.
The family $\mathcal{M}$ is a *Moore family* on $X$ when both conditions hold.

1. $X \in \mathcal{M}$.
2. For each nonempty subfamily $\mathcal{N} \subseteq \mathcal{M}$, the [[intersection|0839XNQXDK]] $\bigcap \mathcal{N}$ lies in $\mathcal{M}$.

## Remarks

The closed sets of a topological space $X$ form a Moore family: $X$ is closed, and any intersection of closed sets is closed.
The open sets of $\R$ do not: the open intervals $(-1/n, 1/n)$ for $n \ge 1$ have intersection $\set{0}$, which is not open.
If $\mathcal{M}$ is a Moore family, then $c(A) = \bigcap \set{M \in \mathcal{M} : A \subseteq M}$ is a [[closure operator|17FVAN6HXX]] on the subsets of $X$.
Its closed sets are exactly the members of $\mathcal{M}$.
Conversely, the closed sets of any closure operator on the subsets of $X$ form a Moore family.
With the convention that the empty intersection is $X$, the two conditions merge into one: $\mathcal{M}$ is closed under all intersections.
Other names are closure system and intersection-closed family.

## Explanations

### L1 human

A Moore family is a collection of subsets that contains the whole set and survives taking intersections.
Its members are the "closed" sets of a closure operator.
