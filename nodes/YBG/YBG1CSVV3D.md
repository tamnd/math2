---
tag: YBG1CSVV3D
kind: proof
name: Proof of the product formula for the order of HK by counting pairs
msc: [20D60]
proves: 08PY4GNAPK
uses: [G5S1M9, 0N0PXCTYA7, 0NS1YTGM19, 0ZTGMDNVTB, 0C81YBVTWH]
sources:
  - url: https://proofwiki.org/wiki/Order_of_Subgroup_Product
---

## Proof

We count the pairs $(h, k)$ grouped by their product $hk$.

1. Let $G$ be a [[group|G5S1M9]] with identity $e$, and let $H$ and $K$ be finite [[subgroups|0N0PXCTYA7]] of $G$.
2. By definition, the [[product|0NS1YTGM19]] is $HK = \set{hk : h \in H, k \in K}$.
3. Define $f \colon H \times K \to HK$ by $f(h, k) = hk$, on the [[Cartesian product|0C81YBVTWH]]. By step 2, $f$ is surjective.
4. Since the [[intersection of subgroups is a subgroup|0ZTGMDNVTB]], $H \cap K$ is a subgroup of $G$. It contains $e$, so $\abs{H \cap K} \geq 1$.
5. Fix $z \in HK$ and write $z = h_0 k_0$ with $h_0 \in H$ and $k_0 \in K$. Let $F_z = \set{(h, k) \in H \times K : hk = z}$.
6. Claim: $F_z = \set{(h_0 x, x^{-1} k_0) : x \in H \cap K}$.
7. Let $x \in H \cap K$. Then $h_0 x \in H$ and $x^{-1}k_0 \in K$, since $H$ and $K$ are subgroups. Their product is $h_0 x x^{-1} k_0 = z$. So the pair lies in $F_z$.
8. Conversely, let $(h, k) \in F_z$, so $hk = h_0k_0$. Put $x = h_0^{-1}h$, which lies in $H$.
9. From $hk = h_0k_0$ we get $h_0^{-1}h = k_0k^{-1}$. So $x = k_0 k^{-1}$ also lies in $K$, and $x \in H \cap K$.
10. Then $h = h_0x$. Also $x^{-1} = kk_0^{-1}$, so $x^{-1}k_0 = k$. This proves the claim.
11. The map $x \mapsto (h_0x, x^{-1}k_0)$ from $H \cap K$ to $F_z$ is surjective by the claim. It is injective, since $h_0x = h_0x'$ gives $x = x'$.
12. So $\abs{F_z} = \abs{H \cap K}$ for each $z \in HK$.
13. The sets $F_z$ for $z \in HK$ are pairwise disjoint, since each pair has only one product. Their union is $H \times K$, by step 3.
14. Hence $\abs{H} \, \abs{K} = \abs{H \times K} = \sum_{z \in HK} \abs{F_z} = \abs{HK} \, \abs{H \cap K}$.
15. Dividing by $\abs{H \cap K} \geq 1$ gives $\abs{HK} = \dfrac{\abs{H} \, \abs{K}}{\abs{H \cap K}}$.

## Idea

Every element of $HK$ is a product $hk$, usually in several ways. One can move a factor $x \in H \cap K$ across the middle, replacing $(h, k)$ by $(hx, x^{-1}k)$, and these are the only other ways. So each element of $HK$ is counted exactly $\abs{H \cap K}$ times among the $\abs{H}\,\abs{K}$ pairs.
