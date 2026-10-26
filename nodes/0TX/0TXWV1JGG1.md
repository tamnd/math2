---
tag: 0TXWV1JGG1
kind: statement
role: proposition
name: Product of a subgroup and a normal subgroup is a subgroup
msc: [20A05]
uses: [0NS1YTGM19, 0W77CVBCHQ]
sources:
  - url: https://en.wikipedia.org/wiki/Product_of_group_subsets
    locator: Product of subgroups
---

## Statement

Let $G$ be a [[group|G5S1M9]], let $H$ be a [[subgroup|0X1JXT47GA]] of $G$, and let $N$ be a [[normal subgroup|0CB0DX5BVV]] of $G$.
Then the [[product|0PT52XQZD7]] $HN$ is a subgroup of $G$, and $HN = NH$.

## Remarks

If $H$ is also normal, then $HN$ is normal in $G$.
The proof uses $hN = Nh$ for each $h \in H$, so that $HN = \bigcup_{h \in H} hN = \bigcup_{h \in H} Nh = NH$.
This product appears in the second isomorphism theorem.

## Explanations

### L1 human

The product of two subgroups can fail to be a subgroup, but not when one of them is normal.
A normal subgroup lets you move its elements past other elements, at the cost of changing them inside the subgroup.
So products of the form $hn$ stay of that form when you multiply them.
