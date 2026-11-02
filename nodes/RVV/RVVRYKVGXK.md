---
tag: RVVRYKVGXK
kind: definition
name: Partial correlation
msc: [62H20]
defines: TT3BXBR4DB
uses: [0DNN9B6Q2F, 0KBFAWYRTE, 0V7G6WMFK0, 0EB9N0S33C]
sources:
  - url: https://en.wikipedia.org/wiki/Partial_correlation
---

## Definition

Let $X$ and $Y$ be real random variables and let $Z$ be a random vector in $\R^k$, all with finite second moments.
Assume that the [[covariance matrix|0V7G6WMFK0]] $\Sigma_{ZZ}$ of $Z$ is [[invertible|0EB9N0S33C]].
Write $\Sigma_{XZ}$ for the row vector of [[covariances|0KBFAWYRTE]] $\operatorname{Cov}(X, Z_j)$, and similarly $\Sigma_{YZ}$.
The residuals of the best linear predictions of $X$ and $Y$ from $Z$ are
$$e_X = X - \mathbb{E}X - \Sigma_{XZ} \Sigma_{ZZ}^{-1} (Z - \mathbb{E}Z), \qquad e_Y = Y - \mathbb{E}Y - \Sigma_{YZ} \Sigma_{ZZ}^{-1} (Z - \mathbb{E}Z).$$
If $\operatorname{Var}(e_X) > 0$ and $\operatorname{Var}(e_Y) > 0$, the *partial correlation* of $X$ and $Y$ given $Z$ is the [[correlation coefficient|0DNN9B6Q2F]]
$$\rho_{XY \cdot Z} = \operatorname{Corr}(e_X, e_Y).$$

## Remarks

Example: let $Z, U, V$ be uncorrelated with variance $1$ and mean $0$, and let $X = Z + U$, $Y = Z + V$.
Then $\Sigma_{XZ} = \Sigma_{YZ} = 1$ and $\Sigma_{ZZ} = 1$, so $e_X = U$ and $e_Y = V$, and $\rho_{XY \cdot Z} = 0$.
Yet $\operatorname{Corr}(X, Y) = 1/2$.
Non-example: if $X = Z$, then $e_X = 0$, so $\operatorname{Var}(e_X) = 0$ and the partial correlation is not defined.

For a single control variable $Z$, with $\rho_{XY}$, $\rho_{XZ}$, $\rho_{YZ}$ the pairwise correlations,
$$\rho_{XY \cdot Z} = \frac{\rho_{XY} - \rho_{XZ} \rho_{YZ}}{\sqrt{(1 - \rho_{XZ}^2)(1 - \rho_{YZ}^2)}}.$$
If $P = (p_{ij})$ is the inverse of the covariance matrix of $(X, Y, Z)$, then $\rho_{XY \cdot Z} = -p_{12} / \sqrt{p_{11} p_{22}}$.
The sample partial correlation uses the sample covariances, or equivalently the residuals of least squares fits on the data.
