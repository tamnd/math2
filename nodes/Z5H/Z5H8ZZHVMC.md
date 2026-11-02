---
tag: Z5H8ZZHVMC
kind: problem
name: Change detection
msc: [62L10, 62P30]
uses: [9CWYNB9003, WND87FBAKC, 0WQNRCNY3M]
about: [9CWYNB9003]
sources:
  - url: https://en.wikipedia.org/wiki/Change_detection
same_as:
  wikidata: Q25389927
  wikipedia: Change detection
history:
  posed_by: "E. S. Page"
  first_stated: "1954"
  notes: "Page stated sequential change detection with the CUSUM procedure in Continuous inspection schemes, Biometrika 41 (1954)."
---

## Problem

Let $X_1, X_2, \dots$ be observed one at a time.
For an unknown change time $\nu \in \set{1, 2, \dots} \cup \set{\infty}$, the variables are independent, $X_n$ has density $f_0$ for $n < \nu$ and density $f_1$ for $n \ge \nu$, where $f_0 \ne f_1$.
Find a [[stopping time|WND87FBAKC]] $T$ of the observations that raises an alarm soon after the change and rarely before it.

Lorden's minimax form measures the delay by
$$\bar D(T) = \sup_{\nu \ge 1} \operatorname*{ess\,sup} E_\nu\left[ (T - \nu + 1)^+ \mid X_1, \dots, X_{\nu - 1} \right],$$
and the task is to minimize $\bar D(T)$ subject to $E_\infty[T] \ge \gamma$ for a given $\gamma > 1$.
Here $E_\nu$ is the [[expectation|0WQNRCNY3M]] when the change occurs at time $\nu$, and $E_\infty$ is the expectation when there is no change.

## Remarks

The problem is a central problem of [[sequential analysis|9CWYNB9003]], with roots in industrial quality control.
E. S. Page proposed the cumulative sum procedure, or CUSUM, for it in 1954.
Gary Lorden introduced the criterion above in 1971 and showed that CUSUM is asymptotically optimal as $\gamma \to \infty$.
George Moustakides proved in 1986 that CUSUM is exactly optimal for this criterion.
In the Bayesian form, studied by Albert Shiryaev, $\nu$ has a geometric prior and the expected delay is minimized subject to a bound on the probability of a false alarm.
There is also an offline form, in which the whole sample is given and the change time is to be estimated.

## Explanations

### L1 human

A machine runs normally, and at some unknown moment it starts to go wrong.
Each new measurement gives a little evidence, and a monitor must decide when to sound the alarm.
Sounding it too early stops a good machine, and sounding it too late wastes good material.
The problem is to find the best trade-off between quick detection and few false alarms.
