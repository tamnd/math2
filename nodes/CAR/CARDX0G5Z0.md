---
tag: CARDX0G5Z0
kind: proof
name: Proof that a subgroup of smallest prime index is normal
msc: ["20D60"]
topics: [E1506A5A55]
audience: ug2
proves: 0FEBE9NC0E
uses: [0DTXBQPA2S, 03DEH43F4H, 0515A6D2Y1, 01VG2A0BHW, 0JYTG5K9Y4, 0X1JXT47GA, 0W88CEGQP1, 0C9ZKYSPYR, 0CXXJNG5B6, 08MG7H8JW5, 0KYX2N69J0, 3C53TD, 0CEBCS0E0E, 04DC0SRN2K, 084HH1NDCB, 051VYKA1EX, 0CB0DX5BVV]
methods: [0J0XBKG64S, 0WCP0PVET6]
sources:
  - url: https://en.wikipedia.org/wiki/Index_of_a_subgroup
    locator: Properties
---

## Proof

We let $G$ act on the left cosets of $H$ and show that $H$ is the kernel of this action.

1. Let $G$ be a finite group, let $p$ be the smallest prime that divides $|G|$, and let $H \le G$ have [[index|0DTXBQPA2S]] $p$.
2. Let $X$ be the set of [[left cosets|03DEH43F4H]] $xH$ with $x \in G$. By the definition of the index, $|X| = p$. This step uses the hypothesis $[G : H] = p$.
3. For $g \in G$ and a subset $A$ of $G$, write $gA = \{ga : a \in A\}$. Then $g(xH) = (gx)H$ for each $x \in G$.
4. For $g \in G$, define $\rho_g \colon X \to X$ by $\rho_g(C) = gC$. By step 3, $\rho_g(xH) = (gx)H$ lies in $X$, so $\rho_g$ is a map from $X$ to $X$.
5. For $g, h \in G$ and $C \in X$, we have $\rho_g(\rho_h(C)) = g(hC) = (gh)C = \rho_{gh}(C)$. Also $\rho_e(C) = C$, where $e$ is the identity of $G$.
6. By step 5, $\rho_g \circ \rho_{g^{-1}} = \rho_e$ and $\rho_{g^{-1}} \circ \rho_g = \rho_e$ are the identity of $X$. So $\rho_g$ is [[bijective|01VG2A0BHW]].
7. Thus $\rho_g$ lies in the [[symmetric group|0515A6D2Y1]] $\operatorname{Sym}(X)$. By step 5, the map $\rho \colon G \to \operatorname{Sym}(X)$, $g \mapsto \rho_g$, is a [[group homomorphism|0JYTG5K9Y4]].
8. By step 5 and step 6, the image $\operatorname{im} \rho$ contains $\rho_e$ and is closed under products and inverses. So $\operatorname{im} \rho$ is a [[subgroup|0X1JXT47GA]] of $\operatorname{Sym}(X)$.
9. Let $K = \ker \rho$ be the [[kernel|0W88CEGQP1]]. By [[kernels are normal|0C9ZKYSPYR]], $K$ is a normal subgroup of $G$.
10. Let $g \in K$. Then $\rho_g(H) = H$, that is, $gH = H$. Since $e \in H$, we get $g = ge \in gH = H$. So $K \subseteq H$, and $K$ is a subgroup of $H$.
11. By the [[first isomorphism theorem|0CXXJNG5B6]], the [[quotient group|0KYX2N69J0]] $G/K$ is isomorphic to $\operatorname{im} \rho$. An [[isomorphism|08MG7H8JW5]] is a bijection, so $|G/K| = |\operatorname{im} \rho|$.
12. By [[Lagrange's theorem|3C53TD]] and step 8, $|\operatorname{im} \rho|$ divides $|\operatorname{Sym}(X)|$. By the [[number of permutations|0CEBCS0E0E]], $|\operatorname{Sym}(X)| = p!$.
13. The set $G/K$ is the set of left cosets of $K$, so $|G/K| = [G : K]$. Let $d = [G : K]$. By steps 11 and 12, $d$ divides $p!$.
14. Let $m = [H : K]$. By [[the order of a group is the index times the order of the subgroup|04DC0SRN2K]], $|G| = p \, |H|$, $|H| = m \, |K|$ and $|G| = d \, |K|$.
15. By step 14, $d \, |K| = p \, m \, |K|$. Since $|K| \ge 1$, we get $d = pm$.
16. By steps 13 and 15, $pm$ divides $p! = p \cdot (p-1)!$. Dividing by $p$, we get that $m$ divides $(p-1)!$.
17. Suppose, for a contradiction, that $m > 1$. By the [[fundamental theorem of arithmetic|084HH1NDCB]], some prime $q$ divides $m$.
18. By step 14, $|G| = p \, m \, |K|$, so $q$ divides $|G|$. So $q \ge p$. This step uses the hypothesis that $p$ is the smallest prime that divides $|G|$.
19. If $p = 2$, then $(p-1)! = 1$, and the prime $q$ does not divide $1$. This contradicts step 16.
20. If $p \ge 3$, then $q$ divides the product $1 \cdot 2 \cdots (p-1)$. Applying [[Euclid's lemma|051VYKA1EX]] repeatedly, $q$ divides some factor $j$ with $1 \le j \le p-1$.
21. A prime that divides the positive integer $j$ is at most $j$. So $q \le p - 1 < p$, which contradicts step 18.
22. Hence $m = 1$, so $|H| = |K|$ by step 14. Since $K \subseteq H$ and $H$ is finite, $K = H$.
23. By step 9, $H = K$ is [[normal|0CB0DX5BVV]] in $G$.

## Idea

The group permutes the $p$ cosets of $H$, which gives a homomorphism to a group of order $p!$.
Its kernel lies inside $H$, and the index of the kernel divides both $|G|$ and $p!$.
The only common divisor of this kind is the prime $p$ itself, because $|G|$ has no prime factor below $p$ and $p!$ has only one factor $p$.
So the kernel has index $p$, and it must be all of $H$.

## Variants

A proof with orbits avoids the first isomorphism theorem.

1. Let $H$ act on the set $X$ of the $p$ left cosets of $H$ by $h \cdot xH = (hx)H$.
2. The coset $H$ is fixed by each $h \in H$. So $H$ permutes the other $p - 1$ cosets.
3. By the [[orbit-stabiliser theorem|0E2HSCKZ6C]], the size of each orbit divides $|H|$, and $|H|$ divides $|G|$.
4. So each prime factor of the size of an orbit is at least $p$. This uses the hypothesis that $p$ is the smallest prime divisor.
5. An orbit inside the $p - 1$ other cosets has size at most $p - 1$. So its size has no prime factor, and it is $1$.
6. So $hxH = xH$ for each $h \in H$ and each $x \in G$. Then $x^{-1}hx \in H$, by the test for equal cosets.
7. So $x^{-1}Hx \subseteq H$ for each $x \in G$, and with $x^{-1}$ in place of $x$, $H$ is normal.
