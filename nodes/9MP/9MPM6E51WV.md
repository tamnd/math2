---
tag: 9MPM6E51WV
kind: definition
name: Autoregressive integrated moving average
msc: [62M10, 91B84]
defines: KTDVZP4DF2
uses: [B1HNX0YT0Z, EA3MF4VTEH, 04VZE3FZXF]
sources:
  - url: https://en.wikipedia.org/wiki/Autoregressive_integrated_moving_average
---

## Definition

Let $B$ be the backshift operator, $B X_t = X_{t-1}$, and let $\nabla = 1 - B$ be the difference operator, so $\nabla X_t = X_t - X_{t-1}$.
Let $p, d, q \ge 0$ be integers.
A [[time series|EA3MF4VTEH]] $(X_t)$ is an *ARIMA($p$, $d$, $q$) process* if the differenced series $Y_t = \nabla^d X_t$ is a causal [[ARMA($p$, $q$) process|B1HNX0YT0Z]].
Equivalently, $\phi(B) (1 - B)^d X_t = c + \theta(B) \varepsilon_t$ for a white noise $(\varepsilon_t)$, a constant $c$, and polynomials $\phi$ of degree $p$ and $\theta$ of degree $q$.
Here $\phi(0) = \theta(0) = 1$, and $\phi$ has no root in the closed unit disk.

## Remarks

For $d = 0$ this is a causal ARMA($p$, $q$) process.
For $d \ge 1$ the process is not stationary in general.
It is determined by $Y$ only up to $d$ starting values, since $\nabla^d$ kills polynomials in $t$ of degree less than $d$.
A series whose $d$-th difference is stationary but whose $(d-1)$-th difference is not is called integrated of order $d$, written I($d$).

Example: the [[random walk|04VZE3FZXF]] $X_t = X_{t-1} + \varepsilon_t$ is ARIMA($0$, $1$, $0$), because $\nabla X_t = \varepsilon_t$ is a white noise, which is ARMA($0$, $0$).
The model $X_t = X_{t-1} + 0.5 (X_{t-1} - X_{t-2}) + \varepsilon_t$ is ARIMA($1$, $1$, $0$), since $\nabla X_t = 0.5 \nabla X_{t-1} + \varepsilon_t$.

Non-example: the explosive series with $X_0 = 0$ and $X_t = 1.5 X_{t-1} + \varepsilon_t$ for $t \ge 1$ is not ARIMA for any $d$.
Its autoregressive polynomial $1 - 1.5 z$ has the root $2/3$ inside the unit disk, so the variance of $X_t$ grows geometrically.
Differencing does not remove this explosive root, because $\nabla^d$ only contributes the root $1$, so $\nabla^d X_t$ is never stationary.

Seasonal ARIMA models also apply seasonal differences $1 - B^s$ for a period $s$, such as $s = 12$ for monthly data.
