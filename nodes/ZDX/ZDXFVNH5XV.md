---
tag: ZDXFVNH5XV
kind: example
name: The core of a subgroup of order 8 in S4
msc: ["20B30"]
topics: [E1506A5A55]
audience: ug2
instance_of: [0GETX79CJN]
uses: [0515A6D2Y1, 0PMRQJVTME, 0H11ZPX4ND, 0J438GAC8K, 0ZTGMDNVTB]
sources:
  - url: https://en.wikipedia.org/wiki/Core_(group_theory)
    locator: The normal core
---

## Example

In the [[symmetric group|0515A6D2Y1]] $S_4$, compose permutations from right to left.
Let $V_4 = \{e, (1\,2)(3\,4), (1\,3)(2\,4), (1\,4)(2\,3)\}$, a copy of the [[Klein four-group|0PMRQJVTME]].
Let $P = V_4 \cup (1\,2)V_4 = V_4 \cup \{(1\,2), (3\,4), (1\,3\,2\,4), (1\,4\,2\,3)\}$.
This $P$ is a subgroup of order $8$ by [[the theorem on HN|0TXWV1JGG1]].
Then the [[normal core|0GETX79CJN]] of $P$ in $S_4$ is $V_4$.

1. $V_4$ is normal in $S_4$. By the [[classification of conjugacy classes in S_n|0J438GAC8K]], conjugation keeps the cycle type, and $V_4$ contains $e$ and all three products of two disjoint transpositions.
2. So $V_4 = gV_4g^{-1} \subseteq gPg^{-1}$ for each $g \in S_4$. Thus $V_4 \subseteq \operatorname{core}_{S_4}(P)$.
3. Conjugation by $(2\,3)$ sends $(1\,2)$ to $(1\,3)$, $(3\,4)$ to $(2\,4)$, $(1\,3\,2\,4)$ to $(1\,2\,3\,4)$ and $(1\,4\,2\,3)$ to $(1\,4\,3\,2)$. So $P' = (2\,3)P(2\,3)^{-1} = V_4 \cup \{(1\,3), (2\,4), (1\,2\,3\,4), (1\,4\,3\,2)\}$.
4. The [[intersection|0ZTGMDNVTB]] $P \cap P'$ is $V_4$, because the four elements outside $V_4$ in $P$ are not in $P'$.
5. So $\operatorname{core}_{S_4}(P) \subseteq P \cap P' = V_4$.
6. By steps 2 and 5, $\operatorname{core}_{S_4}(P) = V_4$.

## Remarks

$P$ has $[S_4 : P] = 3$ cosets, so the core has index at most $3! = 6$ in $S_4$.
Here the index of the core is $24/4 = 6$, so the bound is attained.
The action of $S_4$ on the three cosets of $P$ gives a homomorphism $S_4 \to S_3$ with kernel $V_4$.
This homomorphism is surjective, so $S_4/V_4 \cong S_3$.
There is a third conjugate, $(2\,4)P(2\,4)^{-1} = V_4 \cup \{(1\,4), (2\,3), (1\,3\,4\,2), (1\,2\,4\,3)\}$.
It is not needed for the computation, because two conjugates already meet in $V_4$.
The subgroup $P$ is a copy of the [[dihedral group|0JZ27DMJ5D]] $D_4$ of order $8$.

## Explanations

### L1 human

The group $P$ has eight permutations of four objects.
Four of them are the double swaps, such as "swap $1$ with $2$ and swap $3$ with $4$".
If we rename the four objects, $P$ moves to a different subgroup of order $8$.
The double swaps stay inside every renamed copy, and nothing else does.
So the normal core of $P$ is the group of the four double swaps.

### L2 human

The method has two halves.
First we find a normal subgroup inside $P$, which gives a lower bound for the core.
Then we intersect a few conjugates, which gives an upper bound.
When the two bounds agree, the computation is complete.
The lower bound comes from step 1: a union of conjugacy classes that is a subgroup is a normal subgroup.
The upper bound comes from steps 3 and 4.
A trap is to use the normal subgroup $K = \{e, (1\,2), (3\,4), (1\,2)(3\,4)\}$ of $P$ as the lower bound.
$K$ is normal in $P$, but it is not normal in $S_4$, so it is not inside the core ([[a normal subgroup of P that is not the core|CXK7VSCTNG]]).
