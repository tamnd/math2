---
tag: G9RVEPQJHM
kind: proof
name: Proof that the group of units of Z/pZ is cyclic by counting elements of each order
msc: [11A07, 20K01]
proves: 0QTHB6PE52
uses: [0NV6E43P4A, 0F8X8ZRQ53, 019NFGFPR5, 0WE2NHZJ7B, 08V7JHS3QZ, 031M8HX7DA, 0KJVQV3E0F, 0DPF6WRZW6, 0VVPQNVM8S, 0VV04M41AN, 09JXE6XMCC, 0KVGH0J5B3]
sources:
  - url: https://kconrad.math.uconn.edu/blurbs/grouptheory/cyclicmodp.pdf
    locator: Section 2, Theorem 2.6
---

## Proof

We count the elements of each order and compare with the totient function.

1. Let $p$ be a prime and let $G = (\Z/p\Z)^\times$ be the [[group of units|0F8X8ZRQ53]] of $\Z/p\Z$. Write $1$ for its identity $[1]$.
2. The ring $\Z/p\Z$ is a [[field|0NV6E43P4A]], so each nonzero class is a [[unit|019NFGFPR5]].
3. The class $[0]$ is not a unit, because $[0][x] = [0] \neq [1]$ for each $x$, as $p \geq 2$. So $G$ is the set of the $p - 1$ nonzero classes, and $\abs{G} = p - 1$.
4. For each positive divisor $d$ of $p - 1$, let $N(d)$ be the number of elements of $G$ of [[order|0WE2NHZJ7B]] $d$.
5. Each element of the finite group $G$ has an order, and this order [[divides|08V7JHS3QZ]] $\abs{G} = p - 1$. So $\sum_{d \mid p - 1} N(d) = p - 1$.
6. Fix a positive divisor $d$ of $p - 1$. We show that $N(d) \leq \varphi(d)$, where $\varphi$ is [[Euler's totient function|0VV04M41AN]]. If $N(d) = 0$, this holds, since $\varphi(d) \geq 0$.
7. Otherwise, let $a \in G$ have order $d$. The powers $a^0, a^1, \ldots, a^{d-1}$ are $d$ [[distinct elements|031M8HX7DA]] of $G$.
8. Each power satisfies $(a^k)^d = (a^d)^k = 1$. So each of them is a root of the polynomial $T^d - 1$ in $\Z/p\Z$.
9. The polynomial $T^d - 1$ is nonzero of [[degree|0DPF6WRZW6]] $d$. Since $\Z/p\Z$ is a field, it has [[at most $d$ roots|0KJVQV3E0F]] in $\Z/p\Z$.
10. By steps 7 to 9, the roots of $T^d - 1$ in $\Z/p\Z$ are exactly $a^0, \ldots, a^{d-1}$.
11. Let $b \in G$ have order $d$. Then $b^d = 1$, so $b$ is a root of $T^d - 1$. By step 10, $b = a^k$ for some $k$ with $0 \leq k \leq d - 1$.
12. By the [[order of a power|0VVPQNVM8S]], $a^k$ has order $d / \gcd(d, k)$. This equals $d$ if and only if $\gcd(d, k) = 1$.
13. The powers in step 7 are distinct, so $N(d)$ is the number of $k$ with $0 \leq k \leq d - 1$ and $\gcd(d, k) = 1$.
14. Since $\gcd(d, 0) = d = \gcd(d, d)$, we may replace $k = 0$ by $k = d$. So $N(d)$ is the number of $k$ with $1 \leq k \leq d$ and $\gcd(d, k) = 1$, which is $\varphi(d)$.
15. Thus $N(d) \leq \varphi(d)$ for every positive divisor $d$ of $p - 1$.
16. By step 5, step 15 and the [[sum of the totient over the divisors|09JXE6XMCC]], $p - 1 = \sum_{d \mid p - 1} N(d) \leq \sum_{d \mid p - 1} \varphi(d) = p - 1$.
17. So the inequality in step 16 is an equality. Each term satisfies $N(d) \leq \varphi(d)$, so $N(d) = \varphi(d)$ for each divisor $d$ of $p - 1$.
18. In particular, $N(p - 1) = \varphi(p - 1)$. This is at least $1$, because $k = 1$ satisfies $1 \leq 1 \leq p - 1$ and $\gcd(p - 1, 1) = 1$.
19. So there is an element $g \in G$ of order $p - 1$. The subgroup $\langle g \rangle$ has $p - 1$ [[distinct elements|031M8HX7DA]].
20. Since $\langle g \rangle \subseteq G$ and both sets have $p - 1$ elements, $\langle g \rangle = G$.
21. Hence $G = (\Z/p\Z)^\times$ is [[cyclic|0KVGH0J5B3]] of order $p - 1$.

## Idea

In a field, the equation $x^d = 1$ has at most $d$ solutions. So if one element of order $d$ exists, all elements of order $d$ lie among its powers, and there are exactly $\varphi(d)$ of them. Thus there are at most $\varphi(d)$ elements of order $d$. Since the totients of the divisors of $p - 1$ add up to $p - 1$, no order can be missing, not even $p - 1$.
