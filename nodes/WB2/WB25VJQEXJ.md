---
tag: WB25VJQEXJ
kind: definition
name: Neyman construction
msc: [62F25, 62F03]
defines: EKZB41Y82N
uses: [0K4NMMJBG2, 087P03NEND]
sources:
  - url: https://en.wikipedia.org/wiki/Neyman_construction
---

## Definition

Let $X$ be data with values in a set $\mathcal{X}$, whose law $P_\theta$ depends on a parameter $\theta \in \Theta$, and let $\alpha \in (0, 1)$.
For each $\theta \in \Theta$, choose an acceptance region $A(\theta) \subseteq \mathcal{X}$ with $P_\theta(X \in A(\theta)) \ge 1 - \alpha$.
The *Neyman construction* is the set-valued statistic
$$C(X) = \set{\theta \in \Theta : X \in A(\theta)}.$$

## Remarks

For each $\theta$, the events $\set{\theta \in C(X)}$ and $\set{X \in A(\theta)}$ are equal, so $P_\theta(\theta \in C(X)) \ge 1 - \alpha$.
So $C(X)$ is a [[confidence set|0K4NMMJBG2]] of level $1 - \alpha$; its coverage is exactly $1 - \alpha$ when each $A(\theta)$ has probability exactly $1 - \alpha$.
Equivalently, $A(\theta)$ is the acceptance region of a [[test|087P03NEND]] at level $\alpha$ of the hypothesis that $\theta$ is the true value.
Then $C(X)$ is the set of values that these tests do not reject.
Example: for $X \sim \mathcal{N}(\theta, 1)$ and $A(\theta) = [\theta - 1.96, \theta + 1.96]$, the construction gives $C(X) = [X - 1.96, X + 1.96]$, of level about $0.95$.
Non-example: for $\alpha = 0.05$, the choice $A(\theta) = [\theta - 1, \theta + 1]$ fails the condition, since $P_\theta(X \in A(\theta)) \approx 0.68$; the resulting set has level only about $0.68$.
