---
tag: 0ZQJ7KEFQ5
kind: statement
role: proposition
name: Tower law for indices
aliases: [multiplicativity-of-the-index]
msc: [20A05]
uses: [04QEBF8S49]
sources:
  - url: https://en.wikipedia.org/wiki/Index_of_a_subgroup
    locator: Properties
---

## Statement

Let $G$ be a [[group|G5S1M9]], let $H$ be a [[subgroup|0X1JXT47GA]] of $G$, and let $K$ be a subgroup of $H$.
Then $[G : K] = [G : H] \cdot [H : K]$, where $[\cdot : \cdot]$ is the [[index|0DTXBQPA2S]].

## Remarks

The equation holds as an equation of cardinal numbers; in particular $[G : K]$ is finite if and only if $[G : H]$ and $[H : K]$ are both finite.
For example, in $(\mathbb{Z}, +)$ with $H = 2\mathbb{Z}$ and $K = 6\mathbb{Z}$, the indices are $[\mathbb{Z} : 6\mathbb{Z}] = 6 = 2 \cdot 3$.

## Explanations

### L1 human

Each coset of $H$ in $G$ splits into $[H : K]$ cosets of $K$.
So the number of cosets of $K$ is the number of cosets of $H$ times $[H : K]$.
It is like a box with several drawers, each with the same number of compartments.
