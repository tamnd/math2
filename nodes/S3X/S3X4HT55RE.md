---
tag: S3X4HT55RE
kind: proof
name: Proof of Gauss's lemma on irreducibility over a UFD
msc: [13F20]
proves: 0QFV5Y1Z5X
uses: [06YMXJMXYS, 09S3PFBEPM, 0VF11ZTTMD, 0QA8CHH8MG, 0SP14DZN0G, 00X2A9G9W3, 052SDEPZH7, 0B5Z1EC66J, 0T233AZ1GE, 019NFGFPR5, 0QRCFZKXH8, 0MNHXBSX3M, 0GJM24EXP9, 0DPF6WRZW6]
sources:
  - url: https://en.wikipedia.org/wiki/Gauss%27s_lemma_(polynomials)
---

## Proof

Let $R$ be a [[unique factorisation domain|06YMXJMXYS]] with [[field of fractions|0VF11ZTTMD]] $K$. We identify $a \in R$ with $a/1 \in K$, so $R[x] \subseteq K[x]$. Let $f \in R[x]$ be [[primitive|0SP14DZN0G]].

1. The rings $R$ and $K$ are [[integral domains|09S3PFBEPM]]. So $R[x]$ and $K[x]$ are integral domains by [[the theorem on polynomial rings|0B5Z1EC66J]], and [[degrees add|0T233AZ1GE]] in products.
2. If $u v = 1$ in $R[x]$, then $\deg u + \deg v = 0$, so $u$ and $v$ are constants of $R$. So the [[units|019NFGFPR5]] of $R[x]$ are the units of $R$.
3. In the same way, the units of $K[x]$ are constants. Every nonzero constant is a unit, since $K$ is a [[field|0QA8CHH8MG]]. So the units of $K[x]$ are the polynomials of [[degree|0DPF6WRZW6]] $0$.
4. Let $p \in R$ be [[prime|0MNHXBSX3M]] and let $G = \sum_i a_i x^i$ and $H = \sum_j b_j x^j$ in $R[x]$. Suppose $p$ divides every coefficient of $G H$, but not every $a_i$ and not every $b_j$.
5. Let $s$ and $t$ be the least indices with $p \nmid a_s$ and $p \nmid b_t$. In the coefficient $\sum_{i + j = s + t} a_i b_j$, each term with $i < s$ or $j < t$ is divisible by $p$.
6. Every term other than $a_s b_t$ has $i < s$ or $j < t$. So $p \mid a_s b_t$, and $p \mid a_s$ or $p \mid b_t$. This is a contradiction.
7. So if a prime $p$ divides every coefficient of $G H$, then $p$ divides every coefficient of $G$ or every coefficient of $H$.
8. Claim: if $r \in R$, $r \neq 0$, and $r f = G H$ with $G, H \in R[x]$, then $f = G' H'$ with $G', H' \in R[x]$, $\deg G' = \deg G$ and $\deg H' = \deg H$.
9. Every nonzero $r$ is $r = u p_1 \cdots p_n$ with $u$ a unit, $n \ge 0$ and all $p_k$ [[irreducible|052SDEPZH7]]. We prove the claim by induction on $n$.
10. If $n = 0$, then $r = u$ is a unit. Take $G' = u^{-1} G$ and $H' = H$.
11. If $n \ge 1$, put $p = p_1$ and $r' = u p_2 \cdots p_n$. Since [[irreducible elements are prime|0QRCFZKXH8]] in $R$, $p$ is prime.
12. The prime $p$ divides every coefficient of $r f = G H$. By step 7 we may assume that $p$ divides every coefficient of $G$, so $G = p G_1$ with $G_1 \in R[x]$ and $\deg G_1 = \deg G$.
13. Then $p (r' f) = p (G_1 H)$. [[Cancelling|0GJM24EXP9]] $p \neq 0$ in $R[x]$ gives $r' f = G_1 H$. The induction hypothesis for $r'$ proves the claim.
14. The polynomial $f$ is not $0$, since the nonunit $0$ divides every coefficient of $0$. If $\deg f = 0$, then $f = a \in R$ divides itself, so $a$ is a unit of $R$.
15. Then $f$ is a unit of $R[x]$ and of $K[x]$. So $f$ is [[irreducible|00X2A9G9W3]] in neither ring, and the statement holds. From now on, let $\deg f \ge 1$.
16. By steps 2 and 3, $f$ is a nonzero nonunit both in $R[x]$ and in $K[x]$.
17. Suppose that $f$ is irreducible in $K[x]$, and let $f = g h$ with $g, h \in R[x]$. Then $g$ or $h$ is a unit of $K[x]$, say $g$.
18. By step 3, $g$ is a nonzero constant $a \in R$. Then $a$ divides every coefficient of $f = a h$. Since $f$ is primitive, $a$ is a unit of $R$, hence of $R[x]$.
19. So $f$ is irreducible in $R[x]$.
20. Conversely, suppose that $f$ is irreducible in $R[x]$. Suppose that $f = g h$ in $K[x]$ with $g$ and $h$ not units of $K[x]$.
21. Since $f \neq 0$, also $g, h \neq 0$. By step 3, $\deg g \ge 1$ and $\deg h \ge 1$.
22. Write the coefficients of $g$ as $u_k / v_k$ with $u_k, v_k \in R$ and $v_k \neq 0$. Let $d$ be the product of the $v_k$. Then $d \neq 0$ and $G = d g$ lies in $R[x]$.
23. In the same way, there is $e \in R$ with $e \neq 0$ and $H = e h \in R[x]$. Then $(d e) f = G H$ in $R[x]$, with $\deg G = \deg g$ and $\deg H = \deg h$.
24. By the claim of step 8, $f = G' H'$ with $G', H' \in R[x]$ of degrees at least $1$. By step 2, neither is a unit of $R[x]$.
25. This contradicts the irreducibility of $f$ in $R[x]$. So $f$ is irreducible in $K[x]$, which proves the equivalence.

## Idea

A factorisation over $K$ can be moved to a factorisation over $R$: clear the denominators, then remove the extra constant one prime at a time. Each prime of the constant divides all coefficients of one factor, because it divides all coefficients of the product. Primitivity rules out constant factors over $R$, so the two notions of irreducibility agree.
