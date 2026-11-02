---
tag: 3ZYM0HXA3E
kind: concept
name: Periodogram
msc: [62M15]
sources:
  - url: https://en.wikipedia.org/wiki/Periodogram
same_as:
  wikidata: Q587619
  wikipedia: Periodogram
---

## Summary

The periodogram of a finite [[time series|EA3MF4VTEH]] measures how much of the variation of the series is due to oscillations at each frequency.
It is the squared modulus of the discrete Fourier transform of the data, suitably scaled.
It is the basic estimate of the spectral density of a stationary process and the starting point of spectral analysis.
By itself, however, it is a noisy estimate.

## Explanations

### L1 human

A series that rises and falls every $12$ months has a strong rhythm at the frequency of one cycle per year.
The periodogram scans through all frequencies and asks how well a sine wave of that frequency fits the data.
Frequencies with a good fit show up as peaks.
For example, for monthly sales with a December peak, the periodogram has a peak at the frequency $2\pi/12$ radians per month.
