---
tag: EZF8KV8YM6
kind: proof
name: Proof of Euler's partition theorem by Glaisher's bijection
msc: [05A17]
proves: 0XFZ1BMF5Q
uses: [0404R9P9J3, 0KMVFSHFGZ, 01VG2A0BHW, 0GV2573FP4]
sources:
  - url: https://yufeizhao.com/olympiad/bijections.pdf
    locator: Problem 3
---

## Proof

We build a bijection, due to Glaisher, between the two sets of [[partitions|0404R9P9J3]].

1. A partition of $n$ is determined by its multiplicity function $\mu : \Z_{>0} \to \N$. Here $\mu(k)$ is the number of parts equal to $k$. It has finite support and $\sum_k k\, \mu(k) = n$.
2. Conversely, each such function with finite support and $\sum_k k\, \mu(k) = n$ is the multiplicity function of exactly one partition of $n$.
3. Let $\mathcal{O}$ be the set of these $\mu$ with $\mu(k) = 0$ for every even $k$. These are the partitions of $n$ into odd parts.
4. Let $\mathcal{D}$ be the set of these $\mu$ with $\mu(k) \le 1$ for every $k$. These are the partitions of $n$ into distinct parts.
5. Fact A: each positive integer $d$ is $2^a m$ for exactly one pair $(a, m)$ with $a \in \N$ and $m$ odd.
6. Proof of Fact A. Let $a$ be the largest natural number with $2^a \mid d$; it exists because $2^a \le d$. Then $m = d / 2^a$ is odd, otherwise $2^{a+1} \mid d$.
7. If $2^a m = 2^b m'$ with $m, m'$ odd and $a < b$, then $m = 2^{b-a} m'$ is even, a contradiction. So $a = b$, and then $m = m'$.
8. Fact B: each $k \in \N$ is $\sum_{a \in B} 2^a$ for exactly one finite set $B \subseteq \N$. We call $B$ the binary set of $k$. We use [[strong induction|0KMVFSHFGZ]] on $k$.
9. For $k = 0$ the only such set is $B = \varnothing$, because a nonempty $B$ gives a positive sum.
10. Let $k \ge 1$. In $\sum_{a \in B} 2^a$ all terms with $a \ge 1$ are even. So $0 \in B$ exactly when $k$ is odd.
11. Let $\varepsilon = 1$ if $k$ is odd and $\varepsilon = 0$ otherwise, and let $k' = (k - \varepsilon)/2 < k$.
12. Then $k = \sum_{a \in B} 2^a$ holds if and only if $0 \in B \Leftrightarrow \varepsilon = 1$ and $k' = \sum_{a \in B, a \ge 1} 2^{a-1}$.
13. By the induction hypothesis, $k'$ has exactly one binary set $B'$. So $B = \{a + 1 : a \in B'\}$, together with $0$ when $\varepsilon = 1$, is the only binary set of $k$.
14. Define $\Phi : \mathcal{O} \to \mathcal{D}$. For $\mu \in \mathcal{O}$ and odd $m$, let $B_m$ be the binary set of $\mu(m)$.
15. For $d = 2^a m$ as in Fact A, put $\nu(d) = 1$ if $a \in B_m$, and $\nu(d) = 0$ otherwise. Let $\Phi(\mu) = \nu$.
16. The support of $\nu$ is finite, because only finitely many $m$ have $\mu(m) > 0$ and each $B_m$ is finite.
17. We have $\sum_d d\, \nu(d) = \sum_{m \text{ odd}} m \sum_{a \in B_m} 2^a = \sum_{m \text{ odd}} m\, \mu(m) = n$, by Fact A. So $\nu \in \mathcal{D}$.
18. Define $\Psi : \mathcal{D} \to \mathcal{O}$. For $\nu \in \mathcal{D}$ and odd $m$, let $\mu(m) = \sum_{a \in A_m} 2^a$, where $A_m = \{a \in \N : \nu(2^a m) = 1\}$. Let $\mu(k) = 0$ for even $k$.
19. Each $A_m$ is finite, and only finitely many $A_m$ are nonempty, because $\nu$ has finite support. So $\mu$ has finite support.
20. By Fact A, $\sum_k k\, \mu(k) = \sum_{m \text{ odd}} \sum_{a \in A_m} 2^a m = \sum_d d\, \nu(d) = n$. So $\Psi(\nu) = \mu \in \mathcal{O}$.
21. Let $\mu \in \mathcal{O}$ and $\nu = \Phi(\mu)$. Then $A_m = B_m$ for each odd $m$, so $\Psi(\nu)(m) = \sum_{a \in B_m} 2^a = \mu(m)$. Thus $\Psi \circ \Phi$ is the identity.
22. Let $\nu \in \mathcal{D}$ and $\mu = \Psi(\nu)$. By Fact B, the binary set of $\mu(m)$ is $A_m$. So $\Phi(\mu)(2^a m) = 1$ exactly when $a \in A_m$, that is, when $\nu(2^a m) = 1$.
23. By Fact A every $d \ge 1$ has the form $2^a m$, so $\Phi(\mu) = \nu$. Thus $\Phi \circ \Psi$ is the identity.
24. A map with a two-sided inverse is a [[bijection|01VG2A0BHW]]. So $\Phi$ is a bijection from $\mathcal{O}$ to $\mathcal{D}$.
25. Both sets are finite, since there are finitely many partitions of $n$. By the [[bijection principle|0GV2573FP4]], $\abs{\mathcal{O}} = \abs{\mathcal{D}}$.

## Idea

Group equal odd parts: $m$ appears $\mu(m)$ times. Write $\mu(m)$ in binary and merge the copies of $m$ into parts $2^a m$, one for each binary digit $1$.
The new parts are distinct, because each integer is a power of two times an odd number in only one way. Splitting each part $2^a m$ back into $2^a$ copies of $m$ undoes the map.
