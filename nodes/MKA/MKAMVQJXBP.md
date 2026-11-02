---
tag: MKAMVQJXBP
kind: definition
name: Optimal experimental design
msc: [62K05]
defines: PM5PQX6TVP
uses: [2TE42ZWJ3E, A06SGFCSCE, 00KDZRW4C0, 0BQAA2BK3Q, 0V7G6WMFK0]
sources:
  - url: https://en.wikipedia.org/wiki/Optimal_experimental_design
---

## Definition

Let $\mathcal{X}$ be a compact set, the *design region*, and let $f \colon \mathcal{X} \to \R^p$ be continuous.
Consider the linear model $y = f(x)^T \beta + \varepsilon$ with unknown $\beta \in \R^p$ and uncorrelated errors of mean $0$ and common variance $\sigma^2$.
An *approximate design* is a probability measure $\xi$ on $\mathcal{X}$ with finite support, and its *information matrix* is
$$M(\xi) = \int_{\mathcal{X}} f(x) f(x)^T \, d\xi(x) = \sum_{x \in \operatorname{supp} \xi} \xi(\set{x}) f(x) f(x)^T.$$
A design $\xi^*$ is:

1. *D-optimal* if it maximises $\det M(\xi)$ over all approximate designs;
2. *A-optimal* if $M(\xi^*)$ is invertible and it minimises $\tr M(\xi)^{-1}$ over the designs with $M(\xi)$ invertible;
3. *E-optimal* if it maximises the smallest [[eigenvalue|0BQAA2BK3Q]] of $M(\xi)$;
4. *G-optimal* if it minimises $\max_{x \in \mathcal{X}} f(x)^T M(\xi)^{-1} f(x)$ over the designs with $M(\xi)$ invertible.

## Remarks

For an exact [[design|2TE42ZWJ3E]] with $n$ runs at $x_1, \dots, x_n$ and design matrix $X$ with rows $f(x_i)^T$, one has $M = \frac{1}{n} X^T X$.
If $M$ is invertible, the least squares estimator has [[covariance matrix|0V7G6WMFK0]] $\frac{\sigma^2}{n} M^{-1}$.
So a D-optimal design minimises the volume of the confidence ellipsoid for $\beta$ under normal errors.

Example: $\mathcal{X} = [-1, 1]$ and $f(x) = (1, x)^T$, a straight line.
With moments $m_1 = \int x \, d\xi$ and $m_2 = \int x^2 \, d\xi$, one gets $\det M(\xi) = m_2 - m_1^2$, the variance of $x$ under $\xi$.
On $[-1, 1]$ this variance is at most $1$, with equality exactly for the design with mass $1/2$ at $-1$ and $1/2$ at $1$, which is therefore D-optimal.

Non-example: the design with all mass at $x = 0$ has $M = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$, which is singular, so $\det M = 0$ and the slope cannot be estimated; it fails clause 1.
