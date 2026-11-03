---
tag: T97B6NBPA8
kind: problem
name: Filtering problem
msc: [60G35, "93E11", 62M20]
uses: [B219G9SHJA, 22735FGJV6, 0TTDGTEFMN, HNK1Y62G7V]
about: [0TTDGTEFMN, 0QH5ENKZM1]
sources:
  - url: https://en.wikipedia.org/wiki/Filtering_problem_(stochastic_processes)
same_as:
  wikidata: Q5449244
  wikipedia: Filtering problem (stochastic processes)
history:
  posed_by: "Andrey Kolmogorov and Norbert Wiener"
  first_stated: "1941"
  notes: "Kolmogorov in 1941 and Wiener in a 1942 report independently solved the linear stationary case, the earliest formulation of the problem. The nonlinear problem was formulated by Ruslan Stratonovich around 1959 and by Harold Kushner in the 1960s."
---

## Problem

Let $(\Omega, \mathcal{F}, \mathbb{P})$ be a probability space.
Let $W$ and $V$ be independent standard [[Wiener processes|22735FGJV6]], and let $X_0$ be a random vector in $\R^n$ independent of them.
Let $b$, $\sigma$, $h$ be functions regular enough for the equations below to have unique strong solutions.
The *signal* $X_t \in \R^n$ and the *observation* $Y_t \in \R^d$, $t \ge 0$, solve the [[stochastic differential equations|B219G9SHJA]]
$$dX_t = b(X_t)\, dt + \sigma(X_t)\, dW_t, \qquad dY_t = h(X_t)\, dt + dV_t, \qquad Y_0 = 0.$$
Let $\mathcal{Y}_t = \sigma(Y_s : 0 \le s \le t)$ be the [[filtration|HNK1Y62G7V]] of the observations.
The *filtering problem* asks for the [[conditional expectations|0TTDGTEFMN]]
$$\pi_t(\varphi) = \mathbb{E}\big[\varphi(X_t) \mid \mathcal{Y}_t\big]$$
for all $t \ge 0$ and all bounded measurable $\varphi \colon \R^n \to \R$.
So it asks for the conditional distribution of the current signal given the past observations, and for a description of its evolution in $t$.

## Remarks

The conditional expectation $\pi_t(\varphi)$ is the estimate of $\varphi(X_t)$ with the least mean square error among all $\mathcal{Y}_t$-measurable estimates with finite second moment.
For linear $b$ and $h$, constant $\sigma$ and Gaussian $X_0$, the conditional distribution is Gaussian, and its mean and covariance are given by the [[Kalman–Bucy filter|P9ECW9MXYX]].
In general, the unnormalized conditional distribution satisfies the [[Zakai equation|FQ8TVSR74H]], a linear stochastic partial differential equation, and $\pi_t$ satisfies the nonlinear [[Kushner equation|FQD9YT0DRK]].
These are infinite-dimensional in general, and finite-dimensional filters exist only in special cases, so numerical methods such as the [[particle filter|BZK7HQDMT0]] are used.
The related problems of prediction and smoothing ask for $\mathbb{E}[\varphi(X_s) \mid \mathcal{Y}_t]$ with $s > t$ and $s < t$.

## Explanations

### L1 human

A hidden quantity moves randomly, and one only sees a noisy measurement of it.
The filtering problem asks for the best guess of the hidden quantity now, using all measurements up to now.
More than a single guess, it asks for the full probability distribution of where the hidden quantity might be.
GPS navigation, weather forecasting and tracking of moving objects all solve versions of this problem.
