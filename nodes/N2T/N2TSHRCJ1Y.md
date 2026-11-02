---
tag: N2TSHRCJ1Y
kind: definition
name: Bootstrap
msc: [62G09, 62F40]
defines: 40ATJEVR32
uses: [A05WR6TEK5, 036756NFD6, 0AJN7WHBJZ, 656Y8FA3RY, 0VTN5RKNC5]
sources:
  - url: https://en.wikipedia.org/wiki/Bootstrapping_(statistics)
---

## Definition

Let $X_1, \dots, X_n$ be [[i.i.d.|0AJN7WHBJZ]] with an unknown distribution $F$, and let $\hat\theta = T(X_1, \dots, X_n)$ be a [[statistic|036756NFD6]].
Let $\hat F_n$ be the [[empirical distribution|A05WR6TEK5]] of the observed values $x_1, \dots, x_n$, which puts mass $1/n$ at each $x_i$.
A *bootstrap sample* is a sample $X_1^*, \dots, X_n^*$ i.i.d. from $\hat F_n$, that is, $n$ draws with replacement from $x_1, \dots, x_n$.
The *bootstrap distribution* of $\hat\theta$ is the law of $\hat\theta^* = T(X_1^*, \dots, X_n^*)$ given the data.
The *bootstrap* estimates a feature of the [[sampling distribution|656Y8FA3RY]] of $\hat\theta$ under $F$ by the same feature of the bootstrap distribution.
An example of such a feature is the [[standard deviation|0VTN5RKNC5]].

## Remarks

In practice one draws $B$ independent bootstrap samples, computes $\hat\theta^*_1, \dots, \hat\theta^*_B$, and estimates the standard error of $\hat\theta$ by
$$\widehat{\mathrm{se}}_B = \Big( \frac{1}{B - 1} \sum_{b=1}^{B} \big(\hat\theta^*_b - \bar\theta^*\big)^2 \Big)^{1/2}, \qquad \bar\theta^* = \frac{1}{B} \sum_{b=1}^{B} \hat\theta^*_b.$$
The percentile interval takes the $\alpha/2$ and $1 - \alpha/2$ empirical quantiles of the $\hat\theta^*_b$ as a confidence interval of level about $1 - \alpha$.

Example: data $(1, 3)$ and $\hat\theta = \bar X$.
The four equally likely bootstrap samples $(1,1), (1,3), (3,1), (3,3)$ have means $1, 2, 2, 3$.
Their variance is $(1 + 0 + 0 + 1)/4 = 1/2$, which equals $\hat\sigma^2 / n$ with the plug-in variance $\hat\sigma^2 = 1$.

Non-example: for $X_i$ uniform on $[0, \theta]$ and $\hat\theta = \max_i X_i$, the bootstrap fails.
A bootstrap sample repeats the observed maximum with probability $1 - (1 - 1/n)^n \to 1 - e^{-1}$, so the bootstrap law of $n(\hat\theta - \hat\theta^*)$ has an atom at $0$, while the true law of $n(\theta - \hat\theta)$ is continuous.

The [[jackknife|WQ8TQKDKYT]] is an older resampling method that leaves out one observation at a time.
