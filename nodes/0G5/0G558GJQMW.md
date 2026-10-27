---
tag: 0G558GJQMW
kind: definition
name: Multivariate normal distribution
msc: [62H05]
defines: 0XN3K7RSZY
uses: [07RXBVTVZB, 0DKRR22AEQ]
sources:
  - url: https://en.wikipedia.org/wiki/Multivariate_normal_distribution
    locator: Normal random vector
  - url: https://en.wikipedia.org/wiki/Multivariate_normal_distribution
    locator: Non-degenerate case
inventory: [WZY86RN41E]
---

## Definition

Let $k \ge 1$ and let $X = (X_1, \dots, X_k)^{\mathsf{T}}$ be a random vector in $\mathbb{R}^k$.
Then $X$ is multivariate normal if there exist $\mu \in \mathbb{R}^k$, an integer $\ell \ge 1$ and a real $k \times \ell$ matrix $A$ with this property.
There is a vector $Z = (Z_1, \dots, Z_\ell)^{\mathsf{T}}$ of independent $\mathcal{N}(0, 1)$ random variables with
$$X = AZ + \mu.$$
Then the law of $X$ depends only on $\mu$ and on $\Sigma = AA^{\mathsf{T}}$. It is written $\mathcal{N}_k(\mu, \Sigma)$.

## Remarks

Here $\mu$ is the mean vector, with $\mu_i = E[X_i]$, and $\Sigma$ is the covariance matrix, with $\Sigma_{ij} = \operatorname{Cov}(X_i, X_j)$.
An equivalent condition: $X$ is multivariate normal if and only if $a^{\mathsf{T}} X$ has a [[normal distribution|07RXBVTVZB]] for each $a \in \mathbb{R}^k$. Here a constant counts as normal with variance $0$.
If $\Sigma$ is positive definite, $X$ has the density
$$f(x) = \frac{1}{\sqrt{(2\pi)^k \det \Sigma}} \exp\left(-\tfrac{1}{2} (x - \mu)^{\mathsf{T}} \Sigma^{-1} (x - \mu)\right), \quad x \in \mathbb{R}^k.$$
The components of a multivariate normal vector are independent if and only if they are uncorrelated, that is, if $\Sigma$ is diagonal.

## Explanations

### L1 human

A multivariate normal vector is a list of normal random variables that may be linked to each other.
The covariance matrix says how strongly each pair of components moves together. In two dimensions, the density looks like a hill with elliptical contour lines.
