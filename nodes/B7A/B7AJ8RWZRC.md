---
tag: B7AJ8RWZRC
kind: concept
name: Kaplan–Meier estimator
msc: [62N02, 62G05, 62P10]
sources:
  - url: https://en.wikipedia.org/wiki/Kaplan–Meier_estimator
same_as:
  wikidata: Q1432420
  wikipedia: Kaplan–Meier estimator
---

## Summary

The Kaplan–Meier estimator is a nonparametric estimator of the [[survival function|QTM1HZM53Q]] from right-[[censored|MY8ZZP84NP]] data.
It multiplies, over the observed event times, the fractions of subjects at risk who survive each event time.
Without censoring it reduces to one minus the [[empirical distribution function|A05WR6TEK5]].
It was introduced by Edward Kaplan and Paul Meier, and its step-shaped plot is the most common figure in medical survival studies.

## Explanations

### L1 human

Follow four patients: deaths at months $2$, $5$ and $7$, and one patient who leaves the study at month $3$.
At month $2$ one of four patients at risk dies, so survival drops to $3/4$.
The patient who leaves at month $3$ is simply removed from the group at risk, without counting a death.
At month $5$ one of the two remaining patients dies, so survival drops to $3/4 \cdot 1/2 = 3/8$.
The censored patient helped in the first step, and it does not distort the later ones.
