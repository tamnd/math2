---
tag: 2Y7P8SABM9
kind: definition
name: Factor analysis
msc: [62H25]
defines: 4QQQP1Q886
uses: [C63RVH96TF, 0V7G6WMFK0, 0WQNRCNY3M]
sources:
  - url: https://en.wikipedia.org/wiki/Factor_analysis
---

## Definition

Let $p > k \ge 1$ be integers.
The *factor analysis model* with $k$ factors for a random vector $X$ in $\R^p$ is
$$X = \mu + L F + \varepsilon,$$
where:

1. $\mu \in \R^p$ is a constant vector and $L$ is a constant $p \times k$ matrix, the matrix of *loadings*.
2. $F$ is a random vector in $\R^k$, the *common factors*, with $\mathbb{E}F = 0$ and covariance matrix $I_k$.
3. $\varepsilon$ is a random vector in $\R^p$, the *specific errors*, with $\mathbb{E}\varepsilon = 0$ and diagonal covariance matrix $\Psi$.
4. $F$ and $\varepsilon$ are uncorrelated.

The factors $F$ are not observed; only $X$ is.
*Factor analysis* is the estimation of $L$ and $\Psi$ from observations of $X$, and the interpretation of the factors.

## Remarks

The model implies that the [[covariance matrix|0V7G6WMFK0]] of $X$ is $\Sigma = L L^T + \Psi$.
Example: with $p = 3$, $k = 1$, $L = (1, 1, 1)^T$ and $\Psi = I_3$, the covariance matrix has diagonal entries $2$ and off-diagonal entries $1$.
Non-example: a model $X = \mu + L F + \varepsilon$ with $\Psi$ not diagonal fails clause 3; the errors would then carry shared variation that the factors are meant to explain.
The loadings are determined only up to rotation: if $Q$ is a $k \times k$ orthogonal matrix, then $L Q$ and $L$ give the same $\Sigma$.
For this reason, rotations such as varimax are chosen to make the loadings easier to interpret.
Under normality, $L$ and $\Psi$ are often estimated by maximum likelihood.
