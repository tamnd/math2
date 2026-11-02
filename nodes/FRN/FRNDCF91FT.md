---
tag: FRNDCF91FT
kind: definition
name: Wishart distribution
msc: [62H10, "60E05"]
defines: 8BEMNJW0B9
uses: [0G558GJQMW, 0AJN7WHBJZ, 0QQCG3JWJ4, 0RFMMBHFTV, 0C3CFHDN6R, 07PTPSZPME]
sources:
  - url: https://en.wikipedia.org/wiki/Wishart_distribution
---

## Definition

Let $p$ and $n$ be positive integers and let $\Sigma$ be a $p \times p$ [[positive definite matrix|0QQCG3JWJ4]].
Let $X_1, \dots, X_n$ be [[independent and identically distributed|0AJN7WHBJZ]] random column vectors in $\R^p$ with the [[multivariate normal distribution|0G558GJQMW]] $\mathcal{N}_p(0, \Sigma)$.
The distribution of the random $p \times p$ matrix
$$S = \sum_{i=1}^n X_i X_i^T$$
is the *Wishart distribution* with scale matrix $\Sigma$ and $n$ degrees of freedom, written $W_p(\Sigma, n)$.

## Remarks

The mean is $E(S) = n \Sigma$.
If $n \ge p$, then $S$ is positive definite with probability $1$.
Its density on positive definite matrices is then
$$f(S) = \frac{\det(S)^{(n - p - 1)/2} \exp\left(-\tfrac{1}{2} \tr(\Sigma^{-1} S)\right)}{2^{np/2} \det(\Sigma)^{n/2} \, \Gamma_p(n/2)}$$
where $\det$ is the [[determinant|0C3CFHDN6R]], $\tr$ is the [[trace|07PTPSZPME]] and $\Gamma_p$ is the multivariate gamma function.

Example: for $p = 1$ and $\Sigma = (\sigma^2)$, $S = \sum_i X_i^2 = \sigma^2 \sum_i (X_i/\sigma)^2$ with $X_i/\sigma$ standard normal, so $W_1(\sigma^2, n)$ is $\sigma^2$ times the [[chi-squared distribution|0RFMMBHFTV]] with $n$ degrees of freedom.

Example: if $Y_1, \dots, Y_m$ are i.i.d. $\mathcal{N}_p(\mu, \Sigma)$ with $m \ge 2$ and $\bar{Y}$ is their mean, then $\sum_{i=1}^m (Y_i - \bar{Y})(Y_i - \bar{Y})^T \sim W_p(\Sigma, m - 1)$.

Non-example: if the $X_i$ have a common mean $\mu \ne 0$, then $E(S) = n\Sigma + n\mu\mu^T \ne n\Sigma$, so $S$ is not $W_p(\Sigma, n)$; its law is a noncentral Wishart distribution.
