---
tag: FY0YG17JBE
kind: definition
name: Autoregressive model
msc: [62M10, 91B84]
defines: 2JC96FMGA1
uses: [EA3MF4VTEH, DT0QXJE705, 019MA1VTR2, 04VZE3FZXF]
sources:
  - url: https://en.wikipedia.org/wiki/Autoregressive_model
---

## Definition

A *white noise* with variance $\sigma^2 > 0$ is a sequence $(\varepsilon_t)_{t \in \Z}$ of real random variables with $E[\varepsilon_t] = 0$, $E[\varepsilon_t^2] = \sigma^2$ and $E[\varepsilon_s \varepsilon_t] = 0$ for $s \ne t$.
Let $p \ge 1$, let $c, \phi_1, \dots, \phi_p \in \R$ with $\phi_p \ne 0$, and let $(\varepsilon_t)$ be a white noise.
An *autoregressive model of order $p$*, or AR($p$), is a weakly [[stationary process|DT0QXJE705]] $(X_t)_{t \in \Z}$ that satisfies
$$X_t = c + \phi_1 X_{t-1} + \cdots + \phi_p X_{t-p} + \varepsilon_t \qquad \text{for all } t \in \Z.$$
Its *autoregressive polynomial* is $\phi(z) = 1 - \phi_1 z - \cdots - \phi_p z^p$.

## Remarks

If $\phi(z) \ne 0$ for all complex $z$ with $\abs{z} = 1$, the equation has exactly one weakly stationary solution.
If moreover $\phi$ has no [[root|019MA1VTR2]] in the closed unit disk $\abs{z} \le 1$, this solution is causal: $X_t = \mu + \sum_{j \ge 0} \psi_j \varepsilon_{t-j}$ with $\sum_j \abs{\psi_j} < \infty$ and $\mu = c / (1 - \phi_1 - \cdots - \phi_p)$.
Many texts include causality in the definition.

Example: for $p = 1$, $c = 0$ and $\abs{\phi_1} < 1$, the process $X_t = \sum_{j \ge 0} \phi_1^j \varepsilon_{t-j}$ converges in mean square and satisfies $X_t = \phi_1 X_{t-1} + \varepsilon_t$.
Its variance is $\sigma^2 / (1 - \phi_1^2)$ and its autocorrelation at lag $h$ is $\phi_1^{\abs{h}}$.

Non-example: for $\phi_1 = 1$ and $c = 0$, the equation $X_t = X_{t-1} + \varepsilon_t$ defines a [[random walk|04VZE3FZXF]], and it has no weakly stationary solution.
Indeed $X_t - X_{t-n} = \varepsilon_{t-n+1} + \cdots + \varepsilon_t$ has variance $n \sigma^2$, which is unbounded in $n$, while for a stationary solution it is at most $4 \operatorname{Var}(X_0)$.
Here $\phi(z) = 1 - z$ has the root $z = 1$ on the unit circle.
