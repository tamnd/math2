---
tag: W6V1XYH0K6
kind: proof
name: Proof that homomorphisms preserve identity and inverses
msc: [20A05]
proves: 08FKQD7NJ3
uses: [0HV9Y7WG5R, 0VSNX4P2Q0, 0D9NDGE9KP]
sources:
  - url: https://en.wikipedia.org/wiki/Group_homomorphism
    locator: Properties
---

## Proof

1. Let $\varphi \colon G \to H$ be a [[group homomorphism|0HV9Y7WG5R]], and let $e_G$ and $e_H$ be the identity elements of $G$ and $H$.
2. Since $e_G e_G = e_G$ and $\varphi$ is a homomorphism, $\varphi(e_G) \varphi(e_G) = \varphi(e_G e_G) = \varphi(e_G)$.
3. Since $e_H$ is the identity of $H$, $\varphi(e_G) = \varphi(e_G) e_H$.
4. By steps 2 and 3, $\varphi(e_G) \varphi(e_G) = \varphi(e_G) e_H$. By the [[cancellation laws|0VSNX4P2Q0]], $\varphi(e_G) = e_H$.
5. Let $a \in G$. Since $a a^{-1} = e_G$, step 4 gives $\varphi(a) \varphi(a^{-1}) = \varphi(a a^{-1}) = \varphi(e_G) = e_H$.
6. By step 5 and the [[uniqueness of inverses|0D9NDGE9KP]], $\varphi(a^{-1}) = \varphi(a)^{-1}$.
7. Steps 4 and 6 are the two claims of the statement.

## Idea

The identity is the only element $x$ of a group with $xx = x$, and $\varphi(e_G)$ has this property. Once the identity is preserved, $\varphi(a^{-1})$ is a right inverse of $\varphi(a)$, and inverses in a group are unique.
