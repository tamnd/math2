---
tag: H4QSPK0XTZ
kind: proof
name: Proof of the first isomorphism theorem
msc: ["20A05"]
topics: [E1506A5A55]
audience: ug1
proves: 0CXXJNG5B6
uses: [0C9ZKYSPYR, 0GJ83E78A5, 0N2P0XRTDF, 0S21GNW9ZB, 08MG7H8JW5]
methods: [0NTF6DMVAP, 01XM7JEKHY]
sources:
  - url: https://en.wikipedia.org/wiki/Isomorphism_theorems
    locator: Theorem A (groups)
  - url: https://en.wikipedia.org/wiki/Fundamental_theorem_on_homomorphisms
    locator: Proof
---

## Proof

We get the isomorphism from the universal property of the quotient group.

1. Let $\varphi \colon G \to H$ be a group homomorphism, and let $K = \ker \varphi$. Because $\varphi$ is a homomorphism, [[$K$ is a normal subgroup|0C9ZKYSPYR]] of $G$, so the quotient group $G/K$ exists. This step uses the hypothesis that $\varphi$ is a homomorphism.
2. The [[image|0S21GNW9ZB]] $\operatorname{im} \varphi$ is a subgroup of $H$, because $\varphi$ is a homomorphism.
3. We apply the [[universal property of the quotient group|0GJ83E78A5]] with $N = K$. Its hypothesis $N \subseteq \ker \varphi$ holds, because $N = K = \ker \varphi$.
4. By part 1 of the universal property, there is a homomorphism $\bar{\varphi} \colon G/K \to H$ with $\bar{\varphi}(gK) = \varphi(g)$ for each $g \in G$.
5. By part 2, the image of $\bar{\varphi}$ is $\operatorname{im} \varphi$.
6. By part 3, the kernel of $\bar{\varphi}$ is $K/K = \{kK : k \in K\}$. For $k \in K$ we get $kK = K$, so this kernel is $\{K\}$, the trivial subgroup of $G/K$.
7. A homomorphism with a trivial kernel is injective ([[this statement|0N2P0XRTDF]]). So $\bar{\varphi}$ is injective.
8. By step 5, each value of $\bar{\varphi}$ is in $\operatorname{im} \varphi$. So we can take $\operatorname{im} \varphi$ as the target, and we get a map $\bar{\varphi} \colon G/K \to \operatorname{im} \varphi$. It is still a homomorphism, because the product in $\operatorname{im} \varphi$ is the product in $H$.
9. With the target $\operatorname{im} \varphi$, the map $\bar{\varphi}$ is surjective by step 5, and it is injective by step 7.
10. A bijective homomorphism is an [[isomorphism|08MG7H8JW5]]. So $\bar{\varphi} \colon G/K \to \operatorname{im} \varphi$ is an isomorphism.
11. If $\varphi$ is surjective, then $\operatorname{im} \varphi = H$, so $G/K \cong H$.

This proves the theorem.

## Idea

The universal property applied to the kernel itself gives a homomorphism on $G/\ker \varphi$ with the same image as $\varphi$.
Its kernel is only the identity coset, so it is injective.
An injective homomorphism is an isomorphism onto its image.

## Variants

A direct proof does not use the universal property.

1. Define $\bar{\varphi}(gK) = \varphi(g)$.
2. The map is well defined. If $gK = hK$, then $g^{-1}h \in K$, so $\varphi(g)^{-1}\varphi(h) = \varphi(g^{-1}h) = e$ and $\varphi(g) = \varphi(h)$.
3. The map is a homomorphism, because $\bar{\varphi}((gK)(hK)) = \bar{\varphi}(ghK) = \varphi(gh) = \varphi(g)\varphi(h)$.
4. The map is onto $\operatorname{im} \varphi$, because each $\varphi(g)$ is $\bar{\varphi}(gK)$.
5. If $\bar{\varphi}(gK) = e$, then $\varphi(g) = e$, so $g \in K$ and $gK = K$. So the kernel is trivial, and the map is injective.
