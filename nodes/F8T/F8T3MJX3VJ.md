---
tag: F8T3MJX3VJ
kind: definition
name: Autoregressive–moving-average model
msc: [62M10, 91B84]
defines: B1HNX0YT0Z
uses: [2JC96FMGA1, PEB9DN0AHA, DT0QXJE705, 019MA1VTR2]
sources:
  - url: https://en.wikipedia.org/wiki/Autoregressive_moving-average_model
---

## Definition

Let $(\varepsilon_t)_{t \in \Z}$ be a white noise with variance $\sigma^2 > 0$.
Let $p, q \ge 0$, and let $\phi(z) = 1 - \phi_1 z - \cdots - \phi_p z^p$ and $\theta(z) = 1 + \theta_1 z + \cdots + \theta_q z^q$ be real polynomials with no common [[root|019MA1VTR2]].
An *ARMA($p$, $q$) process* is a weakly [[stationary process|DT0QXJE705]] $(X_t)_{t \in \Z}$ with mean $\mu$ such that
$$X_t - \mu - \sum_{i=1}^{p} \phi_i (X_{t-i} - \mu) = \varepsilon_t + \sum_{j=1}^{q} \theta_j \varepsilon_{t-j} \qquad \text{for all } t \in \Z.$$
With the backshift operator $B X_t = X_{t-1}$, this reads $\phi(B)(X_t - \mu) = \theta(B) \varepsilon_t$.

## Remarks

The case $q = 0$ is the [[autoregressive model|2JC96FMGA1]] and the case $p = 0$ is the [[moving-average model|PEB9DN0AHA]].
A stationary solution exists, and is unique, exactly when $\phi(z) \ne 0$ for $\abs{z} = 1$.
It is causal, a function of present and past shocks only, when $\phi$ has no root with $\abs{z} \le 1$, and invertible when $\theta$ has no root with $\abs{z} \le 1$.
The condition of no common roots excludes redundant parameters.

Example: $X_t = 0.5 X_{t-1} + \varepsilon_t + 0.3 \varepsilon_{t-1}$ has $\phi(z) = 1 - 0.5 z$ with root $2$ and $\theta(z) = 1 + 0.3 z$ with root $-10/3$.
Both roots lie outside the unit disk and they differ, so this is a causal and invertible ARMA($1$, $1$) process.

Non-example: $X_t - 0.5 X_{t-1} = \varepsilon_t - 0.5 \varepsilon_{t-1}$ fails the condition on common roots, since both polynomials equal $1 - 0.5 z$.
Its stationary solution is just $X_t = \varepsilon_t$, a white noise, so the two parameters are not identifiable.
