---
tag: 9JP83HPAEX
kind: definition
name: Sample mean and sample covariance
msc: [62H12, 62F10]
defines: ZP455BADJ3
uses: [0QNRBHWV35, 0JN9P4A944, 02CBHV4ZZQ, 036756NFD6]
sources:
  - url: https://en.wikipedia.org/wiki/Sample_mean_and_covariance
---

## Definition

Let $n \ge 2$ and $k \ge 1$, and let $X_1, \dots, X_n$ be random vectors in $\R^k$, written as columns.
The *sample mean* is the [[statistic|036756NFD6]]
$$\bar{X} = \frac{1}{n} \sum_{i=1}^{n} X_i \in \R^k.$$
The *sample covariance matrix* is the $k \times k$ matrix
$$Q = \frac{1}{n - 1} \sum_{i=1}^{n} \left(X_i - \bar{X}\right)\left(X_i - \bar{X}\right)^T.$$
Its entry $Q_{jl}$ is the sample covariance of the $j$-th and the $l$-th coordinates.

## Remarks

Example: for the observations $(0, 0)^T$ and $(2, 2)^T$, the mean is $(1, 1)^T$ and the deviations are $(-1, -1)^T$ and $(1, 1)^T$.
Each deviation gives the matrix with all entries $1$, so $Q$ has all four entries equal to $2$.
For $k = 1$, $\bar{X}$ is the [[sample mean|0QNRBHWV35]] and $Q$ is the [[sample variance|0JN9P4A944]].
If the $X_i$ are i.i.d. with mean vector $\mu$ and finite [[covariance matrix|02CBHV4ZZQ]] $\Sigma$, then $E[\bar{X}] = \mu$ and $E[Q] = \Sigma$.
Non-example: the matrix with divisor $n$ in place of $n - 1$ is also used, but it is not unbiased; its expectation is $\frac{n-1}{n}\Sigma$.
The matrix $Q$ is symmetric and positive semidefinite, and it is singular when $n \le k$.
