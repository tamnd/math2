---
tag: CARDX0G5Z0
kind: proof
name: Proof that a subgroup whose index is the smallest prime divisor of the order is normal
msc: [20D60]
proves: 0FEBE9NC0E
uses: [04QEBF8S49, 05FD317V2W, 0RJMNEN3BJ, 01VG2A0BHW, 0HV9Y7WG5R, 0N0PXCTYA7, 0Z424HK8CQ, 0C9ZKYSPYR, 0CXXJNG5B6, 085PND4KNT, 3C53TD, 0CEBCS0E0E, 0YYWCNTPWR, 04DC0SRN2K, 084HH1NDCB, 051VYKA1EX, 0W77CVBCHQ]
sources:
  - url: https://en.wikipedia.org/wiki/Index_of_a_subgroup
    locator: Properties
---

## Proof

We let $G$ act on the left cosets of $H$ and show that $H$ is the kernel of this action.

1. Let $G$ be a finite group, let $p$ be the smallest prime that divides $|G|$, and let $H \le G$ have [[index|04QEBF8S49]] $p$.
2. Let $X$ be the set of [[left cosets|05FD317V2W]] $xH$ with $x \in G$. By the definition of the index, $|X| = p$.
3. For $g \in G$ and a subset $A$ of $G$, write $gA = \{ga : a \in A\}$. Then $g(xH) = (gx)H$ for each $x \in G$.
4. For $g \in G$, define $\rho_g \colon X \to X$ by $\rho_g(C) = gC$. By step 3, $\rho_g(xH) = (gx)H$ lies in $X$, so $\rho_g$ is a map from $X$ to $X$.
5. For $g, h \in G$ and $C \in X$, we have $\rho_g(\rho_h(C)) = g(hC) = (gh)C = \rho_{gh}(C)$. Also $\rho_e(C) = C$, where $e$ is the identity of $G$.
6. By step 5, $\rho_g \circ \rho_{g^{-1}} = \rho_e$ and $\rho_{g^{-1}} \circ \rho_g = \rho_e$ are the identity of $X$. So $\rho_g$ is [[bijective|01VG2A0BHW]].
7. Thus $\rho_g$ lies in the [[symmetric group|0RJMNEN3BJ]] $\operatorname{Sym}(X)$. By step 5, the map $\rho \colon G \to \operatorname{Sym}(X)$, $g \mapsto \rho_g$, is a [[group homomorphism|0HV9Y7WG5R]].
8. By step 5 and step 6, the image $\operatorname{im} \rho$ contains $\rho_e$ and is closed under products and inverses. So $\operatorname{im} \rho$ is a [[subgroup|0N0PXCTYA7]] of $\operatorname{Sym}(X)$.
9. Let $K = \ker \rho$ be the [[kernel|0Z424HK8CQ]]. By [[the kernel is a normal subgroup|0C9ZKYSPYR]], $K$ is a normal subgroup of $G$.
10. Let $g \in K$. Then $\rho_g(H) = H$, that is, $gH = H$. Since $e \in H$, we get $g = ge \in gH = H$. So $K \subseteq H$, and $K$ is a subgroup of $H$.
11. By the [[first isomorphism theorem|0CXXJNG5B6]], the [[quotient group|0YYWCNTPWR]] $G/K$ is isomorphic to $\operatorname{im} \rho$. An [[isomorphism|085PND4KNT]] is a bijection, so $|G/K| = |\operatorname{im} \rho|$.
12. By [[Lagrange's theorem|3C53TD]] and step 8, $|\operatorname{im} \rho|$ divides $|\operatorname{Sym}(X)|$. By the [[number of permutations|0CEBCS0E0E]], $|\operatorname{Sym}(X)| = p!$.
13. The set $G/K$ is the set of left cosets of $K$, so $|G/K| = [G : K]$. Let $d = [G : K]$. By steps 11 and 12, $d$ divides $p!$.
14. Let $m = [H : K]$. By [[the order of a group is the index times the order of the subgroup|04DC0SRN2K]], $|G| = p \, |H|$, $|H| = m \, |K|$ and $|G| = d \, |K|$.
15. By step 14, $d \, |K| = p \, m \, |K|$. Since $|K| \ge 1$, we get $d = pm$.
16. By steps 13 and 15, $pm$ divides $p! = p \cdot (p-1)!$. Dividing by $p$, we get that $m$ divides $(p-1)!$.
17. Suppose that $m > 1$. By the [[fundamental theorem of arithmetic|084HH1NDCB]], some prime $q$ divides $m$.
18. By step 14, $|G| = p \, m \, |K|$, so $q$ divides $|G|$. Since $p$ is the smallest prime that divides $|G|$, we get $q \ge p$.
19. If $p = 2$, then $(p-1)! = 1$, and the prime $q$ does not divide $1$. This contradicts step 16.
20. If $p \ge 3$, then $q$ divides the product $1 \cdot 2 \cdots (p-1)$. Applying [[Euclid's lemma|051VYKA1EX]] repeatedly, $q$ divides some factor $j$ with $1 \le j \le p-1$.
21. A prime that divides the positive integer $j$ is at most $j$. So $q \le p - 1 < p$, which contradicts step 18.
22. Hence $m = 1$, so $|H| = |K|$ by step 14. Since $K \subseteq H$ and $H$ is finite, $K = H$.
23. By step 9, $H = K$ is [[normal|0W77CVBCHQ]] in $G$.

## Idea

The group permutes the $p$ cosets of $H$, which gives a homomorphism to a group of order $p!$. Its kernel lies inside $H$, and the index of the kernel divides both $|G|$ and $p!$. The only common room is the prime $p$ itself, because $|G|$ has no prime factor below $p$ and $p!$ has only one factor $p$. So the kernel has index $p$, and it must be all of $H$.
