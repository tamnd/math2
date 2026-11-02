---
tag: FX1A4SN6CF
kind: definition
name: Bayes risk
msc: [62C10]
defines: VEBDNCJJTN
uses: [N26TSVRH2S, 00NBBSXRQS, DWJF7ABPR1, 0WCWA1KT3M]
sources:
  - url: https://en.wikipedia.org/wiki/Bayes_estimator
---

## Definition

Let $\set{P_\theta : \theta \in \Theta}$ be a statistical model with a loss function, and let $R(\theta, \delta)$ be the [[risk function|N26TSVRH2S]] of a decision rule $\delta$.
Let $\Theta$ carry a σ-algebra, and let $\pi$ be a probability measure on $\Theta$, the [[prior|00NBBSXRQS]], such that $\theta \mapsto R(\theta, \delta)$ is measurable for the rules considered.
The *Bayes risk* of $\delta$ under $\pi$ is
$$r(\pi, \delta) = \int_\Theta R(\theta, \delta) \, \pi(d\theta) \in [0, \infty].$$
The *Bayes risk of the prior* $\pi$ is $r(\pi) = \inf_\delta r(\pi, \delta)$, the infimum over all decision rules.

## Remarks

The integral is a [[Lebesgue integral|DWJF7ABPR1]] of a nonnegative function, so it always exists, possibly infinite.
By Fubini's theorem, $r(\pi, \delta)$ is also the expected loss when $\theta$ is drawn from $\pi$ and then $X$ from $P_\theta$.

Example: let $X$ be [[binomial|0WCWA1KT3M]] with parameters $n$ and $\theta \in [0, 1]$, with squared error loss and $\delta(X) = X/n$.
Then $R(\theta, \delta) = \theta(1 - \theta)/n$.
For the uniform prior, $r(\pi, \delta) = \frac{1}{n} \int_0^1 \theta(1 - \theta) \, d\theta = \frac{1}{6n}$.

Non-example: the maximum $\sup_\theta R(\theta, \delta) = \frac{1}{4n}$ is not a Bayes risk of $\delta$ for the uniform prior.
It is the worst-case risk used in the minimax principle; it equals $r(\pi, \delta)$ only for priors that put all their mass where the risk is maximal.
