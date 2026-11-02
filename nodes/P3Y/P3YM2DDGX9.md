---
tag: P3YM2DDGX9
kind: definition
name: Autoregressive conditional heteroskedasticity
msc: [62M10, 91G70, 62P20]
defines: MPN10SB26R
uses: [EA3MF4VTEH, 0VGPX25NXQ, D8VX6XQ3TT, 00MRN0FARV]
sources:
  - url: https://en.wikipedia.org/wiki/Autoregressive_conditional_heteroskedasticity
---

## Definition

Let $q \ge 1$ be an integer.
A real [[time series|EA3MF4VTEH]] $(\varepsilon_t)_{t \in \Z}$ is an *ARCH($q$) process* if it satisfies the following conditions.

1. $\varepsilon_t = \sigma_t z_t$ for all $t$, where $(z_t)_{t \in \Z}$ are [[independent and identically distributed|00MRN0FARV]] random variables with mean $0$ and variance $1$.
2. $\sigma_t^2 = \alpha_0 + \sum_{i=1}^{q} \alpha_i \varepsilon_{t-i}^2$ for all $t$, where $\alpha_0 > 0$ and $\alpha_1, \dots, \alpha_q \ge 0$ are constants and $\sigma_t \ge 0$.
3. $z_t$ is independent of $(\varepsilon_s)_{s < t}$ for all $t$.

Then $\sigma_t^2$ is the [[conditional variance|0VGPX25NXQ]] of $\varepsilon_t$ given the past $(\varepsilon_s)_{s < t}$.

## Remarks

The GARCH($p$, $q$) model replaces clause 2 by $\sigma_t^2 = \alpha_0 + \sum_{i=1}^{q} \alpha_i \varepsilon_{t-i}^2 + \sum_{j=1}^{p} \beta_j \sigma_{t-j}^2$ with $\beta_j \ge 0$.

Example: take $q = 1$, $\alpha_0 = 1$ and $\alpha_1 = 1/2$.
If the process is weakly stationary with variance $v$, then taking expectations in clause 2 gives $v = 1 + v/2$, so $v = 2$.
In general a weakly stationary ARCH($q$) process exists if and only if $\alpha_1 + \cdots + \alpha_q < 1$, and then its variance is $\alpha_0 / (1 - \alpha_1 - \cdots - \alpha_q)$.

Non-example: the rule $\sigma_t^2 = 1 - \frac12 \varepsilon_{t-1}^2$ fails clause 2 because $\alpha_1 < 0$.
It gives a negative "variance" as soon as $\abs{\varepsilon_{t-1}} > \sqrt{2}$.

An ARCH process is uncorrelated in time, but it is not independent: the squares $\varepsilon_t^2$ follow an autoregressive pattern.
