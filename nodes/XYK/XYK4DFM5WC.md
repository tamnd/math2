---
tag: XYK4DFM5WC
kind: proof
name: Proof of the subgroup criterion
msc: [20A05]
proves: 05N4TQKPH0
uses: [G5S1M9, 0N0PXCTYA7, 0D9NDGE9KP]
sources:
  - url: https://proofwiki.org/wiki/One-Step_Subgroup_Test
---

## Proof

1. Let $G$ be a [[group|G5S1M9]] with identity $e$, and let $H \subseteq G$.
2. Suppose $H$ is a [[subgroup|0N0PXCTYA7]] of $G$. Then $e \in H$, so $H$ is not empty.
3. Let $a, b \in H$. Since $H$ is a subgroup, $b^{-1} \in H$, and then $ab^{-1} \in H$ by closure under products.
4. Conversely, suppose $H$ is not empty and $ab^{-1} \in H$ for all $a, b \in H$.
5. Choose $a \in H$. Taking $b = a$ gives $e = aa^{-1} \in H$.
6. Let $b \in H$. Taking the pair $e, b$ gives $b^{-1} = eb^{-1} \in H$. So $H$ contains the inverse of each of its elements.
7. For $b \in G$ we have $b^{-1}b = e$, so $(b^{-1})^{-1} = b$ by [[uniqueness of inverses|0D9NDGE9KP]].
8. Let $a, b \in H$. By step 6, $b^{-1} \in H$. Taking the pair $a, b^{-1}$ gives $a(b^{-1})^{-1} = ab \in H$, by step 7.
9. By steps 5, 6 and 8, $H$ contains $e$ and is closed under products and inverses. So $H$ is a subgroup of $G$.

## Idea

The single condition $ab^{-1} \in H$ hides the three subgroup conditions. Use it with $a = b$ to get $e$, with $a = e$ to get inverses, and with $b$ replaced by $b^{-1}$ to get products.
