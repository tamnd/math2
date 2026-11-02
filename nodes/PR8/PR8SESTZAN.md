---
tag: PR8SESTZAN
kind: definition
name: U-statistic
msc: [62G05, 62G20]
defines: NTVQB1DC56
uses: [036756NFD6, 0AJN7WHBJZ, 0DCT0QZVQ1]
sources:
  - url: https://en.wikipedia.org/wiki/U-statistic
---

## Definition

Let $X_1, \dots, X_n$ be [[i.i.d.|0AJN7WHBJZ]] random variables with values in a measurable space $E$.
Let $r \le n$ be a positive integer, and let $h \colon E^r \to \R$ be a measurable function that is symmetric in its $r$ arguments, the *kernel*.
The *U-statistic* with kernel $h$ is
$$U_n = \binom{n}{r}^{-1} \sum_{1 \le i_1 < i_2 < \dots < i_r \le n} h(X_{i_1}, \dots, X_{i_r}).$$
The integer $r$ is the degree of the kernel.

## Remarks

If $E\abs{h(X_1, \dots, X_r)} < \infty$, then $U_n$ is an unbiased estimator of $\theta = E[h(X_1, \dots, X_r)]$, by linearity of [[expectation|0DCT0QZVQ1]].
Let $h_1(x) = E[h(x, X_2, \dots, X_r)]$ and $\zeta_1 = \operatorname{Var}(h_1(X_1))$.
If $E[h^2] < \infty$, Hoeffding's theorem gives $\sqrt{n}(U_n - \theta) \to N(0, r^2 \zeta_1)$ in distribution.

Example: $r = 2$ and $h(x, y) = (x - y)^2 / 2$.
The identity $\sum_{i < j} (x_i - x_j)^2 = n \sum_i (x_i - \bar x)^2$ gives $U_n = \frac{2}{n(n-1)} \cdot \frac{n}{2} \sum_i (X_i - \bar X)^2 = \frac{1}{n-1} \sum_i (X_i - \bar X)^2$, the sample variance.
Here $\theta = \operatorname{Var}(X_1)$.
With $r = 1$ and $h(x) = x$, $U_n$ is the sample mean.

Non-example: the average $\frac{1}{n^2} \sum_{i, j} h(X_i, X_j)$ over all ordered pairs, including $i = j$, is a V-statistic, not a U-statistic.
For $h(x, y) = (x - y)^2/2$ it equals $\frac{1}{n} \sum_i (X_i - \bar X)^2$, which is biased.

Two-sample U-statistics average a kernel over one subset from each of two samples; the [[Mann–Whitney statistic|CKF9KDXBP7]] is one.
