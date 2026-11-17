---
tag: E7SWCC1JR5
kind: example
name: A core-free subgroup of S3
msc: ["20B30"]
topics: [E1506A5A55]
audience: ug2
instance_of: [0GETX79CJN]
uses: [0515A6D2Y1, 0H11ZPX4ND, 0ZTGMDNVTB]
sources:
  - url: https://en.wikipedia.org/wiki/Core_(group_theory)
    locator: The normal core
---

## Example

In the [[symmetric group|0515A6D2Y1]] $S_3$, let $H = \{e, (1\,2)\}$.
Compose permutations from right to left, and conjugate by $g$ as $gHg^{-1}$.
The [[normal core|0GETX79CJN]] of $H$ in $S_3$ is $\{e\}$.

1. Conjugation by $g$ sends the transposition $(a\,b)$ to $(g(a)\,g(b))$.
2. For $g = (1\,3)$ we get $(1\,3)(1\,2)(1\,3)^{-1} = (3\,2) = (2\,3)$. So $gHg^{-1} = \{e, (2\,3)\}$.
3. For $g = (2\,3)$ we get $(2\,3)(1\,2)(2\,3)^{-1} = (1\,3)$. So $gHg^{-1} = \{e, (1\,3)\}$.
4. Every [[conjugate|0H11ZPX4ND]] of $H$ has order $2$, and $S_3$ has exactly three subgroups of order $2$. Steps 2 and 3 found all three.
5. The [[intersection|0ZTGMDNVTB]] $\{e, (1\,2)\} \cap \{e, (1\,3)\} \cap \{e, (2\,3)\}$ is $\{e\}$.
6. So $\operatorname{core}_{S_3}(H) = \{e\}$, and $H$ is core-free.

## Remarks

The action of $S_3$ on the three left cosets of $H$ has kernel $\operatorname{core}_{S_3}(H) = \{e\}$.
So this action is faithful, and it is the usual action of $S_3$ on $\{1, 2, 3\}$, because $H$ is the stabiliser of $3$.
Compare the subgroup $A_3 = \{e, (1\,2\,3), (1\,3\,2)\}$: it is normal, so its core is $A_3$.

## Explanations

### L1 human

The subgroup $\{e, (1\,2)\}$ swaps $1$ and $2$.
If we rename the numbers, the swap becomes a swap of two other numbers.
The only permutation that stays inside all the renamed copies is the identity.
So the largest normal subgroup inside $H$ is the trivial subgroup.

### L2 human

The computation uses one rule: conjugation keeps the cycle type and renames the entries.
So it is enough to know where $g$ sends $1$ and $2$.
A shortcut is possible here.
The core is a normal subgroup of $S_3$ inside $H$, so its order divides $2$.
The normal subgroups of $S_3$ are $\{e\}$, $A_3$ and $S_3$, and only $\{e\}$ has order $1$ or $2$.
So the core is $\{e\}$ without any computation of conjugates.
A trap is to say that the core is $H$ because $H$ is normal in itself.
The core asks for normality in $S_3$, not in $H$.
