---
tag: J1EZZN14WC
kind: definition
name: Jackknife
msc: [62G09, 62F40]
defines: WQ8TQKDKYT
uses: [036756NFD6, 01BD2TFFP4, 007QED3E0Y, 0JN9P4A944]
sources:
  - url: https://en.wikipedia.org/wiki/Jackknife_resampling
---

## Definition

Let $x_1, \dots, x_n$ be data with $n \ge 2$, and let $\hat\theta = T_n(x_1, \dots, x_n)$ be a [[statistic|036756NFD6]] defined for every sample size.
For $i = 1, \dots, n$, let $\hat\theta_{(i)} = T_{n-1}(x_1, \dots, x_{i-1}, x_{i+1}, \dots, x_n)$ be the leave-one-out value, and let $\hat\theta_{(\cdot)} = \frac{1}{n} \sum_{i=1}^{n} \hat\theta_{(i)}$.
The *jackknife* gives:

1. the bias estimate $\widehat{\mathrm{bias}} = (n - 1)\big(\hat\theta_{(\cdot)} - \hat\theta\big)$;
2. the bias-corrected estimate $\hat\theta_{\mathrm{jack}} = \hat\theta - \widehat{\mathrm{bias}} = n\hat\theta - (n - 1)\hat\theta_{(\cdot)}$;
3. the variance estimate $\widehat{\operatorname{Var}}_{\mathrm{jack}} = \frac{n - 1}{n} \sum_{i=1}^{n} \big(\hat\theta_{(i)} - \hat\theta_{(\cdot)}\big)^2$.

## Remarks

If the [[bias|01BD2TFFP4]] of $\hat\theta$ has the form $a/n + O(1/n^2)$, the bias of $\hat\theta_{\mathrm{jack}}$ is $O(1/n^2)$.

Example: for the sample mean $\hat\theta = \bar x$, one has $\hat\theta_{(i)} = (n \bar x - x_i)/(n - 1)$, so $\hat\theta_{(i)} - \hat\theta_{(\cdot)} = (\bar x - x_i)/(n-1)$.
Then $\widehat{\operatorname{Var}}_{\mathrm{jack}} = \frac{1}{n(n-1)} \sum_i (x_i - \bar x)^2 = s^2/n$, the usual estimate of the [[variance|007QED3E0Y]] of $\bar x$, with $s^2$ the [[sample variance|0JN9P4A944]].
For the plug-in variance $\hat\theta = \frac1n \sum_i (x_i - \bar x)^2$, the bias-corrected estimate is exactly $s^2 = \frac{1}{n-1}\sum_i (x_i - \bar x)^2$.

Non-example: for the sample median the variance estimate in clause 3 is not consistent.
The median is not a smooth function of the data, and its leave-one-out values take only two or three distinct values.
