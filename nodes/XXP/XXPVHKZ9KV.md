---
tag: XXPVHKZ9KV
kind: proof
name: Proof of the Riemann rearrangement theorem by a greedy construction
msc: [40A05]
proves: 0E7VBYGFF7
uses: [02YRQXZDCS, 0HRJ2Y74T3, 0VVY4H92G2, 0MX1HZBBXJ, 0RAM4E07NR, 0734RSVF2V, 0XKWSSY8P2, 09AZCV6GMC, 0W3K3QPEWT]
sources:
  - url: https://en.wikipedia.org/wiki/Riemann_series_theorem
    locator: Proof
---

## Proof

Let $s_N = \sum_{n=0}^{N} a_n$. Let $p_n = \max(a_n, 0)$ and $q_n = \max(-a_n, 0)$, with partial sums $P_N$ and $Q_N$. Then $a_n = p_n - q_n$ and $\abs{a_n} = p_n + q_n$.

*The positive and negative parts.*

1. The series converges, so $a_n \to 0$ by the [[term test|0VVY4H92G2]].
2. Suppose $P_N \to P$ for a real $P$. Then $Q_N = P_N + (-1) s_N$ converges, by the limits of [[sums|0RAM4E07NR]] and [[products|0734RSVF2V]]. So $\sum \abs{a_n}$ has partial sums $P_N + Q_N$, which converge.
3. Step 2 contradicts the definition of [[conditional convergence|02YRQXZDCS]]: $\sum \abs{a_n}$ diverges. So $\sum p_n$ diverges. In the same way, using $P_N = s_N + Q_N$, the series $\sum q_n$ diverges.
4. By the [[criterion for nonnegative series|0MX1HZBBXJ]], $(P_N)$ and $(Q_N)$ are not bounded above. Both are increasing, so both tend to $+\infty$.
5. Let $U = \set{n : a_n \ge 0}$ and $V = \set{n : a_n < 0}$. They are disjoint, and their union is $\N$. Both are infinite: otherwise $(Q_N)$ or $(P_N)$ would be constant from some index on, contradicting step 4.
6. List them in increasing order: $U = \set{u_1 < u_2 < \cdots}$ and $V = \set{v_1 < v_2 < \cdots}$. Then $\sum_{i=1}^{K} a_{u_i} = P_{u_K}$ and $\sum_{j=1}^{K} \abs{a_{v_j}} = Q_{v_K}$.
7. Since $u_K, v_K \ge K - 1$, step 4 shows that both sums in step 6 tend to $+\infty$ as $K \to \infty$. The same holds for these sums started at any fixed index.

*The construction.*

8. Each rearrangement below is built step by step. At step $n = 0, 1, 2, \dots$ a rule chooses a "$U$-step" or a "$V$-step". A $U$-step sets $\sigma(n)$ to the first $u_i$ not yet used; a $V$-step sets $\sigma(n)$ to the first $v_j$ not yet used.
9. Every $u_i$ and $v_j$ is used at most once, so $\sigma \colon \N \to \N$ is injective. If both kinds of step occur infinitely often, then the $i$-th $U$-step uses $u_i$ and the $j$-th $V$-step uses $v_j$. Then $\sigma$ is also surjective, by step 5.
10. Let $S_n = \sum_{m=0}^{n} a_{\sigma(m)}$ and $S_{-1} = 0$. A $U$-step gives $S_n \ge S_{n-1}$ and a $V$-step gives $S_n < S_{n-1}$.

*A rearrangement with sum $M$.*

11. Rule: step $n$ is a $U$-step if $S_{n-1} \le M$, and a $V$-step if $S_{n-1} > M$.
12. Suppose all steps from $n_0$ on are $V$-steps. By step 7, $S_n \to -\infty$, so some $n \ge n_0$ has $S_n \le M$. Then step $n + 1$ is a $U$-step, a contradiction. So there are infinitely many $U$-steps.
13. In the same way, if all steps from $n_0$ on were $U$-steps, then $S_n \to +\infty$ by step 7, which forces a $V$-step. So there are infinitely many $V$-steps, and $\sigma$ is a bijection by step 9.
14. Let $\varepsilon > 0$. By step 1, there is $k_0$ with $\abs{a_k} < \varepsilon$ for $k \ge k_0$. Only finitely many $n$ have $\sigma(n) < k_0$. So there is $n_1$ with $\abs{a_{\sigma(n)}} < \varepsilon$ for all $n \ge n_1$.
15. Let $I = (M - \varepsilon, M + \varepsilon)$, and let $n \ge n_1$ with $S_{n-1} \in I$. If $S_{n-1} \le M$, then $S_{n-1} \le S_n < M + \varepsilon$. If $S_{n-1} > M$, then $M - \varepsilon < S_n < S_{n-1}$. In both cases $S_n \in I$.
16. By steps 12 and 13, there is a $U$-step $n \ge n_1$ such that step $n + 1$ is a $V$-step. Then $S_{n-1} \le M < S_n$, and $S_n = S_{n-1} + a_{\sigma(n)} < M + \varepsilon$. So $S_n \in I$.
17. By steps 15 and 16 and induction, $S_m \in I$ for every $m \ge n$. Since $\varepsilon > 0$ was arbitrary, $S_m \to M$ by the definition of the [[limit|0XKWSSY8P2]].
18. So the [[rearrangement|0HRJ2Y74T3]] $\sum a_{\sigma(n)}$ converges to $M$.

*A rearrangement that diverges to $+\infty$.*

19. Let $J(n)$ be the number of $V$-steps among steps $0, \dots, n$, with $J(-1) = 0$. Rule: step $n$ is a $U$-step if $S_{n-1} \le J(n-1) + 1$, and a $V$-step otherwise.
20. Suppose all steps from $n_0$ on are $U$-steps. Then $J(n) = J(n_0 - 1)$ for $n \ge n_0$, while $S_n \to +\infty$ by step 7. So some $S_n$ exceeds $J(n) + 1$, which forces a $V$-step. This is a contradiction.
21. Suppose all steps from $n_0$ on are $V$-steps. Then $S_n \to -\infty$ by step 7, while $J(n) + 1 \ge 1$. So some $S_n \le J(n) + 1$, which forces a $U$-step. This is a contradiction.
22. So both kinds of step occur infinitely often, $\sigma$ is a bijection by step 9, and $J(n) \to +\infty$.
23. As in step 14, there is $n_1$ with $\abs{a_{\sigma(n)}} < 1$ for all $n \ge n_1$.
24. Let $n \ge n_1$ be a $V$-step. Then $S_{n-1} > J(n-1) + 1$, so $S_n > S_{n-1} - 1 > J(n-1) = J(n) - 1$.
25. Let $n \ge n_1$ be a $U$-step with $S_{n-1} > J(n-1) - 1$. Then $S_n \ge S_{n-1} > J(n-1) - 1 = J(n) - 1$.
26. Let $n_2$ be the first $V$-step with $n_2 \ge n_1$. By steps 24 and 25 and induction, $S_n > J(n) - 1$ for all $n \ge n_2$.
27. Since $J(n)$ is increasing and tends to $+\infty$, step 26 shows that $S_n \to +\infty$, as a [[sequence tending to infinity|09AZCV6GMC]].

*A rearrangement that diverges to $-\infty$.*

28. The series $\sum (-a_n)$ has partial sums $(-1) s_N$, which converge by the limit of products. Since $\abs{-a_n} = \abs{a_n}$, it does not converge [[absolutely|0W3K3QPEWT]]. So it converges conditionally.
29. Steps 19 to 27 give a bijection $\sigma$ with $\sum_{m=0}^{n} (-a_{\sigma(m)}) \to +\infty$. So the partial sums of $\sum a_{\sigma(n)}$ tend to $-\infty$.

## Idea

In a conditionally convergent series, the positive terms alone and the negative terms alone both sum to infinity, while the terms tend to $0$. So we can add positive terms until the running sum passes a target, then negative terms until it falls back, forever. The overshoots shrink because the terms shrink, so the sums settle at the target. Raising the target step by step instead gives divergence to infinity.
