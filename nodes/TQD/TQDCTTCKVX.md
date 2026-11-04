---
tag: TQDCTTCKVX
kind: proof
name: Proof of the fundamental theorem of Galois theory
msc: [12F10]
proves: 0T1Q8D0FW8
uses: [0DS2F7GK05, 0XVR72M51M, 02NBKVQFRQ, 0KMJ6919WS, 07QY5RPFBR, X7R15C00ET, P75CXH2Q2B, 0BDJBH8B4Z, 0A7KJ68XHT, 02NZZ1J0FH, 03J8BS7FMV, 0MA5B744K3, 0N0PXCTYA7, 0W77CVBCHQ, 0HV9Y7WG5R, 0YYWCNTPWR, 0CXXJNG5B6, 0CBRFQ7DVZ, 0GK1WB9R98, 0NFEG48RDR, 0SHMC00RJV]
sources:
  - url: https://www.jmilne.org/math/CourseNotes/FT.pdf
    locator: Theorem 3.17
---

## Proof

The main tool is [[Artin's theorem on fixed fields|X7R15C00ET]]. We prove the four parts in order.

1. Let $L/K$ be a finite [[Galois extension|0DS2F7GK05]] and $G = \operatorname{Gal}(L/K)$. By [[the order of the Galois group|0BDJBH8B4Z]], $G$ is finite with $|G| = [L : K]$.
2. Let $H$ be a [[subgroup|0N0PXCTYA7]] of $G$. Its [[fixed field|0KMJ6919WS]] $L^H$ is a [[subfield|07QY5RPFBR]] of $L$. Each element of $H$ fixes $K$, so $K \subseteq L^H$. Thus $L^H$ is an [[intermediate field|02NBKVQFRQ]].
3. By Artin's theorem applied to the finite group $H$, we get $[L : L^H] = |H|$ and $\operatorname{Gal}(L/L^H) = H$.
4. Let $E$ be an intermediate field. By [[the characterizations of Galois extensions|P75CXH2Q2B]], $L$ is a [[splitting field|02NZZ1J0FH]] over $K$ of a [[separable polynomial|03J8BS7FMV]] $f \in K[x]$.
5. Write $f = c(x - a_1) \cdots (x - a_n)$ in $L[x]$, with $L = K(a_1, \dots, a_n)$. Then $L \supseteq E(a_1, \dots, a_n) \supseteq K(a_1, \dots, a_n) = L$, so $L = E(a_1, \dots, a_n)$.
6. Also $f \in E[x]$ is separable over $E$, because the identity $u f + v f' = 1$ with $u, v \in K[x]$ also holds in $E[x]$. So $L$ is a splitting field of a separable polynomial over $E$.
7. The extension $L/E$ is finite, since $[L : K] = [L : E][E : K]$ by the [[tower law|0A7KJ68XHT]]. By the characterizations again, $L/E$ is Galois.
8. Every automorphism of $L$ fixing $E$ fixes $K$. So $\operatorname{Gal}(L/E)$ is a subset of $G$. It contains the identity and is closed under composition and inverses, so it is a subgroup of $G$.
9. Let $H = \operatorname{Gal}(L/E)$ and $E' = L^H$. Every element of $H$ fixes $E$, so $E \subseteq E'$.
10. Since $L/E$ is Galois, $|H| = [L : E]$ by step 1 applied to $L/E$. By step 3, $[L : E'] = |H|$.
11. By the tower law, $[L : E] = [L : E'][E' : E]$. Step 10 gives $[E' : E] = 1$. So $E'$ is a $1$-dimensional $E$-space that contains $E$, and $E' = E$.
12. Steps 3 and 11 show that $\operatorname{Gal}(L/L^H) = H$ and $L^{\operatorname{Gal}(L/E)} = E$. So the two maps are inverse bijections. This proves part 1.
13. For part 2, let $H_1 \subseteq H_2$ be subgroups. An element fixed by all of $H_2$ is fixed by all of $H_1$. So $L^{H_1} \supseteq L^{H_2}$.
14. Conversely, suppose $L^{H_1} \supseteq L^{H_2}$. An automorphism fixing $L^{H_1}$ fixes $L^{H_2}$. So $\operatorname{Gal}(L/L^{H_1}) \subseteq \operatorname{Gal}(L/L^{H_2})$, that is, $H_1 \subseteq H_2$ by step 3. This proves part 2.
15. For part 3, step 3 gives $[L : L^H] = |H|$. The tower law gives $[L : K] = [L : L^H][L^H : K]$. With step 1, $[L^H : K] = |G| / |H|$.
16. For part 4, fix a subgroup $H$ and let $E = L^H$. Suppose first that $E/K$ is [[normal|0CBRFQ7DVZ]]. Let $\sigma \in G$ and $a \in E$.
17. Let $q$ be the [[minimal polynomial|0GK1WB9R98]] of $a$ over $K$. It is [[irreducible|0NFEG48RDR]] and has the root $a \in E$. By normality, $q$ [[splits|0SHMC00RJV]] over $E$ as $q = (x - e_1) \cdots (x - e_m)$ with $e_i \in E$.
18. Since $\sigma$ fixes the coefficients of $q$, we get $q(\sigma(a)) = \sigma(q(a)) = 0$. So $\prod_i (\sigma(a) - e_i) = 0$ in the field $L$, and $\sigma(a) = e_i$ for some $i$. Hence $\sigma(E) \subseteq E$ for every $\sigma \in G$.
19. Let $\tau \in H$, $\sigma \in G$ and $a \in E$. By step 18 for $\sigma^{-1}$, $\sigma^{-1}(a) \in E$, so $\tau(\sigma^{-1}(a)) = \sigma^{-1}(a)$. Thus $\sigma \tau \sigma^{-1}(a) = a$.
20. So $\sigma \tau \sigma^{-1}$ fixes $E$ and lies in $\operatorname{Gal}(L/E) = H$, by step 3. Hence $H$ is a [[normal subgroup|0W77CVBCHQ]] of $G$.
21. Now suppose that $H$ is normal in $G$. Let $\sigma \in G$, $a \in E$ and $\tau \in H$. Then $\sigma^{-1} \tau \sigma \in H$, so $\tau(\sigma(a)) = \sigma(\sigma^{-1} \tau \sigma(a)) = \sigma(a)$.
22. So $\sigma(a) \in L^H = E$, that is, $\sigma(E) \subseteq E$ for every $\sigma \in G$. Applying this to $\sigma^{-1}$ gives $E \subseteq \sigma(E)$. So $\sigma(E) = E$.
23. Hence the restriction $\sigma|_E$ is an automorphism of $E$ fixing $K$. The map $r \colon G \to \operatorname{Aut}(E)$, $\sigma \mapsto \sigma|_E$, is a [[group homomorphism|0HV9Y7WG5R]], since restriction respects composition.
24. Its kernel is the set of $\sigma \in G$ that fix $E$ pointwise. This is $\operatorname{Gal}(L/E) = H$, by step 3.
25. The image $r(G)$ is a finite group of automorphisms of $E$. An element $a \in E$ fixed by all of $r(G)$ lies in $L^G$. By step 12 with $E = K$, $L^G = L^{\operatorname{Gal}(L/K)} = K$. So $E^{r(G)} = K$.
26. By Artin's theorem applied to $E$ and $r(G)$, the extension $E/K$ is Galois, so it is normal. This proves that $E/K$ is normal if and only if $H$ is normal in $G$.
27. Artin's theorem also gives $\operatorname{Gal}(E/K) = r(G)$. By the [[first isomorphism theorem|0CXXJNG5B6]] and step 24, the [[quotient group|0YYWCNTPWR]] $G/H$ is isomorphic to $r(G) = \operatorname{Gal}(L^H/K)$.
28. In both directions of part 4, $H$ is normal, so steps 21 to 27 apply. This proves part 4 and the theorem.

## Idea

Artin's theorem says that a finite group $H$ of automorphisms is exactly the group of symmetries of $L$ over its fixed field, and that $[L : L^H] = |H|$. This gives one round trip. For the other, $L$ stays Galois over every intermediate field, and a degree count shows that the fixed field of $\operatorname{Gal}(L/E)$ cannot be larger than $E$. Normality matches because $\sigma$ moves $L^H$ to $L^{\sigma H \sigma^{-1}}$, so $L^H$ is stable under $G$ exactly when $H$ is.
