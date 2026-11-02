---
tag: 5JQRYAKHSB
kind: definition
name: Accelerated failure time model
msc: [62N01, 62N05, 62N02]
defines: JP1QV1KQ0P
uses: [QTM1HZM53Q, Y959NKQ3XW, K3AMMSY8DD]
sources:
  - url: https://en.wikipedia.org/wiki/Accelerated_failure_time_model
---

## Definition

Let $T$ be an event time with values in $(0, \infty)$ and let $x \in \R^p$ be a vector of covariates.
An *accelerated failure time model* is the following [[statistical model|K3AMMSY8DD]].
The conditional [[survival function|QTM1HZM53Q]] of $T$ given $x$ is
$$S(t \mid x) = S_0\!\left(t \, e^{-\beta^T x}\right), \qquad t \ge 0,$$
where $\beta \in \R^p$ is a parameter and $S_0$ is a baseline survival function.

## Remarks

Equivalently, $T = e^{\beta^T x} T_0$, where $T_0$ has survival function $S_0$, so that $\log T = \beta^T x + \log T_0$.
Parametric versions fix the law of $\log T_0$, for example normal (log-normal model), logistic (log-logistic model) or extreme value (Weibull model).
If $S_0$ has [[hazard function|Y959NKQ3XW]] $h_0$, then $h(t \mid x) = e^{-\beta^T x} h_0(t e^{-\beta^T x})$.

Example: if $T_0$ is exponential with rate $1$, then $S(t \mid x) = \exp(-t e^{-\beta^T x})$, so $T$ given $x$ is exponential with rate $e^{-\beta^T x}$.
Its median $e^{\beta^T x} \log 2$ is the baseline median times $e^{\beta^T x}$, as the model requires.

Non-example: the family $S(t \mid x) = \exp(-t^{k(x)})$, with a shape $k(x) > 0$ that varies with $x$, is not an accelerated failure time model.
If two members with shapes $k_1 \ne k_2$ were related by a change of time scale, then $\exp(-t^{k_2}) = \exp(-(ct)^{k_1})$ for all $t > 0$ and some $c > 0$.
This is impossible, since $t^{k_2} / t^{k_1}$ is not constant in $t$.
