---
tag: H82J4YJF8N
kind: definition
name: Bayesian information criterion
msc: [62F15, 62B10]
defines: GXP6H9VGRB
uses: [05FSTXM92W, 0FREPFKNS7]
sources:
  - url: https://en.wikipedia.org/wiki/Bayesian_information_criterion
---

## Definition

Let $M$ be a parametric statistical model with $k$ free real parameters, and let $x$ be data of $n$ observations.
Let $\hat L$ be the maximum of the [[likelihood function|05FSTXM92W]] of $M$ at $x$, the value at the [[maximum likelihood estimate|0FREPFKNS7]].
The *Bayesian information criterion* of $M$ at $x$ is
$$\mathrm{BIC} = k \ln n - 2 \ln \hat L.$$
Among several candidate models for the same data, the BIC rule selects a model with the smallest BIC.

## Remarks

Under regularity conditions, $-\mathrm{BIC}/2$ approximates the logarithm of the marginal likelihood of $M$, up to a term that stays bounded as $n \to \infty$.
So differences of BIC approximate $-2$ times the logarithm of a Bayes factor.
Example: with $n = 100$, a model with $k = 2$ and $\ln \hat L = -100$ has $\mathrm{BIC} = 2 \ln 100 + 200 \approx 209.2$.
A model with $k = 3$ and $\ln \hat L = -98$ has $\mathrm{BIC} \approx 209.8$, so the BIC rule keeps the smaller model, while the AIC values $204$ and $202$ favour the larger one.
Non-example: $2k - 2 \ln \hat L$ is the [[Akaike information criterion|CMAX3KF9H0]], not the BIC; the two agree only when $\ln n = 2$.
