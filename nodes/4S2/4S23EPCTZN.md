---
tag: 4S23EPCTZN
kind: proof
name: Proof that finite p-groups are nilpotent
msc: [20D15, 20F18]
proves: 081WTKYX6C
uses: [06DAH3VS6M, 0DZPD2MG33, 0RZCTT30H5, 0S7Y9Q990Q, 0W77CVBCHQ, 0YYWCNTPWR, 0JPYSD5E0B]
sources:
  - url: https://en.wikipedia.org/wiki/P-group
    locator: Non-trivial center
---

## Proof

We argue by strong induction on $|G|$.

1. Let $A$ be a group, $B$ a normal subgroup and $x \in A$. The coset $xB$ lies in the [[centre|0S7Y9Q990Q]] of $A/B$ if and only if $x^{-1}g^{-1}xg \in B$ for all $g \in A$. Indeed, $xgB = gxB$ holds if and only if $(gx)^{-1}xg \in B$.
2. If $G = \{e\}$, then the series $N_0 = \{e\} = G$ of length $0$ is a central series. So $G$ is [[nilpotent|0DZPD2MG33]].
3. Let $G \neq \{e\}$ be a finite [[$p$-group|06DAH3VS6M]], and assume the claim for all $p$-groups of smaller order. Let $Z = Z(G)$.
4. By [[this result|0RZCTT30H5]], $Z \neq \{e\}$. The centre is a [[normal subgroup|0W77CVBCHQ]] of $G$, because $gzg^{-1} = z$ for $z \in Z$.
5. The [[quotient group|0YYWCNTPWR]] $\bar G = G/Z$ has $|G|/|Z| < |G|$ elements.
6. For $g \in G$ of [[order|0JPYSD5E0B]] $p^k$, we have $(gZ)^{p^k} = Z$. So the order of $gZ$ divides $p^k$ and is a power of $p$. Hence $\bar G$ is a $p$-group.
7. By the induction hypothesis, $\bar G$ has a central series $\{Z\} = M_0 \subseteq M_1 \subseteq \cdots \subseteq M_k = \bar G$.
8. Let $\pi \colon G \to \bar G$ be the projection $\pi(g) = gZ$. Put $N_0 = \{e\}$ and $N_{j+1} = \pi^{-1}(M_j)$ for $0 \leq j \leq k$. Then $N_1 = Z$ and $N_{k+1} = G$.
9. Each $N_{j+1}$ is a subgroup of $G$ containing $Z$. It is normal in $G$: for $x \in N_{j+1}$ and $g \in G$, $\pi(gxg^{-1}) = \pi(g)\pi(x)\pi(g)^{-1} \in M_j$, since $M_j$ is normal in $\bar G$.
10. The sets $N_j$ increase with $j$, since the $M_j$ increase and $N_0 \subseteq Z = N_1$.
11. The first factor works: for $x \in N_1 = Z$ and $g \in G$, we get $x^{-1}g^{-1}xg = e \in N_0$. By step 1, $N_1/N_0 \subseteq Z(G/N_0)$.
12. Let $1 \leq j \leq k$, let $x \in N_{j+1}$ and $g \in G$, and let $c = x^{-1}g^{-1}xg$. Then $\pi(c) = \pi(x)^{-1}\pi(g)^{-1}\pi(x)\pi(g)$.
13. Since $\pi(x) \in M_j$ and $M_j/M_{j-1} \subseteq Z(\bar G/M_{j-1})$, step 1 in $\bar G$ gives $\pi(c) \in M_{j-1}$. So $c \in \pi^{-1}(M_{j-1}) = N_j$.
14. By step 1, $N_{j+1}/N_j \subseteq Z(G/N_j)$.
15. By steps 8 to 14, $\{e\} = N_0 \subseteq N_1 \subseteq \cdots \subseteq N_{k+1} = G$ is a central series of $G$. So $G$ is nilpotent.

## Idea

A nontrivial finite $p$-group has a nontrivial centre $Z$. Dividing by $Z$ gives a smaller $p$-group, which is nilpotent by induction. Pulling its central series back to $G$ and putting the trivial group below $Z$ gives a central series of $G$.
