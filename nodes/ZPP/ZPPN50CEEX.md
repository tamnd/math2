---
tag: ZPPN50CEEX
kind: definition
name: Observed information
msc: [62F10, 62B10]
defines: KJ9ZQWYBY6
uses: [0VW9E4QXR6, 0693Y2METT, 0FREPFKNS7, G1Z3WSTE8Q, 0XB9GQTN9G]
sources:
  - url: https://en.wikipedia.org/wiki/Observed_information
---

## Definition

Let $\set{f(\cdot\,; \theta) : \theta \in \Theta}$ be a family of densities with $\Theta \subseteq \R^d$ open.
Let $x_1, \dots, x_n$ be observed data, and let
$$\ell(\theta) = \sum_{i=1}^{n} \log f(x_i; \theta)$$
be the log-[[likelihood|0VW9E4QXR6]], assumed twice differentiable in $\theta$.
The *observed information* at $\theta$ is the $d \times d$ matrix
$$J(\theta) = -\nabla^2 \ell(\theta), \qquad J_{jk}(\theta) = -\frac{\partial^2 \ell(\theta)}{\partial \theta_j \, \partial \theta_k},$$
that is, minus the [[Hessian matrix|0693Y2METT]] of the log-likelihood.
For $d = 1$ it is the number $J(\theta) = -\ell''(\theta)$.

## Remarks

It is usually evaluated at the [[maximum likelihood estimate|0FREPFKNS7]] $\hat\theta$, and $J(\hat\theta)$ is then positive semidefinite when $\hat\theta$ is an interior maximum.
If the data are independent with density $f(\cdot\,; \theta)$, then under regularity conditions $E_\theta[J(\theta)] = n I(\theta)$, where $I$ is the [[Fisher information|G1Z3WSTE8Q]].
The inverse $J(\hat\theta)^{-1}$ is a standard estimate of the covariance matrix of $\hat\theta$.

Example: [[Poisson|0XB9GQTN9G]] data with mean $\lambda > 0$ and $t = x_1 + \cdots + x_n > 0$.
Then $\ell(\lambda) = t \log \lambda - n\lambda - \sum_i \log(x_i!)$, so $J(\lambda) = t/\lambda^2$.
At $\hat\lambda = t/n$ this gives $J(\hat\lambda) = n^2/t$.

Non-example: minus the second derivative of the likelihood $L = e^{\ell}$ itself is not the observed information.
In the Poisson example with $n = 1$ and $t = 1$, $-L''(\lambda)$ at $\hat\lambda = 1$ equals $e^{-1}$, while $J(1) = 1$.
