---
tag: PEB9DN0AHA
kind: concept
name: Moving-average model
msc: [62M10, 91B84]
sources:
  - url: https://en.wikipedia.org/wiki/Moving-average_model
same_as:
  wikidata: Q1088984
  wikipedia: Moving-average model
---

## Summary

A moving-average model describes each value of a [[time series|EA3MF4VTEH]] as its mean plus a weighted sum of current and recent random shocks.
With $q$ past shocks the model is written MA($q$).
Its autocorrelation vanishes beyond lag $q$, so it suits series whose memory is short.
Together with the autoregressive model it forms the ARMA family.

## Explanations

### L1 human

Imagine a pond where each raindrop makes ripples that last exactly two seconds.
The water level now is the sum of the effects of the drops of the last two seconds, and older drops no longer matter.
In the MA($1$) model $X_t = \varepsilon_t + 0.5 \varepsilon_{t-1}$, each shock acts fully today and half as strongly tomorrow, and then disappears.
So values two or more steps apart are uncorrelated.
