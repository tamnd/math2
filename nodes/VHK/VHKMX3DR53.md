---
tag: VHKMX3DR53
kind: definition
name: Shrinkage estimator
msc: [62J07, 62F10]
defines: GPBSS1V3SS
uses: [0SSS6ERQ0S, 0Q5CG2NEQ8, 05AQE0QR0D, 0KJ7ZS8AJA]
sources:
  - url: https://en.wikipedia.org/wiki/Shrinkage_(statistics)
---

## Definition

Let $X$ be an observation from a statistical model with parameter $\theta \in \R^p$.
Let $\delta_0(X)$ be an [[estimator|0SSS6ERQ0S]] of $\theta$ and let $\nu \in \R^p$ be a fixed target.
Let $w(X)$ be a [[statistic|0Q5CG2NEQ8]] with values in $[0, 1]$.
The estimator
$$\delta(X) = \nu + w(X) \big( \delta_0(X) - \nu \big)$$
is a *shrinkage estimator* of $\theta$, obtained by shrinking $\delta_0$ toward $\nu$.

## Remarks

The weight $w$ may be a constant or may depend on the data.
The term is also used more broadly for any estimator that pulls a basic estimate toward a target, for example by a penalty in a regression.
The plain James–Stein estimator has a weight that can be negative; its positive-part version fits the definition above.

Example: let $X$ be [[normal|05AQE0QR0D]] with mean $\theta$ and known variance $\sigma^2$, and give $\theta$ the normal prior with mean $0$ and variance $\tau^2$.
The [[posterior|0KJ7ZS8AJA]] mean is $\frac{\tau^2}{\tau^2 + \sigma^2} X$.
This is a shrinkage estimator with $\delta_0 = X$, $\nu = 0$ and constant weight $w = \tau^2/(\tau^2 + \sigma^2) \in (0, 1)$.

Non-example: $\delta(X) = 2X$ in the same model.
It has the form above with $\nu = 0$ and $w = 2$, which is not in $[0, 1]$, so it pushes the estimate away from the target rather than toward it.
