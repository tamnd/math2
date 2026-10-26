---
tag: 0QNRBHWV35
kind: definition
name: Sample mean
msc: [62F10]
defines: 03Y6AQ2S0J
uses: [036756NFD6, 0AJN7WHBJZ, 0P7PTC8DDE, 0V0778DCW9]
sources:
  - url: https://en.wikipedia.org/wiki/Sample_mean_and_covariance
    locator: Definition of the sample mean
---

## Definition

Let $X_1, \dots, X_n$ be real random variables, for example an [[i.i.d.|0AJN7WHBJZ]] sample.
The sample mean is the [[statistic|036756NFD6]]
$$\bar{X}_n = \frac{1}{n} \sum_{i=1}^{n} X_i.$$
For observed values $x_1, \dots, x_n$, the sample mean is the number $\bar{x} = (x_1 + \dots + x_n)/n$.

## Remarks

If the $X_i$ are i.i.d. with mean $\mu$, then $E[\bar{X}_n] = \mu$ by [[linearity of expectation|0P7PTC8DDE]]. So $\bar{X}_n$ is an unbiased estimator of $\mu$.
If also $\operatorname{Var}(X_i) = \sigma^2 < \infty$, then $\operatorname{Var}(\bar{X}_n) = \sigma^2 / n$.
For i.i.d. $\mathcal{N}(\mu, \sigma^2)$ variables, $\bar{X}_n \sim \mathcal{N}(\mu, \sigma^2/n)$.
By the law of large numbers, $\bar{X}_n \to \mu$ almost surely.

## Explanations

### L1 human

The sample mean is the ordinary average of the data.
For the measurements $4$, $7$ and $10$, the sample mean is $21/3 = 7$.
