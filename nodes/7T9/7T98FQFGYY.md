---
tag: 7T98FQFGYY
kind: definition
name: Bayes estimator
msc: [62C10, 62F15]
defines: PP1A0JB47Q
uses: [VEBDNCJJTN, N26TSVRH2S, 3BTG6VVCGZ, 00NBBSXRQS, 0KJ7ZS8AJA, 0SSS6ERQ0S, 0EW824Z7G2, 0WCWA1KT3M]
sources:
  - url: https://en.wikipedia.org/wiki/Bayes_estimator
---

## Definition

Let $\set{P_\theta : \theta \in \Theta}$ be a statistical model with a [[loss function|3BTG6VVCGZ]] $L$, and let $\pi$ be a [[prior|00NBBSXRQS]] on $\Theta$.
For an [[estimator|0SSS6ERQ0S]] $\delta$, let $r(\pi, \delta)$ be its [[Bayes risk|VEBDNCJJTN]], the [[risk|N26TSVRH2S]] $R(\theta, \delta)$ averaged over $\pi$.
An estimator $\delta_\pi$ is a *Bayes estimator* with respect to $\pi$ if $r(\pi, \delta_\pi) < \infty$ and
$$r(\pi, \delta_\pi) = \inf_{\delta} r(\pi, \delta),$$
where the infimum is over all estimators $\delta$.

## Remarks

If $r(\pi) < \infty$, an estimator that minimizes the [[posterior|0KJ7ZS8AJA]] expected loss $E[L(\theta, \delta(x)) \mid X = x]$ for almost every $x$ is a Bayes estimator.
Under squared error loss $L(\theta, a) = (a - \theta)^2$, the Bayes estimator is the posterior mean $E[\theta \mid X]$.
Under absolute error loss, it is a posterior median.

Example: let $X$ be [[binomial|0WCWA1KT3M]] with parameters $n$ and $\theta$, and let $\pi$ be the [[beta distribution|0EW824Z7G2]] with parameters $a, b > 0$.
The posterior is the beta distribution with parameters $a + X$ and $b + n - X$.
So under squared error loss the Bayes estimator is its mean $(a + X)/(a + b + n)$.

Non-example: for the uniform prior, $a = b = 1$, the Bayes estimator is $(X + 1)/(n + 2)$.
The proportion $X/n$ differs from it whenever $X \ne n/2$, and for $n \ge 1$ its Bayes risk $1/(6n)$ is larger, so $X/n$ is not the Bayes estimator for this prior.
