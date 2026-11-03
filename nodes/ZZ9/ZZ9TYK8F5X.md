---
tag: ZZ9TYK8F5X
kind: definition
name: Spence signaling model
msc: [91B44, 91B39, 91A27]
defines: BH0QN3M8H0
uses: [DNVNS5HNYR, RG94E9CBQJ]
sources:
  - url: https://en.wikipedia.org/wiki/Signalling_(economics)
---

## Definition

The *Spence signaling model* is the following [[signaling game|DNVNS5HNYR]] between a worker and competing employers.

1. The worker has a type $\theta \in \set{\theta_L, \theta_H}$ with $0 < \theta_L < \theta_H$, which equals the worker's productivity.
   The type is $\theta_H$ with prior probability $\lambda \in (0, 1)$, and only the worker knows it.
2. The worker chooses an education level $e \ge 0$ at a cost $c(e, \theta)$ with $c(0, \theta) = 0$ that is increasing in $e$.
   The marginal cost $\partial c / \partial e$ is strictly smaller for $\theta_H$ than for $\theta_L$ (the single-crossing condition).
3. Employers observe $e$ but not $\theta$, form a belief $\mu(e) \in [0, 1]$ that the type is $\theta_H$, and compete.
   So the wage is the expected productivity $w(e) = \mu(e)\theta_H + (1 - \mu(e))\theta_L$.
4. A worker of type $\theta$ who chooses $e$ receives the payoff $w(e) - c(e, \theta)$.

Education does not change productivity.
The solution concept is the [[perfect Bayesian equilibrium|RG94E9CBQJ]].
An equilibrium is *separating* if the two types choose different education levels, and *pooling* if they choose the same level.

## Remarks

Example: let $\theta_L = 1$, $\theta_H = 2$ and $c(e, \theta) = e/\theta$.
Let the low type choose $e = 0$, the high type choose $e^* \in [1, 2]$, and let $\mu(e) = 1$ if $e \ge e^*$ and $\mu(e) = 0$ otherwise.
The low type gets $1$ at $e = 0$ and at most $2 - e^* \le 1$ by mimicking, so it does not deviate.
The high type gets $2 - e^*/2 \ge 1$, which is at least what it gets at any $e < e^*$, so it does not deviate either.
Beliefs are correct on the equilibrium path, so this is a separating equilibrium.
The least costly one has $e^* = 1$.

Non-example: if the cost is $c(e, \theta) = e$ for both types, the single-crossing clause fails.
A separating level $e^*$ then needs $2 - e^* \le 1$ and $2 - e^* \ge 1$, so $e^* = 1$ and both types are indifferent; the signal no longer separates the types strictly.

The model has many equilibria, because beliefs off the equilibrium path are free.
Refinements such as the intuitive criterion select the least costly separating equilibrium.
