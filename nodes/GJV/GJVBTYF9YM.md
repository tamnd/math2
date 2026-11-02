---
tag: GJVBTYF9YM
kind: definition
name: Cointegration
msc: [62M10, 91B84, 62P20]
defines: V1S1223G5E
uses: [KTDVZP4DF2, DT0QXJE705, 0V8F3E48E6, 04VZE3FZXF, 26E0HYRDS8]
sources:
  - url: https://en.wikipedia.org/wiki/Cointegration
---

## Definition

A real time series is *integrated of order $1$*, written I($1$), if it is not weakly [[stationary|DT0QXJE705]] but its first difference $\Delta x_t = x_t - x_{t-1}$ is.
An example is an [[ARIMA($p$, $1$, $q$) process|KTDVZP4DF2]] whose moving-average polynomial has no root at $1$, such as a random walk.
Let $x_t = (x_{1,t}, \dots, x_{k,t})^T$, with $k \ge 2$, be a vector time series whose components are all I($1$).
The series $x_t$ is *cointegrated* if there is a vector $\beta \in \R^k$, $\beta \ne 0$, such that the [[linear combination|0V8F3E48E6]] $\beta^T x_t$ is weakly stationary.
Such a $\beta$ is a *cointegrating vector*.

## Remarks

The cointegrating vectors, together with $0$, form a linear subspace of $\R^k$; its dimension $r$, with $0 \le r \le k - 1$, is the cointegrating rank.
More generally, components that are I($d$) are cointegrated of order ($d$, $b$) when some nonzero combination is I($d - b$) with $b > 0$.

Example: let $w_t$ be a [[random walk|04VZE3FZXF]] and $e_t$ a white noise independent of it, and set $x_{1,t} = w_t$ and $x_{2,t} = 2 w_t + e_t$.
Both components are I($1$), and $\beta = (2, -1)^T$ gives $\beta^T x_t = -e_t$, which is stationary, so the pair is cointegrated.

Non-example: two independent random walks $w_t$ and $v_t$ with step variance $\sigma^2 > 0$ are not cointegrated.
For $\beta = (a, b)^T \ne 0$, the combination $a w_t + b v_t$ is again a random walk with step variance $(a^2 + b^2) \sigma^2 > 0$, which is not stationary.

In the Engle–Granger method, $\beta$ is estimated by regressing one component on the others.
Then a [[Dickey–Fuller type test|26E0HYRDS8]] is applied to the residuals, with critical values adjusted for the estimation step.
The Granger representation theorem links cointegration with error-correction models.
