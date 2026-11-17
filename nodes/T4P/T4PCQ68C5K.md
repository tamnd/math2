---
tag: T4PCQ68C5K
kind: example
name: The alternating group A3 is normal in S3
msc: ["20B30"]
topics: [E1506A5A55]
audience: ug1
instance_of: [0CB0DX5BVV]
illustrates: [0V547YQRMV, 01E7SWYJX3]
uses: [0Z5905Q73D, 0515A6D2Y1, 0DTXBQPA2S, 0ZKPH2BD1T]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_subgroup
    locator: Examples
  - url: https://en.wikipedia.org/wiki/Alternating_group
    locator: Basic properties
---

## Example

Let $S_3$ be the [[symmetric group|0515A6D2Y1]] on $\{1, 2, 3\}$.
We use [[cycle notation|0ZKPH2BD1T]] and compose permutations from right to left, so $\sigma\tau$ means first $\tau$, then $\sigma$.
Let $A_3 = \{e, (1\,2\,3), (1\,3\,2)\}$ be the [[alternating group|0Z5905Q73D]] of degree $3$, and let $T = \{(1\,2), (1\,3), (2\,3)\}$.
We show that $A_3$ is [[normal|0CB0DX5BVV]] in $S_3$ in three ways.

1. $A_3$ is a subgroup: $(1\,2\,3)^2 = (1\,3\,2)$ and $(1\,2\,3)^3 = e$, so $A_3 = \langle (1\,2\,3) \rangle$.
2. $|S_3| = 6$ and $|A_3| = 3$, so $A_3$ has [[index|0DTXBQPA2S]] $2$. So $A_3$ is normal, because [[subgroups of index two are normal|0V547YQRMV]].
3. Directly with cosets: for $g \in A_3$, $gA_3 = A_3 = A_3g$.
4. For $g = (1\,2)$: $gA_3 = \{(1\,2), (2\,3), (1\,3)\} = T$, because $(1\,2)(1\,2\,3) = (2\,3)$ and $(1\,2)(1\,3\,2) = (1\,3)$.
5. Also $A_3g = \{(1\,2), (1\,3), (2\,3)\} = T$, because $(1\,2\,3)(1\,2) = (1\,3)$ and $(1\,3\,2)(1\,2) = (2\,3)$.
6. For $g = (1\,3)$ or $g = (2\,3)$, the cosets $gA_3$ and $A_3g$ have $3$ elements and do not meet $A_3$. The only such subset of $S_3$ is $T$, so $gA_3 = T = A_3g$.
7. So $gA_3 = A_3g$ for each $g \in S_3$, and $A_3$ is normal by [[normality via cosets|01E7SWYJX3]].
8. Directly with conjugates: conjugation keeps the order of an element. The elements of order $1$ or $3$ in $S_3$ are exactly the elements of $A_3$. So $gA_3g^{-1} \subseteq A_3$ for each $g$.

## Remarks

$A_3$ is also the kernel of the sign homomorphism $S_3 \to \{1, -1\}$, so it is normal because [[kernels are normal|0C9ZKYSPYR]].
The two cosets $A_3$ and $T$ form the quotient group $S_3/A_3$, a group of order $2$.
In contrast, the subgroup $\{e, (1\,2)\}$ of $S_3$ is not normal ([[a subgroup of order two in S3 is not normal|XD0WBC1MWB]]).
So $S_3$ has normal subgroups of order $1$, $3$ and $6$, and no normal subgroup of order $2$.

## Explanations

### L1 human

The six moves of three cups are of two kinds: the three swaps of two cups, and the three turns, where "do nothing" counts as a turn.
The turns form a subgroup.
A renaming of the cups sends a turn to a turn, so the turns form a normal subgroup.

### L2 human

The fastest of the three proofs is step 2, because the index is $2$.
Step 8 is the method that works in general: a subgroup that is a union of conjugacy classes is normal.
The left and right cosets agree as sets, but the elements do not commute.
For example, $(1\,2)(1\,2\,3) = (2\,3)$, but $(1\,2\,3)(1\,2) = (1\,3)$.
So $gA_3 = A_3g$ does not mean that $g$ commutes with the elements of $A_3$.
