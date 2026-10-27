---
tag: 4N1WKH2ZQV
kind: proof
name: Proof that subgroups of index two are normal
msc: [20A05]
proves: 0V547YQRMV
uses: [04QEBF8S49, 01E7SWYJX3, 03DEH43F4H]
sources:
  - url: https://en.wikipedia.org/wiki/Index_of_a_subgroup
    locator: Properties
---

## Proof

1. Let $H$ be a subgroup of a group $G$ with [[index|04QEBF8S49]] $2$.
2. There are two [[left cosets|03DEH43F4H]]. One is $H$, so the other is $G \setminus H$.
3. In the same way, there are two right cosets, $H$ and $G \setminus H$.
4. Let $g \in G$. If $g \in H$, then $gH = H = Hg$.
5. If $g \notin H$, then $gH \ne H$ and $Hg \ne H$. Thus $gH = G \setminus H = Hg$.
6. So $gH = Hg$ for all $g \in G$, and [[$H$ is normal|01E7SWYJX3]].

## Idea

With only two cosets, one of them is the subgroup and the other is its complement. This is true on the left and on the right, so the left and right cosets agree.
