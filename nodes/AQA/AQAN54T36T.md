---
tag: AQAN54T36T
kind: proof
name: Proof of the fundamental theorem of cyclic groups
msc: ["20K01"]
topics: [BAVE5RN4EE]
audience: ug1
proves: 0423TXR9AN
uses: [0KVGH0J5B3, 0X1JXT47GA, 08ABT85339, 0WE2NHZJ7B, 031M8HX7DA, 0VVPQNVM8S, 0KB1ND7XDS, 00DRK90Z6K, 0C8WYW4KYQ, 007NPQX34K, 0PG2H7WKGG, 0SRATCFF1W, 0D3WA36K2Q, 0ZTGMDNVTB]
methods: [0NTF6DMVAP]
sources:
  - url: https://kconrad.math.uconn.edu/blurbs/grouptheory/cyclicgp.pdf
    locator: Theorems 3.5 and 3.6
  - url: https://proofwiki.org/wiki/Subgroup_of_Finite_Cyclic_Group_is_Determined_by_Order
---

## Proof

Let $G = \langle g \rangle$ be a [[cyclic group|0KVGH0J5B3]] of finite order $n$.
For a positive divisor $d$ of $n$, put $H_d = \langle g^{n/d} \rangle$.

Preparation.

1. By the [[order of a cyclic subgroup|031M8HX7DA]], an element of infinite [[order|0WE2NHZJ7B]] generates an infinite subgroup. Since $\langle g \rangle = G$ is finite, $g$ has finite order.
2. The same result gives $\abs{\langle x \rangle}$ equal to the order of $x$, for each $x \in G$. In particular, $g$ has order $\abs{G} = n$.

Part 1, existence and uniqueness.

3. Let $d$ be a positive [[divisor|0PG2H7WKGG]] of $n$, and put $c = n/d$, a positive integer.
4. The integer $c$ divides $n$ and $c$, and every divisor of $c$ is at most $c$. So $\gcd(n, c) = c$, by the definition of the [[greatest common divisor|0C8WYW4KYQ]].
5. By the [[order of a power|0VVPQNVM8S]], $g^c$ has order $n / \gcd(n, c) = n/c = d$. By step 2, $H_d = \langle g^c \rangle$ has order $d$.
6. Let $H$ be a [[subgroup|0X1JXT47GA]] of $G$ of order $d$. Since [[subgroups of cyclic groups are cyclic|0KB1ND7XDS]], $H = \langle x \rangle$ for some $x \in G$.
7. Write $x = g^k$ with $k \in \Z$. By step 2 and the order of a power, $d = \abs{H} = n / \gcd(n, k)$. So $\gcd(n, k) = n/d = c$.
8. The gcd of $n$ and $k$ divides $k$, so $c$ divides $k$. Write $k = cu$ with $u \in \Z$.
9. Each element of $H$ is $x^j$ for some $j \in \Z$. By the [[laws of exponents|00DRK90Z6K]], $x^j = g^{cuj} = (g^c)^{uj} \in H_d$. So $H \subseteq H_d$.
10. Both $H$ and $H_d$ have exactly $d$ elements. A subset of a finite set with the same number of elements is the whole set. So $H = H_d$.

Part 2, all subgroups.

11. Let $H$ be a subgroup of $G$. As in steps 6 and 7, $H = \langle g^k \rangle$ for some $k \in \Z$, and $\abs{H} = n / \gcd(n, k)$.
12. Put $d = \abs{H}$. Then $n = d \cdot \gcd(n, k)$, so $d$ is a positive divisor of $n$.
13. By steps 6 to 10, applied to $H$ and $d$, we get $H = H_d$. So every subgroup is one of the groups $H_d$.
14. By step 5, $H_d$ has order $d$. So $H_d \neq H_{d'}$ when $d \neq d'$. Thus $d \mapsto H_d$ is a bijection from the positive divisors of $n$ onto the subgroups of $G$.

Part 3, containment.

15. Let $d$ and $d'$ be positive divisors of $n$, and suppose that $d \mid d'$. Write $d' = dt$ with $t$ a positive integer.
16. Then $n/d = (n/d') \cdot t$. By the laws of exponents, $g^{n/d} = (g^{n/d'})^t$, so $g^{n/d} \in H_{d'}$.
17. A subgroup that contains $x$ contains the [[cyclic subgroup|08ABT85339]] $\langle x \rangle$. With $x = g^{n/d}$, this gives $H_d \subseteq H_{d'}$.
18. Conversely, suppose that $H_d \subseteq H_{d'}$. Then $H_d$ is a subgroup of $H_{d'}$.
19. The group $H_{d'}$ is cyclic of order $d'$, by step 5. By part 2 applied to $H_{d'}$, the order $d$ of $H_d$ divides $d'$.

Part 4, the lattice.

20. By step 14, the map $H \mapsto \abs{H}$ is a bijection from the subgroups of $G$ onto the positive divisors of $n$. Its inverse is $d \mapsto H_d$.
21. By part 3, $H \subseteq K$ if and only if $\abs{H}$ divides $\abs{K}$. So the map is an [[order isomorphism|0D3WA36K2Q]].
22. Let $H = H_d$ and $K = H_{d'}$. The [[intersection of subgroups|0ZTGMDNVTB]] $H \cap K$ is a subgroup, so $H \cap K = H_f$ with $f = \abs{H \cap K}$, by part 2.
23. Since $H_f \subseteq H_d$ and $H_f \subseteq H_{d'}$, part 3 gives $f \mid d$ and $f \mid d'$.
24. Put $u = \gcd(d, d')$. Then $u \mid d$ and $d \mid n$, so $u$ is a positive divisor of $n$. By part 3, $H_u \subseteq H_d$ and $H_u \subseteq H_{d'}$, so $H_u \subseteq H_f$, and $u \mid f$.
25. By the [[classification of the subgroups of the integers|0SRATCFF1W]], part 3, $u = dx + d'y$ for some integers $x, y$. By step 23, $f$ divides $u$.
26. So $u \mid f$ and $f \mid u$, with $u, f > 0$. Thus $f = u = \gcd(d, d')$.
27. Now let $J = \langle H \cup K \rangle$, the least subgroup that contains $H$ and $K$. By part 2, $J = H_s$ with $s = \abs{J}$.
28. Since $H_d \subseteq H_s$ and $H_{d'} \subseteq H_s$, part 3 gives $d \mid s$ and $d' \mid s$. So $s$ is a common multiple of $d$ and $d'$.
29. Put $v = \operatorname{lcm}(d, d')$. By part 4 of the classification of the subgroups of the integers, $d\Z \cap d'\Z = v\Z$. Since $s$ lies in $d\Z \cap d'\Z$, we get $v \mid s$.
30. Also $n$ lies in $d\Z \cap d'\Z = v\Z$, so $v \mid n$, and $H_v$ is defined. By part 3, $H_d \subseteq H_v$ and $H_{d'} \subseteq H_v$.
31. Since $J$ is the least subgroup that contains $H$ and $K$, we get $H_s = J \subseteq H_v$. So $s \mid v$ by part 3.
32. So $s \mid v$ and $v \mid s$, with $s, v > 0$. Thus $s = v = \operatorname{lcm}(d, d')$.
33. So the map $H \mapsto \abs{H}$ sends $H \cap K$ to $\gcd(\abs{H}, \abs{K})$ and $\langle H \cup K \rangle$ to $\operatorname{lcm}(\abs{H}, \abs{K})$. $\blacksquare$

## Idea

A subgroup of $G$ is generated by one power $g^k$, and its size is $n / \gcd(n, k)$, a divisor of $n$.
The subgroup depends only on its size $d$, because its generator is a power of $g^{n/d}$.
So the subgroups match the divisors of $n$.
Containment matches divisibility, because a cyclic group of order $d'$ has subgroups only of orders that divide $d'$.
Then intersection and generation match $\gcd$ and $\operatorname{lcm}$.

## Variants

The theorem also follows from the integers.
The map $k \mapsto g^k$ identifies $G$ with $\Z/n\Z$.
By the [[correspondence theorem|0S9ZVZ34MD]], the subgroups of $\Z/n\Z$ match the subgroups of $\Z$ that contain $n\Z$.
These are the groups $c\Z$ with $c \mid n$, and $c\Z / n\Z$ has order $n/c$.
Containment, intersection and sum of the groups $c\Z$ then follow from the rules for the integers.
