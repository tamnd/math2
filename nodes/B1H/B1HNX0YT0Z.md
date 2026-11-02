---
tag: B1HNX0YT0Z
kind: concept
name: Autoregressive–moving-average model
msc: [62M10, 91B84]
sources:
  - url: https://en.wikipedia.org/wiki/Autoregressive_moving-average_model
same_as:
  wikidata: Q290467
  wikipedia: Autoregressive moving-average model
---

## Summary

An autoregressive–moving-average model, or ARMA($p$, $q$) model, combines an [[autoregressive model|2JC96FMGA1]] of order $p$ with a [[moving-average model|PEB9DN0AHA]] of order $q$.
Each value is a linear combination of $p$ past values plus the current shock and $q$ past shocks.
ARMA models describe a wide range of stationary time series with few parameters, and they are the core of the Box–Jenkins approach to forecasting.

## Explanations

### L1 human

An autoregressive part lets the series remember its own past values, and a moving-average part lets recent shocks echo for a few steps.
Using both parts often describes the data with fewer numbers than using either part alone.
For example, $X_t = 0.5 X_{t-1} + \varepsilon_t + 0.3 \varepsilon_{t-1}$ is an ARMA($1$, $1$) model.
Forecasts from it decay towards the mean at the rate $0.5$ per step, after a first step that also uses the last shock.
