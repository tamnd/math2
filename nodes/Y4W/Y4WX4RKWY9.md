---
tag: Y4WX4RKWY9
kind: proof
name: Proof of the correspondence theorem
msc: [20A05]
proves: 0S9ZVZ34MD
uses: [0W77CVBCHQ, 0YYWCNTPWR, 05FD317V2W, 0N0PXCTYA7, 05N4TQKPH0, 0D9NDGE9KP]
sources:
  - url: https://proofwiki.org/wiki/Correspondence_Theorem_(Group_Theory)
---

## Proof

We show that taking the preimage under $g \mapsto gN$ is an inverse of $K \mapsto K/N$, and then check inclusions and normality.

1. Let $G$ be a group with identity $e$, and let $N$ be a [[normal subgroup|0W77CVBCHQ]] of $G$. The [[quotient group|0YYWCNTPWR]] $G/N$ has the operation $(aN)(bN) = (ab)N$ and the identity $eN = N$.
2. For $b \in G$, $(bN)(b^{-1}N) = N$. By the [[uniqueness of inverses|0D9NDGE9KP]], $(bN)^{-1} = b^{-1}N$.
3. Let $a \in G$. If $a \in N$, then $aN = N$: closure gives $aN \subseteq N$, and each $m \in N$ is $a(a^{-1}m) \in aN$.
4. Let $\mathcal{A}$ be the set of [[subgroups|0N0PXCTYA7]] $K$ of $G$ with $N \subseteq K$, and $\mathcal{B}$ the set of subgroups of $G/N$.
5. For $K \in \mathcal{A}$, let $K/N = \{kN : k \in K\}$, the set of [[left cosets|05FD317V2W]] of $N$ with a representative in $K$.
6. Let $K \in \mathcal{A}$. The set $K/N$ contains $eN$. For $a, b \in K$, step 2 gives $(aN)(bN)^{-1} = (ab^{-1})N$, and $ab^{-1} \in K$. By the [[subgroup criterion|05N4TQKPH0]], $K/N \in \mathcal{B}$.
7. For $Q \in \mathcal{B}$, let $\beta(Q) = \{g \in G : gN \in Q\}$.
8. Let $Q \in \mathcal{B}$. Then $e \in \beta(Q)$, since $eN$ is the identity of $Q$. For $a, b \in \beta(Q)$, $(ab^{-1})N = (aN)(bN)^{-1} \in Q$, so $ab^{-1} \in \beta(Q)$.
9. By step 8 and the subgroup criterion, $\beta(Q)$ is a subgroup of $G$. For $n \in N$, step 3 gives $nN = N \in Q$, so $N \subseteq \beta(Q)$. Thus $\beta(Q) \in \mathcal{A}$.
10. Let $K \in \mathcal{A}$. We claim $\beta(K/N) = K$. Each $k \in K$ has $kN \in K/N$, so $K \subseteq \beta(K/N)$.
11. Conversely, let $g \in \beta(K/N)$, so $gN = kN$ for some $k \in K$. Then $g = ge \in kN$, so $g = kn$ with $n \in N \subseteq K$. Hence $g \in K$.
12. Let $Q \in \mathcal{B}$. We claim $\beta(Q)/N = Q$. Each element of $\beta(Q)/N$ is $gN$ with $gN \in Q$. Each element of $Q$ is a coset $gN$, and then $g \in \beta(Q)$.
13. By steps 10 to 12, the maps $K \mapsto K/N$ and $Q \mapsto \beta(Q)$ are inverse to each other. So $K \mapsto K/N$ is a bijection from $\mathcal{A}$ to $\mathcal{B}$.
14. Let $K, L \in \mathcal{A}$. If $K \subseteq L$, then each $kN$ with $k \in K$ lies in $L/N$, so $K/N \subseteq L/N$.
15. Let $K/N \subseteq L/N$. Each $g$ with $gN \in K/N$ has $gN \in L/N$, so $\beta(K/N) \subseteq \beta(L/N)$. By step 10, $K \subseteq L$. So $K \subseteq L$ exactly when $K/N \subseteq L/N$.
16. Let $K \in \mathcal{A}$ be normal in $G$. For $g \in G$ and $k \in K$, step 2 gives $(gN)(kN)(gN)^{-1} = (gkg^{-1})N$, and $gkg^{-1} \in K$. So $K/N$ is normal in $G/N$.
17. Conversely, let $K/N$ be normal in $G/N$, and let $g \in G$ and $k \in K$. Then $(gkg^{-1})N = (gN)(kN)(gN)^{-1} \in K/N$.
18. By step 17, $gkg^{-1} \in \beta(K/N)$, which is $K$ by step 10. So $K$ is normal in $G$.
19. Steps 13, 15, 16 and 18 prove all the claims of the statement.

## Idea

A subgroup of $G$ that contains $N$ is a union of cosets of $N$, so it can be recovered from the set of these cosets. This is why taking the preimage undoes $K \mapsto K/N$. Since products and conjugates in $G/N$ are computed on representatives, the inclusions and the normality pass back and forth.
