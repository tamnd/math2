---
tag: GA46NC0CJZ
kind: statement
role: theorem
name: Yule–Walker equations
msc: [62M10]
uses: [2JC96FMGA1, YCZHYY8VE5, GKY2WSHE26, 0KBFAWYRTE]
about: [2JC96FMGA1]
sources:
  - url: https://en.wikipedia.org/wiki/Autoregressive_model
---

## Statement

Let $(\varepsilon_t)_{t \in \Z}$ be a white noise with variance $\sigma^2 > 0$.
Let $(X_t)_{t \in \Z}$ be a causal [[autoregressive model|2JC96FMGA1]] of order $p$ with mean $0$,
$$X_t = \phi_1 X_{t-1} + \cdots + \phi_p X_{t-p} + \varepsilon_t,$$
so that $X_t = \sum_{j \ge 0} \psi_j \varepsilon_{t-j}$ with $\sum_j \abs{\psi_j} < \infty$.
Let $\gamma(h) = E[X_{t+h} X_t]$ be its autocovariance function.
Then
$$\gamma(h) = \phi_1 \gamma(h-1) + \cdots + \phi_p \gamma(h-p) \quad \text{for } h \ge 1, \qquad \gamma(0) = \phi_1 \gamma(1) + \cdots + \phi_p \gamma(p) + \sigma^2.$$
In matrix form, $\Gamma_p \phi = \gamma_p$ and $\sigma^2 = \gamma(0) - \phi^T \gamma_p$, where $\Gamma_p = [\gamma(i - j)]_{i,j=1}^{p}$, $\phi = (\phi_1, \dots, \phi_p)^T$ and $\gamma_p = (\gamma(1), \dots, \gamma(p))^T$.

## Remarks

Multiply the defining equation by $X_{t-h}$ and take expectations.
For $h \ge 1$, causality makes $X_{t-h}$ a function of $\varepsilon_s$ with $s \le t - h < t$, so $E[\varepsilon_t X_{t-h}] = 0$, which gives the first equations.
For $h = 0$, $E[\varepsilon_t X_t] = E[\varepsilon_t^2] = \sigma^2$, which gives the last one.
The matrix $\Gamma_p$ is a symmetric [[Toeplitz matrix|GKY2WSHE26]], and it is nonsingular because $\gamma(0) > 0$ and $\gamma(h) \to 0$ as $h \to \infty$.
So the autocovariances $\gamma(0), \dots, \gamma(p)$ determine $\phi$ and $\sigma^2$.

Example: for $p = 1$, the equations read $\gamma(1) = \phi_1 \gamma(0)$ and $\gamma(0) = \phi_1 \gamma(1) + \sigma^2$.
Hence $\phi_1 = \rho(1)$ and $\gamma(0) = \sigma^2 / (1 - \phi_1^2)$.

The *Yule–Walker estimator* replaces $\gamma$ by the sample autocovariance $\hat\gamma$ and solves $\hat\Gamma_p \hat\phi = \hat\gamma_p$.
Causality is needed: for the non-causal stationary solution of $X_t = 2 X_{t-1} + \varepsilon_t$, the shock $\varepsilon_t$ is correlated with the past values $X_{t-h}$ and the first equation fails.

## Explanations

### L1 human

In an autoregressive model, each value is a weighted sum of earlier values plus fresh noise.
The Yule–Walker equations say that the correlations of the series obey the same recursion with the same weights.
So once the correlations are known, the weights can be found by solving a small linear system.

### L2 human

The equations give the simplest estimator of the coefficients of an AR($p$) model, computed from the sample [[autocorrelation function|YCZHYY8VE5]].
For a Gaussian causal AR process, this estimator has the same asymptotic distribution as the maximum likelihood estimator.
The Durbin–Levinson algorithm solves the Toeplitz system for $p = 1, 2, 3, \dots$ in turn, and the last coefficient at each order is the partial autocorrelation.
The equations are named after Udny Yule and Gilbert Walker.
