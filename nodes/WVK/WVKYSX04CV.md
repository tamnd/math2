---
tag: WVKYSX04CV
kind: proof
name: Proof that all cosets have the same size
msc: ["20A05"]
topics: [1VHQWXC64D]
audience: ug1
proves: 0DKMBWTD7P
uses: [G5S1M9, 0X1JXT47GA, 03DEH43F4H, 0NE1DK7H4T, 0GG9TVW90M, 0B0KR7FH2Q, 0G0ASKNA6Z]
methods: [0NTF6DMVAP]
sources:
  - url: https://proofwiki.org/wiki/Cosets_are_Equivalent
  - url: https://en.wikipedia.org/wiki/Coset
    locator: Properties
---

## Proof

Let $G$ be a [[group|G5S1M9]], let $H$ be a [[subgroup|0X1JXT47GA]] of $G$, and let $g \in G$.

1. Define $\lambda \colon H \to gH$ by $\lambda(h) = gh$. Each value $gh$ is in the [[left coset|03DEH43F4H]] $gH = \{gh : h \in H\}$, by the definition of $gH$.
2. The map $\lambda$ is surjective. Each element of $gH$ has the form $gh$ with $h \in H$, and $gh = \lambda(h)$.
3. The map $\lambda$ is injective. If $gh = gh'$, then we multiply on the left by $g^{-1}$ and get $h = h'$.
4. By steps 2 and 3, $\lambda$ is a [[bijection|0GG9TVW90M]] from $H$ to $gH$.
5. Define $\rho \colon H \to Hg$ by $\rho(h) = hg$. Each value is in the [[right coset|0NE1DK7H4T]] $Hg = \{hg : h \in H\}$.
6. The map $\rho$ is surjective, because each element of $Hg$ has the form $hg = \rho(h)$ with $h \in H$.
7. The map $\rho$ is injective. If $hg = h'g$, then we multiply on the right by $g^{-1}$ and get $h = h'$.
8. By steps 6 and 7, $\rho$ is a bijection from $H$ to $Hg$.
9. By steps 4 and 8, the sets $gH$ and $Hg$ are [[equinumerous|0B0KR7FH2Q]] with $H$. Thus $|gH| = |H| = |Hg|$ as [[cardinalities|0G0ASKNA6Z]].
10. Let $C$ and $D$ be two cosets of $H$, left or right. By step 9, $|C| = |H|$ and $|D| = |H|$, so $|C| = |D|$.

This proves that all cosets of $H$ have the same size.

## Idea

Multiplication by a fixed element $g$ can be undone by multiplication by $g^{-1}$.
Thus it moves $H$ onto the coset without losing elements and without merging two elements.
No step uses finiteness, so the result holds for infinite groups too.

## Variants

The inverse of $\lambda$ is the map $x \mapsto g^{-1}x$ from $gH$ to $H$.
Giving this inverse proves the bijection in one step.
A third form uses the left regular action: $\lambda_g \colon G \to G$ is a bijection of $G$, and it maps $H$ onto $gH$.
