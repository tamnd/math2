---
tag: ~a9ed74fa
kind: statement
role: proposition
name: Product of a subgroup and a normal subgroup is a subgroup
msc: [20A05]
uses: [~89bfda2d, ~4f5a4072]
sources:
  - url: https://en.wikipedia.org/wiki/Product_of_group_subsets
    locator: Product of subgroups
---

## Statement

Let $G$ be a [[group|G5S1M9]], let $H$ be a [[subgroup|~b600248b]] of $G$, and let $N$ be a [[normal subgroup|~ebf813cb]] of $G$.
Then the [[product|~133a4882]] $HN$ is a subgroup of $G$, and $HN = NH$.

## Remarks

If $H$ is also normal, then $HN$ is normal in $G$.
The proof uses $hN = Nh$ for each $h \in H$, so that $HN = \bigcup_{h \in H} hN = \bigcup_{h \in H} Nh = NH$.
This product appears in the second isomorphism theorem.

## Explanations

### L1 human

The product of two subgroups can fail to be a subgroup, but not when one of them is normal.
A normal subgroup lets you move its elements past other elements, at the cost of changing them inside the subgroup.
So products of the form $hn$ stay of that form when you multiply them.
