---
tag: 497YFJNJCY
kind: proof
name: Proof that exponential growth beats polynomial growth
msc: [26A12, 33B10]
proves: 0CT6CBGTYY
uses: [0RMVS7RXZX, 0PVJRACB9H, 0MX1HZBBXJ]
sources:
  - url: https://proofwiki.org/wiki/Exponential_Dominates_Polynomial
---

## Proof

We bound $e^x$ below by a single term of its series.

1. Let $n$ be a natural number. Here $\lim_{x \to \infty} \frac{e^x}{x^n} = \infty$ means the following. For each real $M$ there is $X$ with $\frac{e^x}{x^n} > M$ for all $x > X$.
2. Let $x > 0$. By the definition of the [[exponential function|0RMVS7RXZX]], $e^x = \sum_{k=0}^{\infty} \frac{x^k}{k!}$. The series converges, since its [[radius of convergence is infinite|0PVJRACB9H]].
3. Every term $\frac{x^k}{k!}$ is nonnegative. By the [[result on series of nonnegative terms|0MX1HZBBXJ]], the sum is the supremum of the partial sums. So $e^x \ge \sum_{k=0}^{n+1} \frac{x^k}{k!}$.
4. The terms with $k \le n$ in this partial sum are nonnegative. So $e^x \ge \frac{x^{n+1}}{(n+1)!}$.
5. Divide by $x^n > 0$. This gives $\frac{e^x}{x^n} \ge \frac{x}{(n+1)!}$ for all $x > 0$.
6. Let $M$ be real, and let $X = \max(0, M \cdot (n+1)!)$. For $x > X$, we have $x > 0$ and $\frac{x}{(n+1)!} > M$.
7. By step 5, $\frac{e^x}{x^n} > M$ for all $x > X$. So $\frac{e^x}{x^n} \to \infty$ as $x \to \infty$.

## Idea

For positive $x$, all terms of the exponential series are positive. Keeping only the term $x^{n+1}/(n+1)!$ already beats $x^n$ by a factor that grows like $x$.
