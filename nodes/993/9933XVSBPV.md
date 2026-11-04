---
tag: 9933XVSBPV
kind: proof
name: Proof of Kummer's theorem from Legendre's formula
msc: [11B65]
proves: 0VBWK9XYDG
uses: [04VCPS30ZE, 01WPV9PHN7, 033KTKKRV6, 0850JJMJYZ, 0CHQKZFK5S, 0YVRNEDSVG, 092GEF38YD]
sources:
  - url: https://en.wikipedia.org/wiki/Kummer%27s_theorem
    locator: Statement
  - url: https://en.wikipedia.org/wiki/Legendre%27s_formula
    locator: Alternate form
---

## Proof

1. Let $p$ be a prime and let $m, n$ be natural numbers. For a natural number $x$ with base-$p$ digits $x = \sum_{j \ge 0} x_j p^j$, $0 \le x_j < p$, let $s(x) = \sum_j x_j$ be its digit sum.
2. Base-$p$ digits are unique. If $\sum_j a_j p^j = \sum_j b_j p^j$ with all digits in $\set{0, \dots, p-1}$, the [[division algorithm|0CHQKZFK5S]] by $p$ gives $a_0 = b_0$. Subtracting, dividing by $p$ and repeating gives $a_j = b_j$ for all $j$.
3. Fix $x$ as in step 1 and $i \ge 1$. Write $x = p^i A + B$ with $A = \sum_{j \ge i} x_j p^{j-i}$ and $B = \sum_{j < i} x_j p^j$.
4. Then $0 \le B \le \sum_{j<i} (p-1) p^j = p^i - 1$. So $A \le x / p^i < A + 1$, and $A = \lfloor x/p^i \rfloor$ by the definition of the [[floor function|0YVRNEDSVG]].
5. By [[Legendre's formula|01WPV9PHN7]] and step 4, $\nu_p(x!) = \sum_{i \ge 1} \sum_{j \ge i} x_j p^{j-i} = \sum_{j \ge 1} x_j (p^{j-1} + \dots + p + 1)$.
6. Since $p^{j-1} + \dots + 1 = (p^j - 1)/(p - 1)$, this gives $\nu_p(x!) = \sum_j x_j (p^j - 1)/(p-1) = (x - s(x))/(p - 1)$.
7. By the [[factorial formula|033KTKKRV6]], $\binom{m+n}{m} \, m! \, n! = (m+n)!$. By the [[valuation of a product|0850JJMJYZ]] and step 6, $\nu_p \binom{m+n}{m} = \dfrac{s(m) + s(n) - s(m+n)}{p - 1}$.
8. Now we describe addition in base $p$. Choose $K$ with $m + n < p^K$, and write $m = \sum_{j=0}^{K} m_j p^j$ and $n = \sum_{j=0}^{K} n_j p^j$ with digits in $\set{0, \dots, p-1}$.
9. Set $c_{-1} = 0$. For $j = 0, 1, \dots, K$ in turn, let $c_j = 1$ if $m_j + n_j + c_{j-1} \ge p$ and $c_j = 0$ otherwise. Put $r_j = m_j + n_j + c_{j-1} - p c_j$.
10. By induction on $j$, $c_j \in \set{0, 1}$ and $0 \le r_j \le p - 1$. Indeed $0 \le m_j + n_j + c_{j-1} \le 2p - 1$. The carry $c_j = 1$ is exactly a carry at place $j$, so the number of carries is $C = \sum_{j=0}^{K} c_j$.
11. Summing $r_j p^j$ over $j$, the carry terms telescope: $\sum_{j=0}^{K} r_j p^j = m + n + c_{-1} - c_K p^{K+1} = m + n - c_K p^{K+1}$.
12. The left side is at least $0$. If $c_K = 1$, this gives $m + n \ge p^{K+1}$, against $m + n < p^K$. So $c_K = 0$, and $\sum_{j=0}^{K} r_j p^j = m + n$.
13. By step 2, the $r_j$ are the base-$p$ digits of $m + n$. So $s(m+n) = \sum_j r_j$.
14. Summing the definition of $r_j$ over $j$ gives $s(m+n) = s(m) + s(n) + \sum_{j=0}^{K} c_{j-1} - p \sum_{j=0}^{K} c_j$.
15. Since $c_{-1} = 0$ and $c_K = 0$, we have $\sum_{j=0}^{K} c_{j-1} = C$. So $s(m) + s(n) - s(m+n) = pC - C = (p - 1) C$.
16. With step 7, $\nu_p \binom{m+n}{m} = C$, the number of carries when one adds $m$ and $n$ in base $p$.

## Idea

Legendre's formula can be rewritten as $\nu_p(x!) = (x - s(x))/(p - 1)$, with $s(x)$ the base-$p$ digit sum. So the valuation of $\binom{m+n}{m}$ measures how much the digit sum drops when one adds $m$ and $n$. Each carry replaces $p$ in one place by $1$ in the next place, so it lowers the digit sum by exactly $p - 1$.
