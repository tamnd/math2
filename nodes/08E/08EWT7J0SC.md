---
tag: 08EWT7J0SC
kind: definition
name: Complete metric space
aliases: [complete-space]
msc: ["54E50"]
defines: 0BY52JW6NK
uses: [063W5JMY85, 0MCK8K2D7Z, 06JYPJ4WHH]
sources:
  - url: https://en.wikipedia.org/wiki/Complete_metric_space
    locator: Definition
---

## Definition

A [[metric space|063W5JMY85]] $(X, d)$ is complete when each [[Cauchy sequence|0MCK8K2D7Z]] in $X$ [[converges|06JYPJ4WHH]] to a point of $X$.

## Remarks

The real line $\mathbb{R}$ with the usual metric is complete. So is $\mathbb{R}^n$ with the Euclidean metric.
The rationals $\mathbb{Q}$ and the open interval $(0, 1)$ are not complete. In $(0, 1)$, the sequence $1/n$ is Cauchy but has no limit in $(0, 1)$.
Completeness depends on the metric, not only on the topology: $(0, 1)$ is homeomorphic to $\mathbb{R}$, but only $\mathbb{R}$ is complete with the usual metric.
Each metric space has a [[completion|0G4J7Z7WPJ]].

## Explanations

### L1 human

A complete space has no holes: each sequence that looks convergent really has a limit in the space.
The rationals have holes, for example at $\sqrt{2}$, and the reals fill them.
