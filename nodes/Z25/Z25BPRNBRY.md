---
tag: Z25BPRNBRY
kind: proof
name: Proof that the product of a subgroup and a normal subgroup is a subgroup
msc: [20A05]
proves: 0TXWV1JGG1
uses: [0NS1YTGM19, 0W77CVBCHQ, 0N0PXCTYA7, 0D9NDGE9KP, 05N4TQKPH0]
sources:
  - url: https://en.wikipedia.org/wiki/Product_of_group_subsets
    locator: Product of subgroups
---

## Proof

We first show $HN = NH$ and then apply the subgroup criterion.

1. Let $G$ be a group with identity $e$, let $H$ be a subgroup of $G$, and let $N$ be a [[normal subgroup|0W77CVBCHQ]] of $G$.
2. By the [[definition of the product|0NS1YTGM19]], $HN = \{hn : h \in H, n \in N\}$. In the same way, $NH = \{nh : n \in N, h \in H\}$.
3. Let $h \in H$ and $n \in N$. Then $hn = (hnh^{-1}) h$. Since $N$ is normal, $hnh^{-1} \in N$. So $hn \in NH$, and $HN \subseteq NH$.
4. Let $n \in N$ and $h \in H$. Then $nh = h (h^{-1} n h)$. Since $N$ is normal, $h^{-1} n h = h^{-1} n (h^{-1})^{-1} \in N$. So $nh \in HN$, and $NH \subseteq HN$.
5. By steps 3 and 4, $HN = NH$.
6. For $a, b \in G$, we have $(ab)(b^{-1}a^{-1}) = e$. By the [[uniqueness of inverses|0D9NDGE9KP]], $(ab)^{-1} = b^{-1} a^{-1}$.
7. Since $e \in H$ and $e \in N$ by the [[definition of a subgroup|0N0PXCTYA7]], $e = ee \in HN$. So $HN$ is not empty.
8. Let $a, b \in HN$, say $a = h_1 n_1$ and $b = h_2 n_2$ with $h_1, h_2 \in H$ and $n_1, n_2 \in N$.
9. By step 6, $b^{-1} = n_2^{-1} h_2^{-1}$. So $ab^{-1} = h_1 n h_2^{-1}$, where $n = n_1 n_2^{-1}$ lies in $N$.
10. The element $n h_2^{-1}$ lies in $NH$. By step 5, it lies in $HN$, so $n h_2^{-1} = h' n'$ with $h' \in H$ and $n' \in N$.
11. Then $ab^{-1} = (h_1 h') n'$. Since $h_1 h' \in H$, this shows $ab^{-1} \in HN$.
12. By steps 7 and 11 and the [[subgroup criterion|05N4TQKPH0]], $HN$ is a subgroup of $G$. Together with step 5, this proves the statement.

## Idea

Normality lets an element of $N$ pass to the other side of an element of $H$, at the price of being replaced by a conjugate in $N$. This gives $HN = NH$. Then in $h_1 n h_2^{-1}$ we can move the middle factor past $h_2^{-1}$, so the product keeps the form "element of $H$ times element of $N$".
