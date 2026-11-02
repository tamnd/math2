---
tag: 93GK2SPBKV
kind: concept
name: Nelson–Aalen estimator
msc: [62N02, 62G05]
sources:
  - url: https://en.wikipedia.org/wiki/Nelson–Aalen_estimator
same_as:
  wikidata: Q6990830
  wikipedia: Nelson–Aalen estimator
---

## Summary

The Nelson–Aalen estimator is a nonparametric estimator of the cumulative [[hazard function|Y959NKQ3XW]] from right-[[censored|MY8ZZP84NP]] data.
At each observed event time it adds the number of events divided by the number of subjects at risk.
It is the natural estimator in the counting process approach to survival analysis, where its large-sample theory follows from martingale results.
Taking $e^{-\hat H(t)}$ gives an estimator of the survival function close to the [[Kaplan–Meier estimator|B7AJ8RWZRC]].

## Explanations

### L1 human

The cumulative hazard adds up the risk of the event over time.
At each moment when someone has the event, the Nelson–Aalen estimator adds "events now divided by people still at risk".
If one person of four dies, it adds $1/4$; if later one person of two dies, it adds $1/2$.
The total grows faster when events are frequent among those still at risk.
Plotting it shows whether the hazard is constant (a straight line) or changes with time.
