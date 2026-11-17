---
tag: AEAQCZRWYJ
kind: proof
name: Proof that subgroups and quotients of cyclic groups are cyclic
msc: ["20K27"]
topics: [BAVE5RN4EE]
audience: ug1
proves: 0KB1ND7XDS
uses: [0KVGH0J5B3, 0X1JXT47GA, 08ABT85339, 00DRK90Z6K, 0CHQKZFK5S, 01BX15HSRR, 04RG02S6BA, 0CB0DX5BVV, 0KYX2N69J0]
methods: [0NTF6DMVAP, 0J0XBKG64S]
sources:
  - url: https://kconrad.math.uconn.edu/blurbs/grouptheory/cyclicgp.pdf
    locator: Theorem 2.1
  - url: https://proofwiki.org/wiki/Subgroup_of_Cyclic_Group_is_Cyclic
---

## Proof

Let $G$ be a [[cyclic group|0KVGH0J5B3]] with generator $g$ and identity $e$.
By the definition of a cyclic group, $G = \langle g \rangle = \set{g^k : k \in \Z}$.

Part 1, subgroups.

1. Let $H$ be a [[subgroup|0X1JXT47GA]] of $G$. Suppose first that $H = \set{e}$. By the [[laws of exponents|00DRK90Z6K]], $e^k = e$ for each $k \in \Z$. So $\langle e \rangle = \set{e} = H$, and $H$ is cyclic.
2. Now suppose that $H \neq \set{e}$. We first show: if $x \in H$ and $q \in \Z$, then $x^q \in H$.
3. The power $x^0 = e$ lies in $H$. If $x^q \in H$ for some $q \geq 0$, then $x^{q+1} = x^q x \in H$ by closure. By induction, $x^q \in H$ for all $q \geq 0$.
4. Let $q > 0$. By the laws of exponents, $x^{-q} = (x^{-1})^q$. Here $x^{-1} \in H$, so step 3 applied to $x^{-1}$ gives $x^{-q} \in H$.
5. Choose $x \in H$ with $x \neq e$, and write $x = g^k$ with $k \in \Z$. Then $k \neq 0$, because $g^0 = e$.
6. If $k > 0$, then $g^k \in H$ with a positive exponent. If $k < 0$, then $g^{-k} = x^{-1} \in H$ by step 4, and $-k > 0$. So $H$ contains $g^j$ for some $j > 0$.
7. By the [[well-ordering principle|01BX15HSRR]], there is a least positive integer $m$ with $g^m \in H$.
8. By steps 3 and 4, each power $(g^m)^q$ with $q \in \Z$ lies in $H$. So $\langle g^m \rangle \subseteq H$.
9. Let $y \in H$, and write $y = g^k$. By the [[division algorithm|0CHQKZFK5S]], $k = qm + r$ with $q, r \in \Z$ and $0 \leq r < m$.
10. By the laws of exponents, $g^r = g^{k - qm} = g^k (g^m)^{-q}$. Here $g^k = y \in H$, and $(g^m)^{-q} \in H$ by step 8. So $g^r \in H$ by closure.
11. Suppose $r > 0$. Then $g^r \in H$ with $0 < r < m$, and this contradicts the choice of $m$ in step 7. So $r = 0$.
12. So $y = g^{qm} = (g^m)^q$, and $y \in \langle g^m \rangle$. Thus $H \subseteq \langle g^m \rangle$.
13. By steps 8 and 12, $H = \langle g^m \rangle$. So $H$ is cyclic, with generator $g^m$.

Part 2, quotients.

14. Let $N$ be a subgroup of $G$. The group $G$ is abelian, because [[cyclic groups are abelian|04RG02S6BA]].
15. Let $a \in G$. For each $n \in N$, we have $an = na$, so $ana^{-1} = n$. Hence $aNa^{-1} = N$ for each $a \in G$, and $N$ is [[normal|0CB0DX5BVV]] in $G$.
16. So the [[quotient group|0KYX2N69J0]] $G/N$ is defined. Its product is $(aN)(bN) = (ab)N$, and its identity is $eN = N$.
17. Let $a \in G$. We show that $(aN)^k = a^k N$ for each $k \geq 0$. For $k = 0$, both sides are $N$.
18. If $(aN)^k = a^k N$, then $(aN)^{k+1} = (a^k N)(aN) = a^{k+1} N$, by the product rule of step 16. By induction, the formula holds for all $k \geq 0$.
19. The inverse of $aN$ is $a^{-1}N$, because $(aN)(a^{-1}N) = eN$. So for $k > 0$, $(aN)^{-k} = (a^{-1}N)^k = a^{-k}N$, by step 18 applied to $a^{-1}$.
20. So $(gN)^k = g^k N$ for every $k \in \Z$, by steps 17 to 19 with $a = g$.
21. Let $C$ be an element of $G/N$. Then $C = aN$ for some $a \in G$, and $a = g^k$ for some $k \in \Z$. By step 20, $C = g^k N = (gN)^k$.
22. So every element of $G/N$ is a power of $gN$. Thus $G/N = \langle gN \rangle$, and $G/N$ is cyclic. $\blacksquare$

## Idea

The candidate for a generator of $H$ is the power of $g$ with the least positive exponent in $H$.
Division with remainder shows that every other exponent in $H$ is a multiple of this one.
Otherwise the remainder is a smaller positive exponent in $H$.
For the quotient, every coset is $g^k N$, and the map $a \mapsto aN$ sends $g^k$ to $(gN)^k$.
So the image of a generator generates the quotient.

## Variants

Part 1 can also start from the integers.
First prove that each subgroup of $(\Z, +)$ is $m\Z$, by the same division argument.
Then the set $\set{k \in \Z : g^k \in H}$ is a subgroup of $\Z$, so it is $m\Z$, and $H = \langle g^m \rangle$.

Part 2 also follows from a more general fact.
The [[quotient map|0N4F5FMQZW]] $a \mapsto aN$ is a surjective [[homomorphism|0JYTG5K9Y4]], and a homomorphism sends $g^k$ to the $k$-th power of the image of $g$.
So the image of a cyclic group under any homomorphism is cyclic.
