---
tag: SR8DQDKHQN
kind: definition
name: Hotelling's T-squared distribution
msc: [62H10, 62H15]
defines: XS9GETCZX2
uses: [0G558GJQMW, 8BEMNJW0B9, 0E9502NT92, 0QQCG3JWJ4, PBT8VRJADK, 0NQ5798SB1]
sources:
  - url: https://en.wikipedia.org/wiki/Hotelling%27s_T-squared_distribution
---

## Definition

Let $p$ and $m$ be positive integers with $m \ge p$, and let $\Sigma$ be a $p \times p$ [[positive definite matrix|0QQCG3JWJ4]].
Let $x$ be a random vector with the [[multivariate normal distribution|0G558GJQMW]] $\mathcal{N}_p(0, \Sigma)$.
Let $M$ be a random matrix with the [[Wishart distribution|8BEMNJW0B9]] $W_p(\Sigma, m)$, [[independent|0E9502NT92]] of $x$.
The distribution of
$$T^2 = m \, x^T M^{-1} x$$
does not depend on $\Sigma$.
It is *Hotelling's T-squared distribution* with dimension $p$ and $m$ degrees of freedom, written $T^2(p, m)$.

## Remarks

The condition $m \ge p$ makes $M$ invertible with probability $1$.
The distribution is a rescaled [[F-distribution|PBT8VRJADK]]:
$$\frac{m - p + 1}{p m} T^2 \sim F(p, m - p + 1).$$

Example: for $p = 1$, $x = \sigma Z$ with $Z$ standard normal and $M = \sigma^2 V$ with $V$ chi-squared with $m$ degrees of freedom.
Then $T^2 = Z^2/(V/m)$ is the square of a [[Student t|0NQ5798SB1]] variable with $m$ degrees of freedom, and the formula above gives $T^2 \sim F(1, m)$.

Example: let $Y_1, \dots, Y_n$ be i.i.d. $\mathcal{N}_p(\mu, \Sigma)$ with $n - 1 \ge p$, with sample mean $\bar{Y}$ and sample covariance matrix $\hat{\Sigma}$.
Then $\sqrt{n}(\bar{Y} - \mu) \sim \mathcal{N}_p(0, \Sigma)$ and $(n - 1)\hat{\Sigma} \sim W_p(\Sigma, n - 1)$ are independent, so $n (\bar{Y} - \mu)^T \hat{\Sigma}^{-1} (\bar{Y} - \mu) \sim T^2(p, n - 1)$.

Non-example: if $M$ and $x$ are dependent, for instance $p = 1$, $m = 1$ and $M = x^2$, then $T^2 = 1$ always, which is not $T^2(1, 1)$.
