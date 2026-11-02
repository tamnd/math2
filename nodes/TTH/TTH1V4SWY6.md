---
tag: TTH1V4SWY6
kind: concept
name: Spectral density estimation
msc: [62M15, 62G07]
sources:
  - url: https://en.wikipedia.org/wiki/Spectral_density_estimation
same_as:
  wikidata: Q6555326
  wikipedia: Spectral density estimation
---

## Summary

Spectral density estimation is the problem of estimating the spectral density of a stationary process from a finite stretch of data.
The spectral density describes how the variance of the process is spread over frequencies.
The raw [[periodogram|3ZYM0HXA3E]] is too noisy for this, so practical estimators smooth it over nearby frequencies or fit a parametric model.
Spectral estimates reveal periodic components and the memory structure of a series and are used in signal processing, economics and geophysics.

## Explanations

### L1 human

A stationary signal can be thought of as a mix of waves of many frequencies with random amplitudes.
Its spectral density says how much power each frequency carries, like the bars of a music equalizer.
From a recording of finite length, these bars can only be estimated, and a naive estimate flickers wildly from one frequency to the next.
Averaging over neighbouring frequencies, or over several pieces of the recording, gives a steadier picture at the cost of some blurring.
