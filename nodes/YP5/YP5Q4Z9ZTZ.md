---
tag: YP5Q4Z9ZTZ
kind: proof
name: Proof that the Cauchy product of absolutely convergent series converges absolutely to the product
msc: [40A05]
proves: 0AN28XQ45Z
uses: [0W3K3QPEWT, 0B1K9PVWE9, 0NB643K60Q, 0MX1HZBBXJ, 0734RSVF2V, 0RAM4E07NR, 0XMF00T4XQ, 09G6KHS6GY, 03HF5PMY5T]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy_product
    locator: Convergence and Mertens' theorem
---

## Proof

We compare the partial sums of the Cauchy product with products of partial sums.

1. Let $\sum a_n$ and $\sum b_n$ [[converge absolutely|0W3K3QPEWT]], with sums $A$ and $B$. Let $c_n = \sum_{k=0}^{n} a_k b_{n-k}$ define the [[Cauchy product|0B1K9PVWE9]].
2. Let $A_N$, $B_N$, $C_N$ be the [[partial sums|0NB643K60Q]] of $\sum a_n$, $\sum b_n$, $\sum c_n$. Let $P_N = \sum_{n \le N} \abs{a_n}$ and $Q_N = \sum_{n \le N} \abs{b_n}$.
3. Let $P = \sum \abs{a_n}$ and $Q = \sum \abs{b_n}$. The terms are nonnegative, so $P_N \le P$ and $Q_N \le Q$ by the [[criterion for nonnegative series|0MX1HZBBXJ]].
4. The term $c_n$ is the sum of $a_i b_j$ over the pairs $(i, j)$ of natural numbers with $i + j = n$. So $C_N$ is the sum of $a_i b_j$ over the set $T_N$ of pairs with $i + j \le N$.
5. Each pair in $T_N$ has $i \le N$ and $j \le N$. By the [[triangle inequality|03HF5PMY5T]],
$$\sum_{n=0}^{N} \abs{c_n} \le \sum_{(i,j) \in T_N} \abs{a_i} \abs{b_j} \le \sum_{i=0}^{N} \sum_{j=0}^{N} \abs{a_i} \abs{b_j} = P_N Q_N \le P Q.$$
6. So the partial sums of $\sum \abs{c_n}$ are bounded above by $PQ$. By the criterion for nonnegative series, $\sum \abs{c_n}$ converges. Hence $\sum c_n$ converges absolutely.
7. Let $U_N$ be the set of pairs $(i, j)$ with $i \le N$, $j \le N$ and $i + j > N$. Then $A_N B_N = \sum_{i, j \le N} a_i b_j = C_N + \sum_{(i,j) \in U_N} a_i b_j$.
8. Let $E_N = \sum_{(i,j) \in U_N} \abs{a_i} \abs{b_j}$. By step 7 and the triangle inequality, $\abs{A_N B_N - C_N} \le E_N$.
9. In the same way as step 7, $P_N Q_N = \sum_{(i,j) \in T_N} \abs{a_i} \abs{b_j} + E_N$.
10. Let $h = \floor{N/2}$. If $i \le h$ and $j \le h$, then $i + j \le N$. So $\sum_{(i,j) \in T_N} \abs{a_i} \abs{b_j} \ge P_h Q_h$.
11. By steps 9 and 10, $0 \le E_N \le P_N Q_N - P_{\floor{N/2}} Q_{\floor{N/2}}$.
12. By the [[product rule for limits|0734RSVF2V]], $P_N Q_N \to PQ$. Let $\varepsilon > 0$, and take $K$ with $\abs{P_k Q_k - PQ} < \varepsilon$ for $k \ge K$, by the [[epsilon-N form|09G6KHS6GY]].
13. For $N \ge 2K$ we have $\floor{N/2} \ge K$. So $P_{\floor{N/2}} Q_{\floor{N/2}} \to PQ$ as $N \to \infty$.
14. By the [[sum rule for limits|0RAM4E07NR]], the right side of step 11 tends to $0$. By the [[squeeze theorem|0XMF00T4XQ]], $E_N \to 0$.
15. By step 8, $-E_N \le A_N B_N - C_N \le E_N$. The squeeze theorem gives $A_N B_N - C_N \to 0$.
16. By the product rule, $A_N B_N \to AB$. So $C_N = A_N B_N - (A_N B_N - C_N) \to AB - 0 = AB$ by the sum rule.
17. Hence $\sum c_n$ converges absolutely, and its sum is $AB$.

## Idea

The product $A_N B_N$ sums $a_i b_j$ over a square of indices, while $C_N$ sums over the triangle $i + j \le N$ inside it. The missing corner is controlled by the same corner for the absolute values. That corner lies between the squares of sides $N/2$ and $N$, so it tends to $0$.
