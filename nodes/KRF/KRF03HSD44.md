---
tag: KRF03HSD44
kind: definition
name: Hazard function
msc: [62N05, 62N01, "60E05"]
defines: Y959NKQ3XW
uses: [QTM1HZM53Q, 0ZY9DX8FBF, 0990W5PN13, 0E99F51GVB]
sources:
  - url: https://en.wikipedia.org/wiki/Failure_rate
---

## Definition

Let $T$ be a random variable with values in $[0, \infty)$ that has a [[probability density function|0ZY9DX8FBF]] $f$, and let $S$ be its [[survival function|QTM1HZM53Q]].
The *hazard function* of $T$ is defined for all $t \ge 0$ with $S(t) > 0$ by
$$h(t) = \frac{f(t)}{S(t)}.$$
The *cumulative hazard function* is $H(t) = \int_0^t h(u) \, du$.

## Remarks

At every point $t$ where $f$ is continuous, the hazard is the limit of a [[conditional probability|0990W5PN13]] per unit time:
$$h(t) = \lim_{\Delta \downarrow 0} \frac{P(t \le T < t + \Delta \mid T \ge t)}{\Delta}.$$
Since $h = -S'/S = -(\log S)'$ there, one gets $S(t) = e^{-H(t)}$, so $h$ determines the distribution of $T$.

Example: for the [[exponential distribution|0E99F51GVB]] with rate $\lambda$, $f(t) = \lambda e^{-\lambda t}$ and $S(t) = e^{-\lambda t}$, so $h(t) = \lambda$ is constant and $H(t) = \lambda t$.
For the Weibull distribution with shape $k > 0$ and scale $\lambda > 0$, $S(t) = e^{-(t/\lambda)^k}$ and $h(t) = (k/\lambda)(t/\lambda)^{k-1}$, which increases when $k > 1$ and decreases when $k < 1$.

Non-example: if $T$ takes only the values $1$ and $2$, each with probability $1/2$, then $T$ has no density and the formula does not apply.
For discrete times one uses instead the discrete hazard $P(T = t \mid T \ge t)$, here $1/2$ at $t = 1$ and $1$ at $t = 2$.
