---
tag: 2JC96FMGA1
kind: concept
name: Autoregressive model
msc: [62M10, 91B84]
sources:
  - url: https://en.wikipedia.org/wiki/Autoregressive_model
same_as:
  wikidata: Q2202883
  wikipedia: Autoregressive model
---

## Summary

An autoregressive model describes each value of a [[time series|EA3MF4VTEH]] as a linear combination of a few past values plus a random shock.
The number of past values used is the order $p$, and the model is written AR($p$).
It is one of the simplest and most used models for dependent data, and a building block of ARMA and ARIMA models.

## Explanations

### L1 human

The model says that the present is a weighted echo of the recent past plus something new and unpredictable.
In the AR($1$) model $X_t = 0.8 X_{t-1} + \varepsilon_t$, each value keeps $80\%$ of the previous one and adds fresh noise.
A shock therefore fades away slowly, by a factor $0.8$ each step.
If the weight were $1$, shocks would never fade, and the series would wander like a random walk.
