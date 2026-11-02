---
tag: 1QW75YQQR8
kind: definition
name: Rubin causal model
msc: [62D20, 62A01]
defines: 23ATBZMJHR
uses: [0PNRKMRC55, 0WQNRCNY3M, 0GQ938GDE0]
sources:
  - url: https://en.wikipedia.org/wiki/Rubin_causal_model
---

## Definition

Consider units $i = 1, \dots, n$ and a binary treatment.
In the *Rubin causal model* the data are described as follows.

1. Each unit $i$ has two potential outcomes $Y_i(1)$ and $Y_i(0)$: the outcome under treatment and under control.
2. Each unit receives a treatment $W_i \in \set{0, 1}$, and the observed outcome is $Y_i = W_i Y_i(1) + (1 - W_i) Y_i(0)$.
3. The potential outcomes of unit $i$ do not depend on the treatments of the other units.
   There is only one version of each treatment (the stable unit treatment value assumption, SUTVA).

The *unit causal effect* is $Y_i(1) - Y_i(0)$.
When the units are drawn from a population, the *average treatment effect* is $\tau = E[Y(1) - Y(0)]$, an [[expected value|0WQNRCNY3M]] over the population.

## Remarks

Since only one of $Y_i(1)$ and $Y_i(0)$ is observed, unit effects are never observed; this is called the fundamental problem of causal inference.
The assignment is *unconfounded* (ignorable) given covariates $X$ if $W$ is [[independent|0GQ938GDE0]] of $(Y(0), Y(1))$ conditionally on $X$.

Example: in a completely randomised experiment, randomization gives $W$ independent of $(Y(0), Y(1))$.
Then $E[Y \mid W = 1] = E[Y(1) \mid W = 1] = E[Y(1)]$, and likewise for $W = 0$, so $\tau = E[Y \mid W = 1] - E[Y \mid W = 0]$.

Non-example: in a vaccine trial in which unvaccinated people can be protected by their vaccinated neighbours, the outcome of a unit depends on the treatments of others.
Clause 3 fails, and the two potential outcomes per unit are not enough to describe the situation.
