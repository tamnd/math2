---
tag: CNZB94AHDM
kind: statement
role: theorem
name: Mutual fund separation theorem
msc: [91G10]
uses: [ZBDA8W9D6V, SCTRT97C2R, XADAEPN54D]
about: [SCTRT97C2R]
sources:
  - url: https://en.wikipedia.org/wiki/Mutual_fund_separation_theorem
same_as:
  wikidata: Q17082552
  wikipedia: Mutual fund separation theorem
---

## Statement

Consider $n \ge 2$ risky assets with mean vector $m$ and positive definite covariance matrix $\Sigma$, as in [[modern portfolio theory|ZBDA8W9D6V]].
Let $\mathbf{1} = (1, \dots, 1)$ and assume that $m$ is not a multiple of $\mathbf{1}$.
Let $A = \mathbf{1}^T \Sigma^{-1} \mathbf{1}$, $B = \mathbf{1}^T \Sigma^{-1} m$, $C = m^T \Sigma^{-1} m$ and $D = AC - B^2$.

1. (Two-fund separation.) For each $\mu \in \R$, the minimum-variance portfolio with mean $\mu$ is $w(\mu) = g + \mu h$, where
$$g = \frac{C \, \Sigma^{-1} \mathbf{1} - B \, \Sigma^{-1} m}{D}, \qquad h = \frac{A \, \Sigma^{-1} m - B \, \Sigma^{-1} \mathbf{1}}{D}.$$
Hence any two distinct minimum-variance portfolios $w(\mu_1), w(\mu_2)$ generate all of them as affine combinations $\lambda w(\mu_1) + (1 - \lambda) w(\mu_2)$.
2. (One-fund separation.) Suppose also that a riskless asset with return $r_f < B/A$ can be held in any amount.
   Then every efficient portfolio consists of the riskless asset and a non-negative multiple of the *tangency portfolio*
$$w_T = \frac{\Sigma^{-1} (m - r_f \mathbf{1})}{B - A r_f}.$$

## Remarks

For part 1, [[Lagrange multipliers|XADAEPN54D]] for the two constraints give $\Sigma w = \lambda m + \gamma \mathbf{1}$, so $w = \lambda \Sigma^{-1} m + \gamma \Sigma^{-1} \mathbf{1}$.
The constraints are linear equations for $(\lambda, \gamma)$, whose solution is affine in $\mu$.
For part 2, the same computation with the riskless asset shows that the risky part of every optimal portfolio is proportional to $\Sigma^{-1}(m - r_f \mathbf{1})$.

Example: for two uncorrelated assets with means $1, 2$ and variances $1, 1$, one gets $A = 2$, $B = 3$, $C = 5$, $D = 1$.
Then $g = (2, -1)$ and $h = (-1, 1)$, so $w(\mu) = (2 - \mu, \mu - 1)$, which is the direct computation.

If $\Sigma$ is singular, the minimum-variance portfolio need not be unique and the formulas break down.
The condition $r_f < B/A$ says that the riskless return is below the mean of the global minimum-variance portfolio.
It makes the tangency portfolio lie on the [[efficient frontier|SCTRT97C2R]] of the risky assets, the upper half of the minimum-variance hyperbola.

## Explanations

### L1 human

Investors with different tastes for risk do not need different menus of assets.
Without a safe asset, every best portfolio is a mix of the same two funds.
With a safe asset, every best portfolio is a mix of the safe asset and one single fund of risky assets.
Cautious investors put more in the safe asset; bold ones borrow to buy more of the risky fund.

### L2 human

Part 1 says that the set of minimum-variance portfolios is a line in the space of weights, so it is spanned by any two of its points.
Part 2 is the basis of the capital market line.
In the $(\sigma, \mu)$ plane, the efficient portfolios lie on the ray from $(0, r_f)$ tangent to the efficient frontier of risky assets.
If all investors hold the same tangency portfolio, it must be the market portfolio, which leads to the capital asset pricing model.
