---
tag: EJM2Z7PE30
kind: concept
name: Lomb–Scargle periodogram
msc: [62M15, 85A04]
specializes: [3ZYM0HXA3E]
sources:
  - url: https://en.wikipedia.org/wiki/Least-squares_spectral_analysis
---

## Summary

The Lomb–Scargle periodogram is a [[periodogram|3ZYM0HXA3E]] for [[time series|EA3MF4VTEH]] sampled at uneven times.
At each trial frequency it measures how well a sinusoid of that frequency fits the data by [[least squares|0BYTQ4X1HC]].
Astronomers use it to find periods of variable stars and exoplanets, whose observations are rarely evenly spaced.

## Explanations

### L1 human

Suppose you measure the brightness of a star on random nights, when the weather allows.
To find whether it pulses with a period, you try many periods and see which sine wave fits the measurements best.
The Lomb–Scargle periodogram is a score for each trial frequency, and a high peak signals a likely period.
With evenly spaced data it agrees with the classical periodogram, but it also works with gaps.
