---
tag: EA3MF4VTEH
kind: concept
name: Time series
msc: [62M10, 91B84]
sources:
  - url: https://en.wikipedia.org/wiki/Time_series
same_as:
  wikidata: Q186588
  wikipedia: Time series
---

## Summary

A time series is a sequence of observations recorded in time order, such as daily temperatures or monthly unemployment rates.
Time series analysis models such data as one realization of a [[stochastic process|0QH5ENKZM1]], in which nearby observations are usually dependent.
The goals are to describe this dependence, to estimate models, and to forecast future values.

## Explanations

### L1 human

Most statistical methods assume that the observations are independent, like separate draws from a hat.
A time series is different: today's value says a lot about tomorrow's value.
Plotting the data against time shows trends, seasonal cycles and random wiggles.
For example, the monthly sales $x_1, \dots, x_{36}$ of a shop over three years form a time series, and a peak every December is a seasonal pattern.
