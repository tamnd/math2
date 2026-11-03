---
tag: AEAQCZRWYJ
kind: proof
name: Proof that subgroups of cyclic groups are cyclic
msc: [20K27]
proves: 0KB1ND7XDS
uses: [0B85Q41RP6, 0YT586TKXF, 0N0PXCTYA7, 00DRK90Z6K, 0CHQKZFK5S, 01BX15HSRR]
sources:
  - url: https://kconrad.math.uconn.edu/blurbs/grouptheory/cyclicgp.pdf
    locator: Theorem 2.1
  - url: https://proofwiki.org/wiki/Subgroup_of_Cyclic_Group_is_Cyclic
---

## Proof

1. Let $G$ be a [[cyclic group|0B85Q41RP6]] with generator $g$ and identity $e$. So $G = \set{g^k : k \in \Z}$ by the definition of the [[cyclic subgroup|0YT586TKXF]].
2. Let $H$ be a [[subgroup|0N0PXCTYA7]] of $G$. If $H = \set{e}$, then $H = \langle e \rangle$. Indeed, by the [[laws of exponents|00DRK90Z6K]], $e^k = (e^0)^k = e^0 = e$ for each $k \in \Z$. So $H$ is cyclic.
3. Now suppose $H \neq \set{e}$. Claim: if $x \in H$ and $q \in \Z$, then $x^q \in H$.
4. Indeed $x^0 = e \in H$, and $x^{q+1} = x^q x \in H$ when $x^q \in H$. So $x^q \in H$ for all $q \geq 0$.
5. For $q > 0$, $x^{-q} = (x^{-1})^q$, and $x^{-1} \in H$. By step 4 applied to $x^{-1}$, $x^{-q} \in H$.
6. Choose $x \in H$ with $x \neq e$, and write $x = g^k$. Then $k \neq 0$. By the [[laws of exponents|00DRK90Z6K]], $g^k g^{-k} = g^0 = e$, so $g^{-k} = x^{-1} \in H$. So $g^j \in H$ for some $j > 0$.
7. By the [[well-ordering principle|01BX15HSRR]], there is a least positive integer $m$ with $g^m \in H$.
8. By step 3, each power $(g^m)^q$ lies in $H$. So $\langle g^m \rangle \subseteq H$.
9. Let $y \in H$ and write $y = g^k$. By the [[division algorithm|0CHQKZFK5S]], $k = qm + r$ with $q, r \in \Z$ and $0 \leq r < m$.
10. By the laws of exponents, $g^r = g^{k - qm} = g^k (g^m)^{-q}$. Here $g^k = y \in H$ and $(g^m)^{-q} \in H$ by step 3. So $g^r \in H$.
11. If $r > 0$, this contradicts the minimality of $m$. So $r = 0$, and $y = g^{qm} = (g^m)^q \in \langle g^m \rangle$.
12. So $H \subseteq \langle g^m \rangle$. With step 8, $H = \langle g^m \rangle$, and $H$ is cyclic.

## Idea

The natural candidate for a generator of $H$ is the power of $g$ with the smallest positive exponent in $H$. Division with remainder shows that any other exponent in $H$ is a multiple of this one. Otherwise the remainder would be a smaller positive exponent in $H$.
