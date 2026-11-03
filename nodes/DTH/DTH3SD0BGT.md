---
tag: DTH3SD0BGT
kind: proof
name: Proof that a subgroup is normal iff its left and right cosets agree
msc: [20A05]
proves: 01E7SWYJX3
uses: [G5S1M9, 0N0PXCTYA7, 0W77CVBCHQ, 05FD317V2W, 060Z37VVB6]
sources:
  - url: https://proofwiki.org/wiki/Equivalence_of_Definitions_of_Normal_Subgroup
---

## Proof

1. Let $G$ be a [[group|G5S1M9]] and let $N$ be a [[subgroup|0N0PXCTYA7]] of $G$.
2. Suppose $N$ is [[normal|0W77CVBCHQ]], so $gng^{-1} \in N$ for all $g \in G$ and $n \in N$. Fix $g \in G$.
3. Let $x$ be in the [[left coset|05FD317V2W]] $gN$, so $x = gn$ with $n \in N$. Then $x = (gng^{-1})g$ with $gng^{-1} \in N$. So $x$ lies in the [[right coset|060Z37VVB6]] $Ng$.
4. So $gN \subseteq Ng$.
5. Let $x \in Ng$, so $x = ng$ with $n \in N$. Normality applied to $g^{-1}$ gives $g^{-1}n(g^{-1})^{-1} = g^{-1}ng \in N$.
6. Then $x = g(g^{-1}ng) \in gN$. So $Ng \subseteq gN$, and with step 4, $gN = Ng$.
7. Conversely, suppose $gN = Ng$ for each $g \in G$. Let $g \in G$ and $n \in N$.
8. Then $gn \in gN = Ng$, so $gn = n'g$ for some $n' \in N$.
9. Multiplying on the right by $g^{-1}$ gives $gng^{-1} = n' \in N$. So $N$ is normal in $G$.

## Idea

The equation $gn = (gng^{-1})g$ turns an element of $gN$ into an element of $Ng$, provided the conjugate $gng^{-1}$ stays in $N$. Read backwards, $gN = Ng$ says that each $gn$ can be written as $n'g$, and then $gng^{-1} = n'$ lies in $N$.
