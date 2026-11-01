---
tag: KS3KDRRJ58
kind: definition
name: Self-similar process
msc: [60G18]
defines: RASDTDEKP7
uses: [0QH5ENKZM1, Y0CN7V3B7E]
sources:
  - url: https://en.wikipedia.org/wiki/Self-similar_process
---

## Definition

Let $(X_t)_{t \ge 0}$ be a real-valued [[stochastic process|0QH5ENKZM1]] and let $H > 0$.
The process is *self-similar with Hurst index $H$* if for every $a > 0$ the processes $(X_{at})_{t \ge 0}$ and $(a^H X_t)_{t \ge 0}$ have the same [[finite-dimensional distributions|Y0CN7V3B7E]].
That is, for all $n \ge 1$ and $t_1, \dots, t_n \ge 0$, the vectors $(X_{a t_1}, \dots, X_{a t_n})$ and $(a^H X_{t_1}, \dots, a^H X_{t_n})$ have the same law.

## Remarks

The [[Wiener process|22735FGJV6]] $W$ is self-similar with $H = 1/2$.
Check: $(W_{at})_{t \ge 0}$ and $(\sqrt{a}\, W_t)_{t \ge 0}$ are both centred Gaussian processes with covariance $a \min(s, t)$, so they have the same finite-dimensional distributions.
Brownian motion with drift, $X_t = W_t + t$, is not self-similar for any $H$.
Indeed $E[X_{at}] = at$ and $E[a^H X_t] = a^H t$ force $H = 1$, while $\operatorname{Var}(X_{at}) = at$ and $\operatorname{Var}(a^H X_t) = a^{2H} t$ force $H = 1/2$.
One often writes $X_{at} \overset{d}{=} a^H X_t$, where equality in law is meant for the whole process.
Taking $t = 0$ gives $X_0 \overset{d}{=} a^H X_0$ for all $a > 0$, which forces $X_0 = 0$ almost surely.
