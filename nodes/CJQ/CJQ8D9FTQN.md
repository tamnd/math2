---
tag: CJQ8D9FTQN
kind: statement
role: proposition
name: Bias–variance decomposition
msc: [62F10, 62J05]
uses: [0V4VSCBXP3, 01BD2TFFP4, 007QED3E0Y, 0DCT0QZVQ1, 0E9502NT92]
about: [05NZ1HHQMV]
sources:
  - url: https://en.wikipedia.org/wiki/Bias–variance_tradeoff
---

## Statement

Let $x$ be a fixed point and let $Y = f(x) + \varepsilon$, where $f(x)$ is a real number and $\varepsilon$ is a random variable with $E(\varepsilon) = 0$ and $\operatorname{Var}(\varepsilon) = \sigma^2$.
Let $\hat{f}(x)$ be a random variable with $E(\hat{f}(x)^2) < \infty$ that is [[independent|0E9502NT92]] of $\varepsilon$.
For example, $\hat{f}(x)$ is a prediction built from a training sample independent of the new observation.
Then
$$E\big[(Y - \hat{f}(x))^2\big] = \big(E[\hat{f}(x)] - f(x)\big)^2 + \operatorname{Var}\big(\hat{f}(x)\big) + \sigma^2.$$

## Remarks

Proof: write $Y - \hat{f} = \varepsilon + (f - E\hat{f}) + (E\hat{f} - \hat{f})$.
Expand the square and take [[expectations|0DCT0QZVQ1]]: the three cross terms vanish, because $E\varepsilon = 0$, $E(E\hat{f} - \hat{f}) = 0$, and $\varepsilon$ is independent of $\hat{f}$.
The remaining terms are $\sigma^2$, the squared bias and the [[variance|007QED3E0Y]] of $\hat{f}$.

The case without noise is the decomposition of the [[mean squared error|0V4VSCBXP3]] of an estimator $\hat{\theta}$ of a parameter $\theta$:
$$E\big[(\hat{\theta} - \theta)^2\big] = \operatorname{Bias}(\hat{\theta})^2 + \operatorname{Var}(\hat{\theta}),$$
with the [[bias|01BD2TFFP4]] $\operatorname{Bias}(\hat{\theta}) = E(\hat{\theta}) - \theta$.

Example: for i.i.d. $X_1, \dots, X_n$ with variance $\sigma^2$, the estimator $\hat{\sigma}^2 = \frac{1}{n}\sum_i (X_i - \bar{X})^2$ has bias $-\sigma^2/n$.
For normal data its variance is $2(n-1)\sigma^4/n^2$, so its mean squared error is $(2n - 1)\sigma^4/n^2$, which is smaller than the mean squared error $2\sigma^4/(n-1)$ of the unbiased sample variance.
A small bias can thus buy a larger reduction of variance.

The irreducible term $\sigma^2$ does not depend on $\hat{f}$; no predictor can do better than it on average.

## Explanations

### L1 human

The average squared error of a prediction has three parts.
The bias is how far the prediction is off on average.
The variance is how much the prediction jumps around when the training data change.
The noise is the part of the outcome that nobody can predict.
Simple models tend to have large bias and small variance, flexible models the opposite.

### L2 human

The decomposition is the basis of the bias–variance tradeoff in model selection: adding complexity lowers the bias but raises the variance, and the best expected error lies in between.
Shrinkage methods such as ridge regression accept bias to reduce variance.
In point estimation it explains why an unbiased estimator need not have the smallest mean squared error.
Note that the decomposition holds at each fixed point $x$; averaging over $x$ gives the decomposition of the expected prediction error.
