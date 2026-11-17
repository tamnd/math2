---
tag: ~2bee9c8c
kind: proof
name: Proof of the product formula for the order of HK by counting cosets
msc: ["20D60"]
topics: [1VHQWXC64D]
audience: ug1
proves: 08PY4GNAPK
uses: [G5S1M9, 0X1JXT47GA, 0PT52XQZD7, 03DEH43F4H, 0ZTGMDNVTB, 0DKMBWTD7P, 3C53TD]
methods: [0NTF6DMVAP]
sources:
  - book: isbn:9780471433347
    locator: Section 3.2
  - url: https://en.wikipedia.org/wiki/Product_of_group_subsets
    locator: Product of subgroups
---

## Proof

Let $G$ be a [[group|G5S1M9]], and let $H$ and $K$ be finite [[subgroups|0X1JXT47GA]] of $G$.
We write the [[product|0PT52XQZD7]] $HK$ as a union of [[left cosets|03DEH43F4H]] of $K$, and we count these cosets.

1. For each $h \in H$, the left coset $hK = \{hk : k \in K\}$ is a subset of $HK$, by the definition of $HK$.
2. Each element $hk$ of $HK$ lies in the coset $hK$. Thus $HK = \bigcup_{h \in H} hK$.
3. Let $h, h' \in H$. Two left cosets satisfy $hK = h'K$ if and only if $h^{-1}h' \in K$, by the coset criterion.
4. The element $h^{-1}h'$ is always in $H$, because $H$ is a subgroup.
5. By steps 3 and 4, $hK = h'K$ if and only if $h^{-1}h' \in H \cap K$.
6. The [[intersection $H \cap K$ is a subgroup|0ZTGMDNVTB]] of $H$.
7. By the coset criterion in $H$, $h^{-1}h' \in H \cap K$ if and only if $h(H \cap K) = h'(H \cap K)$.
8. By steps 5 and 7, $hK = h'K$ if and only if $h(H \cap K) = h'(H \cap K)$.
9. Thus the rule $h(H \cap K) \mapsto hK$ is a well defined injective map. It goes from the left cosets of $H \cap K$ in $H$ to the cosets $hK$ with $h \in H$.
10. The map in step 9 is surjective, because each $hK$ with $h \in H$ is the image of $h(H \cap K)$.
11. Thus the number of distinct cosets $hK$ with $h \in H$ is the index $[H : H \cap K]$.
12. By [[Lagrange's theorem|3C53TD]] for the finite group $H$, $[H : H \cap K] = |H| / |H \cap K|$.
13. Distinct left cosets of $K$ are disjoint, and [[each has $|K|$ elements|0DKMBWTD7P]].
14. By steps 2, 11 and 13, $HK$ is the disjoint union of $[H : H \cap K]$ sets of size $|K|$.
15. Thus $|HK| = [H : H \cap K] \cdot |K| = |H| \, |K| / |H \cap K|$, by step 12.

This proves the product formula.

## Idea

The set $HK$ is the union of the left cosets $hK$ with $h$ in $H$.
Two elements of $H$ give the same coset of $K$ exactly when they lie in the same coset of $H \cap K$.
Thus $HK$ consists of $[H : H \cap K]$ disjoint cosets of $K$, each with $|K|$ elements.

## Variants

Steps 1 to 11 do not use that $H$ and $K$ are finite.
Thus, for any subgroups $H$ and $K$ of any group, $HK$ is the disjoint union of $[H : H \cap K]$ left cosets of $K$.
The [[first proof|YBG1CSVV3D]] counts the pairs $(h, k)$ with a given product instead of cosets.
