---
tag: ~cae7d72f
kind: statement
role: proposition
name: Product formula for the order of HK
msc: [20D60]
uses: [~89bfda2d, ~32db75ea, ~93dcd132]
sources:
  - url: https://en.wikipedia.org/wiki/Product_of_group_subsets
    locator: Product of subgroups
---

## Statement

Let $G$ be a [[group|G5S1M9]] and let $H$ and $K$ be finite [[subgroups|~b600248b]] of $G$.
Then the [[product|~133a4882]] $HK$ has exactly $\dfrac{|H| \, |K|}{|H \cap K|}$ elements.

## Remarks

The formula holds also when $HK$ is not a subgroup.
The proof counts the pairs $(h, k)$: two pairs $(h, k)$ and $(h', k')$ give the same product exactly when $h' = hx$ and $k' = x^{-1}k$ for some $x \in H \cap K$.
For example, two distinct subgroups of order $2$ in $S_3$ meet in $\{e\}$, and their product has $2 \cdot 2 / 1 = 4$ elements.

## Explanations

### L1 human

Each product $hk$ can be written in several ways, because you can move an element of $H \cap K$ from one factor to the other.
Each element of $HK$ has exactly $|H \cap K|$ such ways.
So you divide the number of pairs, $|H| \, |K|$, by $|H \cap K|$.
