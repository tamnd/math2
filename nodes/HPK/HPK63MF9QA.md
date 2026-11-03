---
tag: HPK63MF9QA
kind: proof
name: Proof of the tower law for indices
msc: [20A05]
proves: 0ZQJ7KEFQ5
uses: [G5S1M9, 0N0PXCTYA7, 05FD317V2W, 04QEBF8S49, 0HTGB13FE2, 0C81YBVTWH, 0QKPNZKNEA, 08EJHHMB5R]
sources:
  - url: https://proofwiki.org/wiki/Tower_Law_for_Subgroups
---

## Proof

We build an explicit bijection from pairs of coset representatives to the left cosets of $K$ in $G$.

1. Let $G$ be a [[group|G5S1M9]] with identity $e$. Let $H$ be a [[subgroup|0N0PXCTYA7]] of $G$, and $K$ a subgroup of $H$. Then $K$ is also a subgroup of $G$.
2. For a group $M$ with a subgroup $L$, let $M/L$ be the set of [[left cosets|05FD317V2W]] $xL$ with $x \in M$. By the definition of the [[index|04QEBF8S49]], $[M : L] = \abs{M/L}$.
3. Claim: if two left cosets $xL$ and $yL$ have a common element, then $xL = yL$.
4. Indeed, let $xa = yb$ with $a, b \in L$. Then $y = xab^{-1}$, so $yl = x(ab^{-1}l) \in xL$ for each $l \in L$. So $yL \subseteq xL$, and by symmetry $xL = yL$.
5. Each $x \in M$ lies in $xL$, since $x = xe$. So $x \in yL$ implies $xL = yL$, by step 3.
6. By the [[axiom of choice|0HTGB13FE2]], choose $R \subseteq G$ that contains exactly one element of each left coset of $H$ in $G$.
7. The map $r \mapsto rH$ from $R$ to $G/H$ is surjective, by step 5. It is injective, because distinct elements of $R$ lie in distinct cosets. So $\abs{R} = [G : H]$.
8. In the same way, choose $S \subseteq H$ that contains exactly one element of each left coset of $K$ in $H$. Then $\abs{S} = [H : K]$.
9. Define $F \colon R \times S \to G/K$ by $F(r, s) = rsK$, on the [[Cartesian product|0C81YBVTWH]] $R \times S$.
10. $F$ is surjective. Let $x \in G$. By step 5 there is $r \in R$ with $x \in rH$, so $x = rh$ with $h \in H$.
11. By step 5 for $K$ in $H$, there is $s \in S$ with $h \in sK$, so $h = sk$ with $k \in K$. Then $x = rsk$, so $xK = rsK$ by step 5 for $K$ in $G$.
12. $F$ is injective. Suppose $rsK = r's'K$ with $r, r' \in R$ and $s, s' \in S$. Since $rs \in rsK$, we have $rs = r's'k$ for some $k \in K$.
13. Here $s'k \in H$ because $K \subseteq H$. So $rs$ lies in both $rH$ and $r'H$. By step 3, $rH = r'H$, so $r = r'$ by the choice of $R$.
14. Cancelling $r$ in $rs = rs'k$ gives $s = s'k \in s'K$. By step 5, $sK = s'K$, so $s = s'$ by the choice of $S$.
15. So $F$ is a bijection, and $G/K$ is [[equinumerous|08EJHHMB5R]] with $R \times S$.
16. The product of two [[cardinal numbers|0QKPNZKNEA]] $\abs{R}$ and $\abs{S}$ is by definition $\abs{R \times S}$. For finite sets it is the ordinary product.
17. Hence $[G : K] = \abs{R \times S} = \abs{R} \cdot \abs{S} = [G : H] \cdot [H : K]$.

## Idea

Each left coset of $K$ in $G$ is found in two stages. First choose the coset of $H$ that contains it, then the coset of $K$ inside that copy of $H$. So the cosets of $K$ match the pairs of choices, and their number is the product of the two indices.
