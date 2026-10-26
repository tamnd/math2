---
tag: 0JWRJX2RMP
kind: concept
name: Bayesian inference
aliases: [bayesian-statistics, bayesian-updating]
msc: [62F15]
uses: [0NM6E9VW04, 00NBBSXRQS, 0KJ7ZS8AJA, 05FSTXM92W, 0PP5ZAJPP7]
sources:
  - url: https://en.wikipedia.org/wiki/Bayesian_inference
    locator: Formal description
  - url: https://en.wikipedia.org/wiki/Bayesian_inference
    locator: Conjugate priors
same_as:
  wikidata: Q812535
  wikipedia: Bayesian inference
---

## Summary

Bayesian inference is a method of statistical inference that treats an unknown parameter $\theta$ as a random variable. It uses [[Bayes' theorem|0NM6E9VW04]] to update a probability distribution for $\theta$ when data arrive.
One starts from a [[prior distribution|00NBBSXRQS]] with density $\pi(\theta)$ and a model with [[likelihood|05FSTXM92W]] $L(\theta \mid x) = f(x \mid \theta)$. The [[posterior distribution|0KJ7ZS8AJA]] has the density
$$\pi(\theta \mid x) = \frac{f(x \mid \theta)\, \pi(\theta)}{\int_\Theta f(x \mid \theta')\, \pi(\theta')\, d\theta'}.$$

## Remarks

In short, the posterior is proportional to the likelihood times the prior.
Example: with a $\operatorname{Beta}(a, b)$ prior for the success probability $p$, and $k$ successes in $n$ Bernoulli($p$) trials, the posterior is $\operatorname{Beta}(a + k, b + n - k)$ (see [[beta distribution|0PP5ZAJPP7]]). The prior is conjugate.
The posterior gives point estimates, such as the posterior mean, and credible intervals.
For new observations, the posterior predictive distribution is $f(\tilde{x} \mid x) = \int_\Theta f(\tilde{x} \mid \theta)\, \pi(\theta \mid x)\, d\theta$, if $\tilde{x}$ and $x$ are conditionally independent given $\theta$.

## Explanations

### L1 human

Bayesian inference starts with a belief about an unknown quantity, written as a probability distribution.
Each new piece of data updates this belief with Bayes' theorem. The result, the posterior, combines the prior belief with the evidence.
