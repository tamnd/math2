---
tag: 0W77CVBCHQ
kind: definition
name: Normal subgroup
msc: [20A05]
defines: 0CB0DX5BVV
uses: [0N0PXCTYA7, 0D6WHTTH7T]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_subgroup
    locator: Definitions
inventory: [F3D99PH13A]
---

## Definition

Let $G$ be a [[group|G5S1M9]] and let $N$ be a [[subgroup|0X1JXT47GA]] of $G$.
The subgroup $N$ is normal in $G$ when $gng^{-1} \in N$ for all $g \in G$ and all $n \in N$.
The notation is $N \trianglelefteq G$.

## Remarks

Equivalently, $gNg^{-1} = N$ for each $g \in G$, that is, $N$ equals each of its [[conjugates|0H11ZPX4ND]].
Each group $G$ has the normal subgroups $\{e\}$ and $G$.
In the symmetric group $S_3$, the subgroup $\{e, (1\,2\,3), (1\,3\,2)\}$ is normal, but the subgroup $\{e, (1\,2)\}$ is not.

## Explanations

### L1 human

A normal subgroup does not move when you conjugate it by any element of the group.
This is the condition that lets you divide the group by the subgroup and get a new group.
In an abelian group, every subgroup is normal.
