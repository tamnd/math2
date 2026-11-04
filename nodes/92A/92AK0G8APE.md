---
tag: 92AK0G8APE
kind: proof
name: Proof that the trace is the sum of the eigenvalues by comparing coefficients
msc: [15A15, 15A18]
proves: 0NMXDCNNKR
uses: [0FRYPZ6D0X, 039HF58KQ5, 0DPF6WRZW6]
sources:
  - url: https://en.wikipedia.org/wiki/Trace_(linear_algebra)
    locator: Trace as the sum of eigenvalues
---

## Proof

We compute the coefficient of $t^{n-1}$ of $p_A$ in two ways.

1. Let $A$ be an $n \times n$ matrix over $F$. The [[characteristic polynomial|039HF58KQ5]] is defined for $n \ge 1$, so $n \ge 1$. Assume that its characteristic polynomial is $p_A(t) = (t - \lambda_1) \cdots (t - \lambda_n)$ with $\lambda_i \in F$.
2. Claim: for $k \ge 1$, $\prod_{i=1}^{k} (t - \lambda_i) = t^k - (\lambda_1 + \cdots + \lambda_k) t^{k-1} + r_k$, where $r_k$ is $0$ or has [[degree|0DPF6WRZW6]] at most $k - 2$.
3. For $k = 1$, the claim holds with $r_1 = 0$.
4. Suppose the claim holds for $k$, and let $s = \lambda_1 + \cdots + \lambda_k$ and $c = \lambda_{k+1}$. Multiply both sides by $t - c$.
5. This gives $t^{k+1} - (s + c) t^k + r_{k+1}$, with $r_{k+1} = c s\, t^{k-1} + t\, r_k - c\, r_k$.
6. Each of the three terms of $r_{k+1}$ is $0$ or has degree at most $k - 1$. So the claim holds for $k + 1$, and by induction for all $k$.
7. By step 2 with $k = n$, the coefficient of $t^{n-1}$ in $p_A$ is $-(\lambda_1 + \cdots + \lambda_n)$.
8. By the rule for the [[trace as a coefficient|0FRYPZ6D0X]], the same coefficient is $-\tr A$.
9. By steps 7 and 8, $\tr A = \lambda_1 + \lambda_2 + \cdots + \lambda_n$.

## Idea

Multiplying out $(t - \lambda_1) \cdots (t - \lambda_n)$ gives $t^n - (\lambda_1 + \cdots + \lambda_n) t^{n-1} + \cdots$. The same coefficient of $t^{n-1}$ is $-\tr A$ when $\det(t I - A)$ is expanded. Comparing the two gives the result.
