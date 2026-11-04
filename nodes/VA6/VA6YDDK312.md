---
tag: VA6YDDK312
kind: proof
name: Proof that absolutely convergent series in a Banach space converge
msc: [40A05]
proves: 082MGNWNA8
uses: [0BDTTM24DP, 08EWT7J0SC, 0MCK8K2D7Z, 0QY87R9CY3, 0FJZMBX0ZZ, 06JYPJ4WHH]
sources:
  - url: https://en.wikipedia.org/wiki/Absolute_convergence
    locator: Proof that any absolutely convergent series in a Banach space is convergent
---

## Proof

We show that the partial sums form a Cauchy sequence, and then bound the norm of the limit.

1. Let $t_N = \sum_{n=1}^{N} \|x_n\|$ and $L = \sum_{n \ge 1} \|x_n\| = \lim_N t_N$. The terms are nonnegative, so $t_N$ increases and $t_N \le L$.
2. For $M > N$, $s_M - s_N = \sum_{n=N+1}^{M} x_n$. By the [[triangle inequality|0FJZMBX0ZZ]] and induction on the number of terms, $\|s_M - s_N\| \le \sum_{n=N+1}^{M} \|x_n\| = t_M - t_N$.
3. The real sequence $(t_N)$ converges, so it is a Cauchy sequence by [[this result|0QY87R9CY3]]. Given $\varepsilon > 0$, there is $N_0$ with $|t_M - t_N| < \varepsilon$ for $M, N \ge N_0$.
4. By step 2, $\|s_M - s_N\| < \varepsilon$ for $M, N \ge N_0$. So $(s_N)$ is a [[Cauchy sequence|0MCK8K2D7Z]] in $V$.
5. $V$ is a [[Banach space|0BDTTM24DP]], so it is [[complete|08EWT7J0SC]]. Hence $(s_N)$ [[converges|06JYPJ4WHH]] to some $s \in V$.
6. For each $N$, the triangle inequality gives $\|s_N\| \le t_N \le L$.
7. Then $\|s\| \le \|s - s_N\| + \|s_N\| \le \|s - s_N\| + L$ for each $N$.
8. Suppose $\|s\| > L$. Let $\varepsilon = \|s\| - L$. For large $N$, $\|s - s_N\| < \varepsilon$, and step 7 gives $\|s\| < \|s\|$, a contradiction.
9. Thus $\|s\| \le \sum_{n \ge 1} \|x_n\|$.

## Idea

The triangle inequality bounds the size of a block of terms of the series by the corresponding block of the convergent real series of norms. So the partial sums are Cauchy, and completeness gives a limit. The same inequality, passed to the limit, bounds the norm of the sum.
