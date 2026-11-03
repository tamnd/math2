---
tag: KA4EA7GTAF
kind: concept
name: Hull–White model
msc: [91G30, 60H10]
specializes: [7TZ87AS1MW]
sources:
  - url: https://en.wikipedia.org/wiki/Hull%E2%80%93White_model
same_as:
  wikidata: Q6148579
  wikipedia: Hull–White model
---

## Summary

The Hull–White model is a [[short-rate model|7TZ87AS1MW]] that extends the [[Vasicek model|QXHQ57B0R2]] by letting the mean-reversion level depend on time.
It was introduced by John Hull and Alan White in 1990.
The time-dependent level is chosen so that the model reproduces today's observed bond prices exactly.
It keeps the Gaussian structure and closed-form bond and bond option prices of the Vasicek model.

## Explanations

### L1 human

The Vasicek model has only a few constant parameters, so it cannot match all the bond prices seen in the market today.
The Hull–White model replaces the fixed target level by a target that changes with time.
This target is tuned so that the model price of every zero-coupon bond equals its market price.
For example, if the market curve rises steeply over the next two years, the target level is set higher over those years.
