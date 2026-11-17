---
tag: DTH3SD0BGT
kind: proof
name: Proof of normality via cosets
msc: ["20A05"]
topics: [E1506A5A55]
audience: ug1
proves: 01E7SWYJX3
uses: [0X1JXT47GA, 0CB0DX5BVV, 03DEH43F4H, 0NE1DK7H4T]
methods: [0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_subgroup
    locator: Equivalent conditions
  - url: https://proofwiki.org/wiki/Equivalence_of_Definitions_of_Normal_Subgroup
---

## Proof

Let $G$ be a [[group|G5S1M9]] and let $N$ be a [[subgroup|0X1JXT47GA]] of $G$.
We prove a lemma on equal cosets, and then the implications $1 \Rightarrow 2 \Rightarrow 1$ and $1 \Rightarrow 3 \Rightarrow 1$.

Lemma: for $x, y \in G$, $xN = yN$ exactly when $y^{-1}x \in N$.

1. If $n \in N$, then $nN = N$. Indeed $nN \subseteq N$ because $N$ is closed under products, and each $m \in N$ is $n(n^{-1}m) \in nN$.
2. Suppose $xN = yN$. Then $x = xe \in xN = yN$, so $x = yn$ for some $n \in N$, and $y^{-1}x = n \in N$.
3. Suppose $y^{-1}x = n \in N$. Then $x = yn$, and $xN = y(nN) = yN$ by step 1.

Proof that condition 1 gives condition 2.

4. Assume condition 1. Fix $g \in G$.
5. Let $x \in gN$, so $x = gn$ with $n \in N$. Then $x = (gng^{-1})g$, and $gng^{-1} \in N$ by the hypothesis that $N$ is normal. So $x \in Ng$.
6. So $gN \subseteq Ng$.
7. Let $x \in Ng$, so $x = ng$ with $n \in N$. Condition 1 for the element $g^{-1}$ gives $g^{-1}n(g^{-1})^{-1} = g^{-1}ng \in N$.
8. Then $x = g(g^{-1}ng) \in gN$. So $Ng \subseteq gN$, and with step 6, $gN = Ng$.

Proof that condition 2 gives condition 1.

9. Assume condition 2. Let $g \in G$ and $n \in N$.
10. Then $gn \in gN = Ng$, so $gn = n'g$ for some $n' \in N$. This step uses the hypothesis $gN = Ng$.
11. Multiplication on the right by $g^{-1}$ gives $gng^{-1} = n' \in N$. So condition 1 holds.

Proof that condition 1 gives condition 3.

12. Assume condition 1. Let $aN = a'N$ and $bN = b'N$.
13. By the lemma, $a^{-1}a' = n_1$ and $b^{-1}b' = n_2$ with $n_1, n_2 \in N$. So $a' = an_1$ and $b' = bn_2$.
14. Then $a'b' = an_1bn_2 = ab(b^{-1}n_1b)n_2$, because $bb^{-1} = e$.
15. $b^{-1}n_1b \in N$ by condition 1 for the element $b^{-1}$. This step uses the hypothesis that $N$ is normal.
16. So $(ab)^{-1}(a'b') = (b^{-1}n_1b)n_2 \in N$, because $N$ is closed under products.
17. By the lemma, $abN = a'b'N$. So condition 3 holds.

Proof that condition 3 gives condition 1.

18. Assume condition 3. Let $g \in G$ and $n \in N$.
19. Let $a = e$, $a' = n$ and $b = b' = g^{-1}$. Then $aN = N = nN$ by step 1, and $bN = b'N$.
20. Condition 3 gives $abN = a'b'N$, that is, $g^{-1}N = ng^{-1}N$. This step uses the hypothesis of condition 3.
21. By the lemma, $(g^{-1})^{-1}(ng^{-1}) = gng^{-1} \in N$. So condition 1 holds.

The four implications show that the three conditions are equivalent.

## Idea

The identity $gn = (gng^{-1})g$ moves an element of $gN$ into $Ng$, provided that $gng^{-1}$ stays in $N$.
For the product of cosets, a change of representatives $a' = an_1$ and $b' = bn_2$ changes $ab$ by the element $(b^{-1}n_1b)n_2$.
This element is in $N$ for all choices exactly when $N$ is closed under conjugation.

## Variants

Condition 2 can be weakened to $gN \subseteq Ng$ for each $g \in G$.
Steps 9 to 11 use only this inclusion, so it already gives condition 1.
