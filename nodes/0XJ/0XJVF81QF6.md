---
tag: 0XJVF81QF6
kind: definition
name: Consistent estimator
msc: [62F12]
defines: 0AS800VAYX
uses: [0TTNRP5PFQ, 0EFDDXTVD6]
sources:
  - url: https://en.wikipedia.org/wiki/Consistent_estimator
    locator: Definition
---

## Definition

For each $n \ge 1$, let $\hat{\theta}_n$ be an [[estimator|0TTNRP5PFQ]] of a real parameter $\theta$ that uses the first $n$ observations of a sample.
The sequence $(\hat{\theta}_n)$ is consistent if, for each $\theta \in \Theta$, $\hat{\theta}_n \to \theta$ [[in probability|0EFDDXTVD6]] when $\theta$ is the true parameter:
$$\lim_{n \to \infty} P_\theta\left(|\hat{\theta}_n - \theta| > \varepsilon\right) = 0 \quad \text{for each } \varepsilon > 0.$$

## Remarks

If the convergence is almost sure, the sequence is strongly consistent.
By the weak law of large numbers, the sample mean of an i.i.d. sample is a consistent estimator of the mean.
If the mean squared error of $\hat{\theta}_n$ tends to $0$, then $(\hat{\theta}_n)$ is consistent. This follows from Markov's inequality.
Consistent estimators can be biased, and unbiased estimators can fail to be consistent. For example, the estimator $X_1$ of the mean uses only one observation: it is unbiased but not consistent, unless $X_1$ is almost surely constant.

## Explanations

### L1 human

A consistent estimator gets closer and closer to the truth when you collect more and more data.
This is a minimal requirement for a reasonable estimator.
