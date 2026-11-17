---
tag: AY60KQR8RT
kind: proof
name: Proof that kernels are normal
msc: ["20A05"]
topics: [E1506A5A55]
audience: ug1
proves: 0C9ZKYSPYR
uses: [0JYTG5K9Y4, 0W88CEGQP1, 0CB0DX5BVV, 08FKQD7NJ3, 05N4TQKPH0]
methods: [0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_subgroup
    locator: Normal subgroups, quotient groups and homomorphisms
  - url: https://en.wikipedia.org/wiki/Kernel_(algebra)
    locator: Group homomorphisms
---

## Proof

1. Let $\varphi \colon G \to H$ be a [[group homomorphism|0JYTG5K9Y4]], and let $K = \ker\varphi$ be its [[kernel|0W88CEGQP1]].
2. $\varphi(e_G) = e_H$, because [[homomorphisms preserve the identity|08FKQD7NJ3]]. So $e_G \in K$, and $K$ is not empty.
3. Let $a, b \in K$. Then $\varphi(ab^{-1}) = \varphi(a)\varphi(b)^{-1}$, because $\varphi$ preserves products and inverses. This step uses the hypothesis that $\varphi$ is a homomorphism.
4. So $\varphi(ab^{-1}) = e_H e_H^{-1} = e_H$, and $ab^{-1} \in K$.
5. By the [[subgroup criterion|05N4TQKPH0]], steps 2 and 4 show that $K$ is a subgroup of $G$.
6. Let $g \in G$ and $k \in K$. Then $\varphi(gkg^{-1}) = \varphi(g)\varphi(k)\varphi(g)^{-1}$. This step uses the hypothesis that $\varphi$ is a homomorphism.
7. Since $\varphi(k) = e_H$, this is $\varphi(g)\varphi(g)^{-1} = e_H$. So $gkg^{-1} \in K$.
8. So $gKg^{-1} \subseteq K$ for each $g \in G$, and $K$ is a [[normal subgroup|0CB0DX5BVV]] of $G$.

## Idea

A homomorphism respects products and inverses.
So the set of elements that it sends to the identity is closed under products, inverses and conjugation.
Conjugation of the identity $e_H$ by any element of $H$ gives $e_H$ again.

## Variants

The same argument shows more: the preimage $\varphi^{-1}(M)$ of each normal subgroup $M$ of $H$ is normal in $G$.
The kernel is the case $M = \{e_H\}$.
Steps 6 and 7 can also be read as one identity of maps: $\varphi \circ c_g = c_{\varphi(g)} \circ \varphi$, where $c_x(y) = xyx^{-1}$.
The map $c_{\varphi(g)}$ fixes $e_H$, so $c_g$ sends $K$ into $K$.
