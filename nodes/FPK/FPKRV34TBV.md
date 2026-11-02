---
tag: FPKRV34TBV
kind: definition
name: Causal inference
msc: [62D20, 62A01]
defines: V3QJFN5800
uses: [23ATBZMJHR, JZ2S01BHJJ]
sources:
  - url: https://en.wikipedia.org/wiki/Causal_inference
---

## Definition

*Causal inference* is the branch of [[statistical inference|JZ2S01BHJJ]] whose targets are causal quantities.
These are the values an outcome would take under interventions that set a treatment or exposure to given values.
In the [[potential outcomes framework|23ATBZMJHR]], a typical target is the average treatment effect $E[Y(1) - Y(0)]$.
Here $Y(w)$ is the outcome a unit would have under treatment level $w$.
A causal quantity is *identified* if, under stated assumptions, it is a function of the distribution of the observed variables.

## Remarks

Causal inference has two steps: identification, which shows that the target is a function of the observed distribution under assumptions, and estimation of that function from data.

Example: in a completely randomised experiment with treatment $W \in \set{0, 1}$, randomization makes $W$ independent of $(Y(0), Y(1))$.
Then $E[Y(1) - Y(0)] = E[Y \mid W = 1] - E[Y \mid W = 0]$, so the average treatment effect is identified and estimated by the difference of group means.

Non-example: estimating $E[Y \mid W = 1] - E[Y \mid W = 0]$ in observational data, with no assumption linking it to $Y(1)$ and $Y(0)$, is a description of an association, not causal inference.
If sicker patients choose the treatment, this difference may even have the opposite sign to the causal effect.
