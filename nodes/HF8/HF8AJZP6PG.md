---
tag: HF8AJZP6PG
kind: definition
name: Mahalanobis distance
msc: [62H30, 62H20]
defines: P546TSFBK2
uses: [0V7G6WMFK0, 0KX66CZMBB, 0WQNRCNY3M]
sources:
  - url: https://en.wikipedia.org/wiki/Mahalanobis_distance
---

## Definition

Let $X$ be a random vector in $\R^p$ with [[mean|0WQNRCNY3M]] $\mu$ and [[covariance matrix|0V7G6WMFK0]] $\Sigma$, and assume that $\Sigma$ is [[positive definite|0KX66CZMBB]].
The *Mahalanobis distance* of a point $x \in \R^p$ from the distribution of $X$ is
$$D_M(x) = \sqrt{(x - \mu)^T \Sigma^{-1} (x - \mu)}.$$
The Mahalanobis distance between two points $x, y \in \R^p$ with respect to $\Sigma$ is
$$d_M(x, y) = \sqrt{(x - y)^T \Sigma^{-1} (x - y)}.$$

## Remarks

Example: let $\mu = 0$ and $\Sigma = \operatorname{diag}(4, 1)$.
Then $\Sigma^{-1} = \operatorname{diag}(1/4, 1)$, so $D_M(2, 0) = \sqrt{4/4} = 1$ and $D_M(0, 1) = 1$, while $D_M(0, 2) = 2$.
Non-example: if $\Sigma = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$, then $\Sigma$ is not invertible, so the formula is not defined.
If $\Sigma = A A^T$ with $A$ invertible, then $d_M(x, y) = \abs{A^{-1} x - A^{-1} y}$, the Euclidean distance after the change of variables $x \mapsto A^{-1} x$.
So $d_M$ is a metric on $\R^p$.
If $\Sigma$ is the identity, $d_M$ is the Euclidean distance.
If $X$ is multivariate normal, then $D_M(X)^2$ has the chi-squared distribution with $p$ degrees of freedom.
