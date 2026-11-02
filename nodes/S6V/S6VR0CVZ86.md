---
tag: S6VR0CVZ86
kind: definition
name: Survival analysis
msc: [62N01, 62N02, 62P10]
defines: 443ZWDX88P
uses: [QTM1HZM53Q, Y959NKQ3XW, MY8ZZP84NP, JZ2S01BHJJ]
sources:
  - url: https://en.wikipedia.org/wiki/Survival_analysis
---

## Definition

*Survival analysis* is the branch of [[statistical inference|JZ2S01BHJJ]] whose data are times to an event.
Its setting is a nonnegative random variable $T$, the event time, together with observations of $T$ that may be [[censored|MY8ZZP84NP]].
Its aims are to estimate the [[survival function|QTM1HZM53Q]] $S(t) = P(T > t)$ and the [[hazard function|Y959NKQ3XW]] of $T$.
It also compares them between groups and models how they depend on covariates.

## Remarks

The data of subject $i$ usually take the form $(\tilde t_i, \delta_i, x_i)$, where $x_i$ is a vector of covariates.
Here $\tilde t_i = \min(T_i, C_i)$ is the observed time, $C_i$ is a censoring time, and $\delta_i = 1$ if $T_i \le C_i$ and $0$ otherwise.

Example: estimating the fraction of light bulbs that still work after $1000$ hours, when the test is stopped at $1500$ hours, is a survival analysis problem.
The bulbs still working at $1500$ hours give right-censored times.

Non-example: estimating the mean weight of the bulbs is not survival analysis, since the quantity of interest is not a time to an event.
