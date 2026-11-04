---
tag: WFYM20H4MK
kind: proof
name: Proof of Legendre's formula by counting multiples of prime powers
msc: [11A51]
proves: 01WPV9PHN7
uses: [04VCPS30ZE, 0850JJMJYZ, 0WFCGVMRRC, 0YVRNEDSVG, 0SN0MAEKYX]
sources:
  - url: https://en.wikipedia.org/wiki/Legendre%27s_formula
    locator: Proof
---

## Proof

1. Let $p$ be a [[prime number|0SN0MAEKYX]] and $n$ a natural number. If $n = 0$, then $0! = 1$ by the definition of the [[factorial|0WFCGVMRRC]]. So $\nu_p(0!) = 0$, and every term $\lfloor 0 / p^i \rfloor$ is $0$. Assume now $n \ge 1$.
2. We have $n! = 1 \cdot 2 \cdots n$. Applying the [[valuation of a product|0850JJMJYZ]] $n - 1$ times gives $\nu_p(n!) = \sum_{k=1}^{n} \nu_p(k)$.
3. Let $1 \le k \le n$ and $i \ge 1$. By the definition of the [[p-adic valuation|04VCPS30ZE]], $p^i \mid k$ holds if and only if $i \le \nu_p(k)$. Indeed, if $i \le \nu_p(k)$ then $p^i \mid p^{\nu_p(k)} \mid k$, and if $i > \nu_p(k)$ then $p^i \nmid k$ by maximality.
4. So $\nu_p(k)$ is the number of integers $i \ge 1$ with $p^i \mid k$.
5. Substituting step 4 into step 2 and counting the pairs $(k, i)$ the other way gives $\nu_p(n!) = \sum_{i \ge 1} N_i$. Here $N_i$ is the number of $k$ with $1 \le k \le n$ and $p^i \mid k$.
6. Only finitely many $N_i$ are nonzero, because $p^i > n$ implies $N_i = 0$.
7. Fix $i \ge 1$ and let $d = p^i$. The multiples of $d$ in $\set{1, \dots, n}$ are the numbers $jd$ with $j$ an integer and $1 \le j \le n/d$.
8. An integer $j$ satisfies $j \le n/d$ if and only if $j \le \lfloor n/d \rfloor$, by the definition of the [[floor function|0YVRNEDSVG]]. So $N_i = \lfloor n / p^i \rfloor$.
9. Hence $\nu_p(n!) = \sum_{i=1}^{\infty} \lfloor n / p^i \rfloor$, where only finitely many terms are nonzero.

## Idea

Each $k \le n$ contributes $\nu_p(k)$ factors of $p$ to $n!$. Count these factors by layers: every multiple of $p$ gives one, every multiple of $p^2$ gives one more, and so on. The number of multiples of $p^i$ up to $n$ is $\lfloor n/p^i \rfloor$.
