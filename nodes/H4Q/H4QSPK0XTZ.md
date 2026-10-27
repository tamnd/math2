---
tag: H4QSPK0XTZ
kind: proof
name: Proof of the first isomorphism theorem
msc: [20A05]
proves: 0CXXJNG5B6
uses: [0C9ZKYSPYR, 0N2P0XRTDF, 0112DTS464, 085PND4KNT]
sources:
  - url: https://en.wikipedia.org/wiki/Isomorphism_theorems
    locator: Theorem A (groups)
---

## Proof

1. Let $\varphi : G \to H$ be a group homomorphism with kernel $K$. [[$K$ is a normal subgroup|0C9ZKYSPYR]] of $G$, so the quotient group $G/K$ exists.
2. Define $\psi : G/K \to \varphi(G)$ by $\psi(gK) = \varphi(g)$.
3. The map $\psi$ is well defined. If $gK = hK$, then $g^{-1}h \in K$, so $\varphi(g)^{-1}\varphi(h) = e$ and $\varphi(g) = \varphi(h)$.
4. The map $\psi$ is a homomorphism, because $\psi(gK\,hK) = \psi(ghK) = \varphi(gh) = \varphi(g)\varphi(h)$.
5. The map $\psi$ is onto the [[image|0112DTS464]] $\varphi(G)$, because each $\varphi(g)$ is $\psi(gK)$.
6. If $\psi(gK) = e$, then $\varphi(g) = e$, so $g \in K$ and $gK = K$. Thus the kernel of $\psi$ is trivial, and [[$\psi$ is injective|0N2P0XRTDF]].
7. Thus $\psi$ is an [[isomorphism|085PND4KNT]], and $G/K \cong \varphi(G)$.

## Idea

Send each coset of the kernel to the common image of its elements. This map is well defined, respects products, and has a trivial kernel.
