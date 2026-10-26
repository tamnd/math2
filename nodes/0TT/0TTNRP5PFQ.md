---
tag: 0TTNRP5PFQ
kind: definition
name: Estimator
msc: [62F10]
defines: 0SSS6ERQ0S
uses: [036756NFD6, 0AJN7WHBJZ]
sources:
  - url: https://en.wikipedia.org/wiki/Estimator
    locator: Definition
---

## Definition

Let $\Theta$ be a set of parameters, and for each $\theta \in \Theta$ let $P_\theta$ be a probability distribution. Let $X_1, \dots, X_n$ be a sample whose joint law is determined by an unknown $\theta \in \Theta$. Let $\tau \colon \Theta \to \mathbb{R}^k$ be a function.
An estimator of $\tau(\theta)$ is a [[statistic|036756NFD6]] $\hat{\tau} = g(X_1, \dots, X_n)$ with values in $\mathbb{R}^k$, where $g$ does not depend on $\theta$.
The value of $\hat{\tau}$ for observed data is an estimate of $\tau(\theta)$.

## Remarks

The definition does not ask that $\hat{\tau}$ is close to $\tau(\theta)$. One measures the quality of an estimator with its [[bias|01BD2TFFP4]], its variance and its [[mean squared error|0V4VSCBXP3]].
For an i.i.d. sample, the sample mean is an estimator of the mean, and the sample variance is an estimator of the variance.
One often writes $\hat{\theta}$ for an estimator of $\theta$ itself.

## Explanations

### L1 human

An estimator is a recipe that turns data into a guess of an unknown quantity.
For example, the fraction of "yes" answers in a poll is an estimator of the fraction of "yes" voters in the whole population.
