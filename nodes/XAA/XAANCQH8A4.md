---
tag: XAANCQH8A4
kind: definition
name: Proportional hazards model
msc: [62N01, 62N02, 62J12]
defines: N029V3JX60
uses: [Y959NKQ3XW, MY8ZZP84NP, 0VW9E4QXR6, K3AMMSY8DD]
sources:
  - url: https://en.wikipedia.org/wiki/Proportional_hazards_model
---

## Definition

Let $T$ be an event time with values in $[0, \infty)$ and let $x \in \R^p$ be a vector of covariates.
The *Cox proportional hazards model* is the following [[statistical model|K3AMMSY8DD]].
The conditional [[hazard function|Y959NKQ3XW]] of $T$ given $x$ is
$$h(t \mid x) = h_0(t) \, e^{\beta^T x}, \qquad t \ge 0,$$
where $\beta \in \R^p$ is an unknown parameter and the baseline hazard $h_0 \colon [0, \infty) \to [0, \infty)$ is an unknown function.

## Remarks

For two covariate vectors $x$ and $x'$, the hazard ratio $h(t \mid x) / h(t \mid x') = e^{\beta^T (x - x')}$ does not depend on $t$; this is the proportional hazards property.
Equivalently, the survival functions satisfy $S(t \mid x) = S_0(t)^{e^{\beta^T x}}$, where $S_0$ is the baseline survival function.

Given right-[[censored|MY8ZZP84NP]] data $(\tilde t_i, \delta_i, x_i)$ without tied times, $\beta$ is estimated by maximising the partial [[likelihood|0VW9E4QXR6]]
$$L(\beta) = \prod_{i \,:\, \delta_i = 1} \frac{e^{\beta^T x_i}}{\sum_{j \,:\, \tilde t_j \ge \tilde t_i} e^{\beta^T x_j}}.$$

Example: the Weibull model with shape $k > 0$ and hazard $h(t \mid x) = k t^{k-1} \lambda^{-k} e^{\beta^T x}$ is a proportional hazards model with $h_0(t) = k t^{k-1} \lambda^{-k}$.

Non-example: if a treatment has hazard $h_1(t) = 2t$ and the control has $h_0(t) = 1$, the ratio $2t$ changes with time and the curves cross at $t = 1/2$.
No constant $\beta$ satisfies $h_1 = h_0 e^{\beta}$, so these two groups do not follow a proportional hazards model.
