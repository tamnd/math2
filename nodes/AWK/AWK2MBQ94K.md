---
tag: AWK2MBQ94K
kind: definition
name: Canonical correlation
msc: [62H20]
defines: E0WKQ3XBAC
uses: [0DNN9B6Q2F, 0V7G6WMFK0, 0KX66CZMBB, 0BQAA2BK3Q]
sources:
  - url: https://en.wikipedia.org/wiki/Canonical_correlation
---

## Definition

Let $X$ be a random vector in $\R^p$ and $Y$ a random vector in $\R^q$, with finite second moments.
Assume that the [[covariance matrices|0V7G6WMFK0]] $\Sigma_{XX}$ and $\Sigma_{YY}$ are [[positive definite|0KX66CZMBB]], and let $\Sigma_{XY} = \operatorname{Cov}(X, Y)$.
Let $m = \min(p, q)$.
For $i = 1, \ldots, m$, the $i$-th pair of *canonical variates* $(a_i^T X, b_i^T Y)$ is defined inductively:
$a_i \in \R^p$ and $b_i \in \R^q$ maximise the [[correlation|0DNN9B6Q2F]] $\operatorname{Corr}(a^T X, b^T Y)$ under these constraints:

1. $\operatorname{Var}(a^T X) = \operatorname{Var}(b^T Y) = 1$;
2. $\operatorname{Cov}(a^T X, a_j^T X) = 0$ for all $j < i$;
3. $\operatorname{Cov}(b^T Y, b_j^T Y) = 0$ for all $j < i$.

The maximal value $\rho_i = \operatorname{Corr}(a_i^T X, b_i^T Y)$ is the $i$-th *canonical correlation*.

## Remarks

One has $1 \ge \rho_1 \ge \rho_2 \ge \cdots \ge \rho_m \ge 0$.
The numbers $\rho_1^2, \ldots, \rho_m^2$ are the $m$ largest [[eigenvalues|0BQAA2BK3Q]] of $\Sigma_{XX}^{-1} \Sigma_{XY} \Sigma_{YY}^{-1} \Sigma_{YX}$.
Example: for $p = q = 1$, the only canonical correlation is $\rho_1 = \abs{\operatorname{Corr}(X, Y)}$, attained with $b_1 = \pm 1/\sqrt{\operatorname{Var}(Y)}$ chosen with the sign of the covariance.
Non-example: for $X = (X_1, X_2)$ with $X_1 = Y$ and $X_2$ independent of $Y$, the pair $a = (0, 1)/\sqrt{\operatorname{Var}(X_2)}$ gives correlation $0$, which is not maximal, since $a = (1, 0)/\sqrt{\operatorname{Var}(Y)}$ gives correlation $1$.
The sample version replaces the covariance matrices by sample covariance matrices.
