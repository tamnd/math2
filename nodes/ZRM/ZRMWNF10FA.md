---
tag: ZRMWNF10FA
kind: definition
name: Point estimation
msc: [62F10]
defines: ATQPY2WPTA
uses: [0TTNRP5PFQ, 036756NFD6, K3AMMSY8DD, 0FREPFKNS7]
sources:
  - url: https://en.wikipedia.org/wiki/Point_estimation
---

## Definition

Let $(\mathcal{X}, \mathcal{A})$ be a sample space and let $\set{P_\theta : \theta \in \Theta}$ be a [[statistical model|K3AMMSY8DD]] on it.
Let $g \colon \Theta \to D$ be a function, the *estimand*, with values in a measurable space $D$.
A *point estimator* of $g(\theta)$ is a [[statistic|036756NFD6]] $T \colon \mathcal{X} \to D$, that is, a measurable map that does not depend on $\theta$.
For observed data $x \in \mathcal{X}$, the value $T(x)$ is the *point estimate* of $g(\theta)$.
*Point estimation* is the problem of choosing such a $T$ so that $T(X)$ is close to $g(\theta)$ when $X \sim P_\theta$, for every $\theta \in \Theta$.

## Remarks

The general notion of [[estimator|0TTNRP5PFQ]] covers the same object; the word "point" stresses that the output is a single element of $D$, not a set.

Example: in the model of $n$ independent Bernoulli($p$) trials with $\Theta = [0, 1]$ and $g(p) = p$, the map $T(x) = \frac{1}{n}\sum_i x_i$ is a point estimator; it is the [[maximum likelihood estimator|0FREPFKNS7]].

Non-example: the map $T(x) = \frac{1}{n}\sum_i x_i - p$ is not a point estimator of $p$, because it depends on the unknown parameter $p$.
Also, a confidence interval $[T_1(x), T_2(x)]$ is an interval estimator, not a point estimator, since its value is a set, not an element of $D$.

Closeness is measured by a loss function, most often the squared error $(T - g(\theta))^2$, whose expectation is the mean squared error.
