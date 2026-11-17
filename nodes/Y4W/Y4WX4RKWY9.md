---
tag: Y4WX4RKWY9
kind: proof
name: Proof of the correspondence theorem
msc: ["20A05"]
topics: [E1506A5A55]
audience: ug2
proves: 0S9ZVZ34MD
methods: [0NTF6DMVAP, 01XM7JEKHY]
uses: [0CB0DX5BVV, 0KYX2N69J0, 03DEH43F4H, 0X1JXT47GA, 05N4TQKPH0, 0D9NDGE9KP, 0DTXBQPA2S, 0ZTGMDNVTB, 0RP7VWQ0YN]
sources:
  - url: https://en.wikipedia.org/wiki/Correspondence_theorem
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Isomorphism_theorems
    locator: Theorem D (groups)
---

## Proof

We show that the preimage under $\pi$ is an inverse of $M \mapsto M/N$.
Then we check inclusions, indices, normality, intersections and joins.

1. Let $G$ be a group with identity $e$, and let $N$ be a [[normal subgroup|0CB0DX5BVV]] of $G$. The [[quotient group|0KYX2N69J0]] $G/N$ has the product $(aN)(bN) = (ab)N$ and the identity $eN = N$. This step uses the hypothesis that $N$ is normal.
2. For $b \in G$, we get $(bN)(b^{-1}N) = N$. By the [[uniqueness of inverses|0D9NDGE9KP]], $(bN)^{-1} = b^{-1}N$.
3. Let $K$ be a subgroup of $G$ and let $x, y \in G$. Then the [[left cosets|03DEH43F4H]] satisfy $xK = yK$ if and only if $x^{-1}y \in K$. If $xK = yK$, then $y = ye \in xK$, so $y = xk$ with $k \in K$, and $x^{-1}y = k$. If $x^{-1}y = k \in K$, then $yK = xkK = xK$, because $kK = K$: closure gives $kK \subseteq K$, and each $k' \in K$ equals $k(k^{-1}k')$ with $k^{-1}k' \in K$.
4. By step 3 with $K = N$, $x = e$ and $y = a$, we get $aN = N$ if and only if $a \in N$.
5. Let $\mathcal{A}$ be the set of [[subgroups|0X1JXT47GA]] $M$ of $G$ with $N \subseteq M$, and let $\mathcal{B}$ be the set of subgroups of $G/N$.
6. Let $M \in \mathcal{A}$. The set $M/N$ contains the identity $eN$. For $a, b \in M$, step 2 gives $(aN)(bN)^{-1} = (ab^{-1})N$, and $ab^{-1} \in M$. By the [[subgroup criterion|05N4TQKPH0]], $M/N \in \mathcal{B}$.
7. For $Q \in \mathcal{B}$, let $\beta(Q) = \pi^{-1}(Q) = \{g \in G : gN \in Q\}$.
8. Let $Q \in \mathcal{B}$. Then $e \in \beta(Q)$, because $eN$ is the identity of $Q$. For $a, b \in \beta(Q)$, step 2 gives $(ab^{-1})N = (aN)(bN)^{-1} \in Q$, so $ab^{-1} \in \beta(Q)$. By the subgroup criterion, $\beta(Q)$ is a subgroup of $G$.
9. For $n \in N$, step 4 gives $nN = N \in Q$, so $N \subseteq \beta(Q)$. Thus $\beta(Q) \in \mathcal{A}$.
10. Let $M \in \mathcal{A}$. We show $\beta(M/N) = M$. Each $m \in M$ has $mN \in M/N$, so $M \subseteq \beta(M/N)$.
11. Conversely, let $g \in \beta(M/N)$, so $gN = mN$ for some $m \in M$. By step 3, $m^{-1}g = n \in N$, so $g = mn$. Because $N \subseteq M$, we get $n \in M$ and $g \in M$. This step uses the hypothesis that $N \subseteq M$.
12. Let $Q \in \mathcal{B}$. We show $\beta(Q)/N = Q$. Each element of $\beta(Q)/N$ is $gN$ with $g \in \beta(Q)$, so it is in $Q$. Each element of $Q$ is a coset $gN$, and then $g \in \beta(Q)$, so $gN \in \beta(Q)/N$.
13. By steps 10 to 12, the maps $M \mapsto M/N$ and $Q \mapsto \beta(Q)$ are inverse to each other. So $M \mapsto M/N$ is a bijection from $\mathcal{A}$ to $\mathcal{B}$. This proves part 1.
14. Let $M, L \in \mathcal{A}$. If $M \subseteq L$, then each $mN$ with $m \in M$ is in $L/N$, so $M/N \subseteq L/N$.
15. If $M/N \subseteq L/N$, then each $g$ with $gN \in M/N$ also has $gN \in L/N$, so $\beta(M/N) \subseteq \beta(L/N)$. By step 10, $M \subseteq L$. With step 14, this proves part 2. The same argument shows that $\beta$ keeps inclusions: $Q \subseteq Q'$ gives $\beta(Q) \subseteq \beta(Q')$.
16. Let $M, L \in \mathcal{A}$ with $M \subseteq L$, and let $x, y \in L$. By step 3 in $L/N$, then step 2, then step 10, we get $(xN)(M/N) = (yN)(M/N)$ if and only if $(x^{-1}y)N \in M/N$, if and only if $x^{-1}y \in M$.
17. By step 3 in $L$, we get $xM = yM$ if and only if $x^{-1}y \in M$. With step 16, the formula $\alpha(xM) = (xN)(M/N)$ gives a well defined and injective map from the left cosets of $M$ in $L$ to the left cosets of $M/N$ in $L/N$.
18. Each element of $L/N$ is $xN$ with $x \in L$, so each left coset of $M/N$ in $L/N$ is $\alpha(xM)$ for some $x \in L$. Thus $\alpha$ is a bijection, and the [[indices|0DTXBQPA2S]] agree: $[L : M] = [L/N : M/N]$. This proves part 3.
19. Let $M \in \mathcal{A}$ be normal in $G$. For $g \in G$ and $m \in M$, step 2 gives $(gN)(mN)(gN)^{-1} = (gmg^{-1})N$, and $gmg^{-1} \in M$. So $M/N$ is normal in $G/N$.
20. Conversely, let $M/N$ be normal in $G/N$, and let $g \in G$ and $m \in M$. Then $(gmg^{-1})N = (gN)(mN)(gN)^{-1} \in M/N$. So $gmg^{-1} \in \beta(M/N)$, which is $M$ by step 10. Thus $M$ is normal in $G$. With step 19, this proves part 4.
21. Let $M, L \in \mathcal{A}$. The [[intersection|0ZTGMDNVTB]] $M \cap L$ is a subgroup that contains $N$, so it is in $\mathcal{A}$. By step 14, $(M \cap L)/N \subseteq (M/N) \cap (L/N)$.
22. The set $(M/N) \cap (L/N)$ is a subgroup of $G/N$. By step 15, its preimage is contained in $\beta(M/N) \cap \beta(L/N) = M \cap L$. By step 12 and step 14, $(M/N) \cap (L/N) \subseteq (M \cap L)/N$. With step 21, $(M \cap L)/N = (M/N) \cap (L/N)$.
23. Let $J = \langle M \cup L \rangle$ be the [[subgroup generated|0RP7VWQ0YN]] by $M \cup L$, and let $P = \langle (M/N) \cup (L/N) \rangle$. Then $J \in \mathcal{A}$, because $N \subseteq M \subseteq J$. By step 14, $J/N$ contains $M/N$ and $L/N$, so $P \subseteq J/N$.
24. By step 15, $\beta(P)$ contains $\beta(M/N) = M$ and $\beta(L/N) = L$. So $\beta(P)$ is a subgroup that contains $M \cup L$, and $J \subseteq \beta(P)$. By steps 14 and 12, $J/N \subseteq \beta(P)/N = P$. With step 23, $J/N = P$. With step 22, this proves part 5.

This proves all five parts of the theorem.

## Idea

A subgroup of $G$ that contains $N$ is a union of cosets of $N$, so the set of these cosets fixes it.
This is why the preimage undoes $M \mapsto M/N$.
Products and conjugates in $G/N$ are computed on representatives, so inclusions, cosets and normality pass between $G$ and $G/N$.
Intersections and joins are the largest lower bounds and the smallest upper bounds, so a bijection that keeps inclusions in both directions keeps them too.

## Variants

Part 4 also follows from the first isomorphism theorem.
If $M/N$ is normal in $G/N$, then $M$ is the kernel of the composite $G \to G/N \to (G/N)/(M/N)$, so $M$ is normal in $G$.
Parts 1 and 2 are often stated for a surjective homomorphism $\varphi \colon G \to H$ in place of $\pi$, with the subgroups of $G$ that contain $\ker \varphi$.
The proof is the same.
