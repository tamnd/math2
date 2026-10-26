---
tag: 0V547YQRMV
kind: statement
role: proposition
name: Subgroups of index two are normal
msc: [20A05]
uses: [01E7SWYJX3, 04QEBF8S49]
sources:
  - url: https://en.wikipedia.org/wiki/Index_of_a_subgroup
    locator: Properties
---

## Statement

Let $G$ be a [[group|G5S1M9]] and let $H$ be a [[subgroup|0X1JXT47GA]] of $G$ of [[index|0DTXBQPA2S]] $2$.
Then $H$ is [[normal|0CB0DX5BVV]] in $G$.

## Remarks

For $g \notin H$, the left cosets are $H$ and $gH = G \setminus H$, and the right cosets are $H$ and $Hg = G \setminus H$.
Thus $gH = Hg$ for each $g \in G$, and [[the coset criterion|01E7SWYJX3]] applies.
For example, the alternating group $A_n$ has index $2$ in the symmetric group $S_n$, and thus it is normal.

## Explanations

### L1 human

When a subgroup has only two cosets, one coset is the subgroup and the other is everything else.
This is true for the left cosets and for the right cosets.
So the left and right cosets agree, and the subgroup is normal.
