---
tag: 02CBHV4ZZQ
kind: definition
name: Covariance matrix
msc: [62H05]
defines: 0V7G6WMFK0
uses: [0DJ8W3HP2D, 007QED3E0Y, 0DCT0QZVQ1]
sources:
  - url: https://en.wikipedia.org/wiki/Covariance_matrix
    locator: Definition
---

## Definition

Let $X = (X_1, \dots, X_n)^{\mathsf{T}}$ be a random vector in $\mathbb{R}^n$ with $E[X_i^2] < \infty$ for each $i$, and let $\mu = E[X]$ be its mean vector.
The covariance matrix of $X$ is the $n \times n$ matrix $\Sigma = \operatorname{Cov}(X)$ with entries
$$\Sigma_{ij} = \operatorname{Cov}(X_i, X_j), \quad 1 \le i, j \le n.$$
In matrix form, $\Sigma = E\left[(X - \mu)(X - \mu)^{\mathsf{T}}\right]$.

## Remarks

The diagonal entries are the [[variances|007QED3E0Y]] $\Sigma_{ii} = \operatorname{Var}(X_i)$.
$\Sigma$ is symmetric and positive semidefinite: $a^{\mathsf{T}} \Sigma a = \operatorname{Var}(a^{\mathsf{T}} X) \ge 0$ for each $a \in \mathbb{R}^n$.
For a real $m \times n$ matrix $A$ and $b \in \mathbb{R}^m$, $\operatorname{Cov}(AX + b) = A \Sigma A^{\mathsf{T}}$.
The covariance matrix and the mean vector are the two parameters of the [[multivariate normal distribution|0G558GJQMW]].

## Explanations

### L1 human

For a random vector, one number is not enough to describe the spread.
The covariance matrix collects the variance of each component and the covariance of each pair in one table.
