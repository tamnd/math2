---
tag: 0V547YQRMV
kind: statement
role: proposition
name: Subgroups of index two are normal
msc: [20A05]
about: [0CB0DX5BVV, 0DTXBQPA2S]
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

### L2 agent

A subgroup $H$ is normal when $gH = Hg$ for each $g \in G$. In general this is a real condition. For a subgroup of index $2$ it is automatic.

The reason is that two cosets leave no choice:

1. The left cosets are $H$ and one other coset. Since the cosets partition $G$, the other coset is $G \setminus H$.
2. In the same way, the right cosets are $H$ and $G \setminus H$.
3. If $g \in H$, then $gH = H = Hg$.
4. If $g \notin H$, then $gH = G \setminus H = Hg$.

A worked example with $G = S_3$ and $H = A_3 = \{e, (1\,2\,3), (1\,3\,2)\}$:

1. $|S_3| = 6$ and $|A_3| = 3$, so the index is $2$.
2. For $g = (1\,2)$, the left coset $gA_3$ is the set of the three transpositions.
3. The right coset $A_3g$ is the same set. Thus $gA_3 = A_3g$.

The index two condition is sharp. The subgroup $\{e, (1\,2)\}$ of $S_3$ has index $3$, and it is not normal: $(1\,2\,3)H = \{(1\,2\,3), (1\,3)\}$, but $H(1\,2\,3) = \{(1\,2\,3), (2\,3)\}$.

Standard examples are $A_n$ in $S_n$, the rotations in a dihedral group, and $2\mathbb{Z}$ in $\mathbb{Z}$. A related fact is that a subgroup whose index is the smallest prime divisor of $|G|$ is also normal. The proof of that fact needs a group action.
