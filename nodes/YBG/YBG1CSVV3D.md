---
tag: YBG1CSVV3D
kind: proof
name: Proof of the product formula for the order of HK by counting pairs
msc: ["20D60"]
topics: [1VHQWXC64D]
audience: ug1
proves: 08PY4GNAPK
uses: [G5S1M9, 0X1JXT47GA, 0PT52XQZD7, 0ZTGMDNVTB, 0C81YBVTWH]
methods: [0F8YBHF2W3, 0NTF6DMVAP]
sources:
  - url: https://proofwiki.org/wiki/Order_of_Subgroup_Product
  - url: https://en.wikipedia.org/wiki/Product_of_group_subsets
    locator: Product of subgroups
---

## Proof

Let $G$ be a [[group|G5S1M9]] with identity $e$, and let $H$ and $K$ be finite [[subgroups|0X1JXT47GA]] of $G$.
We count the pairs $(h, k)$ in $H \times K$, sorted by their product $hk$.

1. By definition, the [[product|0PT52XQZD7]] is $HK = \{hk : h \in H, k \in K\}$.
2. Define $f \colon H \times K \to HK$ by $f(h, k) = hk$, on the [[Cartesian product|0C81YBVTWH]] $H \times K$.
3. By step 1, $f$ is surjective. Thus $HK$ is finite, because $H \times K$ is finite.
4. The [[intersection $H \cap K$ is a subgroup|0ZTGMDNVTB]] of $G$. It contains $e$, so $|H \cap K| \ge 1$.
5. Fix $z \in HK$, and write $z = h_0 k_0$ with $h_0 \in H$ and $k_0 \in K$.
6. Let $F_z = \{(h, k) \in H \times K : hk = z\}$ be the set of pairs with product $z$.
7. We claim that $F_z = \{(h_0 x, x^{-1} k_0) : x \in H \cap K\}$.
8. Let $x \in H \cap K$. Then $h_0 x \in H$ and $x^{-1} k_0 \in K$, because $H$ and $K$ are subgroups.
9. The product of this pair is $h_0 x x^{-1} k_0 = h_0 k_0 = z$. Thus the pair is in $F_z$.
10. Conversely, let $(h, k) \in F_z$, so $hk = h_0 k_0$. Put $x = h_0^{-1} h$. Then $x \in H$.
11. Multiply $hk = h_0 k_0$ by $h_0^{-1}$ on the left and by $k^{-1}$ on the right. This gives $h_0^{-1} h = k_0 k^{-1}$.
12. Thus $x = k_0 k^{-1}$ is also in $K$, so $x \in H \cap K$.
13. From $x = h_0^{-1} h$ we get $h = h_0 x$. From $x = k_0 k^{-1}$ we get $k = x^{-1} k_0$. This proves the claim.
14. The map $x \mapsto (h_0 x, x^{-1} k_0)$ from $H \cap K$ to $F_z$ is surjective, by the claim.
15. This map is injective, because $h_0 x = h_0 x'$ gives $x = x'$ by cancellation.
16. Thus $|F_z| = |H \cap K|$ for each $z \in HK$.
17. The sets $F_z$ with $z \in HK$ are pairwise disjoint, because each pair has only one product.
18. Their union is $H \times K$, because each pair $(h, k)$ lies in $F_{hk}$.
19. By steps 16 to 18, $|H| \cdot |K| = |H \times K| = \sum_{z \in HK} |F_z| = |HK| \cdot |H \cap K|$.
20. Divide by $|H \cap K| \ge 1$. This gives $|HK| = |H| \, |K| / |H \cap K|$.

This proves the product formula.

## Idea

Each element of $HK$ is a product $hk$, in general in several ways.
A factor $x \in H \cap K$ can move across the middle: the pair $(h, k)$ becomes $(hx, x^{-1}k)$, with the same product.
These moves give all the pairs with a given product, so each element of $HK$ is counted exactly $|H \cap K|$ times among the $|H| \, |K|$ pairs.

## Variants

A [[second proof|BEYJE2N47J]] writes $HK$ as a union of left cosets $hK$ and counts these cosets with Lagrange's theorem.
A third proof uses the action of $H \times K$ on $G$ by $(h, k) \cdot g = hgk^{-1}$.
The orbit of $e$ is $HK$, and the stabiliser of $e$ is isomorphic to $H \cap K$.
The [[orbit-stabiliser theorem|0E2HSCKZ6C]] then gives the formula.
