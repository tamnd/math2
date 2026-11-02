---
tag: YCZHYY8VE5
kind: concept
name: Autocorrelation function
msc: [62M10, 60G10]
sources:
  - url: https://en.wikipedia.org/wiki/Autocorrelation
same_as:
  wikidata: Q786970
  wikipedia: Autocorrelation
---

## Summary

The autocorrelation function of a weakly [[stationary process|DT0QXJE705]] gives, for each lag $h$, the correlation between $X_t$ and $X_{t+h}$.
It summarizes the linear dependence in a [[time series|EA3MF4VTEH]] in one function of the lag.
Its sample version is the first tool for identifying a time series model.

## Explanations

### L1 human

Take a time series and lay a copy of it next to the original, shifted by $h$ steps.
The autocorrelation at lag $h$ measures how well the shifted copy lines up with the original, on a scale from $-1$ to $1$.
For daily temperatures, the autocorrelation at lag $1$ is high, because today is usually like yesterday.
For independent coin tosses, the autocorrelation is $0$ at every lag $h \ne 0$.
