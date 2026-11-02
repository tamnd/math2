---
tag: RNV041SNCT
kind: definition
name: Risk function
msc: [62C05]
defines: N26TSVRH2S
uses: [K3AMMSY8DD, 3BTG6VVCGZ, 0WQNRCNY3M, 05NZ1HHQMV, 05AQE0QR0D]
sources:
  - url: https://en.wikipedia.org/wiki/Loss_function
---

## Definition

Let $\set{P_\theta : \theta \in \Theta}$ be a [[statistical model|K3AMMSY8DD]] for an observation $X$ with values in a measurable space $\mathcal{X}$.
Let $\mathcal{A}$ be a measurable space of actions and let $L \colon \Theta \times \mathcal{A} \to [0, \infty)$ be a [[loss function|3BTG6VVCGZ]], measurable in $a$ for each $\theta$.
A (non-randomized) *decision rule* is a measurable map $\delta \colon \mathcal{X} \to \mathcal{A}$.
The *risk function* of $\delta$ is the map $R(\cdot, \delta) \colon \Theta \to [0, \infty]$ given by
$$R(\theta, \delta) = E_\theta\big[ L(\theta, \delta(X)) \big] = \int_{\mathcal{X}} L(\theta, \delta(x)) \, P_\theta(dx).$$

## Remarks

The risk is an [[expected value|0WQNRCNY3M]] over the data, for a fixed $\theta$.
Under the squared error loss $L(\theta, a) = (a - g(\theta))^2$, the risk of an estimator is its [[mean squared error|05NZ1HHQMV]].
For randomized rules, one also averages over the randomization.

Example: let $X_1, \dots, X_n$ be independent [[normal|05AQE0QR0D]] with mean $\theta$ and variance $1$, with squared error loss.
For $\delta = \bar X$, the risk is $R(\theta, \delta) = E_\theta[(\bar X - \theta)^2] = \operatorname{Var}_\theta(\bar X) = 1/n$ for every $\theta$.

Non-example: the realized loss $L(\theta, \delta(x))$ at the observed data $x$ is not the risk.
It depends on the data, while the risk is an average over all possible data.
