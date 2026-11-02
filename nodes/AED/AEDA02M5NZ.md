---
tag: AEDA02M5NZ
kind: definition
name: Identifiability
msc: [62A01, 62F99]
defines: 605M5NMFD5
uses: [JZ6R7J36K5, 0PVG1CRAJN]
sources:
  - url: https://en.wikipedia.org/wiki/Identifiability
    locator: Definition
---

## Definition

Let $\mathcal{P} = \set{P_\theta : \theta \in \Theta}$ be a [[statistical model|JZ6R7J36K5]] indexed by a parameter space $\Theta$.
The model is *identifiable* if the map $\theta \mapsto P_\theta$ from $\Theta$ to the set of probability measures is [[injective|0PVG1CRAJN]].
That is, for all $\theta_1, \theta_2 \in \Theta$, if $P_{\theta_1} = P_{\theta_2}$, then $\theta_1 = \theta_2$.

## Remarks

Example: the normal model $P_{(\mu, \sigma^2)} = \mathcal{N}(\mu, \sigma^2)$ with $\mu \in \R$ and $\sigma^2 > 0$ is identifiable, because the mean and the variance of the law recover $\mu$ and $\sigma^2$.
Non-example: let $P_{(a, b)} = \mathcal{N}(a + b, 1)$ with $(a, b) \in \R^2$.
Then $P_{(1, 0)} = P_{(0, 1)}$ while $(1, 0) \ne (0, 1)$, so the model is not identifiable.
A function $\tau(\theta)$ is identifiable when $P_{\theta_1} = P_{\theta_2}$ implies $\tau(\theta_1) = \tau(\theta_2)$; in the non-example, $\tau(a, b) = a + b$ is identifiable.
