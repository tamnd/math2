---
tag: Q4FCVHGJ40
kind: proof
name: Proof of the formula for the order of a power
msc: [20A05]
topics: [BAZT8JJ70S]
audience: ug1
proves: 0VVPQNVM8S
uses: [G5S1M9, 0WE2NHZJ7B, 00DRK90Z6K, 0F5QC101Q7, 0C8WYW4KYQ, 03BAREW1Z5, 0PG2H7WKGG, 0DQVHMYAGA, YJRBCWQV6B]
methods: [0NTF6DMVAP, 0ASJVEFA9J]
sources:
  - url: https://proofwiki.org/wiki/Order_of_Power_of_Group_Element
---

## Proof

We prove part 1 first.

1. Let $G$ be a [[group|G5S1M9]] with identity $e$. Let $g \in G$ have [[order|0WE2NHZJ7B]] $n \geq 1$, and let $k \in \Z$.
2. Let $d = \gcd(n, k)$ be the [[greatest common divisor|0C8WYW4KYQ]]. Since $n \neq 0$ and $1$ is a common divisor, $d \geq 1$.
3. Since $d$ [[divides|0PG2H7WKGG]] $n$ and $k$, write $n = dt$ and $k = dk'$ with integers $t, k'$. Then $t = n/d \geq 1$.
4. Claim: $\gcd(t, k') = 1$. Let $c = \gcd(t, k')$. Since $t \neq 0$, we have $c \geq 1$.
5. Then $cd$ divides $dt = n$ and $dk' = k$. So $cd$ is a common divisor of $n$ and $k$, and hence $cd \leq d$. So $c \leq 1$, and $c = 1$.
6. Let $s$ be a positive integer. By the [[laws of exponents|00DRK90Z6K]], $(g^k)^s = g^{ks}$.
7. By [[the divisibility criterion for powers|0F5QC101Q7]], $g^{ks} = e$ if and only if $n$ divides $ks$.
8. Since $n = dt$ and $ks = dk's$ with $d \neq 0$, $n$ divides $ks$ if and only if $t$ divides $k's$. Indeed, for $q \in \Z$, $ks = nq$ means $dk's = dtq$, which is $k's = tq$.
9. If $t$ divides $k's$, then $t$ divides $s$, by step 4 and the [[generalized Euclid's lemma|03BAREW1Z5]]. If $t$ divides $s$, then $t$ divides $k's$.
10. By steps 6 to 9, for each positive integer $s$, $(g^k)^s = e$ if and only if $t$ divides $s$.
11. In particular $(g^k)^t = e$. Each positive $s$ with $(g^k)^s = e$ is a positive multiple of $t$, so $s \geq t$.
12. So $t$ is the least positive integer $s$ with $(g^k)^s = e$. The order of $g^k$ is $t = n / \gcd(n, k)$.

Now we prove part 2.
Let $g, h \in G$ with $gh = hg$, let $g$ have order $m$, let $h$ have order $n$, and let $\gcd(m, n) = 1$.

13. For each integer $s \geq 0$, we have $h g^s = g^s h$. Proof by [[induction|0ASJVEFA9J]] on $s$: for $s = 0$ both sides are $h$. If $h g^s = g^s h$, then $h g^{s+1} = h g^s g = g^s h g = g^s g h = g^{s+1} h$, by the hypothesis $hg = gh$.
14. For each integer $s \geq 0$, we have $(gh)^s = g^s h^s$. Proof by induction on $s$: for $s = 0$ both sides are $e$. If $(gh)^s = g^s h^s$, then $(gh)^{s+1} = g^s h^s g h$.
15. The elements $g$ and $h^s$ commute, by step 13 with the roles of $g$ and $h$ exchanged. So $g^s h^s g h = g^s g h^s h = g^{s+1} h^{s+1}$, and the induction is complete.
16. By step 14 and the laws of exponents, $(gh)^{mn} = g^{mn} h^{mn} = (g^m)^n (h^n)^m = e^n e^m = e$.
17. Now let $s$ be a positive integer with $(gh)^s = e$. By step 14, $g^s h^s = e$.
18. Multiply on the right by $h^{-s}$: $g^s = g^s h^s h^{-s} = e h^{-s} = h^{-s}$. Let $y = g^s = h^{-s}$.
19. Then $y^m = (g^s)^m = (g^m)^s = e$, and $y^n = (h^{-s})^n = (h^n)^{-s} = e$, by the laws of exponents.
20. Since $\gcd(m, n) = 1$, [[Bezout's identity|0DQVHMYAGA]] gives integers $u$ and $v$ with $um + vn = 1$.
21. So $y = y^{um + vn} = (y^m)^u (y^n)^v = e$, by step 19 and the laws of exponents.
22. Thus $g^s = y = e$ and $h^{-s} = y = e$. Then $h^s = (h^{-s})^{-1} = e^{-1} = e$.
23. By the divisibility criterion, $m$ divides $s$ and $n$ divides $s$. Write $s = m s'$ with $s' \in \Z$.
24. Then $n$ divides $m s'$, and $\gcd(n, m) = 1$. By the generalized Euclid's lemma, $n$ divides $s'$. So $mn$ divides $s$.
25. By step 24, each positive $s$ with $(gh)^s = e$ is a positive multiple of $mn$, so $s \geq mn$.
26. By step 16, $(gh)^{mn} = e$, and $mn$ is positive. With step 25, $mn$ is the least positive integer $s$ with $(gh)^s = e$. So $gh$ has order $mn$.

## Idea

For part 1, $(g^k)^s = e$ exactly when $n$ divides $ks$.
After the common factor $d = \gcd(n, k)$ is removed from $n$ and $k$, the parts that are left are coprime.
So the condition becomes "$n/d$ divides $s$", and the least such $s$ is $n/d$.
For part 2, $(gh)^s = e$ forces the element $g^s = h^{-s}$ to have an order that divides both $m$ and $n$, so this element is $e$, and then $s$ is a multiple of both $m$ and $n$.

## Variants

1. Part 1 through [[cyclic subgroups|08ABT85339]]. The subgroup $\langle g^k \rangle$ equals $\langle g^d \rangle$ with $d = \gcd(n, k)$, because $d = un + vk$ gives $g^d = (g^k)^v$. The powers $e, g^d, g^{2d}, \ldots, g^{n - d}$ are the $n/d$ different elements of $\langle g^d \rangle$.
2. Part 2 through subgroups. The element $g^s = h^{-s}$ of step 18 lies in $\langle g \rangle \cap \langle h \rangle$. The order of this intersection divides $m$ and $n$ by [[Lagrange's theorem|3C53TD]], so it is $1$. This gives step 22 without Bezout's identity.
