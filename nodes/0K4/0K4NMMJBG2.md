---
tag: 0K4NMMJBG2
kind: definition
name: Confidence interval
msc: [62F25]
defines: 0S6T9KQNC0
uses: [036756NFD6, 07RXBVTVZB, 0QNRBHWV35, 05RZ4YZG4E]
sources:
  - url: https://en.wikipedia.org/wiki/Confidence_interval
    locator: Definition
---

## Definition

Let $X$ be a sample whose law $P_\theta$ depends on an unknown parameter $\theta \in \Theta$. Let $\tau \colon \Theta \to \mathbb{R}$ be a function and let $\gamma \in (0, 1)$.
A confidence interval for $\tau(\theta)$ with confidence level $\gamma$ is a random interval $[L(X), U(X)]$, where $L \le U$ are [[statistics|036756NFD6]], such that
$$P_\theta\big(L(X) \le \tau(\theta) \le U(X)\big) = \gamma \quad \text{for each } \theta \in \Theta.$$
If only "$\ge \gamma$" holds for each $\theta$, the interval is a conservative confidence interval.

## Remarks

Example: let $X_1, \dots, X_n$ be i.i.d. $\mathcal{N}(\mu, \sigma^2)$ with $\sigma$ known. Then $\bar{X}_n \pm 1.96\, \sigma / \sqrt{n}$ is a confidence interval for $\mu$ with level approximately $0.95$.
If $\sigma$ is unknown, one replaces $\sigma$ with the sample standard deviation and $1.96$ with a quantile of Student's t-distribution with $n - 1$ degrees of freedom.
The probability refers to the random interval, not to $\theta$. After one computes the interval from data, it either contains $\tau(\theta)$ or it does not.
The confidence level is often written as $1 - \alpha$, for example $95\%$ for $\alpha = 0.05$.

## Explanations

### L1 human

A $95\%$ confidence interval comes from a procedure that captures the true value in $95\%$ of repeated experiments.
It does not mean that the true value has a $95\%$ probability to be in one particular computed interval.
