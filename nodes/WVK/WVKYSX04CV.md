---
tag: WVKYSX04CV
kind: proof
name: Proof that cosets have the same cardinality as the subgroup
msc: [20A05]
proves: 0DKMBWTD7P
uses: [G5S1M9, 0N0PXCTYA7, 05FD317V2W, 060Z37VVB6, 08EJHHMB5R, 0JTGRV4WT4]
sources:
  - url: https://proofwiki.org/wiki/Cosets_are_Equivalent
---

## Proof

1. Let $G$ be a [[group|G5S1M9]], let $H$ be a [[subgroup|0N0PXCTYA7]] of $G$, and let $g \in G$.
2. Define $\lambda \colon H \to gH$ by $\lambda(h) = gh$. It maps into the [[left coset|05FD317V2W]] $gH = \set{gh : h \in H}$.
3. The map $\lambda$ is surjective: each element of $gH$ has the form $gh = \lambda(h)$ with $h \in H$.
4. The map $\lambda$ is injective: if $gh = gh'$, then multiplying on the left by $g^{-1}$ gives $h = h'$.
5. So $\lambda$ is a bijection from $H$ to $gH$.
6. Define $\rho \colon H \to Hg$ by $\rho(h) = hg$. It maps into the [[right coset|060Z37VVB6]] $Hg = \set{hg : h \in H}$.
7. Each element of $Hg$ is $hg = \rho(h)$, so $\rho$ is surjective. If $hg = h'g$, multiplying on the right by $g^{-1}$ gives $h = h'$, so $\rho$ is injective.
8. So $\rho$ is a bijection from $H$ to $Hg$.
9. By steps 5 and 8, $gH$ and $Hg$ are [[equinumerous|08EJHHMB5R]] with $H$. By the definition of [[cardinality|0JTGRV4WT4]], $\abs{gH} = \abs{H} = \abs{Hg}$.

## Idea

Multiplying by a fixed element $g$ can be undone by multiplying by $g^{-1}$. So it moves $H$ onto the coset without merging or losing any elements.
