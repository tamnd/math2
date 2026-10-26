---
tag: ~cebdb41e
kind: statement
role: theorem
name: Product of cyclic groups is cyclic iff the orders are coprime
msc: [20K01]
uses: [~d2c30e2f, ~5b224101, ~47dae8e0]
sources:
  - url: https://en.wikipedia.org/wiki/Cyclic_group
    locator: Additional properties
---

## Statement

Let $G$ and $H$ be finite [[cyclic groups|~333626b6]] of orders $m$ and $n$.
Let $G \times H$ be the group of pairs $(g, h)$ with $g \in G$ and $h \in H$, with the operation $(g, h)(g', h') = (gg', hh')$.
Then $G \times H$ is cyclic if and only if $\gcd(m, n) = 1$.

## Remarks

When $\gcd(m, n) = 1$, the group $\mathbb{Z}/mn\mathbb{Z}$ is isomorphic to $\mathbb{Z}/m\mathbb{Z} \times \mathbb{Z}/n\mathbb{Z}$, and this is a form of the Chinese remainder theorem.
When $\gcd(m, n) > 1$, each element of $G \times H$ has order at most $\operatorname{lcm}(m, n) < mn$.
For example, $\mathbb{Z}/12\mathbb{Z}$ is isomorphic to $\mathbb{Z}/3\mathbb{Z} \times \mathbb{Z}/4\mathbb{Z}$, but $\mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/6\mathbb{Z}$ is not cyclic.

## Explanations

### L1 human

The order of a pair $(g, h)$ is the least common multiple of the orders of $g$ and $h$.
A pair of generators has order $mn$ exactly when $m$ and $n$ have no common factor.
For example, $(1, 1)$ in $\mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/3\mathbb{Z}$ has order $6$, so this group is cyclic.
