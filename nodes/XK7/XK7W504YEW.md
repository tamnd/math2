---
tag: XK7W504YEW
kind: definition
name: Generalized least squares
msc: [62J05]
defines: P142WXJCF3
uses: [A06SGFCSCE, YM708KHV2W, 0V7G6WMFK0, 0KX66CZMBB, N3YMNMWANM]
sources:
  - url: https://en.wikipedia.org/wiki/Generalized_least_squares
---

## Definition

Let $X$ be a fixed real $n \times p$ matrix of rank $p$, and let $y = X\beta + \varepsilon$ with $\beta \in \R^p$ unknown.
Assume $E[\varepsilon] = 0$ and $\operatorname{Cov}(\varepsilon) = \sigma^2 \Omega$, where $\sigma^2 > 0$ and $\Omega$ is a known symmetric [[positive definite|0KX66CZMBB]] $n \times n$ matrix.
The *generalized least squares estimator* of $\beta$ is the minimiser of
$$(y - X b)^T \Omega^{-1} (y - X b)$$
over $b \in \R^p$, which is
$$\hat\beta_{\mathrm{GLS}} = (X^T \Omega^{-1} X)^{-1} X^T \Omega^{-1} y.$$

## Remarks

Equivalent form: let $P$ be an invertible matrix with $P^T P = \Omega^{-1}$, for example $P = \Omega^{-1/2}$.
Then $P y = P X \beta + P \varepsilon$ with $\operatorname{Cov}(P\varepsilon) = \sigma^2 I_n$.
The estimator $\hat\beta_{\mathrm{GLS}}$ is the [[ordinary least squares|YM708KHV2W]] estimator of this transformed model.
By the [[Gauss–Markov theorem|N3YMNMWANM]] applied to the transformed model, it is the best linear unbiased estimator; this is Aitken's theorem.
Its covariance matrix is $\sigma^2 (X^T \Omega^{-1} X)^{-1}$.

Example: if $\Omega = I_n$, the estimator reduces to ordinary least squares.
If $\Omega$ is diagonal, it is the weighted least squares estimator with weights $1/\Omega_{ii}$.

Non-example: if $\Omega$ is only positive semidefinite and singular, then $\Omega^{-1}$ does not exist and the formula is not defined.

When $\Omega$ is unknown and is replaced by an estimate, the method is called *feasible* generalized least squares.
