---
tag: MM017WE5FS
kind: definition
name: Moving-average model
msc: [62M10, 91B84]
defines: PEB9DN0AHA
uses: [EA3MF4VTEH, YCZHYY8VE5, 2JC96FMGA1, 019MA1VTR2]
sources:
  - url: https://en.wikipedia.org/wiki/Moving-average_model
---

## Definition

Let $(\varepsilon_t)_{t \in \Z}$ be a white noise with variance $\sigma^2 > 0$: the $\varepsilon_t$ have mean $0$, variance $\sigma^2$ and are pairwise uncorrelated.
Let $q \ge 1$, and let $\mu, \theta_1, \dots, \theta_q \in \R$ with $\theta_q \ne 0$.
A *moving-average model of order $q$*, or MA($q$), is the [[time series|EA3MF4VTEH]] model
$$X_t = \mu + \varepsilon_t + \theta_1 \varepsilon_{t-1} + \cdots + \theta_q \varepsilon_{t-q}, \qquad t \in \Z.$$
Its *moving-average polynomial* is $\theta(z) = 1 + \theta_1 z + \cdots + \theta_q z^q$.

## Remarks

Every MA($q$) process is weakly stationary with mean $\mu$.
With $\theta_0 = 1$, its autocovariance is $\gamma(h) = \sigma^2 \sum_{j=0}^{q - \abs{h}} \theta_j \theta_{j + \abs{h}}$ for $\abs{h} \le q$ and $\gamma(h) = 0$ for $\abs{h} > q$.
So its [[autocorrelation function|YCZHYY8VE5]] vanishes beyond lag $q$.
The model is *invertible* when $\theta$ has no [[root|019MA1VTR2]] in the closed unit disk.
Then $\varepsilon_t$ is a convergent linear combination of $X_t, X_{t-1}, \dots$, and the process is an [[autoregressive model|2JC96FMGA1]] of infinite order.

Example: for MA($1$), $X_t = \varepsilon_t + \theta \varepsilon_{t-1}$ has $\gamma(0) = \sigma^2 (1 + \theta^2)$, $\gamma(\pm 1) = \theta \sigma^2$ and $\gamma(h) = 0$ otherwise.
Hence $\rho(1) = \theta / (1 + \theta^2)$, which always lies in $[-1/2, 1/2]$.

Non-example: the process $X_t = \sum_{j \ge 0} 0.5^j \varepsilon_{t-j}$ is not an MA($q$) for any finite $q$, because its autocorrelation $0.5^{\abs{h}}$ is nonzero at every lag.

The name has nothing to do with the moving average used to smooth data, although both are weighted sums over a window.
