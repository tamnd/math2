---
tag: 849ASYBYJ6
kind: definition
name: Multivariate analysis of variance
msc: [62H15, 62J10]
defines: 8J3B7N8CAT
uses: [M9AQ5HKGP4, 0XN3K7RSZY, 087P03NEND, 00KDZRW4C0, 0XC1RDBY7A, 0EB9N0S33C]
sources:
  - url: https://en.wikipedia.org/wiki/Multivariate_analysis_of_variance
---

## Definition

Let $g \ge 2$ and $p \ge 1$ be integers.
For $i = 1, \ldots, g$ and $j = 1, \ldots, n_i$, let $X_{ij}$ be independent random vectors in $\R^p$ with $X_{ij} \sim N_p(\mu_i, \Sigma)$, a [[multivariate normal distribution|0XN3K7RSZY]] with unknown $\mu_i$ and unknown common $\Sigma$.
Let $N = n_1 + \cdots + n_g$, let $\bar X_i$ be the mean of group $i$ and $\bar X$ the mean of all $N$ observations.
The between-group and within-group matrices are
$$B = \sum_{i=1}^g n_i (\bar X_i - \bar X)(\bar X_i - \bar X)^T, \qquad W = \sum_{i=1}^g \sum_{j=1}^{n_i} (X_{ij} - \bar X_i)(X_{ij} - \bar X_i)^T.$$
*One-way multivariate analysis of variance* is the [[test|087P03NEND]] of $H_0 \colon \mu_1 = \cdots = \mu_g$ by a statistic that depends on the eigenvalues of $W^{-1} B$.
The standard statistics are:

1. Wilks' lambda $\Lambda = \det W / \det(W + B)$, which rejects for small values.
2. Pillai's trace $\tr(B (B + W)^{-1})$.
3. The Hotelling–Lawley trace $\tr(W^{-1} B)$.
4. Roy's largest root, the largest eigenvalue of $W^{-1} B$.

## Remarks

The matrix $W$ is [[invertible|0EB9N0S33C]] with probability $1$ when $N - g \ge p$ and $\Sigma$ is positive definite.
Example: for $p = 1$, $B$ and $W$ are the between and within sums of squares of the one-way [[analysis of variance|M9AQ5HKGP4]].
Then $\Lambda = W/(W + B)$, a decreasing function of the usual $F$ statistic, so MANOVA reduces to ANOVA.
Non-example: with $p = 5$ responses and $g = 3$ groups of $2$ observations each, $N - g = 3 < p$, so $W$ has rank at most $3$, is not invertible, and $\Lambda = 0$ whatever the data.
For $g = 2$ the four statistics are equivalent to Hotelling's $T^2$ statistic.
