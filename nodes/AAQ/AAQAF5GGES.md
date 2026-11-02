---
tag: AAQAF5GGES
kind: definition
name: Kriging
msc: [62M30, 62M20, 62H11]
defines: VP9S3PNJQ0
uses: [ZF8AA2JVKV, 0QH5ENKZM1, 0WQNRCNY3M, 05NZ1HHQMV]
sources:
  - url: https://en.wikipedia.org/wiki/Kriging
---

## Definition

Let $D \subseteq \R^d$ and let $(Z(s))_{s \in D}$ be a real random field of the form $Z(s) = \mu + \delta(s)$.
Here $\mu$ is an unknown constant and $\delta$ is intrinsically stationary with [[variogram|ZF8AA2JVKV]] $2\gamma$ and $E[\delta(s)] = 0$.
Let $s_1, \dots, s_n, s_0 \in D$, and write $\gamma_{ij} = \gamma(s_i - s_j)$ for $0 \le i, j \le n$.

The *ordinary kriging predictor* of $Z(s_0)$ is $\hat Z(s_0) = \sum_{i=1}^{n} \lambda_i Z(s_i)$, where the weights minimise the [[mean squared error|05NZ1HHQMV]] $E[(Z(s_0) - \hat Z(s_0))^2]$ subject to $\sum_{i=1}^{n} \lambda_i = 1$.
Equivalently, $\lambda_1, \dots, \lambda_n$ and a number $m$ solve the linear system
$$\sum_{j=1}^{n} \lambda_j \gamma_{ij} + m = \gamma_{i0} \quad (1 \le i \le n), \qquad \sum_{j=1}^{n} \lambda_j = 1.$$

## Remarks

The constraint $\sum_i \lambda_i = 1$ makes the predictor unbiased, $E[\hat Z(s_0)] = \mu = E[Z(s_0)]$, whatever the value of $\mu$.
The minimal mean squared error, the kriging variance, is $\sum_{i=1}^{n} \lambda_i \gamma_{i0} + m$.
Simple kriging assumes $\mu$ known and drops the constraint; universal kriging replaces $\mu$ by a linear combination of known functions of $s$.

Example: with one observation, $n = 1$, the constraint forces $\lambda_1 = 1$, so $\hat Z(s_0) = Z(s_1)$.
The first equation then gives $m = \gamma_{10} - \gamma_{11} = \gamma(s_1 - s_0)$, since $\gamma(0) = 0$, so the kriging variance is $2\gamma(s_1 - s_0)$, which is indeed $E[(Z(s_0) - Z(s_1))^2]$.

Non-example: inverse distance weighting also predicts by a weighted average with weights summing to $1$.
Its weights are fixed by the distances alone and do not minimise the mean squared error for the given variogram, so it is not kriging.
