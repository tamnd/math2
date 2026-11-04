---
tag: 32JRQJ5MKN
kind: proof
name: Proof of the sum of the totient over the divisors
msc: [11A25]
proves: 09JXE6XMCC
uses: [0VV04M41AN, 096PW7Q014, 02WF878BH1, 0GFKP8F8AG, 0DQVHMYAGA]
methods: [0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Euler%27s_totient_function
    locator: Divisor sum
---

## Proof

We sort the integers $1, \dots, n$ by their greatest common divisor with $n$.

1. Let $n$ be a positive integer. For each positive [[divisor|096PW7Q014]] $d$ of $n$, let $S_d$ be the set of integers $k$ with $1 \le k \le n$ and $\gcd(k, n) = n / d$.
2. Let $1 \le k \le n$. The [[greatest common divisor|02WF878BH1]] $g = \gcd(k, n)$ is a positive divisor of $n$. So $d = n / g$ is a positive divisor of $n$, and $k \in S_d$.
3. The sets $S_d$ are pairwise disjoint, since $n / d$ determines $d$. With step 2, they partition $\{ 1, \dots, n \}$. So $n = \sum_{d \mid n} \abs{S_d}$.
4. Fix a positive divisor $d$ of $n$, and let $e = n / d$, so $n = e d$. We show that $\abs{S_d} = \varphi(d)$, where $\varphi$ is [[Euler's totient function|0VV04M41AN]].
5. If $k \in S_d$, then $e = \gcd(k, n)$ divides $k$. So $k = e j$ for an integer $j$, and $1 \le k \le n$ gives $1 \le j \le d$.
6. So it suffices to show, for $1 \le j \le d$, that $\gcd(e j, e d) = e$ if and only if $\gcd(j, d) = 1$.
7. Assume $\gcd(j, d) = c > 1$. Then $e c$ divides $e j$ and $e d$. So $\gcd(e j, e d) \ge e c > e$.
8. Assume $\gcd(j, d) = 1$. By [[Bézout's identity|0DQVHMYAGA]], $j u + d v = 1$ for some integers $u$ and $v$. Then $(e j) u + (e d) v = e$.
9. So each common divisor of $e j$ and $e d$ divides $e$, and is at most $e$. Since $e$ is itself a common divisor, $\gcd(e j, e d) = e$.
10. By steps 5 to 9, $k \mapsto k / e$ is a bijection from $S_d$ onto the set of $j$ with $1 \le j \le d$ and $j$ [[coprime|0GFKP8F8AG]] to $d$. That set has $\varphi(d)$ elements, so $\abs{S_d} = \varphi(d)$.
11. By steps 3 and 10, $\sum_{d \mid n} \varphi(d) = n$.

## Idea

Group the numbers $1, \dots, n$ by their gcd with $n$. The numbers with gcd $n / d$ are $n / d$ times the numbers up to $d$ that are coprime to $d$, so there are $\varphi(d)$ of them. Adding over all groups counts each of $1, \dots, n$ once.
