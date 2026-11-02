---
tag: K0KF9KMF5W
kind: definition
name: Autocorrelation function
msc: [62M10, 60G10]
defines: YCZHYY8VE5
uses: [EA3MF4VTEH, DT0QXJE705, 0KBFAWYRTE, 0DNN9B6Q2F]
sources:
  - url: https://en.wikipedia.org/wiki/Autocorrelation
---

## Definition

Let $(X_t)_{t \in \Z}$ be a real weakly [[stationary process|DT0QXJE705]]: $E[X_t^2] < \infty$, the mean $E[X_t] = \mu$ does not depend on $t$, and the [[covariance|0KBFAWYRTE]] $\operatorname{Cov}(X_{t+h}, X_t)$ depends only on $h$.
The *autocovariance function* is $\gamma(h) = \operatorname{Cov}(X_{t+h}, X_t)$ for $h \in \Z$.
If $\gamma(0) > 0$, the *autocorrelation function* is
$$\rho(h) = \frac{\gamma(h)}{\gamma(0)}, \qquad h \in \Z.$$
It is the [[correlation coefficient|0DNN9B6Q2F]] of $X_{t+h}$ and $X_t$.
For observations $x_1, \dots, x_n$ of a [[time series|EA3MF4VTEH]] with mean $\bar x$, the *sample autocovariance* and *sample autocorrelation* at lag $\abs{h} < n$ are
$$\hat\gamma(h) = \frac1n \sum_{t=1}^{n - \abs{h}} (x_{t + \abs{h}} - \bar x)(x_t - \bar x), \qquad \hat\rho(h) = \frac{\hat\gamma(h)}{\hat\gamma(0)}.$$

## Remarks

Every autocorrelation function satisfies $\rho(0) = 1$, $\rho(-h) = \rho(h)$ and $\abs{\rho(h)} \le 1$.
It is nonnegative definite: $\sum_{i,j} a_i a_j \rho(t_i - t_j) \ge 0$ for all real $a_i$ and integers $t_i$, since this sum is $\operatorname{Var}(\sum_i a_i X_{t_i}) / \gamma(0)$.

Example: let $(\varepsilon_t)$ be uncorrelated with mean $0$ and variance $\sigma^2 > 0$, and let $X_t = \varepsilon_t + \varepsilon_{t-1}$.
Then $\gamma(0) = 2\sigma^2$, $\gamma(\pm 1) = \sigma^2$ and $\gamma(h) = 0$ for $\abs{h} \ge 2$, so $\rho(\pm 1) = 1/2$ and $\rho(h) = 0$ for $\abs{h} \ge 2$.

Non-example: for a random walk $S_t = \varepsilon_1 + \cdots + \varepsilon_t$, the variance $t \sigma^2$ depends on $t$, so the process is not weakly stationary and $\rho$ is not defined.

The divisor $n$ in $\hat\gamma$, rather than $n - \abs{h}$, makes the sample autocovariance nonnegative definite.
In signal processing, autocorrelation often means the unnormalized $E[X_{t+h} X_t]$.
