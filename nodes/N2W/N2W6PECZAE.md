---
tag: N2W6PECZAE
kind: proof
name: Proof that a finite group is nilpotent iff it is the product of its Sylow subgroups
msc: [20F18, 20D15]
proves: 00Y9N80VSS
uses: [0DZPD2MG33, 0S7Y9Q990Q, 0W77CVBCHQ, 0YYWCNTPWR, 0JWZX6FKSH, 0AT1ZSNM25, 0QTZDKJEDV, 09GCQ5STVJ, 0V98WY94B8, 0Q2MVQ7JMT, 0PPP2J2DJV, 08PY4GNAPK, 3C53TD, 0YP7WYXF9V, 085PND4KNT, 08V7JHS3QZ, 081WTKYX6C]
sources:
  - url: https://en.wikipedia.org/wiki/Nilpotent_group
    locator: Properties
---

## Proof

We prove three general facts, then the implications $1 \Rightarrow 2 \Rightarrow 3 \Rightarrow 1$.

1. Let $N$ be a [[normal subgroup|0W77CVBCHQ]] of a group $X$ and let $x \in X$. Then $xN$ lies in the [[centre|0S7Y9Q990Q]] of the [[quotient|0YYWCNTPWR]] $X/N$ if and only if $x^{-1}g^{-1}xg \in N$ for all $g \in X$. Indeed, $xgN = gxN$ holds if and only if $(gx)^{-1}xg \in N$.
2. Let $H$ and $K$ be normal subgroups of $X$. By the [[second isomorphism theorem|0PPP2J2DJV]], $HK$ is a subgroup. It is normal, because $g(hk)g^{-1} = (ghg^{-1})(gkg^{-1})$.
3. Let $H$ and $K$ be normal in $X$ with $H \cap K = \{e\}$, and let $h \in H$, $k \in K$. The element $c = h^{-1}(k^{-1}hk)$ lies in $H$, and $c = (h^{-1}k^{-1}h)k$ lies in $K$. So $c = e$ and $hk = kh$.
4. In the situation of step 3, the map $H \times K \to HK$, $(h, k) \mapsto hk$, from the [[direct product|0YP7WYXF9V]] is a homomorphism, since $h_1k_1h_2k_2 = h_1h_2k_1k_2$. It is onto. If $hk = e$, then $h = k^{-1} \in H \cap K$, so $h = k = e$. So the map is an [[isomorphism|085PND4KNT]].
5. ($1 \Rightarrow 2$.) Let $G$ be [[nilpotent|0DZPD2MG33]] with central series $\{e\} = N_0 \subseteq \cdots \subseteq N_n = G$. Let $H \neq G$ be a subgroup. We show that $H$ is strictly smaller than its [[normaliser|0AT1ZSNM25]] $N_G(H)$.
6. Since $N_0 \subseteq H$ and $N_n \not\subseteq H$, there is a largest $i < n$ with $N_i \subseteq H$. Pick $x \in N_{i+1}$ with $x \notin H$.
7. Let $h \in H$. Since $N_{i+1}/N_i$ lies in the centre of $G/N_i$, step 1 with $x^{-1} \in N_{i+1}$ and $g = h^{-1}$ gives $xhx^{-1}h^{-1} \in N_i \subseteq H$. So $xhx^{-1} \in H$.
8. In the same way, step 1 with $x$ and $g = h^{-1}$ gives $x^{-1}hxh^{-1} \in H$, so $x^{-1}hx \in H$. With step 7, $xHx^{-1} = H$. So $x \in N_G(H)$ and $x \notin H$.
9. Let $p$ be a prime and let $P$ be a [[Sylow $p$-subgroup|0JWZX6FKSH]] of $G$; it exists by the [[first Sylow theorem|0V98WY94B8]]. Let $M = N_G(P)$ and $K = N_G(M)$. These are subgroups, with $P \trianglelefteq M$ and $M \trianglelefteq K$.
10. The order $|M|$ divides $|G|$ and is divisible by $|P|$, by [[Lagrange's theorem|3C53TD]]. So $P$ is a Sylow $p$-subgroup of $M$.
11. By the [[Frattini argument|0QTZDKJEDV]] in the group $K$, with the normal subgroup $M$, we get $K = N_K(P)\,M$. Since $N_K(P) \subseteq N_G(P) = M$, this gives $K \subseteq M$. So $N_G(M) = M$.
12. If $M \neq G$, then steps 5 to 8 give $M \subsetneq N_G(M)$, which contradicts step 11. So $N_G(P) = G$, and $P$ is normal in $G$.
13. By the [[second Sylow theorem|09GCQ5STVJ]], each Sylow $p$-subgroup of $G$ equals $gPg^{-1} = P$ for some $g \in G$. So $G$ has exactly one Sylow $p$-subgroup. This proves 2.
14. ($2 \Rightarrow 3$.) Write $|G| = p_1^{a_1} \cdots p_r^{a_r}$ with distinct primes $p_k$ and $a_k \geq 1$. Let $P_k$ be the only Sylow $p_k$-subgroup of $G$.
15. For $g \in G$, the subgroup $gP_kg^{-1}$ has order $|P_k|$, so it is a Sylow $p_k$-subgroup. Hence $gP_kg^{-1} = P_k$, and $P_k$ is normal in $G$.
16. Let $Q_0 = \{e\}$ and $Q_k = Q_{k-1} P_k$ for $1 \leq k \leq r$. By step 2 and induction on $k$, each $Q_k$ is a normal subgroup of $G$.
17. We show $|Q_k| = p_1^{a_1} \cdots p_k^{a_k}$ by induction on $k$. The case $k = 0$ is clear. Let $k \geq 1$.
18. By Lagrange's theorem, $|Q_{k-1} \cap P_k|$ divides both $|Q_{k-1}| = p_1^{a_1} \cdots p_{k-1}^{a_{k-1}}$ and $p_k^{a_k}$. These numbers are coprime, so $Q_{k-1} \cap P_k = \{e\}$.
19. By the [[product formula|08PY4GNAPK]], $|Q_k| = |Q_{k-1}|\,|P_k| = p_1^{a_1} \cdots p_k^{a_k}$.
20. So for each $k \geq 1$, the group $Q_k$ is the [[internal direct product|0Q2MVQ7JMT]] of its normal subgroups $Q_{k-1}$ and $P_k$. Also $|Q_r| = |G|$, so $Q_r = P_1 \cdots P_r = G$. This is what 3 says.
21. ($3 \Rightarrow 1$.) Assume 3, in the sense of step 20. So $G$ has Sylow subgroups $P_1, \dots, P_r$, and the groups $Q_0 = \{e\}$ and $Q_k = Q_{k-1}P_k$ satisfy the following. Each $Q_k$ with $k \geq 1$ is the internal direct product of its normal subgroups $Q_{k-1}$ and $P_k$, and $Q_r = G$.
22. Let $X$ and $Y$ be nilpotent with central series $(N_i)$ and $(M_i)$. Adding copies of $X$ or $Y$ at the top keeps a central series, since a trivial factor lies in any centre. So both series have the same length $c$.
23. Let $L_i = N_i \times M_i$. Each $L_i$ is normal in $X \times Y$, since conjugation acts in each coordinate. Also $L_0 = \{e\}$ and $L_c = X \times Y$.
24. For $(x, y) \in L_{i+1}$ and $(g, h) \in X \times Y$, the element $(x, y)^{-1}(g, h)^{-1}(x, y)(g, h)$ equals $(x^{-1}g^{-1}xg,\ y^{-1}h^{-1}yh)$. It lies in $L_i$ by step 1. By step 1 again, $(L_i)$ is a central series, so $X \times Y$ is nilpotent.
25. Let $\alpha \colon X \to X'$ be an isomorphism and let $(N_i)$ be a central series of $X$. Then $(\alpha(N_i))$ is a central series of $X'$, because $\alpha$ preserves the condition of step 1. So a group isomorphic to a nilpotent group is nilpotent.
26. The [[order of each element|08V7JHS3QZ]] of $P_k$ divides $p_k^{a_k}$. So $P_k$ is a finite $p_k$-group, and it is nilpotent because [[finite $p$-groups are nilpotent|081WTKYX6C]].
27. We show by induction on $k$ that $Q_k$ is nilpotent. The group $Q_0 = \{e\}$ is nilpotent. For $k \geq 1$, steps 4 and 21 give $Q_k \cong Q_{k-1} \times P_k$. By steps 24 to 26 and the induction hypothesis, $Q_k$ is nilpotent.
28. So $G = Q_r$ is nilpotent. This proves 1 and closes the cycle of implications.

## Idea

In a nilpotent group, every proper subgroup grows strictly when one passes to its normaliser. The Frattini argument shows that the normaliser of a Sylow normaliser does not grow, so the Sylow normaliser is all of $G$. Once each Sylow subgroup is normal, coprime orders give trivial intersections, and $G$ splits as their direct product. Products of $p$-groups are nilpotent, which closes the circle.
