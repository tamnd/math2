---
tag: 05FSTXM92W
kind: definition
name: Likelihood function
msc: [62F10]
defines: 0VW9E4QXR6
uses: [0WF4EJP91W, 04YG690N5V, 0AJN7WHBJZ]
sources:
  - url: https://en.wikipedia.org/wiki/Likelihood_function
    locator: Definition
---

## Definition

Let $\Theta$ be a set of parameters. For each $\theta \in \Theta$, let $f(\cdot \mid \theta)$ be a [[probability mass function|0WF4EJP91W]] or a [[density|04YG690N5V]] on $\mathbb{R}^n$. It gives the law of the data $X = (X_1, \dots, X_n)$ when $\theta$ is the true parameter.
For observed data $x \in \mathbb{R}^n$, the likelihood function is the function $L \colon \Theta \to [0, \infty)$ with
$$L(\theta \mid x) = f(x \mid \theta).$$
The log-likelihood is $\ell(\theta \mid x) = \ln L(\theta \mid x)$.

## Remarks

For an [[i.i.d.|0AJN7WHBJZ]] sample with mass function or density $f_1(\cdot \mid \theta)$ for each observation, $L(\theta \mid x) = \prod_{i=1}^{n} f_1(x_i \mid \theta)$ and $\ell(\theta \mid x) = \sum_{i=1}^{n} \ln f_1(x_i \mid \theta)$.
The likelihood is not a probability distribution on $\Theta$. In general, its integral over $\theta$ is not $1$.
Example: for $k$ successes in $n$ Bernoulli($p$) trials, $L(p \mid x) = p^k (1 - p)^{n - k}$ for $p \in [0, 1]$.
Only ratios $L(\theta_1 \mid x) / L(\theta_2 \mid x)$ matter for inference. These ratios compare how well two parameter values explain the data.

## Explanations

### L1 human

The likelihood answers the question: "If the parameter were $\theta$, how probable would my data be?"
Parameter values with a high likelihood explain the observed data well.
