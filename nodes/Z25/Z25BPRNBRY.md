---
tag: Z25BPRNBRY
kind: proof
name: Proof that HN is a subgroup when N is normal
msc: ["20A05"]
topics: [E1506A5A55]
audience: ug1
proves: 0TXWV1JGG1
uses: [0PT52XQZD7, 0CB0DX5BVV, 0X1JXT47GA, 0D9NDGE9KP, 05N4TQKPH0]
methods: [0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Product_of_group_subsets
    locator: Product of subgroups
---

## Proof

We first show $HN = NH$, then we apply the subgroup criterion, and last we check normality.

1. Let $G$ be a group with identity $e$, let $H$ be a subgroup of $G$, and let $N$ be a [[normal subgroup|0CB0DX5BVV]] of $G$. Thus $gng^{-1} \in N$ for all $g \in G$ and $n \in N$.
2. By the definition of the [[product of two subgroups|0PT52XQZD7]], $HN = \{hn : h \in H, n \in N\}$ and $NH = \{nh : n \in N, h \in H\}$.
3. Let $h \in H$ and $n \in N$. Then $hn = (hnh^{-1})h$. By step 1, $hnh^{-1} \in N$. So $hn \in NH$, and $HN \subseteq NH$. This step uses the hypothesis that $N$ is normal.
4. Let $n \in N$ and $h \in H$. Then $nh = h(h^{-1}nh)$, and $h^{-1}nh = h^{-1}n(h^{-1})^{-1}$. By step 1 with $g = h^{-1}$, this element is in $N$. So $nh \in HN$, and $NH \subseteq HN$.
5. By steps 3 and 4, $HN = NH$. This is claim 1.
6. For $a, b \in G$, we have $(ab)(b^{-1}a^{-1}) = e$. By the [[uniqueness of inverses|0D9NDGE9KP]], $(ab)^{-1} = b^{-1}a^{-1}$.
7. By the definition of a [[subgroup|0X1JXT47GA]], $e \in H$ and $e \in N$. So $e = ee \in HN$, and $HN$ is not empty.
8. Let $a, b \in HN$. Write $a = h_1 n_1$ and $b = h_2 n_2$ with $h_1, h_2 \in H$ and $n_1, n_2 \in N$.
9. By step 6, $b^{-1} = n_2^{-1}h_2^{-1}$. So $ab^{-1} = h_1 n h_2^{-1}$, where $n = n_1 n_2^{-1}$. Since $N$ is a subgroup, $n \in N$.
10. The element $nh_2^{-1}$ is in $NH$, because $h_2^{-1} \in H$. By step 5, it is in $HN$. So $nh_2^{-1} = h'n'$ for some $h' \in H$ and $n' \in N$.
11. Then $ab^{-1} = h_1 h' n'$. Since $H$ is a subgroup, $h_1 h' \in H$. So $ab^{-1} \in HN$.
12. By steps 7 and 11 and the [[subgroup criterion|05N4TQKPH0]], $HN$ is a subgroup of $G$. This is claim 2.
13. Now suppose that $H$ is also normal in $G$. Let $g \in G$, and let $x = hn$ with $h \in H$ and $n \in N$.
14. Then $gxg^{-1} = ghng^{-1} = (ghg^{-1})(gng^{-1})$, because $g^{-1}g = e$.
15. Since $H$ is normal, $ghg^{-1} \in H$. Since $N$ is normal, $gng^{-1} \in N$. This step uses the hypothesis of claim 3.
16. By steps 14 and 15, $gxg^{-1} \in HN$. So $HN$ is closed under conjugation by each $g \in G$.
17. By steps 12 and 16, $HN$ is a normal subgroup of $G$. This is claim 3, and the proof is complete.

## Idea

Normality lets an element of $N$ move to the other side of an element of $H$, at the price of a change to a conjugate that is still in $N$.
This gives $HN = NH$.
Then in the product $h_1 n h_2^{-1}$ we move the middle factor past $h_2^{-1}$, so the product keeps the form "element of $H$ times element of $N$".
For claim 3, we insert $g^{-1}g$ between $h$ and $n$ and conjugate each factor separately.

## Variants

A second proof of claim 2 uses the [[quotient group|0KYX2N69J0]] $G/N$.
Let $\pi \colon G \to G/N$ be the projection $g \mapsto gN$.
Then $\pi(H)$ is a subgroup of $G/N$, and $HN$ is the preimage of $\pi(H)$ under $\pi$.
The preimage of a subgroup under a homomorphism is a subgroup, so $HN$ is a subgroup.
Steps 7 to 12 prove the general fact that $HK$ is a subgroup whenever $HK = KH$.
