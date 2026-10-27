---
tag: AY60KQR8RT
kind: proof
name: Proof that the kernel is a normal subgroup
msc: [20A05]
proves: 0C9ZKYSPYR
uses: [0Z424HK8CQ, 0W77CVBCHQ, 08FKQD7NJ3]
methods: [0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_subgroup
    locator: Normal subgroups, quotient groups and homomorphisms
---

## Proof

1. Let $\varphi : G \to H$ be a group homomorphism, and let $K = \ker \varphi$ be its [[kernel|0Z424HK8CQ]].
2. [[$\varphi(e) = e$ and $\varphi(b^{-1}) = \varphi(b)^{-1}$|08FKQD7NJ3]]. Thus $e \in K$, and $K$ is not empty.
3. Let $a, b \in K$. Then $\varphi(ab^{-1}) = \varphi(a)\varphi(b)^{-1} = e e^{-1} = e$, so $ab^{-1} \in K$. Thus $K$ is a subgroup of $G$.
4. Let $k \in K$ and $g \in G$. Then $\varphi(gkg^{-1}) = \varphi(g)\, e\, \varphi(g)^{-1} = e$.
5. Thus $gKg^{-1} \subseteq K$ for all $g \in G$, and $K$ is a [[normal subgroup|0W77CVBCHQ]] of $G$.

## Idea

A homomorphism sends the identity to the identity and respects inverses. Thus the elements sent to the identity are closed under the group operations and under conjugation.
