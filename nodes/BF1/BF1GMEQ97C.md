---
tag: BF1GMEQ97C
kind: proof
name: Proof of the uniqueness of limits
msc: [40A05]
proves: 0ZXJ2455NJ
uses: [09G6KHS6GY, 03HF5PMY5T, 0J0XBKG64S]
sources:
  - url: https://www.jirka.org/ra/html/sec_seqsandlims.html
    locator: Proposition 2.1.6
---

## Proof

We argue [[by contradiction|0J0XBKG64S]].

1. Assume that $(a_n)$ converges to $L$ and to $L'$, and that $L \ne L'$.
2. Let $\varepsilon = |L - L'|/2$. Then $\varepsilon > 0$.
3. By the [[epsilon-N definition|09G6KHS6GY]], there is $N_1$ with $|a_n - L| < \varepsilon$ for all $n \ge N_1$.
4. In the same way, there is $N_2$ with $|a_n - L'| < \varepsilon$ for all $n \ge N_2$.
5. Let $n = \max(N_1, N_2)$. By the [[triangle inequality|03HF5PMY5T]], $|L - L'| \le |L - a_n| + |a_n - L'|$.
6. By steps 3 and 4, the right side is less than $2 \varepsilon = |L - L'|$.
7. So $|L - L'| < |L - L'|$, which is impossible.
8. Hence $L = L'$.

## Idea

Two different numbers have a gap between them. Take windows of half the gap around each number. These windows do not meet, so the terms cannot eventually lie in both of them.
