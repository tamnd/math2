---
tag: 0V4VSCBXP3
kind: definition
name: Mean squared error
msc: [62F10]
defines: 05NZ1HHQMV
uses: [0TTNRP5PFQ, 01BD2TFFP4, 007QED3E0Y, 0DCT0QZVQ1]
sources:
  - url: https://en.wikipedia.org/wiki/Mean_squared_error
    locator: Estimator
---

## Definition

Let $\hat{\theta}$ be an [[estimator|0TTNRP5PFQ]] of a real parameter $\theta$, with $E_\theta[\hat{\theta}^2] < \infty$, where $E_\theta$ is the expectation when $\theta$ is the true parameter.
The mean squared error of $\hat{\theta}$ at $\theta$ is
$$\operatorname{MSE}_\theta(\hat{\theta}) = E_\theta\left[(\hat{\theta} - \theta)^2\right].$$

## Remarks

It decomposes as $\operatorname{MSE}_\theta(\hat{\theta}) = \operatorname{Var}_\theta(\hat{\theta}) + \operatorname{Bias}_\theta(\hat{\theta})^2$, with the [[bias|01BD2TFFP4]] $\operatorname{Bias}_\theta(\hat{\theta}) = E_\theta[\hat{\theta}] - \theta$.
For an unbiased estimator, the mean squared error is the [[variance|007QED3E0Y]].
For the sample mean of $n$ i.i.d. variables with variance $\sigma^2$, the mean squared error is $\sigma^2/n$.
For $n$ predictions $\hat{y}_i$ of observed values $y_i$, one also calls $\frac{1}{n}\sum_i (y_i - \hat{y}_i)^2$ the mean squared error.

## Explanations

### L1 human

The mean squared error measures how far, on average, an estimator is from the truth.
It is large if the estimator spreads widely, or if it is systematically off, or both.
