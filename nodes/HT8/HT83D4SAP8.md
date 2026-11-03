---
tag: HT83D4SAP8
kind: proof
name: Proof that an intersection of subgroups is a subgroup
msc: [20A05]
proves: 0ZTGMDNVTB
uses: [G5S1M9, 0N0PXCTYA7]
sources:
  - url: https://proofwiki.org/wiki/Intersection_of_Subgroups_is_Subgroup
---

## Proof

1. Let $G$ be a [[group|G5S1M9]] with identity $e$. Let $(H_i)_{i \in I}$ be [[subgroups|0N0PXCTYA7]] of $G$ with $I$ nonempty, and put $K = \bigcap_{i \in I} H_i$.
2. Since $I$ is nonempty, choose $i_0 \in I$. Then $K \subseteq H_{i_0} \subseteq G$, so $K$ is a subset of $G$.
3. Each $H_i$ is a subgroup, so $e \in H_i$ for every $i \in I$. Hence $e \in K$.
4. Let $a, b \in K$. For each $i \in I$, $a, b \in H_i$, so $ab \in H_i$. Hence $ab \in K$.
5. Let $a \in K$. For each $i \in I$, $a \in H_i$, so $a^{-1} \in H_i$. Hence $a^{-1} \in K$.
6. By steps 2 to 5, $K$ is a subgroup of $G$.

## Idea

Each subgroup condition is a statement "this element lies in the set". If such a statement holds in every $H_i$, it holds in their intersection. The index set must be nonempty so that the intersection is taken inside $G$.
