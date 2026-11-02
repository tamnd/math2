---
tag: SKS1JPBW2N
kind: definition
name: Hypoelliptic operator
msc: [35H10]
defines: K9DSR21DQC
uses: [0V33BNKZ9S, XY8GEQSWPR]
sources:
  - url: https://en.wikipedia.org/wiki/Hypoelliptic_operator
---

## Definition

Let $\Omega \subseteq \R^n$ be an open set and let $P = \sum_{\abs{\alpha} \le m} a_\alpha(x) \partial^\alpha$ be a linear differential operator on $\Omega$ whose coefficients $a_\alpha$ are [[smooth functions|0V33BNKZ9S]].
A distribution on an open set $U$ is a continuous linear functional on the space of test functions on $U$.
The operator $P$ is *hypoelliptic* if the following holds for every open set $U \subseteq \Omega$ and every distribution $u$ on $U$.
If $Pu$ is a smooth function on $U$, then $u$ is a smooth function on $U$.

## Remarks

Equivalently, $\operatorname{sing\,supp} u = \operatorname{sing\,supp} Pu$ for every distribution $u$, where the singular support is the complement of the largest open set on which the distribution is smooth.
Example: every [[elliptic operator|XY8GEQSWPR]] with smooth coefficients is hypoelliptic; this is elliptic regularity.
The heat operator $\partial_t - \Delta$ on $\R^{n+1}$ is hypoelliptic but not elliptic.
Non-example: the wave operator $\partial_t^2 - \partial_x^2$ on $\R^2$ is not hypoelliptic.
For the Heaviside function $H$, the distribution $u(x, t) = H(x - t)$ satisfies $\partial_t^2 u - \partial_x^2 u = H''(x - t) - H''(x - t) = 0$, which is smooth, but $u$ is not smooth.
