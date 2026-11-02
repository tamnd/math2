---
tag: KTDVZP4DF2
kind: concept
name: Autoregressive integrated moving average
msc: [62M10, 91B84]
sources:
  - url: https://en.wikipedia.org/wiki/Autoregressive_integrated_moving_average
same_as:
  wikidata: Q2566298
  wikipedia: Autoregressive integrated moving average
---

## Summary

An autoregressive integrated moving average model, or ARIMA($p$, $d$, $q$) model, is a time series model whose $d$-th differences form an [[ARMA($p$, $q$) process|B1HNX0YT0Z]].
It extends ARMA models to non-stationary series with trends or random-walk behaviour.
The word "integrated" refers to undoing the differencing by summation.
ARIMA models are among the most widely used models for forecasting economic and business series.

## Explanations

### L1 human

Many series, such as a stock price index, do not hover around a fixed level; they drift and wander.
The changes from one step to the next, however, often look stable.
ARIMA models fit an ARMA model to these changes, and then add the changes back up to forecast the series itself.
The simplest case is the random walk $X_t = X_{t-1} + \varepsilon_t$, which is ARIMA($0$, $1$, $0$): its changes $X_t - X_{t-1} = \varepsilon_t$ are pure noise.
