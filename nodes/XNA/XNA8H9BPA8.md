---
tag: XNA8H9BPA8
kind: definition
name: Admissible decision rule
msc: [62C15]
defines: DSTF6X8DRJ
uses: [N26TSVRH2S, CPFSBBHXT5, 05AQE0QR0D]
sources:
  - url: https://en.wikipedia.org/wiki/Admissible_decision_rule
---

## Definition

Let $\set{P_\theta : \theta \in \Theta}$ be a statistical model with a loss function, and let $R(\theta, \delta)$ be the [[risk function|N26TSVRH2S]] of a decision rule $\delta$.
A rule $\delta'$ *dominates* a rule $\delta$ if both conditions hold:

1. $R(\theta, \delta') \le R(\theta, \delta)$ for every $\theta \in \Theta$;
2. $R(\theta_0, \delta') < R(\theta_0, \delta)$ for some $\theta_0 \in \Theta$.

A rule $\delta$ is *admissible* if no rule dominates it, and *inadmissible* otherwise.

## Remarks

Admissibility depends on the [[decision problem|CPFSBBHXT5]]: on the model, on the loss and on the class of rules allowed.

Example: let $X$ be [[normal|05AQE0QR0D]] with mean $\theta \in \R$ and variance $1$, with squared error loss, and let $\delta \equiv \theta_0$ be a constant.
Its risk is $(\theta - \theta_0)^2$, which is $0$ at $\theta_0$.
A rule $\delta'$ with $R(\theta_0, \delta') \le 0$ must equal $\theta_0$ almost surely under $P_{\theta_0}$.
All $P_\theta$ have the same null sets, so $\delta' = \theta_0$ almost surely for every $\theta$, and $\delta'$ has the same risk as $\delta$.
So nothing dominates $\delta$, and it is admissible.

Non-example: in the same problem, $\delta(X) = 2X$ has risk $E_\theta[(2X - \theta)^2] = 4 + \theta^2$.
The rule $X$ has risk $1 < 4 + \theta^2$ for every $\theta$, so it dominates $2X$, which is inadmissible.
