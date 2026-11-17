---
tag: HT83D4SAP8
kind: proof
name: Proof of the intersection lemma for subgroups
msc: ["20A05"]
topics: [BAVE5RN4EE]
audience: ug1
proves: 0ZTGMDNVTB
uses: [G5S1M9, 0X1JXT47GA]
methods: [0NTF6DMVAP, 0J0XBKG64S]
sources:
  - url: https://proofwiki.org/wiki/Intersection_of_Subgroups_is_Subgroup
  - book: isbn:9780471433347
    locator: Section 2.1
---

## Proof

Let $G$ be a [[group|G5S1M9]] with identity $e$.
A [[subgroup|0X1JXT47GA]] is a subset that contains $e$ and is closed under products and inverses.

Part 1, the intersection.

1. Let $(H_i)_{i \in I}$ be subgroups of $G$ with $I$ nonempty, and put $L = \bigcap_{i \in I} H_i$.
2. Since $I$ is nonempty, choose $i_0 \in I$. Then $L \subseteq H_{i_0} \subseteq G$, so $L$ is a subset of $G$.
3. Each $H_i$ is a subgroup, so $e \in H_i$ for every $i \in I$. Hence $e \in L$.
4. Let $a, b \in L$. For each $i \in I$, we have $a, b \in H_i$, so $ab \in H_i$ because $H_i$ is closed under products. Hence $ab \in L$.
5. Let $a \in L$. For each $i \in I$, we have $a \in H_i$, so $a^{-1} \in H_i$ because $H_i$ is closed under inverses. Hence $a^{-1} \in L$.
6. By steps 2 to 5, $L$ is a subgroup of $G$.

Part 2, the union of two subgroups.

7. Let $H$ and $K$ be subgroups of $G$. Suppose $H \subseteq K$. Then $H \cup K = K$, which is a subgroup. The case $K \subseteq H$ is the same with $H$ and $K$ exchanged.
8. Conversely, suppose that $H \cup K$ is a subgroup. For a contradiction, suppose that $H \not\subseteq K$ and $K \not\subseteq H$.
9. Then there is an element $h \in H$ with $h \notin K$, and there is an element $k \in K$ with $k \notin H$.
10. Both $h$ and $k$ lie in $H \cup K$. This set is a subgroup, so it is closed under products, and $hk \in H \cup K$.
11. Case $hk \in H$. Since $h^{-1} \in H$, we get $k = h^{-1}(hk) \in H$. This contradicts $k \notin H$.
12. Case $hk \in K$. Since $k^{-1} \in K$, we get $h = (hk)k^{-1} \in K$. This contradicts $h \notin K$.
13. Both cases give a contradiction. So $H \subseteq K$ or $K \subseteq H$.

Part 3, no group is the union of two proper subgroups.

14. Suppose that $G = H \cup K$, where $H$ and $K$ are subgroups of $G$.
15. Then $H \cup K = G$ is a subgroup of $G$. By part 2, $H \subseteq K$ or $K \subseteq H$.
16. If $H \subseteq K$, then $G = H \cup K = K$. If $K \subseteq H$, then $G = H$.
17. So one of $H$ and $K$ equals $G$, and the two subgroups are not both proper.

This proves the three parts.
$\blacksquare$

## Idea

Each subgroup condition says that some element lies in the set.
If such a statement holds in every $H_i$, it holds in the intersection.
For a union, take $h$ only in $H$ and $k$ only in $K$.
The product $hk$ must lie in one of the two subgroups, and then we can cancel $h$ or $k$ to get a contradiction.

## Variants

Part 1 also follows from the one-step [[subgroup criterion|05N4TQKPH0]].
The set $L$ is nonempty because $e \in L$.
For $a, b \in L$ and each $i \in I$, the criterion in $H_i$ gives $ab^{-1} \in H_i$, so $ab^{-1} \in L$.
