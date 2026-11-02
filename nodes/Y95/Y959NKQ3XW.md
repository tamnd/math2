---
tag: Y959NKQ3XW
kind: concept
name: Hazard function
msc: [62N05, 62N01, "60E05"]
sources:
  - url: https://en.wikipedia.org/wiki/Failure_rate
---

## Summary

The hazard function of a lifetime $T$ gives the instantaneous rate of the event at time $t$.
The rate is taken among the subjects that have not had the event yet.
It equals the density of $T$ divided by its [[survival function|QTM1HZM53Q]].
Its integral, the cumulative hazard, determines the survival function through $S(t) = e^{-H(t)}$.
Hazards are the natural scale of many models in [[survival analysis|443ZWDX88P]], such as the [[proportional hazards model|N029V3JX60]].
In reliability theory the hazard is called the failure rate.

## Explanations

### L1 human

The hazard at age $70$ answers: among people alive at $70$, how fast are they dying right now, per year?
It is a rate, not a probability, so it can be larger than $1$.
A machine part that wears out has a hazard that grows with age.
A part that fails only by pure accident, like a fuse hit by random surges, has a constant hazard; its lifetime is exponential.
Newborn mortality followed by a long flat period and then ageing gives the well-known bathtub-shaped hazard.
