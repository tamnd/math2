---
tag: 9GKRK5B2B5
kind: definition
name: Monotone likelihood ratio
msc: [62F03]
defines: 4Z73AFN7WT
uses: [05FSTXM92W, 036756NFD6, 04YG690N5V]
sources:
  - url: https://en.wikipedia.org/wiki/Monotone_likelihood_ratio
---

## Definition

Let $\Theta \subseteq \R$ and let $\set{f_\theta : \theta \in \Theta}$ be a family of [[densities|04YG690N5V]] (or probability mass functions) on a sample space $\mathcal{X}$.
Let $T \colon \mathcal{X} \to \R$ be a [[statistic|036756NFD6]].
The family has a *monotone likelihood ratio* in $T$ if, for all $\theta_1 < \theta_2$ in $\Theta$:

1. $f_{\theta_1} \ne f_{\theta_2}$;
2. there is a nondecreasing function $g \colon \R \to [0, \infty]$ with $f_{\theta_2}(x)/f_{\theta_1}(x) = g(T(x))$ for every $x$ with $f_{\theta_1}(x) > 0$ or $f_{\theta_2}(x) > 0$.

Here $c/0 = \infty$ for $c > 0$.

## Remarks

The ratio in clause 2 is the [[likelihood ratio|05FSTXM92W]] of $\theta_2$ to $\theta_1$ at the data $x$.
Example: let $f_\theta(x) = h(x) \exp\big(\eta(\theta) T(x) - A(\theta)\big)$ be a one-parameter exponential family with $\eta$ strictly increasing.
Then $f_{\theta_2}(x)/f_{\theta_1}(x) = \exp\big((\eta(\theta_2) - \eta(\theta_1)) T(x) - A(\theta_2) + A(\theta_1)\big)$, which is increasing in $T(x)$.
This covers the binomial law in $p$ with $T(x) = x$, and $\mathcal{N}(\theta, 1)$ with $T(x) = x$.
Non-example: the Cauchy location family $f_\theta(x) = 1/(\pi(1 + (x - \theta)^2))$ fails clause 2 with $T(x) = x$.
For $\theta_1 = 0$ and $\theta_2 = 1$, the ratio $(1 + x^2)/(1 + (x - 1)^2)$ tends to $1$ as $x \to \pm\infty$ and is larger than $1$ at $x = 1$, so it is not monotone.
